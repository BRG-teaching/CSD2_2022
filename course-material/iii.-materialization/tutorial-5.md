# Tutorial 5

## Computational Structural Design II - Geometry, Data and Visualization

#### Learning Goal:

* Understand Mesh Datastructure
* How to Construct a Mesh
* Mehs Vertices, Faces, Edges

#### Content:

* [A. Mesh Introduction](tutorial-5.md#MeshIntro)
* [B. Mesh Vertex, Edge, Face](tutorial-5.md#MeshB)
* [C. Mesh Normals](tutorial-5.md#MeshC)
* [D. Exercise: Geodesic Dome](tutorial-5.md#d.-exercise-geodesic-dome)



***

***

```python
# ! pip install compas_notebook
```

## A. Mesh Introduction

### A1. Mesh in Form Finding

Form finding a cable-net or generating a compression-only vault usually starts with a **2D mesh**, which represents the horizontal projection of the eventual structure. The line segments of this mesh is called **Pattern**. The following picture shows you an existing structure and its corresponding pattern. The form-found **Thrust** is also a mesh, but in 3D space.

![img](https://files.gitbook.com/v0/b/gitbook-legacy-files/o/assets%2F-M730QpQnbAMvz44bqhc%2F-MOff3g181Ib3KNlmKgc%2F-MOfhAWYJRaSfNZucLzL%2Fimage.png?alt=media\&token=839252d4-a77e-42cb-81cf-4b6071a5c598)

Nave Vault of the Sherborne Abbey, Dorset, UK (photo by Lawrence Lew)\


### A2. Generate Polygon - Geometry and Topology

Firstly, let's create 4 polygons using `compas.geometry.Polygon` and visualize them in different colors. Make sure that the winding order (point order) of the polygons are either all clockwise or all counter-clockwise.

![
](../../.gitbook/assets/image.png)

#### A2\_a. Generate Polygon from Points

```python
from compas.geometry import Polygon
from compas_plotters import Plotter

polygon_1 = Polygon([[0, 0, 0], [2.5, 0, 0], [1.5, 2, 0], [0, 2, 0]])
polygon_2 = Polygon([[2.5, 0, 0], [4, 0, 0], [4, 2, 0], [1.5, 2, 0]])
polygon_3 = Polygon([[0, 2, 0], [1.5, 2, 0], [2.5, 4, 0], [0, 4, 0]])
polygon_4 = Polygon([[1.5, 2, 0], [4, 2, 0], [4, 4, 0], [2.5, 4, 0]])

# visualize the Point
plotter = Plotter(show_axes=True)
plotter.add(polygon_1, facecolor=(1, 0, 0))
plotter.add(polygon_2, facecolor=(0, 0, 1))
plotter.add(polygon_3, facecolor=(0, 1, 0))
plotter.add(polygon_4, facecolor=(1, 1, 0))
plotter.zoom_extents()
plotter.show()
```

#### A2\_b. Generate Polygon Using Connectivity

If we change the xyz coordinates of one point in the polygon, the three other polygons will not be influenced. This is because no topological information between the polygons is stored. Another way to construct the polygons is to create a `list` collection contains points information. We can refer to this list to generate the polygons. In this way, we know which points are connected and which are not.

![](<../../.gitbook/assets/image (1).png>)

| Point Index |     xyz     |
| :---------: | :---------: |
|      0      |  (0, 0, 0)  |
|      1      | (2.5, 0, 0) |
|      2      |  (4, 0, 0)  |
|      3      |  (0, 2, 0)  |
|      4      | (1.5, 2, 0) |
|      5      |  (4, 2, 0)  |
|      6      |  (0, 4, 0)  |
|      7      | (2.5, 4, 0) |
|      8      |  (4, 4, 0)  |

\


```python
from compas.geometry import Polygon
from compas_plotters import Plotter

points = [[0, 0, 0], [2.5, 0, 0], [4, 0, 0],
         [0, 2, 0], [1.5, 2, 0], [4, 2, 0],
         [0, 4, 0], [2.5, 4, 0], [4, 4, 0]]
polygon_1 = Polygon([points[0], points[1], points[4], points[3]])
polygon_2 = Polygon([points[1], points[2], points[5], points[4]])
polygon_3 = Polygon([points[3], points[4], points[7], points[6]])
polygon_4 = Polygon([points[4], points[5], points[8], points[7]])

# visualize the Point
plotter = Plotter(show_axes=True)
plotter.add(polygon_1, facecolor=(1, 0, 0))
plotter.add(polygon_2, facecolor=(0, 0, 1))
plotter.add(polygon_3, facecolor=(0, 1, 0))
plotter.add(polygon_4, facecolor=(1, 1, 0))
plotter.zoom_extents()
plotter.show()
```

### A3. Mesh and COMPAS Mesh

A mesh is a collection of polygons arranged in a way that it can not only conserve geometric information but also topological information. Here is the API reference of COMPAS mesh: https://compas.dev/compas/latest/api/generated/compas.datastructures.Mesh.html#compas.datastructures.Mesh

There are different ways to construct a mesh.

#### A3\_a. COMPAS Mesh

```python
from compas.datastructures import Mesh
mesh = Mesh()
print(mesh)
```

```
<Mesh with 0 vertices, 0 faces, 0 edges>
```

#### A3\_b. Build a COMPAS Mesh

Meshes can be built from scratch by adding vertices and faces.

```python
from compas.datastructures import Mesh
from compas_plotters import Plotter

mesh = Mesh()

# add vertices
v_0 = mesh.add_vertex(x=0, y=0, z=0)
v_1 = mesh.add_vertex(x=2.5, y=0, z=0)
v_2 = mesh.add_vertex(x=4, y=0, z=0)
v_3 = mesh.add_vertex(x=0, y=2, z=0)
v_4 = mesh.add_vertex(x=1.5, y=2, z=0)
v_5 = mesh.add_vertex(x=4, y=2, z=0)
v_6 = mesh.add_vertex(x=0, y=4, z=0)
v_7 = mesh.add_vertex(x=2.5, y=4, z=0)
v_8 = mesh.add_vertex(x=4, y=4, z=0)

# add faces

mesh.add_face([v_0, v_1, v_4, v_3])
mesh.add_face([v_1, v_2, v_5, v_4])
mesh.add_face([v_3, v_4, v_7, v_6])
mesh.add_face([v_4, v_5, v_8, v_7])

# visualize the mesh
plotter = Plotter(show_axes=True)
plotter.add(mesh, sizepolicy='absolute')
plotter.zoom_extents()
plotter.show()
```

#### A3\_c. `Mesh.from_vertices_and_faces`

`Mesh.from_vertices_and_faces` construct a mesh object from a list of vertices and faces.\
API reference: https://compas.dev/compas/1.5.0/api/generated/compas.datastructures.Mesh.from\_vertices\_and\_faces.html#compas.datastructures.Mesh.from\_vertices\_and\_faces\
Source code: https://github.com/compas-dev/compas/blob/81606f4580b5d4139e56b592f05354f965954388/src/compas/datastructures/mesh/mesh.py#L440

```python
from compas.datastructures import Mesh
from compas_plotters import Plotter

vertices = [[0, 0, 0], [2.5, 0, 0], [4, 0, 0],
         [0, 2, 0], [1.5, 2, 0], [4, 2, 0],
         [0, 4, 0], [2.5, 4, 0], [4, 4, 0]]

faces = [[0, 1, 4, 3], [1, 2, 5, 4], [3, 4, 7, 6], [4, 5, 8, 7]]

mesh = Mesh.from_vertices_and_faces(vertices, faces)

plotter = Plotter(show_axes=True)
plotter.add(mesh, sizepolicy='absolute')
plotter.zoom_extents()
plotter.show()
```

#### A3\_d. `Mesh.from_polygons`

`Mesh.from_polygons` converts a series of polygons to a mesh.\
API reference: https://compas.dev/compas/1.5.0/api/generated/compas.datastructures.Mesh.from\_polygons.html\
Github source code: https://github.com/compas-dev/compas/blob/main/src/compas/datastructures/mesh/mesh.py

```python
from compas.datastructures import Mesh
from compas.geometry import Polygon
from compas_plotters import Plotter

polygon_1 = Polygon([[0, 0, 0], [2.5, 0, 0], [1.5, 2, 0], [0, 2, 0]])
polygon_2 = Polygon([[2.5, 0, 0], [4, 0, 0], [4, 2, 0], [1.5, 2, 0]])
polygon_3 = Polygon([[0, 2, 0], [1.5, 2, 0], [2.5, 4, 0], [0, 4, 0]])
polygon_4 = Polygon([[1.5, 2, 0], [4, 2, 0], [4, 4, 0], [2.5, 4, 0]])

polygons = [polygon_1, polygon_2, polygon_3, polygon_4]

mesh = Mesh.from_polygons(polygons)

# visualize the mesh
plotter = Plotter(show_axes=True)
plotter.add(mesh, sizepolicy='absolute')
plotter.zoom_extents()
plotter.show()
```

### A4. Visualize Mesh in 3D Viewer

Mesh is often used to represent 3D objects. We can use the 3D viewer to visualize the mesh. The following example visualize a thrust diagram that is exported from RhinoVault2.

```python
from compas.datastructures import Mesh
from compas_notebook.app import App

mesh = Mesh.from_json("https://raw.githubusercontent.com/BlockResearchGroup/CSD2_2022/main/3_Materialization/Tutorial5/data/simple_dome.json")

viewer = App()
viewer.add(mesh)
viewer.show()
```

Let's pick up a random vertex in the mesh and move it 1 unit up along the z axis.

```python
from compas.datastructures import Mesh
from compas_notebook.app import App

mesh = Mesh.from_json("https://raw.githubusercontent.com/BlockResearchGroup/CSD2_2022/main/3_Materialization/Tutorial5/data/simple_dome.json")

vkey = mesh.get_any_vertex()
xyz = mesh.vertex_coordinates(vkey)
mesh.vertex_attribute(vkey, "z", xyz[2] + 1)

viewer = App()
viewer.add(mesh)
viewer.show()
```

***

## B. Mesh Vertex, Edge, Face

Mesh has three main components: **Vertex**, **edge** and **face**.

![](<../../.gitbook/assets/image (2).png>)

A vertex is a point in 3D space, represented by the \[x, y, z] coordinate.

| Vertex Key | Coordinates |
| :--------: | :---------: |
|      0     |  (0, 0, 0)  |
|      1     |  (2, 0, 0)  |
|      2     |  (2, 2, 0)  |
|      3     |  (0, 2, 0)  |
|      4     |  (1, 1, 2)  |

An edge connects two vertices together.

| Edge Key | (u, v) |
| :------: | :----: |
|     0    | (0, 1) |
|     1    | (1, 2) |
|     2    | (2, 3) |
|     3    | (0, 3) |
|     4    | (1, 4) |
|     5    | (2, 4) |
|     6    | (3, 4) |
|     7    | (0, 4) |

A face is constructed by connecting the edges together. A 3D geometry can be constructed by connecting faces together.

| Face Key | Face Vertices |
| :------: | :-----------: |
|     0    |   (0, 1, 4)   |
|     1    |   (1, 2, 4)   |
|     2    |   (2, 3, 4)   |
|     3    |   (0, 3, 4)   |

### B1. Access Mesh Vertices, Faces and Edges

`mesh.vertices()`, `mesh.edges(`), `mesh.faces()` access the vertices, edges and faces of the mesh data structure. Note that these methods return generator objects that have to be consumed by iteration.

```python
# generator objects
vertices = [[0, 0, 0], [2, 0, 0], [2, 2, 0],
         [0, 2, 0], [1, 1, 2]]

faces = [[0, 1, 4], [1, 2, 4], [2, 3, 4], [0, 3, 4]]

mesh = Mesh.from_vertices_and_faces(vertices, faces)

print(mesh.vertices())
print(mesh.edges())
print(mesh.faces())
```

```python
print("Vertices")
for vertex in mesh.vertices():
     print(vertex, end=" ")

print("\nEdges")
for edge in mesh.edges():
     print(edge, end=" ")
        
print("\nFaces")
for face in mesh.faces():
     print(face, end=" ")        
```

```python
vertices = list(mesh.vertices())
print(vertices)

edges = list(mesh.edges())
print(edges)

faces = list(mesh.faces())
print(faces)
```

### B2. Visualize the Points

```python
from compas.datastructures import Mesh
from compas.geometry import Sphere, Point
from compas_notebook.app import App

mesh = Mesh.from_json("https://raw.githubusercontent.com/BlockResearchGroup/CSD2_2022/main/3_Materialization/Tutorial5/data/simple_dome.json")

viewer = App()

for vkey in mesh.vertices():
    xyz = mesh.vertex_coordinates(vkey)
    viewer.add(Sphere(xyz, 0.05), facecolor=(0.7, 0., 0.7))

# # only visualize Vertex 4
# vkey = 4
# xyz = mesh.vertex_coordinates(vkey)
# viewer.add(Sphere(xyz, 0.05), facecolor=(0.7, 0., 0.7))

viewer.add(mesh)
viewer.show()
```

### B3. Visualize the Lines

```python
from compas.datastructures import Mesh
from compas.geometry import Line
from compas_notebook.app import App

mesh = Mesh.from_json("https://raw.githubusercontent.com/BlockResearchGroup/CSD2_2022/main/3_Materialization/Tutorial5/data/simple_dome.json")

viewer = App()

for edge in mesh.edges():
    a, b = mesh.edge_coordinates(*edge)
    line = Line(a, b)
    viewer.add(line, linecolor=(0, 0, 1))

# viewer.add(mesh)
viewer.show()
```

### B4. Visualize the Faces

```python
from compas.datastructures import Mesh
from compas.geometry import Polygon
from compas_notebook.app import App

mesh = Mesh.from_json("https://raw.githubusercontent.com/BlockResearchGroup/CSD2_2022/main/3_Materialization/Tutorial5/data/simple_dome.json")

viewer = App()

for fkey in mesh.faces():
    points = mesh.face_coordinates(fkey)
    polygon = Polygon(points)
    viewer.add(polygon)

# viewer.add(mesh)
viewer.show()
```

***

## C. Mesh Normals

There are two kinds of normals that. Face normals are orthogonal vectors to the faces of the mesh. Whereas vertex normals are orthogonal to the vertices.

![](<../../.gitbook/assets/image (4).png>)

### C1. Face Normals

The face normal is a vector that describes the direction that the face polygon is facing. The winding of the vertices determines the direction of the face normal.

```python
from compas.datastructures import Mesh
from compas.geometry import Polygon, add_vectors, scale_vector
from compas_notebook.app import App

mesh = Mesh.from_json("https://raw.githubusercontent.com/BlockResearchGroup/CSD2_2022/main/3_Materialization/Tutorial5/data/simple_dome.json")

viewer = App()

scale_factor = 0.5 
for fkey in mesh.faces():
    f_normal = mesh.face_normal(fkey)
    f_centorid = mesh.face_centroid(fkey)
    line = Line(f_centorid, add_vectors(f_centorid, scale_vector(f_normal, scale_factor)))
    viewer.add(line, linecolor=(1.0, 0, 0))

viewer.add(mesh)
viewer.show()
```

### C2. Vertex Normals

The vertex normal is the weighted average of the normals of the neighbouring faces.

```python
from compas.datastructures import Mesh
from compas.geometry import Polygon, add_vectors, scale_vector
from compas_notebook.app import App

mesh = Mesh.from_json("https://raw.githubusercontent.com/BlockResearchGroup/CSD2_2022/main/3_Materialization/Tutorial5/data/simple_dome.json")

viewer = App()

scale_factor = 0.5 
for vkey in mesh.vertices():
    v_normal = mesh.vertex_normal(vkey)
    xyz = mesh.vertex_coordinates(vkey)
    line = Line(xyz, add_vectors(xyz, scale_vector(v_normal, scale_factor)))
    viewer.add(line, linecolor=(1.0, 0, 0))

viewer.add(mesh)
viewer.show()
```

***

## D. Exercise: Geodesic Dome

### D1. Load Mesh

In the following example, we will try to materialize a geodesic dome. We will use spheres/cylinders, cylinders, polygons to represent joints, bars and facades.\


![](https://i.pinimg.com/originals/0e/ce/2f/0ece2f10e2f7ef68e8603fc07d786bd6.jpg)

```python
from compas.datastructures import Mesh
from compas.geometry import Polygon, add_vectors, scale_vector
from compas_notebook.app import App

mesh = Mesh.from_json("https://raw.githubusercontent.com/BlockResearchGroup/CSD2_2022/main/3_Materialization/Tutorial5/data/geodome.json")

viewer = App()
viewer.add(mesh)
viewer.show()
```

### D2. Draw Joints

```python
from compas.geometry import Sphere

viewer = App()

for vkey in mesh.vertices():
    viewer.add(Sphere(mesh.vertex_coordinates(vkey), 0.1), color=(1.0, 0, 0))

# viewer.add(mesh)
viewer.show()
```

```python
from compas.geometry import Cylinder, Plane, Circle

viewer = App()

for vkey in mesh.vertices():
    xyz = mesh.vertex_coordinates(vkey)
    normal = mesh.vertex_normal(vkey)
    
    plane = Plane(xyz, normal) # center, normal
    circle = Circle(plane, 0.1)
    
    cylinder = Cylinder(circle, 0.1)
    viewer.add(cylinder, color=(1, 0, 0))

# viewer.add(mesh)
viewer.show()
```

### D3. Draw Bars

```python
from compas.geometry import Plane, Vector, Circle, Cylinder
from compas_notebook.app import App

viewer = App()
# viewer.add(mesh)

for vkey in mesh.vertices():
    xyz = mesh.vertex_coordinates(vkey)
    normal = mesh.vertex_normal(vkey)
    
    plane = Plane(xyz, normal) # center, normal
    circle = Circle(plane, 0.1)
    
    cylinder = Cylinder(circle, 0.1)
    viewer.add(cylinder, color=(1, 0, 0))
    
    
for (u, v) in mesh.edges():
    u_xyz = mesh.vertex_coordinates(u)
    v_xyz = mesh.vertex_coordinates(v)

# pipe:   circle ([plane, radius] | Circle) – The circle of the cylinder.
#         height (float) – The height of the cylinder.
    center = [0.5 * (a + b) for a, b in zip(u_xyz, v_xyz)]
    normal = Vector.from_start_end(v_xyz, u_xyz)
    plane = Plane(center, normal) # center, normal
    circle = Circle(plane, 0.03)
    
    cylinder = Cylinder(circle, normal.length - 0.1)
    viewer.add(cylinder)

viewer.show()
```

### D4. Draw Facades

```python
from compas.geometry import Polygon, Translation, scale_vector, Scale, Frame
from compas_notebook.app import App

viewer = App()

for vkey in mesh.vertices():
    xyz = mesh.vertex_coordinates(vkey)
    normal = mesh.vertex_normal(vkey)
    
    plane = Plane(xyz, normal) # center, normal
    circle = Circle(plane, 0.1)
    
    cylinder = Cylinder(circle, 0.1)
    viewer.add(cylinder, color=(1, 0, 0))
    
    
for (u, v) in mesh.edges():
    u_xyz = mesh.vertex_coordinates(u)
    v_xyz = mesh.vertex_coordinates(v)

# pipe:   circle ([plane, radius] | Circle) – The circle of the cylinder.
#         height (float) – The height of the cylinder.
    center = [0.5 * (a + b) for a, b in zip(u_xyz, v_xyz)]
    normal = Vector.from_start_end(v_xyz, u_xyz)
    plane = Plane(center, normal) # center, normal
    circle = Circle(plane, 0.03)
    
    cylinder = Cylinder(circle, normal.length - 0.1)
    viewer.add(cylinder)
    
dis = 0.05
for fkey in mesh.faces():
    points = mesh.face_coordinates(fkey)
    polygon = Polygon(points)
    
    f_normal = mesh.face_normal(fkey)
    T = Translation.from_vector(scale_vector(f_normal, dis))
    polygon.transform(T)
    
    f_centroid = mesh.face_centroid(fkey)
    plane = Plane(f_centroid, f_normal)
    frame = Frame.from_plane(plane)
    S = Scale.from_factors([0.93] * 3, frame)
    polygon.transform(S)
    
    viewer.add(polygon, facecolor=(0, 0, 0.7))
        
viewer.show()
```

