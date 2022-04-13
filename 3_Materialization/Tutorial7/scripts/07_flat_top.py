import os
import compas

from compas.datastructures  import Mesh
from compas_cgal.meshing import remesh
from compas_cgal.subdivision import catmull_clark
from compas_view2.app import App

from compas.geometry import bestfit_plane
from compas.geometry import intersection_line_plane

# 1. load triangulated mesh from step 2
dirname = os.path.dirname(__file__)
filename = '06_blocks.json'
filepath = os.path.join(dirname, filename)

blocks = [block for block in compas.json_load(filepath)]



for block in blocks:
    bottom = block.face_vertices(0)
    top = block.face_vertices(1)[::-1]

    bottom_points = block.vertices_attributes('xyz', keys=bottom)
    top_points = block.vertices_attributes('xyz', keys=top)



    plane = bestfit_plane(top_points)



    top_new = []
    for a, b in zip(bottom_points, top_points):
        b = intersection_line_plane((a, b), plane)
        top_new.append(b)

    for vertex, point in zip(top, top_new):
        block.vertex_attributes(vertex, 'xyz', point)



# 4. visualise the mesh
viewer = App()

for block in blocks:
    viewer.add(block)
viewer.show()
