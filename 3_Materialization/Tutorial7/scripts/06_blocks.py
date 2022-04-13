import os
import compas

from compas.datastructures  import Mesh
from compas_cgal.meshing import remesh
from compas_cgal.subdivision import catmull_clark
from compas_view2.app import App


# 1. load triangulated mesh from step 2
dirname = os.path.dirname(__file__)
filename = '05_idos.json'
filepath = os.path.join(dirname, filename)
idos = compas.json_load(filepath)

filename = '05_edos.json'
filepath = os.path.join(dirname, filename)
edos = compas.json_load(filepath)

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



data = [block.to_data() for block in blocks]
dirname = os.path.dirname(__file__)
filename = '06_blocks.json'
filepath = os.path.join(dirname, filename)
compas.json_dump(blocks, filepath, pretty=True)



# 4. visualise the mesh
viewer = App()

for block in blocks:
    viewer.add(block)
viewer.show()
