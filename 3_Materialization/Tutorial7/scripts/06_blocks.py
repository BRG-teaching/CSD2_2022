import os
import compas

from compas.datastructures  import Mesh
from compas_view2.app import App


# folder location
dirname = os.path.dirname(__file__) + "/data"


# 1. load idos from step 5
idos_in_name = '05_idos.json'
idos_in_path = os.path.join(dirname, idos_in_name)
idos: Mesh = compas.json_load(idos_in_path)


# 2. load edos from step 5
edos_in_name = '05_edos.json'
edos_in_path = os.path.join(dirname, edos_in_name)
edos: Mesh = compas.json_load(edos_in_path)


# 3. make blocks

blocks = []  # a list of meshes

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


# 4. export blocks to a new file
blocks_out_name = '06_blocks.json'
blocks_out_path = os.path.join(dirname, blocks_out_name)
compas.json_dump(blocks, blocks_out_path, pretty=True)


# 5. visualise the blocks
viewer = App()

for block in blocks:
    viewer.add(block)
viewer.show()
