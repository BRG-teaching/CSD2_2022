#find the start vertex, start edge and start edge loop for the input quad mesh
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
#Helper functions
# ==============================================================================
def find_boundary(mesh):
    """
    identifies the start vertex,  its respective edge and its continuous edge loop
    Param
    -----
    mesh: compas quad mesh

    return
    ------
    list of corner vertex key, start edge tuple, list of start edge continuous loop
    """
    corners = list(mesh.vertices_where({'vertex_degree':2}))
    corner = corners[1]

    corner_edges = mesh.vertex_neighbors(corner)
    start_edge = (corner, corner_edges[0])
    print("start_edge", start_edge)

    start_loop = mesh.edge_loop(start_edge)
    print("start_loop", start_loop)

    return corner, start_edge, start_loop

# ==============================================================================
#Create vertices of the Brick Pattern
# ==============================================================================
#Step_1 identify the start vertex, edge and start edge loop
corner, start_edge, start_loop = find_boundary(quad_mesh)

# ==============================================================================
# Visualize Rhino
# ==============================================================================
edgecolor = {}
for edge in start_loop:
    if edge not in quad_mesh.edges():
        edge = (edge[1], edge[0])
    edgecolor[edge] = (0, 255, 0)

if start_edge not in quad_mesh.edges():
    start = (start_edge[1], start_edge[0])
edgecolor[start_edge] = (255, 0, 0)

vertexcolor = {}
vertexcolor[corner] = (255, 0, 0)

baselayer = "CSD2::BRICK_PATTERN"
artist = MeshArtist(quad_mesh, layer=baselayer+"::input_quad_mesh")
artist.clear_layer()
artist.draw_faces(join_faces=True)
artist.draw_vertices(color=vertexcolor)
artist.draw_edges(color=edgecolor)
artist.draw()

if __name__ == '__main__':
    pass

