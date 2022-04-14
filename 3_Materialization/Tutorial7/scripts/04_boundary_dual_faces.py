import os
import compas

from compas.datastructures  import Mesh
from compas_view2.app import App

from mesh_dual import mesh_dual


# folder location
dirname = os.path.dirname(__file__) + "/data"


# 1. load remeshed_mesh from step 2
file_in_name = '02_remeshed_mesh.json'
file_in_path = os.path.join(dirname, file_in_name)
remeshed: Mesh = compas.json_load(file_in_path)


# 2. make dual mesh
dual_mesh: Mesh = mesh_dual(remeshed)
dual_mesh.flip_cycles()


# 3. add boundary vertices to dual mesh
edge_vertex = {}

boundary_edges = [edge for boundary in remeshed.edges_on_boundaries() for edge in boundary]

for u, v in boundary_edges:
    x, y, z = remeshed.edge_midpoint(u, v)
    edge_vertex[u, v] = edge_vertex[v, u] = dual_mesh.add_vertex(x=x, y=y, z=z)


# 4. add boundary faces

boundary_vertices = [vertex for boundary in remeshed.vertices_on_boundaries() for vertex in boundary]
dual_mesh_vertices = list(dual_mesh.vertices())

for vertex in boundary_vertices:
    x, y, z = remeshed.vertex_coordinates(vertex)
    vertices = [dual_mesh.add_vertex(x=x, y=y, z=z)]
    nbrs = remeshed.vertex_neighbors(vertex, ordered=True)[::-1]
    # vertices.append(edge_vertex[vertex, nbrs[0]])

    for nbr in nbrs:
        if remeshed.is_edge_on_boundary(vertex, nbr):
            vertices.append(edge_vertex[vertex, nbr])

        face = remeshed.halfedge[vertex][nbr]
        if face is not None:
            if face in dual_mesh_vertices:
                vertices.append(face)

    dual_mesh.add_face(vertices)


# 5. export complete dual mesh data to a new file
file_out_name = '04_dual_mesh_with_boundary.json'
file_out_path = os.path.join(dirname, file_out_name)
compas.json_dump(dual_mesh, file_out_path, pretty=True)


# 6. visualise the mesh
viewer = App()

# show remeshed mesh in red
viewer.add(
    remeshed,
    show_faces=False,
    show_edges=True,
    show_vertices=True,
    vertices=boundary_vertices,
    linecolor=(1, 0, 0),
    pointcolor=(1, 0, 0))

# show dual mesh faces

boundary_dual_faces = [face for boundary in dual_mesh.faces_on_boundaries() for face in boundary]

viewer.add(
    dual_mesh,
    faces=boundary_dual_faces,
    facecolor=(0.5, 0.5, 0.5),
    linecolor=(0, 0, 0))
viewer.show()
