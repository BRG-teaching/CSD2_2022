from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import os
import compas

from compas.geometry import add_vectors, scale_vector

from compas.datastructures import Mesh
from compas_rhino.artists import MeshArtist


HERE = os.path.dirname(__file__)

FILE_I1 = os.path.join(HERE, 'data', 'Ribs_Mesh.json')
FILE_I2 = os.path.join(HERE, 'data', 'Caps_Mesh.json')

mesh_ribs = Mesh.from_json(FILE_I1)
mesh_caps = Mesh.from_json(FILE_I2)

FILE_O1 = os.path.join(HERE, 'data', 'ribs_blocks.json')
FILE_O2 = os.path.join(HERE, 'data', 'caps_blocks.json')


def offsets(mesh, thickness=10):
    idos = mesh.copy()
    edos = mesh.copy()

    for vertex in mesh.vertices():
        point = mesh.vertex_coordinates(vertex)
        normal = mesh.vertex_normal(vertex)
        idos.vertex_attributes(vertex, 'xyz', add_vectors(point, scale_vector(normal, +0.5 * thickness)))
        edos.vertex_attributes(vertex, 'xyz', add_vectors(point, scale_vector(normal, -0.5 * thickness)))
    return idos, edos


def draw_offsets(i_mesh, e_mesh):

    artist = MeshArtist(i_mesh,"RV2::Idos")
    artist.clear_layer()
    artist.draw_faces(color=(255, 0, 0))

    artist = MeshArtist(e_mesh,"RV2::Edos")
    artist.clear_layer()
    artist.draw_faces(color=(0, 0, 255))


def materialisation_blocks(idos, edos):
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

    artist = MeshArtist(None, layer="RV2::Blocks")
    artist.clear_layer()

    for block in blocks:
        artist.mesh = block
        artist.draw_faces(color=(0, 255, 255), join_faces=True)

    return blocks



def materialisation(mesh, visualise_offsets=True):

    mesh_idos = offsets(mesh)[0]
    mesh_edos = offsets(mesh)[1]
    if visualise_offsets:
        draw_offsets(mesh_idos, mesh_edos)
    blocks = materialisation_blocks(mesh_idos, mesh_edos)
    return blocks


blocks = materialisation(mesh_ribs, visualise_offsets=True)

compas.json_dump(blocks, FILE_O1)


