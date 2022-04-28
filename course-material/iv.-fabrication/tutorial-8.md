# Tutorial 8

## Tutorial 8

Computational Structural Design II\
Wire Cutting Workflow
---------------------

#### Learning Goal:

* Orient a block on a machine bed
* Generate the required blank material
* Determine wire cutting paths

#### Step One is to Plan

![](https://github.com/BlockResearchGroup/CSD2\_2022/raw/717f04e0081f8d346ebc79bf80227ada8bbb9f0d/4\_Fabrication/Tutorial9/img/wirecutting\_flowchart.png)

#### Content:

* [Determine Machine](tutorial-8.md#mac)
* [Import Blocks](tutorial-8.md#import)
* [Orient on Machining Table](tutorial-8.md#orient)
* [Generate Blanks](tutorial-8.md#blank)
* [Generate Wire Path](tutorial-8.md#wires)

#### Exercise:

* Ex. 9.1 Orient Block for Cutting
* Ex. 9.2 Add Geometry of Cutting Material
* Ex. 9.3 Place Block on Machine Bed
* Ex. 9.4 Generate Blank Material
* Ex. 9.5 Generate Wire Cutter Path & Output\


***

#### Determine a Machine

There are many types of wire-cutting machines, but it is also helpful to instead consider any machine which can cut the geometry we have produced. Therefore, additional machines which do not rely on a wire but cut the same geometries are included for comparison in the following table.

## Possible Types of Machines

|   Wirecutting Type   |                                                                              Image                                                                              |                Possible Materials               |
| :------------------: | :-------------------------------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------: |
|    Hot Wirecutting   | ![](https://github.com/BlockResearchGroup/CSD2\_2022/raw/717f04e0081f8d346ebc79bf80227ada8bbb9f0d/4\_Fabrication/Tutorial9/img/foam\_robotic\_wirecutting.jpeg) |                       Foam                      |
| Abrasive Wirecutting |   ![](https://github.com/BlockResearchGroup/CSD2\_2022/raw/717f04e0081f8d346ebc79bf80227ada8bbb9f0d/4\_Fabrication/Tutorial9/img/robottic-wire-cutting-1.jpeg)  | <p>Wood, Plastic, Rubber,<br>Mycelium, Etc.</p> |
|  Diamond Wirecutting |  ![](https://github.com/BlockResearchGroup/CSD2\_2022/raw/717f04e0081f8d346ebc79bf80227ada8bbb9f0d/4\_Fabrication/Tutorial9/img/curved-wave-jointed-arch.jpeg)  |               Stone, Marble, Etc.               |

|  Non-Wire Cutting Type |                                                                            Image                                                                            | Possible Materials |
| :--------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------: | :----------------: |
|   3D Waterjet Cutting  |  ![](https://github.com/BlockResearchGroup/CSD2\_2022/raw/717f04e0081f8d346ebc79bf80227ada8bbb9f0d/4\_Fabrication/Tutorial9/img/3d-water-jet-cutting2.jpeg) |        Metal       |
| 6-axis Robotic Bandsaw | ![](https://github.com/BlockResearchGroup/CSD2\_2022/raw/717f04e0081f8d346ebc79bf80227ada8bbb9f0d/4\_Fabrication/Tutorial9/img/6axis\_bandsaw\_actual.jpeg) |     Wood, Etc.     |

**Abrasive Wirecutting** is the machine which can handle the geometries which we are generating as well as open the possible material choices to some which are more sustainable than polystyrene foams.

It is worth noting that this is not an industry-standard production method and so while it is suitable for this case, we are working in the assumption that we are prototyping which makes this a more competitive option.

According to [odico.dk](https://odico.dk/en/processesmethods/#), a company which uses abrasive wirecutting, their standard workpiece dimensions are **2400 x 1200 x 1550 mm**. We will use this as our guide.

So we can already set our `machine_dim` variable for the rest of the workflow.

```python
machine_dim = [24.0, 12.0, 15.5]
```

### Let's begin the workflow...

### Set up the Compas and Google Colab Workflow

```python
# % pip install compas_notebook
# % pip install requests
```

```python
# Load the Drive helper and mount
from google.colab import drive

# This will prompt for authorization.
drive.mount('/content/drive')
```

```python
# After executing the cell above, Drive
# files will be present in "/content/drive/My Drive".
!ls "/content/drive/My Drive/Colab Notebooks"
```

### Step 1: Import the blocks and turn it into a usable format

Locate the `.json` file with the exported discretized blocks.

![](https://github.com/BlockResearchGroup/CSD2\_2022/raw/717f04e0081f8d346ebc79bf80227ada8bbb9f0d/4\_Fabrication/Tutorial9/img/diagrams/1\_allBlocks.png)

```python
import os
import compas

from google.colab import drive
from google.colab import files

from compas.datastructures  import Mesh
from compas_notebook.app import App

# 1. load all of the blocks from the json in the drive
blocks = [block for block in compas.json_load("/content/drive/My Drive/Colab Notebooks/07_blocks_flat_top.json")]

# 2. visualise the blocks
viewer = App()

for block in blocks:
    viewer.add(block)
viewer.show()
```

&#x20;

### Step 2: Isolate one Block

This notebook will go through the entire workflow on just one block. We will isolate an arbitrary block to find the wirecutting paths for.

![](https://github.com/BlockResearchGroup/CSD2\_2022/raw/717f04e0081f8d346ebc79bf80227ada8bbb9f0d/4\_Fabrication/Tutorial9/img/diagrams/2\_singleBlock.png)

```python
import os
import compas

from compas.datastructures  import Mesh
from compas_notebook.app import App

# 1. get one block from the list of blocks
my_block = blocks[0]

# 2. visualise individual block
viewer = App()
viewer.add(my_block)
viewer.show()
```



### Step 3: Identify the top and bottom faces of the block

Using the face normals, we compare the face normal to the Z-axis to find the most vertical outside face. We then color-code the faces to ensure we are selecting the correct ones.

Ideally the `top` and `bottom` information would be embedded in the mesh, however in this case we are coding this to be independent of that data.

![](https://github.com/BlockResearchGroup/CSD2\_2022/raw/717f04e0081f8d346ebc79bf80227ada8bbb9f0d/4\_Fabrication/Tutorial9/img/diagrams/3\_singleBlockColor.png)

```python
import os
import compas

from compas.datastructures  import Mesh
from compas.geometry  import Vector
from compas_notebook.app import App

# 1. get the list of faces
faces = list(my_block.faces())

# 2. find top faces
top = sorted(my_block.faces(), key=lambda face: Vector(* my_block.face_normal(face, unitized=True)).dot([0,0,1]))[0]
my_block.face_attribute(top, 'top', True)

# 3. find bottom faces
bottom = sorted(my_block.faces(), key=lambda face: Vector(* my_block.face_normal(face, unitized=True)).dot([0,0,1]))[-1]
my_block.face_attribute(bottom, 'bottom', True)

# 4. set all face colors
facecolors = {face: (0.0, 0.5, 0.0) for face in my_block.faces()}

# 5. set a different facecolor for the top and bottom faces
facecolors[top] = (1.0, 0.0, 0.0)
facecolors[bottom] = (0.0, 0.0, 1.0)


# 6. visualise individual block with top and bottom faces different colors
viewer = App()
viewer.add(my_block, facecolor=facecolors)
viewer.show()
```

```
[0, 1, 2, 3, 4, 5, 6, 7]
(0.0, 0.5, 0.0)
```

### Step 4: Orient the Block on the WorldXY plane

This step orients the block to be within the machine space and placed on the `worldXY` plane. Visualising the machine space ensures that we are cutting a block which is sized appropriately to the machinery.

![](https://github.com/BlockResearchGroup/CSD2\_2022/raw/717f04e0081f8d346ebc79bf80227ada8bbb9f0d/4\_Fabrication/Tutorial9/img/diagrams/4\_roorientBlock.png)

```python
import os
import compas

from compas.datastructures  import Mesh
from compas.geometry import bestfit_frame_numpy
from compas.geometry  import Frame, Rotation, Transformation, Plane, Line
from compas.geometry  import Box
from compas_notebook.app import App

# 1. get a list of the top faces
top = list(my_block.faces_where({'top': True}))[0]

# 2. get corner vertex coordinates the top faces
corners = my_block.face_coordinates(top)
print(corners)

# 3. generate a bestfit frame of the corners
frame = Frame(*bestfit_frame_numpy(corners))

# 4. generate a world frame
world = Frame.worldXY()

# 5. build the frame to frame transformation
X = Transformation.from_frame_to_frame(frame, world)

# 6. perform the transformation on the block
transformed_block = my_block.transformed(X)

# 7. flip the block to make it oriented for the wirecutting
xaxis, yaxis, zaxis = [1, 0, 0], [0, 1, 0], [0, 0, 1]

R = Rotation.from_axis_and_angle(yaxis, 3.14159)
rotated_block = transformed_block.transformed(R)

# 7. set new variable name for the block
final_block = rotated_block

# 9. generate the machining workspace at worldXY
machine_dim = [24.00, 12.00, 15.50]
machine_space = Box(world,machine_dim[0],machine_dim[1],machine_dim[2])
machine_points = machine_space.points

# 8. visualize the correctly oriented block within the machining workspace
viewer = App()

# 9. set the face colors for final_block
facecolors_final = {face: (0.0, 0.5, 0.0) for face in final_block.faces()}
facecolors_final[top] = (1.0, 0.0, 0.0)
facecolors_final[bottom] = (0.0, 0.0, 1.0)

viewer.add(my_block, facecolor=facecolors)
viewer.add(final_block, facecolor=facecolors_final)

for a,b in machine_space.edges:
    line = Line(machine_points[a], machine_points[b])
    viewer.add(line)

viewer.show()
```

```
[[7.230564269705165, 4.848557581589693, 4.139765633420204], [5.4070400413559625, 5.407640841017567, 4.517785878631973], [4.848021697604618, 7.231081034750968, 4.139564011176455], [5.9216052876857095, 8.346651582899844, 3.4849080241529036], [7.573639817288216, 7.573972812346804, 3.222047164490389], [8.346315615879245, 5.922034529244805, 3.485091137001543]]
```

### Step 5: Generate the blank material

This step is done very simply, and finds a dimension of blank material which fully encompasses the block with some buffer space. Ideally further steps would be taken to confirm that this is compatible with the actual blank material dimensions, preferably generating a blank with those dimensions as well.

![](https://github.com/BlockResearchGroup/CSD2\_2022/raw/717f04e0081f8d346ebc79bf80227ada8bbb9f0d/4\_Fabrication/Tutorial9/img/diagrams/5\_blank.png)

```python
import os
import compas

from compas.geometry import Frame, Box
from compas.geometry import Scale
from compas.datastructures import Mesh
from compas.geometry import oriented_bounding_box_numpy
from compas_notebook.app import App


# 1. compute the bounding box of the block mesh
#    and convert it into a box geometry object

bbox = final_block.vertices_attributes('xyz', keys=final_block.vertices())
box = oriented_bounding_box_numpy(bbox)
blank = Box.from_bounding_box(box)
blank_unsized = Box.from_bounding_box(box)
bbf = blank.frame

# 2. add padding to blank material Box object by scaling up in every direction
#    use the frame of the blank as the origin for scaling up

blank.transform(Scale.from_factors([1.10, 1.10, 1.10], frame=bbf))

blank_points = blank.points


# 3. visualize the correctly oriented block within the machining workspace
viewer = App()

for a,b in blank.edges:
    line = Line(blank_points[a], blank_points[b])
    viewer.add(line)

viewer.add(final_block)
viewer.show()
```

&#x20;

### Step 6: Find a side edge

This step ensures that we are selecting an edge which is used in the next step to find the strip of edges located on the inclined sides of the block.

![](https://github.com/BlockResearchGroup/CSD2\_2022/raw/717f04e0081f8d346ebc79bf80227ada8bbb9f0d/4\_Fabrication/Tutorial9/img/diagrams/6\_edge.png)

```python
import os
import compas

from compas.geometry import Frame, Box, Line, Sphere, Point
from compas.geometry import Scale
from compas.datastructures import Mesh
from compas.geometry import oriented_bounding_box_numpy
from compas_notebook.app import App

# 1. get top and bottom face vertices
bottom = my_block.face_vertices(0)
top = my_block.face_vertices(1)[::-1]

# 2. initiate the viewer
viewer = App()

# 3. find an edge which begins at the bottom face and ends at the top face
#    this indicates that it is an edge along the side of the block
#       Loop through the edges
#       If a,b of edge is equal to bottom[0],top[0], indicates it is a side edge

for edge in final_block.edges():
    if edge[0] == bottom[0] and edge[1] == top[0]:
        a, b = final_block.edge_coordinates(*edge)
        line = Line(a, b)

        pt_a = Point(a[0], a[1], a[2])
        pt_b = Point(b[0], b[1], b[2])

        viewer.add(Sphere(pt_a, 0.05), facecolor=(0.7, 0.0, 0.7))
        viewer.add(Sphere(pt_b, 0.05), facecolor=(0.7, 0.0, 0.7))
        viewer.add(line)
        wire_edge = edge



viewer.add(final_block)
viewer.show()
```

&#x20;

### Step 7: Find the edges and extend them to the top face of the blank

This step makes sure that the wire path is properly considered by extending each path to the faces of the blank.

![](https://github.com/BlockResearchGroup/CSD2\_2022/raw/717f04e0081f8d346ebc79bf80227ada8bbb9f0d/4\_Fabrication/Tutorial9/img/diagrams/7\_edges.png)

```python
import os
import compas

from compas.geometry import Frame, Box, Line, Point
from compas.datastructures import Mesh

from compas.geometry import intersection_line_plane, bestfit_plane_numpy
from compas_notebook.app import App

# 1. use edge strip to find all edges on side of block
side_edges = final_block.edge_strip(wire_edge)

# 2. get vertices for top and bottom, make lists of the vertices in each
top_vertices = blank.top
bot_vertices = blank.bottom
all_vertices = blank.vertices

blank_top = []
for i in top_vertices:
    blank_top.append(all_vertices[i])
    
blank_bot = []
for i in bot_vertices:
    blank_bot.append(all_vertices[i])

# 3. generate a bestfit plane of the corners
plane_top = Plane(*bestfit_plane_numpy(blank_top))
plane_bot = Plane(*bestfit_plane_numpy(blank_bot))

wires = []

for edge in side_edges:
    # get the edge_coordinates
    a, b = final_block.edge_coordinates(*edge)
    # draw a line
    line = Line(a, b)

    # make a point at the intersection of that line and the plane at the top of the blank
    pt_a = Point(* intersection_line_plane(line, plane_top))
    # make a point at the intersection of that line and the plane at the bottom of the blank
    pt_b = Point(* intersection_line_plane(line, plane_bot))
    
    # add the points to the wires list
    wires.append((pt_a,pt_b)

# 6. initialize viewer
viewer = App()

viewer.add(final_block)

# draw wireframe of blank
for a,b in blank.edges:
    line = Line(blank_points[a], blank_points[b])
    viewer.add(line)

# draw lines for edges for wirecutter
for a, b in wires:
    viewer.add(Line(a, b))

viewer.show()
    
```

&#x20;&#x20;

### Step 8: Pair the edges together and Interpolate

A wirecutter is one continuous wire with some width dimensions. This line must remain straight, however it is able to perform some rotations. Pairing the edges together will provide two rails for each side of the wirecutter to follow in order to cut the side faces.

Next, we evaluate the distance between edges and generate more edges for the machine to follow such that it will move at a consistend speed throughout the cutting process.

![](https://github.com/BlockResearchGroup/CSD2\_2022/raw/717f04e0081f8d346ebc79bf80227ada8bbb9f0d/4\_Fabrication/Tutorial9/img/diagrams/8\_edgePairs\_labelled\_final-01.png)

![](https://github.com/BlockResearchGroup/CSD2\_2022/raw/717f04e0081f8d346ebc79bf80227ada8bbb9f0d/4\_Fabrication/Tutorial9/img/diagrams/8\_interpolate.png)

```python
import os
import compas

from compas.geometry import Frame, Box, Line
from compas.datastructures import Mesh

from compas.utilities import pairwise, linspace
from compas_notebook.app import App

# 1. zip pairs of points together to determine wirecutter path
A, B = zip(*wires)

# initialise the viewer
viewer = App()

for a, b in wires:
    viewer.add(Line(a, b), linewidth=10, color=(1, 0, 0))
    
# 2. make more lines for a smoother machine path
interpolation = []
for (a, aa), (b, bb) in zip(pairwise(A), pairwise(B)):

    # for each vector between pairs of points...
    a_aa = aa - a
    b_bb = bb - b

    # identify the length of the longest of the two
    # compute the approximate number of steps required to move 0.05 units at a time.

    l = max(a_aa.length, b_bb.length)
    n = int(l / 0.05)

    for i in linspace(0, 1, num=n):
        if i == 0:
            continue

        ai = a + a_aa * i
        bi = b + b_bb * i

        # interpolation.append((ai, bi))
        interpolation.append([ai, bi])
        viewer.add(Line(ai, bi))
    
# 3. flip the direction of the path overall
interpolation.reverse()

viewer.add(final_block)

# draw wireframe of blank
for a,b in blank.edges:
    line = Line(blank_points[a], blank_points[b])
    viewer.add(line)

viewer.show()
```

&#x20;

### Step 9: Find plane and intersections to cut the top

The face of the block which remains to be cut will not necessarily be flat. It is also not guaranteed to have a geometry which has two edges we can pair together and use as a path.

Therefore, we instead find a bestfit plane for the top face, and extend that plane outwards to find where it intersects on the vertical edges of the blank material.

![](https://github.com/BlockResearchGroup/CSD2\_2022/raw/717f04e0081f8d346ebc79bf80227ada8bbb9f0d/4\_Fabrication/Tutorial9/img/diagrams/9\_top\_cuts\_labelled-01.png)

```python
import os
import compas

from compas.geometry import Frame, Box, Line, Point, Plane, Scale
from compas.geometry import bestfit_plane_numpy, intersection_plane_plane
from compas.datastructures import Mesh
from compas_notebook.app import App

# 1. get a list of the bottom faces
#    faces_where
bottom = list(final_block.faces_where({'bottom': True}))[0]

# 2. get corner vertex coordinates the top faces of the block
#    face_coordinates
corners = final_block.face_coordinates(bottom)


# 3. generate a bestfit plane of the corners
#    bestfit_plane_numpy
plane = Plane(*bestfit_plane_numpy(corners))


# 4. get index numbers for the vertices of relavant sides of the blank
#    blank.(name of the side) : left, right, front, back
left_vertices = blank.left
right_vertices = blank.right
front_vertices = blank.front
back_vertices = blank.back

# 5. get the list of all the vertices in the blank
#    blank.vertices
all_vertices = blank.vertices

# 6. make lists of the vertex coordinates for the difference sides
blank_left = []
for i in left_vertices:
    blank_left.append(all_vertices[i])

blank_right = []
for i in right_vertices:
    blank_right.append(all_vertices[i])

blank_front = []
for i in front_vertices:
    blank_front.append(all_vertices[i])

blank_back = []
for i in back_vertices:
    blank_back.append(all_vertices[i])

# 7. generate a bestfit plane of the blank's sides
left_plane = Plane(*bestfit_plane_numpy(blank_left))
right_plane = Plane(*bestfit_plane_numpy(blank_right))
front_plane = Plane(*bestfit_plane_numpy(blank_front))
back_plane = Plane(*bestfit_plane_numpy(blank_back))

# 8. intersect plane at top of block with the sides of the blank
inter = intersection_plane_plane(plane, left_plane)
int_line = Line(inter[0], inter[1])

inter_r = intersection_plane_plane(plane, right_plane)
int_line_r = Line(inter_r[0], inter_r[1])

# 9. find intersections with the edges of the blank
top_wire_start = Point(* intersection_line_plane(int_line, front_plane))
top_wire_end = Point(* intersection_line_plane(int_line, back_plane))

top_wire_start2 = Point(* intersection_line_plane(int_line_r, front_plane))
top_wire_end2 = Point(* intersection_line_plane(int_line_r, back_plane))

top_wires = []
top_wires.append((top_wire_start,top_wire_end))
top_wires.append((top_wire_start2,top_wire_end2))

viewer = App()

viewer.add(final_block)
# viewer.add(plane)
viewer.add(Sphere([top_wire_start.x,top_wire_start.y,top_wire_start.z], 0.05), facecolor=(0.7, 0.0, 0.7))
viewer.add(Sphere([top_wire_end.x,top_wire_end.y,top_wire_end.z], 0.05), facecolor=(0.7, 0.0, 0.7))
viewer.add(Sphere([top_wire_start2.x,top_wire_start2.y,top_wire_start2.z], 0.05), facecolor=(0.7, 0.0, 0.7))
viewer.add(Sphere([top_wire_end2.x,top_wire_end2.y,top_wire_end2.z], 0.05), facecolor=(0.7, 0.0, 0.7))

# draw wireframe of blank
for a,b in blank.edges:
    line = Line(blank_points[a], blank_points[b])
    viewer.add(line)

viewer.show()
```

### Step 10: Pair the Intersections and make the wirecutting path.

We are now able to use those intersections to create two pairs of edges, which then become the wirecutting path.

![](https://github.com/BlockResearchGroup/CSD2\_2022/raw/717f04e0081f8d346ebc79bf80227ada8bbb9f0d/4\_Fabrication/Tutorial9/img/diagrams/10\_top.png)

```python
import os
import compas

from compas.geometry import Frame, Box, Line
from compas.datastructures import Mesh

from compas.utilities import pairwise, linspace
from compas_notebook.app import App

A, B = zip(*top_wires)

interpolation = []

viewer = App()
# Zip together pairs of points on cycle A and cycle B.

for (a, aa), (b, bb) in zip(pairwise(A), pairwise(B)):

    # For each vector between pairs of points
    a_aa = aa - a
    b_bb = bb - b

    # Identify the length of the longest of the two
    # compute the approximate number of steps required to move 0.01 units at a time.

    l = max(a_aa.length, b_bb.length)
    n = int(l / 0.05)

    for i in linspace(0, 1, num=n):
        if i == 0:
            continue

        ai = a + a_aa * i
        bi = b + b_bb * i

        interpolation.append([ai, bi])
        viewer.add(Line(ai, bi))
    

interpolation.reverse()

viewer.add(final_block)

# draw wireframe of blank
for a,b in blank.edges:
    line = Line(blank_points[a], blank_points[b])
    viewer.add(line)

viewer.show()
```

s
