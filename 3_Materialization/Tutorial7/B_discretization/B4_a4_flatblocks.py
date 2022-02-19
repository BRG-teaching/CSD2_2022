# ==============================================================================
#Imports
# ==============================================================================
import os
import compas
from compas.datastructures import Mesh, mesh_flip_cycles
from compas.geometry import intersection_line_plane
from compas_rhino.artists import MeshArtist
from compas_cloud import Proxy
from compas_rv2.rhino import rv2_error

errorHandler = rv2_error(title='Server side Error', showLocalTraceback=False)
proxy = Proxy(errorHandler=errorHandler, background=False)

bestfit = proxy.function('compas.geometry.bestfit_plane_numpy')

HERE = os.path.dirname(__file__)
FILE_I = os.path.join(HERE,'data', 'blocks.json')
FILE_O = os.path.join(HERE, 'data', 'blocksflat.json')

blocks = compas.json_load(open(FILE_I, 'r'))

for block in blocks:
    bottom = block.face_vertices(0)
    top = block.face_vertices(1)[::-1]

    bottom_points = block.vertices_attributes('xyz', keys=bottom)
    top_points = block.vertices_attributes('xyz', keys=top)

    plane = bestfit(bottom_points)

    top_new = []
    for a, b in zip(bottom_points, top_points):

        b = intersection_line_plane((a,b), plane)
        top_new.append(b)

    for vertex, point in zip(bottom, bottom_points):
        block.vertex_attributes(vertex, 'xyz', point)

# # ==============================================================================
# #Output
# # ==============================================================================

compas.json_dump(blocks, open(FILE_O, 'w+'))

# #================================================
# #Visualize
# #================================================

artist = MeshArtist(None, layer="CSD2::DISCRETIZATION::BlocksFlat")
artist.clear_layer()

for block in blocks:
    artist.mesh = block
    artist.draw_faces(color=(0, 255, 0), join_faces=True)
    artist.draw_edges()

artist.redraw()
