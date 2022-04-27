import os
import compas

from compas.datastructures  import Mesh
from compas_view2.app import App

from compas.geometry import add_vectors, scale_vector


# folder location
dirname = os.path.dirname(__file__) + "/data"


# 1. load dual_mesh from step 4
file_in_name = '04_dual_mesh_with_boundary.json'
file_in_path = os.path.join(dirname, file_in_name)
dual_mesh: Mesh = compas.json_load(file_in_path)


# 2. make two meshes for intrados and extrados
idos = dual_mesh.copy()
edos = dual_mesh.copy()


# 3. offset intrados and extrados

thickness = 0.5

for vertex in dual_mesh.vertices():
    point = dual_mesh.vertex_coordinates(vertex)
    normal = dual_mesh.vertex_normal(vertex)

    idos.vertex_attributes(vertex, 'xyz', add_vectors(point, scale_vector(normal, -0.5 * thickness)))
    edos.vertex_attributes(vertex, 'xyz', add_vectors(point, scale_vector(normal, 0.5 * thickness)))


# 4. export intrados to a new file
idos_out_name = '05_idos.json'
idos_out_path = os.path.join(dirname, idos_out_name)
compas.json_dump(idos, idos_out_path, pretty=True)


# 5. export extrados to a new file
edos_out_name = '05_edos.json'
edos_out_path = os.path.join(dirname, edos_out_name)
compas.json_dump(edos, edos_out_path, pretty=True)


# 6. visualise intrados and extrados
viewer = App()
viewer.add(dual_mesh)
viewer.add(idos, facecolor=(1, 0, 0))
viewer.add(edos, facecolor=(0, 0, 1))
viewer.show()
