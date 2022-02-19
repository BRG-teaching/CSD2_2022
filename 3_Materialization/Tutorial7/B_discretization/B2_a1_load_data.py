# ==============================================================================
#Imports
# ==============================================================================
import os
import json

from compas.datastructures import Mesh
from compas_rhino.artists import MeshArtist

# ==============================================================================
#Load data
# ==============================================================================

HERE = os.path.dirname(__file__)
FILE_I = os.path.join(HERE, 'data', 'brick_pattern_data.json')

mesh = Mesh.from_json(FILE_I)

#================================================
#Visualize
#================================================
artist = MeshArtist(mesh, layer="CSD2::hexagonal_tess::Load")
artist.clear_layer()
artist.draw_faces()
artist.draw_facelabels()
artist.draw_vertices()
artist.draw_vertexlabels()
artist.draw_edges()
artist.redraw()

if __name__ == '__main__':
    pass
