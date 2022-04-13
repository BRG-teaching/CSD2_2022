import os
import compas

from compas.datastructures  import Mesh
from compas_view2.app import App


# 1. load thrust json from rv2
thrust_from_rv2 = open('3_Materialization/Tutorial7/scripts/square_base_thrust.json')
thrustdiagram_from_rv2 = compas.json_load(thrust_from_rv2)


# 2. extract thrustdiagram data
thrust_data = thrustdiagram_from_rv2['data']['thrust']


# 3. recreate thrustdiagram as a mesh from thrustdiagram data
thrust_mesh = Mesh.from_data(thrust_data)


# 4. export mesh data to a new file
dirname = os.path.dirname(__file__)
filename = '00_thrust_mesh.json'
filepath = os.path.join(dirname, filename)
compas.json_dump(thrust_mesh, filepath, pretty=True)


# 5. visualise the mesh
viewer = App()
viewer.add(thrust_mesh)
viewer.show()
