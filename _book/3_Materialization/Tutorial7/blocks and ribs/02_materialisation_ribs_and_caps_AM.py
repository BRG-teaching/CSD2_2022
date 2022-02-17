from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import os
from compas.datastructures import Mesh
from compas_rhino.artists import MeshArtist

import compas
from compas_rv2.rhino import get_scene
from compas_rv2.rhino import get_proxy
from compas.geometry import add_vectors, scale_vector
from compas_rv2.rhino import rv2_undo
from compas_rv2.rhino import rv2_error

from compas.datastructures import Mesh
from compas_rhino.artists import MeshArtist


HERE = os.path.dirname(__file__)

FILE_I1 = os.path.join(HERE, 'data', 'Ribs_Mesh.json')
FILE_I2 = os.path.join(HERE, 'data', 'Caps_Mesh.json')

mesh_ribs = Mesh.from_json(FILE_I1)
mesh_caps = Mesh.from_json(FILE_I2)

FILE_O1 = os.path.join(HERE, 'data', 'Ribs_Blocks.json')
FILE_O2 = os.path.join(HERE, 'data', 'Caps_Blocks.json')


def materialisation(mesh, visualise_orientation=True, visualise_offsets=True):

    # check normals' orientation
    # -----------------------------------------------
    for vkey in mesh.vertices():
        print(vkey, mesh.vertex_normal(vkey))

    # visualise normals
    # -----------------------------------------------
    if visualise_orientation:
        artist2 = MeshArtist(mesh, layer="RV2::Normals")
        artist2.clear_layer()
        artist2.draw_edges()
        artist2.draw_vertexnormals(scale=1)

    # make offsets
    # -----------------------------------------------
    idos = mesh.copy()
    edos = mesh.copy()

    for vertex in mesh.vertices():
        point = mesh.vertex_coordinates(vertex)
        normal = mesh.vertex_normal(vertex)
        thickness = 10
        idos.vertex_attributes(vertex, 'xyz', add_vectors(point, scale_vector(normal, +0.5 * thickness)))
        edos.vertex_attributes(vertex, 'xyz', add_vectors(point, scale_vector(normal, -0.5 * thickness)))

    # visualise offsets
    # -----------------------------------------------
    if visualise_offsets:
        
        artist3 = MeshArtist(idos, layer="RV2::Edos")
        artist3.clear_layer()
        artist3.draw_faces(color=(255, 0, 0))

        artist4 = MeshArtist(edos, layer="RV2::Edos")
        artist4.clear_layer()
        artist4.draw_faces(color=(0, 0, 255))

    # create blocks
    # -----------------------------------------------
    blocks = []

    for face in idos.faces():
        bottom = idos.face_coordinates(face)
        top = edos.face_coordinates(face)

        f = len(bottom)

        faces = [
            list(range(f)),
            list(range(f + f - 1, f - 1, -1))]

        for i in range(f - 1):
            faces.append([i, i + f, i + f + 1, i + 1])
        faces.append([f - 1, f + f - 1, f, 0])

        block = Mesh.from_vertices_and_faces(bottom + top, faces)
        blocks.append(block)
    
    return blocks

# --------------------------------------------------------------------------------------------------
# materialisation of ribs blocks 
# --------------------------------------------------------------------------------------------------
ribs_blocks = materialisation(mesh_ribs, visualise_orientation=True, visualise_offsets=True)

artist5 = MeshArtist(None, layer="RV2::Ribs_Blocks")
artist5.clear_layer()

for block in ribs_blocks:
    artist5.mesh = block
    artist5.draw_faces(color=(0, 255, 255), join_faces=True)

# export final ribs blocks in json file
# -----------------------------------------------
ribs_blocks.to_json(FILE_O1)
compas.json_dump(ribs_blocks, FILE_O1)


# --------------------------------------------------------------------------------------------------
# materialisation of caps blocks 
# --------------------------------------------------------------------------------------------------
caps_blocks = materialisation(mesh_caps, visualise_orientation=True, visualise_offsets=True)

artist6 = MeshArtist(None, layer="RV2::Caps_Blocks")
artist6.clear_layer()

for block in caps_blocks:
    artist6.mesh = block
    artist6.draw_faces(color=(255, 0, 255), join_faces=True)

# export final caps blocks in json file
# -----------------------------------------------
caps_blocks.to_json(FILE_O2)
compas.json_dump(caps_blocks, FILE_O2)