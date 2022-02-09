import os
from compas.datastructures import Mesh
from compas_rhino.artists import MeshArtist

from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import compas
from compas_rv2.rhino import get_scene
from compas_rv2.rhino import get_proxy
from compas.geometry import add_vectors, scale_vector
from compas_rv2.rhino import rv2_undo
from compas_rv2.rhino import rv2_error

from compas.datastructures import Mesh
from compas_rhino.artists import MeshArtist


__commandname__ = "RV2materialisation2"


HERE = os.path.dirname(__file__)

mesh_file = 'form.json'
FILE_I = os.path.join(HERE, 'data', mesh_file)
FILE_O = os.path.join(HERE, 'data', 'blocks.json')


def materialisation(mesh, visualise_orientation=True, visualise_offsets=True):

    # subdivide dual
    # -----------------------------------------------
    dual = mesh.dual()

    # visualise dual subdivision
    # -----------------------------------------------

    artist1 = MeshArtist(dual, layer="RV2::Dual")
    artist1.clear_layer()
    artist1.draw_faces()

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
        artist3 = MeshArtist(idos, layer="RV2::Idos")
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

    # visualise blocks
    # -----------------------------------------------
    artist5 = MeshArtist(None, layer="RV2::Blocks")
    artist5.clear_layer()

    for block in blocks:
        artist5.mesh = block
        artist5.draw_faces(color=(0, 255, 255), join_faces=True)

    return blocks


@rv2_error()
@rv2_undo
def RunCommand(is_interactive):

    scene = get_scene()
    if not scene:
        return

    proxy = get_proxy()
    if not proxy:
        return

    # vertical = proxy.function('compas_tna.equilibrium.vertical_from_zmax_proxy')

    form = scene.get('form')[0]
    thrust = scene.get('thrust')[0]

    if not form:
        print("There is no FormDiagram in the scene.")
        return

    if not thrust:
        print("There is no ThrustDiagram in the scene.")
        return

    # get mesh from horizontal equilibrium
    # -----------------------------------------------
    # mesh = thrust.datastructure
    mesh = Mesh.from_json(FILE_I)

    # materialisation
    # -----------------------------------------------
    blocks = materialisation(mesh, visualise_orientation=True, visualise_offsets=True)

    # export final mesh in blocks in json file
    # -----------------------------------------------
    blocks.to_json(FILE_O)
    compas.json_dump(blocks, FILE_O)

    # update scene
    # -----------------------------------------------
    scene.clear()
    scene.update()


# ==============================================================================
# Main
# ==============================================================================


if __name__ == "__main__":

    RunCommand(True)
