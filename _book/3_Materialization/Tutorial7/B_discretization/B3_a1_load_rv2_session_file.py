# ==============================================================================
#Imports
# ==============================================================================
import os
import compas

from compas.datastructures import Mesh
from compas_rhino.artists import MeshArtist

# ==============================================================================
#Load data
# ==============================================================================

HERE = os.path.dirname(__file__)

FILE_I = os.path.join(HERE, 'data', 'armadillo_vertical_new_anchors.rv2')
FILE_O = os.path.join(HERE, 'data', 'form.json')

session = compas.json_load(FILE_I)
form = Mesh.from_data(session['data']['form'])
form.to_json(FILE_O)

#================================================
#Visualize
#================================================

artist = MeshArtist(form, layer="CSD2::DISCRETIZATION::form")
artist.clear_layer()
artist.draw_faces(join_faces=False,faces=list(form.faces_where({'_is_loaded': True})))
artist.draw_edges(edges=list(form.edges_where({'_is_edge': True})))

