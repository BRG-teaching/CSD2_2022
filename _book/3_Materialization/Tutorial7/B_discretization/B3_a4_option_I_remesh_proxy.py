# ==============================================================================
#Imports
# ==============================================================================

import os
from compas.datastructures import Mesh
from compas.rpc import Proxy
from compas.geometry import trimesh_remesh
from compas_rhino.artists import MeshArtist

# ==============================================================================
#Load data
# ==============================================================================
cgal = Proxy('compas_cgal.meshing')

HERE = os.path.dirname(__file__)
FILE_I = os.path.join(HERE, 'data', 'form_trimesh.json')
FILE_O = os.path.join(HERE, 'data', 'form_remeshed.json')

mesh = Mesh.from_json(FILE_I)

lengths = [mesh.edge_length(*edge) for edge in mesh.edges()]
length = sum(lengths) / mesh.number_of_edges()

V, F = cgal.remesh(mesh.to_vertices_and_faces(),length)

mesh = Mesh.from_vertices_and_faces(V, F)

# ==============================================================================
#Output
# ==============================================================================
mesh.to_json(FILE_O)

#================================================
#Visualize
#================================================
artist = MeshArtist(mesh, layer="CSD2::DISCRETIZATION::remesh")
artist.clear_layer()
artist.draw_faces(join_faces=True)
artist.draw_edges()
