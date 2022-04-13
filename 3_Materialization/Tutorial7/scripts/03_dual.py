import os
import compas

from compas.datastructures  import Mesh
from compas_view2.app import App


# folder location
dirname = os.path.dirname(__file__) + "/data"


# 1. load remeshed_mesh from step 2
file_in_name = '02_remeshed_mesh.json'
file_in_path = os.path.join(dirname, file_in_name)
remeshed: Mesh = compas.json_load(file_in_path)


# 2. make dual mesh
dual_mesh: Mesh = remeshed.dual()


# 3. export dual mesh data to a new file
file_out_name = '03_dual_mesh.json'
file_out_path = os.path.join(dirname, file_out_name)
compas.json_dump(dual_mesh, file_out_path, pretty=True)


# 4. visualise the mesh3
viewer = App()

# show remeshed mesh in red
viewer.add(
    remeshed,
    show_faces=False,
    show_edges=True,
    linecolor=(1, 0, 0))

# show dual mesh faces
viewer.add(dual_mesh)
viewer.show()
