# ==============================================================================
#Imports
# ==============================================================================
import os
import compas

from compas.datastructures import Mesh, meshes_join_and_weld
from compas_rhino.artists import MeshArtist
import compas_rhino
from compas_rhino.geometry import RhinoMesh

# ==============================================================================
#Load data
# ==============================================================================
HERE = os.path.dirname(__file__)
FILE_O = os.path.join(HERE, 'data', 'form.json')

guids = compas_rhino.select_meshes()

meshes = []
for guid in guids:
    mesh = RhinoMesh.from_guid(guid).to_compas()
    meshes.append(mesh)

mesh_fix = meshes_join_and_weld(meshes)
mesh.unify_cycles()
mesh_fix.to_json(FILE_O)

#================================================
#Visualize
#================================================
artist = MeshArtist(mesh_fix, layer="CSD2::DISCRETIZATION::mesh")
artist.clear_layer()
artist.draw_faces(join_faces=True)
artist.draw_edges()

