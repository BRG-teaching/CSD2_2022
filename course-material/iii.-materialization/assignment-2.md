# Assignment 2

## Assignment II: Convex Polygon Blocks&#x20;

{% hint style="warning" %}
Complete the tasks below, and submit a zipped folder that includes

1. the completed files or other deliverables
2. and the PDF

by **15:00 on Thursday, April 28th**.

Please follow the file naming convention as shown in the [**Syllabus**](../../syllabus.md). \\

#### [Submit assignment 2 here.](https://www.dropbox.com/request/TxQvRLXEvjDv2CkKQOZp)
{% endhint %}

{% embed url="https://colab.research.google.com/github/BlockResearchGroup/CSD2_2022/blob/main/3_Materialization/Tutorial7/assignment2.ipynb" %}

## Tasks

Complete the following Assignment following the steps below:

Use the [Assignment 2 Jupyter Notebook](https://colab.research.google.com/github/BlockResearchGroup/CSD2\_2022/blob/main/2\_Geometry/Tutorial3/week\_3\_assignment.ipynb) to develop your answer.

Then answer the questions on the following document:

{% file src="../../.gitbook/assets/CSD2_2022_Assignment-2_template.docx" %}

## Assignment

In this assignment, we will generate polygon blocks for the form-found barrel vault**.**

****

![Barrel Vault Quad Mesh ](../../3\_Materialization/Tutorial7/img/brick3.png)

![Tessellation Pattern ](../../3\_Materialization/Tutorial7/img/hex0.png)

### Steps:

* **A. Load Mesh**
* **B. Compute Tessellation Pattern**\
  The input mesh is a quad mesh, A hexagonal polygon can be generated with the vertices around two adjacent quad faces. You can modify the vertex coordinates in the quadmesh. Serialize the modified quad mesh.\
  Secondly, find the correct vertices in each block. Create a list,`block_faces`, and save the vertices on each block as a list in `block_faces`. Serialize the `block_faces`.\
  Visualize the blocks as `Polygon` in the viewer.\

* **C. Generate Blocks**\
  Create a function `generate_block`. The input parameter is **the modified quad mesh**, **vertices on one block**, and **thickness of the block**. The function should return a 3D block, which has a planar top surface.\
  Call the function to generate all the blocks for the barrel vault. Serialize the blocks and visualize them in the viewer.\


```python
# % pip install compas_notebook
```

### A. Load Mesh

```python
from compas.datastructures import Mesh
from compas_notebook.app import App

mesh= Mesh.from_obj("https://raw.githubusercontent.com/BlockResearchGroup/CSD2_2022/main/3_Materialization/Tutorial6/data/barrel_vault.obj")

viewer = App()
viewer.add(mesh)
viewer.show()
```

### B1. Modify the Quad Mesh

Keep the topology of the mesh and modify the coordinates of the vertices in the mesh.

```python
import os
import compas
from compas.geometry import subtract_vectors, add_vectors, scale_vector
from compas.datastructures import Mesh
from compas_notebook.app import App
from google.colab import drive
from google.colab import files

mesh= Mesh.from_obj("https://raw.githubusercontent.com/BlockResearchGroup/CSD2_2022/main/3_Materialization/Tutorial6/data/barrel_vault.obj")

# modify the quad mesh...
s_f = 0.15

# find a corner vertex
vkey = list(mesh.vertices_where({'vertex_degree':2}))[0]

# find vertex neighbours
n_1, n_2 = mesh.vertex_neighbors(vkey)

# find two boundary loops
loop_1 = mesh.edge_loop((vkey, n_1))
loop_2 = mesh.edge_loop((vkey, n_2))

# find the shorter boundary loop
if len(loop_1) < len(loop_2):
    short_bdr_loop = loop_1
else:
    short_bdr_loop = loop_2

for i, (u, v) in enumerate(short_bdr_loop):
    if mesh.halfedge_face(u, v) is None:
        u, v = v, u
    strips = mesh.edge_strip((u,v))
    for j, strip in enumerate(strips): 
        a, b = mesh.edge_coordinates(*strip)
        if i % 2 == 0:
            if j  % 2 == 0:
                v_ab = subtract_vectors(a, b)
                a_off = add_vectors(a, scale_vector(v_ab, s_f))
                if mesh.is_vertex_on_boundary(strip[0]) == False:
                    mesh.vertex_attributes(strip[0], "xyz", a_off)
                    st = a_off
                else:
                    st = a
                v_ba = subtract_vectors(b, a)
                b_off = add_vectors(b, scale_vector(v_ba, s_f))
                if mesh.is_vertex_on_boundary(strip[1]) == False:
                    mesh.vertex_attributes(strip[1], "xyz", b_off)
                    ed = b_off
                else:
                    ed = b
                
            else:
                pass
                # viewer.add(Line(a, b), linecolor=(1.0, 0.0, 0))
        else:
            if j  % 2 == 0:
                pass
                # viewer.add(Line(a, b), linecolor=(1.0, 0.0, 0))
            else:
                v_ab = subtract_vectors(a, b)
                a_off = add_vectors(a, scale_vector(v_ab, s_f))
                if mesh.is_vertex_on_boundary(strip[0]) == False:
                    mesh.vertex_attributes(strip[0], "xyz", a_off)
                    st = a_off
                else:
                    st = a
                v_ba = subtract_vectors(b, a)
                b_off = add_vectors(b, scale_vector(v_ba, s_f))
                if mesh.is_vertex_on_boundary(strip[1]) == False:
                    mesh.vertex_attributes(strip[1], "xyz", b_off)
                    ed = b_off
                else:
                    ed = b

# export modified mesh data to a new file
drive.mount('/content/drive')
dirname = '/content/drive/My Drive/Colab Notebooks'
file_out_name = '01_modified_barrel_vault.json'
file_out_path = os.path.join(dirname, file_out_name)
compas.json_dump(mesh, file_out_path, pretty=True)

# visualization
viewer = App()
viewer.add(mesh)
viewer.show()
```

### B2. 2D Block

```python
import os
import compas
from compas.geometry import Polygon
from compas.datastructures import Mesh
from compas_notebook.app import App
from random import random
from compas.utilities import i_to_rgb

# folder location
dirname = '/content/drive/My Drive/Colab Notebooks'

# load modified mesh from step B1
file_in_name = '01_modified_barrel_vault.json'
file_in_path = os.path.join(dirname, file_in_name)
mesh: Mesh = compas.json_load(file_in_path)

# vertices on the block
block_faces = []

# your code here...
for i, (u, v) in enumerate(short_bdr_loop):
    if mesh.halfedge_face(u, v) is None:
        u, v = v, u
    strips = mesh.edge_strip((u,v))
    for j, strip in enumerate(strips): 
        a, b = mesh.edge_coordinates(*strip)
        if i % 2 == 0:
            if j  % 2 == 0:
                v_ab = subtract_vectors(a, b)
                a_off = add_vectors(a, scale_vector(v_ab, s_f))
                if mesh.is_vertex_on_boundary(strip[0]) == False:
                    mesh.vertex_attributes(strip[0], "xyz", a_off)
                    st = a_off
                else:
                    st = a
                v_ba = subtract_vectors(b, a)
                b_off = add_vectors(b, scale_vector(v_ba, s_f))
                if mesh.is_vertex_on_boundary(strip[1]) == False:
                    mesh.vertex_attributes(strip[1], "xyz", b_off)
                    ed = b_off
                else:
                    ed = b

                if mesh.is_edge_on_boundary(*strip) == False:
                    fkey1 = mesh.halfedge_face(*strip)
                    fkey2 = mesh.halfedge_face(*strip[::-1])
                    v0 = mesh.face_vertex_after(fkey2, strip[0])
                    v1 = strip[0]
                    v2 = mesh.face_vertex_before(fkey1, strip[0])
                    v3 = mesh.face_vertex_before(fkey1, v2)
                    v4 = strip[1]
                    v5 = mesh.face_vertex_after(fkey2, v0)
                    block_faces.append([v0, v1, v2, v3, v4, v5,])
                else:
                    fkey = mesh.halfedge_face(*strip)
                    if fkey is not None:
                        block_faces.append(mesh.face_vertices(fkey))
                    fkey = mesh.halfedge_face(*strip[::-1])
                    if fkey is not None:
                        block_faces.append(mesh.face_vertices(fkey))
        else:
            if j  % 2 != 0:
                if mesh.is_edge_on_boundary(*strip) == False:
                    fkey1 = mesh.halfedge_face(*strip)
                    fkey2 = mesh.halfedge_face(*strip[::-1])
                    v0 = mesh.face_vertex_after(fkey2, strip[0])
                    v1 = strip[0]
                    v2 = mesh.face_vertex_before(fkey1, strip[0])
                    v3 = mesh.face_vertex_before(fkey1, v2)
                    v4 = strip[1]
                    v5 = mesh.face_vertex_after(fkey2, v0)
                    block_faces.append([v0, v1, v2, v3, v4, v5,])
                else:
                    fkey = mesh.halfedge_face(*strip)
                    if fkey is not None:
                        block_faces.append(mesh.face_vertices(fkey))
                    fkey = mesh.halfedge_face(*strip[::-1])
                    if fkey is not None:
                        block_faces.append(mesh.face_vertices(fkey))


# export block_faces
compas.json_dump(block_faces, os.path.join(dirname, "02_block_faces.json"))

# visualization
viewer = App()
# visualize the blocks
for block_face in block_faces:
    v_xyz = [mesh.vertex_coordinates(vkey) for vkey in block_face]
    viewer.add(Polygon(v_xyz), facecolor = i_to_rgb(random(), normalize=True))
viewer.show()
```

## C. Generate Blocks

```python
from compas.geometry import bestfit_plane, intersection_line_plane

def generate_block(mesh, block_face, thickness):
    # top vertices
    top = []
    for vertex in block_face:
      point = mesh.vertex_coordinates(vertex)
      normal = mesh.vertex_normal(vertex)
      top.append(add_vectors(point, scale_vector(normal, -0.5 * thickness)))
    
    # bottom vertices
    bottom = []
    for vertex in block_face:
      point = mesh.vertex_coordinates(vertex)
      normal = mesh.vertex_normal(vertex)
      bottom.append(add_vectors(point, scale_vector(normal, 0.5 * thickness)))

    # flatten the top
    plane = bestfit_plane(top)
    top_new = []
    for a, b in zip(bottom, top):
        b = intersection_line_plane((a, b), plane)
        top_new.append(b)
    vertices = top_new + bottom

    # face vertices
    f = len(block_face)

    faces = [
        list(range(f)),
        list(range(f + f - 1, f - 1, -1))]

    for i in range(f - 1):
        faces.append([i, i + f, i + f + 1, i + 1])
        faces.append([f - 1, f + f - 1, f, 0])

    block = Mesh.from_vertices_and_faces(vertices, faces)

    return block


```

```python
import os
import compas

from compas.datastructures import Mesh
from compas_notebook.app import App

# folder location
dirname = '/content/drive/My Drive/Colab Notebooks'

# load modified mesh from step B1
file_in_name = '01_modified_barrel_vault.json'
file_in_path = os.path.join(dirname, file_in_name)
mesh: Mesh = compas.json_load(file_in_path)

# load block faces
block_faces = compas.json_load(os.path.join(dirname, "02_block_faces.json"))

# generate blocks...
blocks = []
thickness = 5
for block_face in block_faces:
   block = generate_block(mesh, block_face, thickness)
   blocks.append(block)

# visualization
viewer = App()
for block in blocks:
    viewer.add(block)
viewer.show()
```
