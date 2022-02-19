# ==============================================================================
#Imports
# ==============================================================================
import os

from compas.datastructures import Mesh
from compas_rhino.artists import MeshArtist
import compas_rhino
from compas_rhino.geometry import RhinoMesh

# ==============================================================================
#Load data
# ==============================================================================

HERE = os.path.dirname(__file__)
FILE_I = os.path.join(HERE, 'data', 'form.json')
FILE_O = os.path.join(HERE, 'data', 'form_trimesh.json')

form = Mesh.from_json(FILE_I)

form.quads_to_triangles()

form.to_json(FILE_O)

#================================================
#Visualize
#================================================

artist = MeshArtist(form, layer="CSD2::DISCRETIZATION::triangulate")
artist.clear_layer()
artist.draw_faces(join_faces=True)
artist.draw_edges()
