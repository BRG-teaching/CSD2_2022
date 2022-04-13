import os
import compas

from compas.datastructures  import Mesh
from compas_view2.app import App

from compas.geometry import bestfit_plane
from compas.geometry import intersection_line_plane


# folder location
dirname = os.path.dirname(__file__) + "/data"


# 1. load blocks from step 6
blocks_in_name = '06_blocks.json'
blocks_in_path = os.path.join(dirname, blocks_in_name)

blocks = [block for block in compas.json_load(blocks_in_path)]


# 2. flatten top face of each block
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


# 4. export blocks to a new file
blocks_out_name = '07_blocks_flat_top.json'
blocks_out_path = os.path.join(dirname, blocks_out_name)
compas.json_dump(blocks, blocks_out_path, pretty=True)


# 4. visualise the blocks
viewer = App()

for block in blocks:
    viewer.add(block)
viewer.show()
