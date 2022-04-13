import os
import compas

from compas.datastructures  import Mesh
from compas_view2.app import App


# folder location
dirname = os.path.dirname(__file__) + "/data"


# 1. load thrust_mesh from step 0
file_in_name = '00_thrust_mesh.json'
file_in_path = os.path.join(dirname, file_in_name)
thrust_mesh: Mesh = compas.json_load(file_in_path)


# 2. triangulate the quad faces of the thrust_mesh
tri_mesh = thrust_mesh.copy()
tri_mesh.quads_to_triangles()



# 3. export triangulated mesh data to a new file
file_out_name = '01_triangulated_mesh.json'
file_out_path = os.path.join(dirname, file_out_name)
compas.json_dump(tri_mesh, file_out_path, pretty=True)


# 4. visualise the mesh
viewer = App()

viewer.add(
    thrust_mesh,
    show_faces=False,
    show_edges=True,
    linecolor=(1, 0, 0))

viewer.add(tri_mesh)
viewer.show()
