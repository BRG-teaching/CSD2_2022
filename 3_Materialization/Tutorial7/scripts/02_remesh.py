import os
import compas

from compas.datastructures  import Mesh
from compas_cgal.meshing import remesh
from compas_cgal.subdivision import catmull_clark
from compas_view2.app import App


# 1. load triangulated mesh from step 1
dirname = os.path.dirname(__file__)
filename = '01_triangulated_mesh.json'
filepath = os.path.join(dirname, filename)

tri_mesh = compas.json_load(filepath)


# 2. remesh
lengths = [tri_mesh.edge_length(*edge) for edge in tri_mesh.edges()]
length = sum(lengths) / tri_mesh.number_of_edges()

V, F = remesh(tri_mesh.to_vertices_and_faces(), target_edge_length=0.75 * length, number_of_iterations=100)
remeshed_mesh = Mesh.from_vertices_and_faces(V, F)


# 3. export mesh data to a new file
dirname = os.path.dirname(__file__)
filename = '02_remeshed_mesh.json'
filepath = os.path.join(dirname, filename)
compas.json_dump(remeshed_mesh, filepath, pretty=True)


# 4. visualise the mesh
viewer = App()
viewer.add(remeshed_mesh)
viewer.show()
