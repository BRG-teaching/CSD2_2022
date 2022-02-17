# ==============================================================================
#Imports
# ==============================================================================
import os
from compas.datastructures import Mesh
from compas_rhino.artists import MeshArtist

# ==============================================================================
#Load data
# ==============================================================================
HERE = os.path.dirname(__file__)
FILE_I = os.path.join(HERE, 'data', 'form_remeshed.json')
FILE_O = os.path.join(HERE, 'data', 'form_dual.json')

mesh = Mesh.from_json(FILE_I)
dual = mesh.dual()
dual.flip_cycles()
dual.to_json(FILE_O, pretty =True)

#================================================
#Visualize
#================================================
artist = MeshArtist(dual, layer="CSD2::DISCRETIZATION::dual")
artist.clear_layer()
artist.draw_faces()
artist.draw_edges()
