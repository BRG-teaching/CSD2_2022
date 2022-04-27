import os
import compas

from compas.datastructures  import Mesh
from compas_view2.app import App


# folder location
dirname = os.path.dirname(__file__) + "/data"


# 1. load thrust file from RV2
file_in_name = 'square_base_thrust.json'
file_in_path = os.path.join(dirname, file_in_name)
rv2_data = compas.json_load(file_in_path)


# 2. extract thrustdiagram data only
thrust_data = rv2_data['data']['thrust']


# 3. recreate thrustdiagram as a mesh from thrustdiagram data
thrust_mesh = Mesh.from_data(thrust_data)


# 4. export mesh data to a new file
file_out_name = '00_thrust_mesh.json'
file_out_path = os.path.join(dirname, file_out_name)
compas.json_dump(thrust_mesh, file_out_path, pretty=True)


# 5. visualise the mesh
viewer = App()
viewer.add(thrust_mesh)
viewer.show()
