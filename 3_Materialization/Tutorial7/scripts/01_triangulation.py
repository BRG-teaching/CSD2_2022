import os
import compas

from compas.datastructures  import Mesh
from compas_view2.app import App


# 1. load thrust_mesh from step 0
dirname = os.path.dirname(__file__)
filename = '00_thrust_mesh.json'
filepath = os.path.join(dirname, filename)

thrust_mesh = compas.json_load(filepath)


# 2. triangulate the quad faces of the thrust_mesh
thrust_mesh.quads_to_triangles()


# 3. export triangulated mesh data to a new file
dirname = os.path.dirname(__file__)
filename = '01_triangulated_mesh.json'
filepath = os.path.join(dirname, filename)
compas.json_dump(thrust_mesh, filepath, pretty=True)


# 4. visualise the mesh
viewer = App()
viewer.add(thrust_mesh)
viewer.show()
