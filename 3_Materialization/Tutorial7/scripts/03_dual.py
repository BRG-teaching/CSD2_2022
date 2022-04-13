import os
import compas

from compas.datastructures  import Mesh
from compas_cgal.meshing import remesh
from compas_cgal.subdivision import catmull_clark
from compas_view2.app import App


# 1. load triangulated mesh from step 2
dirname = os.path.dirname(__file__)
filename = '02_remeshed_mesh.json'
filepath = os.path.join(dirname, filename)

remeshed_mesh = compas.json_load(filepath)


# 2. make dual mesh
dual_mesh = remeshed_mesh.dual()


# 3. export dual mesh data to a new file
dirname = os.path.dirname(__file__)
filename = '03_dual_mesh.json'
filepath = os.path.join(dirname, filename)
compas.json_dump(remeshed_mesh, filepath, pretty=True)


# 4. visualise the mesh
viewer = App()

viewer.add(dual_mesh)
viewer.show()
