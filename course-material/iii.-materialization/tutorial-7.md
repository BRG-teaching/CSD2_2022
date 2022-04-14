# Tutorial 7

## Computational Structural Design II - Materialization of Thrust Networks

#### Learning Goal:

*

#### Content:

1. Load Thrustdiagram
2. Triangulation
3. Remesh
4. Dual
5. Boundary Dual Faces
6. Offsets
7. Blocks
8. Flat Top

#### Google Colab:

[https://colab.research.google.com/github/BlockResearchGroup/CSD2\_2022/blob/main/3\_Materialization/Tutorial7/tutorial7.ipynb](https://colab.research.google.com/github/BlockResearchGroup/CSD2\_2022/blob/main/3\_Materialization/Tutorial7/tutorial7.ipynb)

***

```python
# % pip install compas_notebook
# % pip install requests
```

***

## 0. Load Thrustdiagram

```python
import os
import compas
from google.colab import drive
from google.colab import files

from compas.datastructures  import Mesh
from compas_notebook.app import App


# 1. load thrust json from rv2
thrust_from_rv2 = "https://raw.githubusercontent.com/BlockResearchGroup/CSD2_2022/main/3_Materialization/Tutorial7/scripts/data/hole_vault_thrust.json"
thrustdiagram_from_rv2 = compas.json_load(thrust_from_rv2)


# 2. extract thrustdiagram data
thrust_data = thrustdiagram_from_rv2['data']['thrust']


# 3. recreate thrustdiagram as a mesh from thrustdiagram data
thrust_mesh = Mesh.from_data(thrust_data)


# 4. export mesh data to a new file in google drive

filename = '00_thrust_mesh.json'

# saving to google drive
drive.mount('/content/drive')
dirname = '/content/drive/My Drive/Colab Notebooks'
googledrive_path = os.path.join(dirname, filename)
compas.json_dump(thrust_mesh, googledrive_path, pretty=True)

# # saving to local
# compas.json_dump(thrust_mesh, filename, pretty=True)
# files.download(filename)


# 5. visualise the mesh
viewer = App()
viewer.add(thrust_mesh)
viewer.show()
```

***

## 1. Triangulation

```python
import os
import compas
from google.colab import files

from compas.datastructures  import Mesh
from compas_notebook.app import App


# folder location
dirname = '/content/drive/My Drive/Colab Notebooks'


# 1. load thrust_mesh from step 0
file_in_name = '00_thrust_mesh.json'
file_in_path = os.path.join(dirname, file_in_name)
thrust_mesh: Mesh = compas.json_load(file_in_path)


# 2. triangulate the quad faces of the thrust_mesh
tri_mesh = thrust_mesh.copy()
tri_mesh.quads_to_triangles()


# 3. export triangulated mesh data to a new file
file_out_name = '01_triangulated_mesh.json'
file_out_path = os.path.join(dirname, file_out_name)
compas.json_dump(tri_mesh, file_out_path, pretty=True)


# 4. visualise the mesh
viewer = App()
viewer.add(thrust_mesh)
viewer.add(tri_mesh)
viewer.show()
```

***

## 2. Remesh

```python
import os
import compas
import requests

from compas.datastructures  import Mesh
from compas_notebook.app import App

from compas.datastructures import trimesh_pull_points_numpy

url = "https://raw.githubusercontent.com/BlockResearchGroup/CSD2_2022/main/3_Materialization/Tutorial7/scripts/trimesh_remesh.py"
r = requests.get(url)
with open('trimesh_remesh.py', 'w') as f:
    f.write(r.text)

from trimesh_remesh import trimesh_remesh


# folder location
dirname = '/content/drive/My Drive/Colab Notebooks'


# 1. load triangulated mesh from step 1
file_in_name = '01_triangulated_mesh.json'
file_in_path = os.path.join(dirname, file_in_name)
trimesh: Mesh = compas.json_load(file_in_path)


# 2. remesh the triangulated mesh

# function for projecting back to the original mesh
def project(k, callback_args=None):
    xyz = remeshed.vertices_attributes("xyz")
    xyz = trimesh_pull_points_numpy(trimesh, xyz)
    for index, vertex in enumerate(remeshed.vertices()):
        remeshed.vertex_attributes(vertex, "xyz", xyz[index])

# remeshing
remeshed = trimesh.copy()
lengths = [trimesh.edge_length(*edge) for edge in trimesh.edges()]
length = sum(lengths) / trimesh.number_of_edges()

boundary_vertices = [vertex for boundary in remeshed.vertices_on_boundaries() for vertex in boundary]

for i in range(5):
    trimesh_remesh(
        remeshed,
        kmax=30,
        target=0.75 * length,
        allow_boundary_split=True,
        allow_boundary_swap=True,
        allow_boundary_collapse=True,
        fixed=boundary_vertices
    )
    project(i)


# 3. smooth and project to original triangulated mesh
remeshed.smooth_area(fixed=boundary_vertices, kmax=50, callback=project)


# 4. export remshed mesh data to a new file
file_out_name = '02_remeshed_mesh.json'
file_out_path = os.path.join(dirname, file_out_name)
compas.json_dump(remeshed, file_out_path, pretty=True)


# 5. visualise the mesh
viewer = App()
viewer.add(remeshed)
viewer.show()
```

***

## 3. Dual

```python
import os
import compas
import requests

from compas.datastructures  import Mesh
from compas_notebook.app import App

url = "https://raw.githubusercontent.com/BlockResearchGroup/CSD2_2022/main/3_Materialization/Tutorial7/scripts/mesh_dual.py"
r = requests.get(url)
with open('mesh_dual.py', 'w') as f:
    f.write(r.text)

from mesh_dual import mesh_dual


# folder location
dirname = '/content/drive/My Drive/Colab Notebooks'


# 1. load remeshed_mesh from step 2
file_in_name = '02_remeshed_mesh.json'
file_in_path = os.path.join(dirname, file_in_name)
remeshed: Mesh = compas.json_load(file_in_path)


# 2. make dual mesh
dual_mesh: Mesh = mesh_dual(remeshed)


# 3. export dual mesh data to a new file
file_out_name = '03_dual_mesh.json'
file_out_path = os.path.join(dirname, file_out_name)
compas.json_dump(dual_mesh, file_out_path, pretty=True)


# 4. visualise the mesh3
viewer = App()
viewer.add(dual_mesh)
viewer.show()
```

***

## 4. Boundary Dual Faces

```python
import os
import compas

from compas.datastructures  import Mesh
from compas_notebook.app import App

url = "https://raw.githubusercontent.com/BlockResearchGroup/CSD2_2022/main/3_Materialization/Tutorial7/scripts/mesh_dual.py"
r = requests.get(url)
with open('mesh_dual.py', 'w') as f:
    f.write(r.text)

from mesh_dual import mesh_dual


# folder location
dirname = '/content/drive/My Drive/Colab Notebooks'


# 1. load remeshed_mesh from step 2
file_in_name = '02_remeshed_mesh.json'
file_in_path = os.path.join(dirname, file_in_name)
remeshed: Mesh = compas.json_load(file_in_path)


# 2. make dual mesh
dual_mesh: Mesh = remeshed.dual()
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
viewer.add(dual_mesh)
viewer.show()
```

***

## 5. Offsets

```python
import os
import compas

from compas.datastructures  import Mesh
from compas_notebook.app import App

from compas.geometry import add_vectors, scale_vector


# folder location
dirname = '/content/drive/My Drive/Colab Notebooks'


# 1. load dual_mesh from step 4
file_in_name = '04_dual_mesh_with_boundary.json'
file_in_path = os.path.join(dirname, file_in_name)
dual_mesh: Mesh = compas.json_load(file_in_path)


# 2. make two meshes for intrados and extrados
idos = dual_mesh.copy()
edos = dual_mesh.copy()


# 3. offset intrados and extrados

thickness = 0.5

for vertex in dual_mesh.vertices():
    point = dual_mesh.vertex_coordinates(vertex)
    normal = dual_mesh.vertex_normal(vertex)

    idos.vertex_attributes(vertex, 'xyz', add_vectors(point, scale_vector(normal, -0.5 * thickness)))
    edos.vertex_attributes(vertex, 'xyz', add_vectors(point, scale_vector(normal, 0.5 * thickness)))


# 4. export intrados to a new file
idos_out_name = '05_idos.json'
idos_out_path = os.path.join(dirname, idos_out_name)
compas.json_dump(idos, idos_out_path, pretty=True)


# 5. export extrados to a new file
edos_out_name = '05_edos.json'
edos_out_path = os.path.join(dirname, edos_out_name)
compas.json_dump(edos, edos_out_path, pretty=True)


# 6. visualise intrados and extrados
viewer = App()
viewer.add(dual_mesh)
viewer.add(idos)
viewer.add(edos)
viewer.show()
```

***

## 6. Blocks

```python
import os
import compas

from compas.datastructures  import Mesh
from compas_notebook.app import App


# folder location
dirname = '/content/drive/My Drive/Colab Notebooks'


# 1. load idos from step 5
idos_in_name = '05_idos.json'
idos_in_path = os.path.join(dirname, idos_in_name)
idos: Mesh = compas.json_load(idos_in_path)


# 2. load edos from step 5
edos_in_name = '05_edos.json'
edos_in_path = os.path.join(dirname, edos_in_name)
edos: Mesh = compas.json_load(edos_in_path)


# 3. make blocks

blocks = []  # a list of meshes

for face in idos.faces():
    bottom = idos.face_coordinates(face)
    top = edos.face_coordinates(face)

    f = len(bottom)

    faces = [
        list(range(f)),
        list(range(f + f - 1, f - 1, -1))]

    for i in range(f - 1):
        faces.append([i, i + f, i + f + 1, i + 1])
    faces.append([f - 1, f + f - 1, f, 0])

    block = Mesh.from_vertices_and_faces(bottom + top, faces)
    blocks.append(block)


# 4. export blocks to a new file
blocks_out_name = '06_blocks.json'
blocks_out_path = os.path.join(dirname, blocks_out_name)
compas.json_dump(blocks, blocks_out_path, pretty=True)


# 5. visualise the blocks
viewer = App()
for block in blocks:
    viewer.add(block)
viewer.show()
```

***

## 7. Flat Tops

```python
import os
import compas

from compas.datastructures  import Mesh
from compas_notebook.app import App

from compas.geometry import bestfit_plane
from compas.geometry import intersection_line_plane


# folder location
dirname = '/content/drive/My Drive/Colab Notebooks'


# 1. load blocks from step 6
blocks_in_name = '06_blocks.json'
blocks_in_path = os.path.join(dirname, blocks_in_name)

blocks = [block for block in compas.json_load(blocks_in_path)]


# 2. flatten top face of each block
for block in blocks:
    bottom = block.face_vertices(0)
    top = block.face_vertices(1)[::-1]

    bottom_points = block.vertices_attributes('xyz', keys=bottom)
    top_points = block.vertices_attributes('xyz', keys=top)

    plane = bestfit_plane(top_points)

    top_new = []
    for a, b in zip(bottom_points, top_points):
        b = intersection_line_plane((a, b), plane)
        top_new.append(b)

    for vertex, point in zip(top, top_new):
        block.vertex_attributes(vertex, 'xyz', point)


# 4. export blocks to a new file
blocks_out_name = '07_blocks_flat_top.json'
blocks_out_path = os.path.join(dirname, blocks_out_name)
compas.json_dump(blocks, blocks_out_path, pretty=True)


# 4. visualise the blocks
viewer = App()

for block in blocks:
    viewer.add(block)
viewer.show()
```
