import os
import compas

from compas.datastructures  import Mesh
from compas_view2.app import App


# 1. load triangulated mesh from step 2
dirname = os.path.dirname(__file__)
filename = '03_dual_mesh.json'
filepath = os.path.join(dirname, filename)

remeshed_mesh = compas.json_load(filepath)


# 2. make dual mesh
dual_mesh = remeshed_mesh.dual()


# 3. add boundary faces to dual mesh
boundary_vertices = remeshed_mesh.vertices_on_boundary()

seen = {}

for vertex in boundary_vertices:

    dual_face = []

    nbrs = remeshed_mesh.vertex_neighbors(vertex, ordered=True)
    for nbr in nbrs[::-1]:

        if remeshed_mesh.is_edge_on_boundary(vertex, nbr):
            if frozenset((vertex, nbr)) in seen:
                mp = seen[frozenset((vertex, nbr))]
            else:
                x, y, z = remeshed_mesh.edge_midpoint(vertex, nbr)
                mp = dual_mesh.add_vertex(x=x, y=y, z=z)
            dual_face.append(mp)
            seen[frozenset((vertex, nbr))] = mp

        face = remeshed_mesh.halfedge[vertex][nbr]
        if face is not None:
            dual_face.append(face)

    dual_mesh.add_face(dual_face[::-1], fkey=vertex)


# 4. export dual mesh data to a new file
dirname = os.path.dirname(__file__)
filename = '04_dual_mesh_with_boundary.json'
filepath = os.path.join(dirname, filename)
compas.json_dump(dual_mesh, filepath, pretty=True)


# 4. visualise the mesh
viewer = App()
viewer.add(dual_mesh)
viewer.show()
