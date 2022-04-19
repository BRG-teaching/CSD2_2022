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

````python
from compas.datastructures import Mesh
from compas_notebook.app import App

mesh= Mesh.from_obj("https://raw.githubusercontent.com/BlockResearchGroup/CSD2_2022/main/3_Materialization/Tutorial6/data/barrel_vault.obj")

viewer = App()
viewer.add(mesh)
viewer.show()


# B. Compute Tessellation Pattern



## B1. Modify the Quad Mesh
Keep the topology of the mesh and modify the coordinates of the vertices in the mesh. 


```python
import os
import compas
from compas.datastructures import Mesh
from compas_notebook.app import App

mesh= Mesh.from_obj("https://raw.githubusercontent.com/BlockResearchGroup/CSD2_2022/main/3_Materialization/Tutorial6/data/barrel_vault.obj")

# modify the quad mesh...

# export modified mesh data to a new file
dirname = '/content/drive/My Drive/Colab Notebooks'
file_out_name = '01_modified_barrel_vault.json'
file_out_path = os.path.join(dirname, file_out_name)
compas.json_dump(mesh, file_out_path, pretty=True)

# visualization
viewer = App()
viewer.add(mesh)
viewer.show()
````

### B2. 2D Block

```python
import os
import compas
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
def generate_block(mesh, block_face, thickness):
    # your code here...
    pass
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
block_faces = compas.json_load(os.path.join(here, "02_block_faces.json"))

# generate blocks...
blocks = []

# export blocks to a new file...

# visualization
viewer = App()
for block in blocks:
    viewer.add(block)
viewer.show()
```
