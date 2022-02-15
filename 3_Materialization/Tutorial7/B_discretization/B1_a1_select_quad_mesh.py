#select rhino quad mesh and convert to compas quad mesh
# ==============================================================================
#Imports
# ==============================================================================
import compas_rhino
from compas_rhino.geometry import RhinoMesh
from compas.datastructures import Mesh
from compas_rhino.artists import MeshArtist

# ==============================================================================
#Select inputs
# ==============================================================================
guid = compas_rhino.select_mesh()
quad_mesh = RhinoMesh.from_guid(guid).to_compas()

# ==============================================================================
# Visualize Rhino
# ==============================================================================
baselayer = "CSD2::BRICK_PATTERN"
artist = MeshArtist(quad_mesh, layer=baselayer+"::input_quad_mesh")
artist.clear_layer()
artist.draw_faces(join_faces=True)
artist.draw_vertices()
artist.draw_edges()
artist.draw()

if __name__ == '__main__':
    pass

