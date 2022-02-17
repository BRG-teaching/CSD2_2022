from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import os
import compas
from compas.datastructures import Mesh
from compas_rhino.artists import MeshArtist
from compas.geometry import add_vectors, scale_vector


HERE = os.path.dirname(__file__)

FILE_I = os.path.join(HERE, 'data', 'form.json')

mesh = Mesh.from_json(FILE_I)

FILE_O = os.path.join(HERE, 'data', 'Mesh_Blocks.json')


def materialisation(mesh, name ="", blocks_color = (255,255,0), visualise_orientation=True, visualise_offsets=True):

    # check normals' orientation
    # -----------------------------------------------
    for vkey in mesh.vertices():
        print(vkey, mesh.vertex_normal(vkey))

    # visualise normals
    # -----------------------------------------------
    if visualise_orientation:
        artist2 = MeshArtist(mesh, layer="RV2::Normals_{}".format(name))
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
        
        artist3 = MeshArtist(idos, layer="RV2::Idos_{}".format(name))
        artist3.clear_layer()
        artist3.draw_faces(color=(255, 0, 0))

        artist4 = MeshArtist(edos, layer="RV2::Edos_{}".format(name))
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
    
    for block in blocks:
        artist5 = MeshArtist(block, layer="RV2::Blocks_{}".format(name))
        artist5.mesh = block
        artist5.draw_faces(color= blocks_color, join_faces=True)

    return blocks


# --------------------------------------------------------------------------------------------------
# materialisation of mesh blocks 
# --------------------------------------------------------------------------------------------------
mesh_color = (51,51,255)
blocks = materialisation(mesh, "Form", mesh_color, visualise_orientation=True, visualise_offsets=True)

# export final blocks in json file
# -----------------------------------------------

compas.json_dump(blocks, FILE_O)

