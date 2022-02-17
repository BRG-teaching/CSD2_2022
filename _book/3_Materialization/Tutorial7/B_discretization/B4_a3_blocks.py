# ==============================================================================
#Imports
# ==============================================================================
import os
import compas
from compas.datastructures import Mesh
from compas_rhino.artists import MeshArtist

# ==============================================================================
#Load data
# ==============================================================================

HERE = os.path.dirname(__file__)

FILE_I1 = os.path.join(HERE, 'data', 'form_idos.json')
FILE_I2 = os.path.join(HERE, 'data', 'form_edos.json')

FILE_O = os.path.join(HERE, 'data', 'blocks.json')

idos = Mesh.from_json(FILE_I1)
edos = Mesh.from_json(FILE_I2)

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

print(blocks)
# # ==============================================================================
# #Output
# # ==============================================================================
compas.json_dump(blocks, FILE_O)

# #================================================
# #Visualize
# #================================================

artist = MeshArtist(None, layer="CSD2::DISCRETIZATION::blocks")
artist.clear_layer()

for block in blocks:
    print(block)
    artist = MeshArtist(block,layer="CSD2::DISCRETIZATION::blocks")
    artist.draw_faces(join_faces=True)
    artist.draw_edges()
