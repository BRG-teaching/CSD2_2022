import os
import compas

from compas.datastructures  import Mesh
from compas_view2.app import App


# folder location
dirname = os.path.dirname(__file__) + "/data"


# 1. load remeshed_mesh from step 2
file_in_name = '02_remeshed_mesh.json'
file_in_path = os.path.join(dirname, file_in_name)
remeshed: Mesh = compas.json_load(file_in_path)


# 2. make dual mesh
dual_mesh: Mesh = remeshed.dual()
dual_mesh.flip_cycles()


# 3. add boundary vertices to dual mesh
edge_vertex = {}
for u, v in remeshed.edges_on_boundary():
    x, y, z = remeshed.edge_midpoint(u, v)
    edge_vertex[u, v] = edge_vertex[v, u] = dual_mesh.add_vertex(x=x, y=y, z=z)


# 4. add boundary faces
for vertex in remeshed.vertices_on_boundary():
    vertices = []
    nbrs = remeshed.vertex_neighbors(vertex, ordered=True)[::-1]
    vertices.append(edge_vertex[vertex, nbrs[0]])
    for nbr in nbrs[:-1]:
        vertices.append(remeshed.halfedge_face(vertex, nbr))
    vertices.append(edge_vertex[vertex, nbrs[-1]])
    dual_mesh.add_face(vertices)


# 5. export complete dual mesh data to a new file
file_out_name = '04_dual_mesh_with_boundary.json'
file_out_path = os.path.join(dirname, file_out_name)
compas.json_dump(dual_mesh, file_out_path, pretty=True)


# 4. visualise the mesh
viewer = App()

# show remeshed mesh in red
viewer.add(
    remeshed,
    show_faces=False,
    show_edges=True,
    show_vertices=True,
    vertices=remeshed.vertices_on_boundary(),
    linecolor=(1, 0, 0),
    pointcolor=(1, 0, 0))

# show dual mesh faces
viewer.add(
    dual_mesh,
    faces=dual_mesh.faces_on_boundary(),
    facecolor=(0.5, 0.5, 0.5),
    linecolor=(0, 0, 0))
viewer.show()
