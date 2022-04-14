import os
import compas

from compas.datastructures  import Mesh
from compas_cgal.meshing import remesh
from compas_cgal.subdivision import catmull_clark
from compas_view2.app import App

from trimesh_remesh import trimesh_remesh
from compas.datastructures import trimesh_pull_points_numpy


# folder location
dirname = os.path.dirname(__file__) + "/data"


# 1. load triangulated mesh from step 1
file_in_name = '01_triangulated_mesh.json'
file_in_path = os.path.join(dirname, file_in_name)
trimesh: Mesh = compas.json_load(file_in_path)


# 2. remesh the triangulated mesh

# function for projecting back to the original mesh
def project(k, callback_args=None):
    xyz = remeshed.vertices_attributes("xyz")
    xyz = trimesh_pull_points_numpy(trimesh, xyz)
    for index, vertex in enumerate(remeshed.vertices()):
        remeshed.vertex_attributes(vertex, "xyz", xyz[index])

# remeshing
remeshed = trimesh.copy()
lengths = [trimesh.edge_length(*edge) for edge in trimesh.edges()]
length = sum(lengths) / trimesh.number_of_edges()

boundary_vertices = [vertex for boundary in remeshed.vertices_on_boundaries() for vertex in boundary]

for i in range(5):
    trimesh_remesh(
        remeshed,
        kmax=30,
        target=0.75 * length,
        allow_boundary_split=True,
        allow_boundary_swap=True,
        allow_boundary_collapse=True,
        fixed=boundary_vertices
    )
    project(i)


# 3. smooth and project to original triangulated mesh
remeshed.smooth_area(fixed=boundary_vertices, kmax=50, callback=project)


# 4. export remshed mesh data to a new file
file_out_name = '02_remeshed_mesh.json'
file_out_path = os.path.join(dirname, file_out_name)
compas.json_dump(remeshed, file_out_path, pretty=True)


# 4. visualise the mesh
viewer = App()

# viewer.add(
#     trimesh,
#     show_faces=False,
#     show_edges=True,
#     linecolor=(1, 0, 0))

viewer.add(remeshed)
viewer.show()
