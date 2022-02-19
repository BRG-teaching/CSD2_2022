#create brick tessellation pattern mesh faces
# ==============================================================================
#Imports
# ==============================================================================
import compas_rhino
from compas_rhino.geometry import RhinoMesh
from compas.datastructures import Mesh
from compas_rhino.artists import MeshArtist

from collections import deque
from itertools import islice, chain
# ==============================================================================
#Select inputs
# ==============================================================================
guid = compas_rhino.select_mesh()
quad_mesh = RhinoMesh.from_guid(guid).to_compas()

#initiate new mesh datastructure
brick_tess_mesh = Mesh()

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
    start_loop = mesh.edge_loop(start_edge)

    return corner, start_edge, start_loop

def loop_edges_for_v_coordinates(start_edges, mesh):
    """
    finds the edges loops and add the vertex coordinates in
    a sequence to a list
    Param
    -----
    start_edges: list of Tuples
    edge identifies

    mesh: dict
    COMPAS mesh
    """
    vertices_coordinates = []
    number_of_vertices_in_each_loop = None
    for edge in start_edges:
        edge_loop = mesh.edge_loop(edge)
        number_of_vertices_in_each_loop = (len(edge_loop)+1)
        for i,e_key in enumerate(edge_loop):
            if i==0:
                for v_key in e_key:
                    vertex_coordinates = quad_mesh.vertex_coordinates(v_key, axes='xyz')
                    vertices_coordinates.append(vertex_coordinates)
            else:
                for i,v_key in enumerate(e_key):
                    if i==1:
                        vertex_coordinates = quad_mesh.vertex_coordinates(v_key, axes='xyz')
                        vertices_coordinates.append(vertex_coordinates)

    return vertices_coordinates, number_of_vertices_in_each_loop

def add_vertices(vertices):
    """
    adds vertices to the new mesh in a sequence
    Param
    -----
    vertices: list of lists
    XYZ coordinates of the mesh
    """
    for xyz in vertices:
        v = brick_tess_mesh.add_vertex(x=xyz[0],y=xyz[1],z=xyz[2])

def chunks(items, n):
    items = iter(items)
    for first in items:
        chunk = chain((first,), islice(items, n-1))
        yield chunk
        deque(chunk, 0)

# ==============================================================================
#Create vertices of the Brick Pattern
# ==============================================================================
#Step_1 identify the start vertex, edge and start edge loop
corner, start_edge, start_loop = find_boundary(quad_mesh)

#Step_2 get all the parallel edge loops
parallel_edges = [edge for edge in quad_mesh.edge_strip(start_edge)]

#Step_3 get all the vertex coorinates of the quad mesh
# and the number of vertices in each edge loop
vertices_coordinates, number_of_vertices_in_each_loop = loop_edges_for_v_coordinates(parallel_edges, quad_mesh)

#Step_4 add all the vertex coordinates to the newly create brick tessellation mesh
create_vertices = add_vertices(vertices_coordinates)

# ==============================================================================
#Build faces
# ==============================================================================
#create poly face (make diagram for this)
v_key = [vkey for vkey in brick_tess_mesh.vertices()]

#group v_keys - here we make a nested list of vertices in each edge loop
v_key_chunks = []
for chunk in map(list,chunks(v_key, number_of_vertices_in_each_loop) ):
    v_key_chunks.append(chunk)

#split groups as even and odd course points
even_course_vertices = []
odd_course_vertices = []
for i, chunk in enumerate(v_key_chunks):
    if i%2 == 0:
        even_course_vertices.append(chunk)
    else:
        odd_course_vertices.append(chunk)

#identify start vertex for each face loop in even and odd courses (make diagram for this)
even_course_start_points = []
for chunk in even_course_vertices:
    for j in chunk:
        if j%2 == 0 and j != chunk[-1]:
            even_course_start_points.append(j)

odd_course_start_points = []
half_brick_start_points = []
for chunk in (odd_course_vertices[:-1]):
    for i,j in enumerate(chunk):
        if i==0 or i==(len(chunk)-2):
            half_brick_start_points.append(j)

        elif i>0 and j%2 == 0 and j != chunk[-2]:
            odd_course_start_points.append(j)

# build poly face / full brick
num = number_of_vertices_in_each_loop
for v_key in (even_course_start_points + odd_course_start_points):
    face = [v_key, v_key+1, v_key+2, v_key+num+2, v_key+num+1, v_key+num]
    brick_tess_mesh.add_face(face)

#build hald brick
for v_key in half_brick_start_points:
    face = [v_key, v_key+1, v_key+num+1, v_key+num]
    brick_tess_mesh.add_face(face)

# ==============================================================================
# Visualize Rhino
# ==============================================================================

baselayer = "CSD2::BRICK_PATTERN"
artist = MeshArtist(brick_tess_mesh, layer=baselayer+"::brick_tess_mesh")
artist.clear_layer()
artist.draw_vertices()
artist.draw_vertexlabels()
artist.draw_edges()
artist.draw_faces(join_faces=True,color=(255,0,0))
artist.draw()

if __name__ == '__main__':
    pass

