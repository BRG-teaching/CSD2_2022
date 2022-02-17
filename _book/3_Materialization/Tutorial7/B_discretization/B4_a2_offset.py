# ==============================================================================
#Imports
# ==============================================================================
import os

from compas.geometry import add_vectors, scale_vector
from compas.datastructures import Mesh
from compas_rhino.artists import MeshArtist

# ==============================================================================
#Load data
# ==============================================================================

HERE = os.path.dirname(__file__)

FILE_I = os.path.join(HERE, 'data', 'form_dual.json')

FILE_O1 = os.path.join(HERE, 'data', 'form_idos.json')
FILE_O2 = os.path.join(HERE, 'data', 'form_edos.json')

mesh = Mesh.from_json(FILE_I)

idos = mesh.copy()
edos = mesh.copy()

for vertex in mesh.vertices():
    point = mesh.vertex_coordinates(vertex)
    normal = mesh.vertex_normal(vertex)
    thickness = 0.1
    idos.vertex_attributes(vertex, 'xyz', add_vectors(point, scale_vector(normal, thickness)))
    edos.vertex_attributes(vertex, 'xyz', add_vectors(point, scale_vector(normal, -1* thickness)))

# ==============================================================================
#Output
# ==============================================================================

idos.to_json(FILE_O1,  pretty=True)
edos.to_json(FILE_O2)

#================================================
#Visualize
#================================================
artist = MeshArtist(None)

artist.mesh = idos
artist.layer = "CSD2::DISCRETIZATION::offset::Idos"
artist.clear_layer()
artist.draw_faces(color=(255, 0, 0))

artist.mesh = edos
artist.layer = "CSD2::DISCRETIZATION::offset::Edos"
artist.clear_layer()
artist.draw_faces(color=(0, 0, 255))
