# ==============================================================================
#Imports
# ==============================================================================
import os
from compas.datastructures import Mesh, mesh_flip_cycles
from compas_rhino.artists import MeshArtist

# ==============================================================================
#Load data
# ==============================================================================
HERE = os.path.dirname(__file__)

FILE_I = os.path.join(HERE, 'data', 'form_dual.json')

mesh = Mesh.from_json(FILE_I)
#================================================
#Visualize
#================================================
artist = MeshArtist(mesh, layer="CSD2::DISCRETIZATION::normals")
artist.clear_layer()
artist.draw_edges()
artist.draw_vertexnormals(scale=1)
