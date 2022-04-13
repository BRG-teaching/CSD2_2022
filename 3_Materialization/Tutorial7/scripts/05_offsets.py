import os
import compas

from compas.datastructures  import Mesh
from compas_cgal.meshing import remesh
from compas_cgal.subdivision import catmull_clark
from compas_view2.app import App

from compas.geometry import add_vectors, scale_vector


# 1. load triangulated mesh from step 2
dirname = os.path.dirname(__file__)
filename = '04_dual_mesh_with_boundary.json'
filepath = os.path.join(dirname, filename)

dual_mesh = compas.json_load(filepath)


idos = dual_mesh.copy()
edos = dual_mesh.copy()


thickness = 0.5

for vertex in dual_mesh.vertices():
    point = dual_mesh.vertex_coordinates(vertex)
    normal = dual_mesh.vertex_normal(vertex)

    idos.vertex_attributes(vertex, 'xyz', add_vectors(point, scale_vector(normal, +0.5 * thickness)))
    edos.vertex_attributes(vertex, 'xyz', add_vectors(point, scale_vector(normal, -0.5 * thickness)))

# 4. export dual mesh data to a new file
dirname = os.path.dirname(__file__)
filename = '05_idos.json'
filepath = os.path.join(dirname, filename)
compas.json_dump(idos, filepath, pretty=True)
filename = '05_edos.json'
filepath = os.path.join(dirname, filename)
compas.json_dump(edos, filepath, pretty=True)



viewer = App()
viewer.add(idos)
viewer.add(edos)
viewer.show()
