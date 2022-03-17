# Tutorial 4

## Computational Structural Design II

## Tutorial 4: Geometry, Data, and Visualization

#### Learning Goal:

* Geometries
* Data
* Visualization

#### Content:

* [A. Geometry Data](week\_4.md#GeometryData)
* [B. Geometry Class](week\_4.md#GeometryClass)
* [C. Geometry and Visualization](week\_4.md#visualization)
* [D. Geometry Operations](week\_4.md#Operations)

Tutorial 4 on Google Colab: [Tutorial4](https://colab.research.google.com/github/BlockResearchGroup/CSD2\_2022/blob/main/2\_Geometry/Tutorial4/week\_4\_lecture.ipynb)

## A. Geometry Data

### A1. Describe a point in Rhinoceros Grasshopper

Inside a three-dimensional(3D) Cartesian coordinate system, a **point** is represented by 3 numbers, which represent the values along the X, Y and Z axis of the system. If you are familiar with Rhino and Grasshopper, a point can be created numerically by inputing 3 values.

\
\


![](https://github.com/BlockResearchGroup/CSD2\_2022/blob/6e83888362c6734355d5abf42e9e573c3afb3052/2\_Geometry/Tutorial4/img/geo\_pt\_gh.png?raw=true)

### A2. Describe a Point by Python list

Similarly, the point can be described through a list `[x, y, z]` in Python. The three numbers represent the **x , y , z** coordinates of the point. Since a point is described as a list, the value in the list can be retrieved, modified, and updated by accessing the corresponding index of the list. Here we create a point `x=0, y=1, z=1` and change the coordinate `y=5`.

```python
# xyz coordinates of the point
my_point = [0, 5, 2] 

print("y coordinate of my_point is", my_point[1])

# re-assign the y coordinates 5
my_point[1] = 5  
print("xyz coordinates of my_point are", my_point)
```

```
y coordinate of my_point is 5
xyz coordinates of my_point are [0, 5, 2]
```

### A3. Geometry Data Summary

Besides **point**, basic geometry types - such as vector, line, plane - can be described numerically in Python by **lists of values**. The length of the list corresponds with the number of dimensions of the space the geometry resides in. In 3D space, the list contains 3 elements. The following table illustrates the data used to describe 3D geometries numerically.

| Geometry | Data                                               | Description                 |
| -------- | -------------------------------------------------- | --------------------------- |
| point    | \[x, y, z]                                         |                             |
| vector   | \[x, y, z]                                         |                             |
| line     | (\[x1, y1, z1], \[x2, y2, z2])                     | (start point, end point)    |
| plane    | (\[x0, y0, z0], \[xn, yn, zn])                     | (origin, normal)            |
| circle   | \[(\[x0, y0, z0], \[xn, yn, zn]), r]               | \[(origin, normal), radius] |
| polyline | (\[x1, y1, z1], \[x2, y2, z2], \[x3, y3, z3, ...]) | collection of points        |
| polygon  | (\[x1, y1, z1], \[x2, y2, z2], \[x3, y3, z3, ...]) | collection of points        |
| frame    | (\[x0, y0, z0], \[x1, y1, z1], \[x2, y2, z2])      | \[origin, vector, vector]   |

\\

***

#### Elements of argorithms - short recap

![](https://github.com/BlockResearchGroup/CSD2\_2022/blob/53513ad8ffd913fba9f70609b0700eab24291594/2\_Geometry/Introduction/Files/Introduction/IntroToJupyterNB\_Comp3.png?raw=true)

## B. Geometry Class

A geometry type can be described by data. We can use a **Class** as a constructor, a template, or a "blueprint" to create **Objects** of a certain geometry type. An **Object** is an instance of a **Class** and it shares all **attributes** and the **behavior** of the Class. Classes are used frequently in Python scripting. A class can not only store data, but also define **methods** (an object-oriented programming term for functions) alongside the data that they operate on and produce.

![](https://github.com/BlockResearchGroup/CSD2\_2022/blob/53513ad8ffd913fba9f70609b0700eab24291594/2\_Geometry/Introduction/Files/Introduction/IntroToJupyterNB\_Comp4.png?raw=true)

In the following session, we will learn anout the Python Class by creating our own **Point class**. Then we will use the class to create a **Point object**, which represents the point `x=0, y=1, z=1`.

### B1. Point Class

#### B1\_a. Create a Class

Class definition cannot be empty. Put the `pass` statement to avoid getting an error.

```python
class Point:
    """ Point class """
    pass

pt = Point()  # instantiate an object of Point
print(pt) # by default, print the name of the object’s class and the address of the object. 
```

```
<__main__.Point object at 0x167f2aeb0>
```

#### B1\_b. `__init__()` function

All classes have a function called `__init__()`, which is always executed when the class is being initiated. We can pass some initial values to the class by calling the `__init__()` function. Before the parameters `x`, `y`, `z`, there is a `self`, which refers to the object itself. Then, we need to create new fields also called `x`, `y`, `z`. Notice `self.x` and `x` are two different variables even though they are both called `x`. You can view the dotted notation `self.x` as the attribute of your Point object, and the `x` as a local variable.

```python
class Point:
    """ Point class"""
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

pt = Point(1, 1, 0) # create a point object
print("xyz coordinates are:", pt.x, pt.y, pt.z)
```

```
xyz coordinates are: 1 1 0
```

#### B1\_c. Object Method

Now let's add a **method** to the Point class to translate the point. It modifies the object attribute `self.x`, `self.y`, `self.z` by adding the translation distance along the corresponding axis.

```python
class Point:
    """ Point class"""
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def translate(self, vec_x, vec_y, vec_z):
        """Translate this point along a 3d vector"""
        self.x += vec_x
        self.y += vec_y
        self.z += vec_z

pt = Point(1, 1, 0) # create a point object
print("xyz coordinates before translation are:", pt.x, pt.y, pt.z) 
pt.translate(1,3,1) 
print("xyz coordinates after translation are:", pt.x, pt.y, pt.z) 
```

```
xyz coordinates before translation are: 1 1 0
xyz coordinates after translation are: 2 4 1
```

#### B1\_d. Modify Object Properties

Objects **properties** can be modified.

```python
pt.x = 3
print("xyz coordinates after modification are:", pt.x, pt.y, pt.z) 
```

```
xyz coordinates after modification are: 3 4 1
```

### B2 The COMPAS framework for Architecture, Engineering, Fabrication, and Construction

Here is the [documentation](https://compas.dev/compas/latest/index.html) of the main library of COMPAS, an open source framework for research and collaboration in Architecture, Engineering, Fabrication, and Construction.

![](https://github.com/BlockResearchGroup/CSD2\_2022/blob/e0a81fec1442f53b6a35ec496ed168db9dcbae52/2\_Geometry/Tutorial4/img/COMPAS.png?raw=true)

#### The Application Programming Interface(API) reference can be found [here](https://compas.dev/compas/latest/api.html).

#### The CSD2 Class will use this reference extensively, especially [COMPAS Geometry](https://compas.dev/compas/latest/api/compas.geometry.html) is relevant for this module.

### B2.1 Use the Point Class from COMPAS

COMPAS contains a [Point](https://compas.dev/compas/latest/api/generated/compas.geometry.Point.html?highlight=point#compas.geometry.Point) class which is similar to the one we have created. However, it contains more object methods which have already been developed. In a COMPAS Point class, a Point has three parameters, `x`, `y`, `z`. They could be accessed through indexing as well as through `.x`, `.y`, and `.z` attributes.

![](https://files.gitbook.com/v0/b/gitbook-28427.appspot.com/o/assets%2F-M730QpQnbAMvz44bqhc%2F-MMzyUtFsDByqwGgOo8D%2F-MN-4caIa6sDF5e1YGok%2Fimage.png?alt=media\&token=2c8d3140-e57b-49a2-8f16-d89ba351319c)

```python
import compas
print(compas.__version__)
from compas.geometry import Point

my_point = Point(0, 1, 1)  # create a point object
print(my_point.y)  # attribute y of point
print(my_point[1] == my_point.y)

my_point.y = 5  # reassign the attribute y
print(my_point) # Point class contains a class function that prints the summary of the object
```

```
1.14.0
1.0
True
Point(0.000, 5.000, 1.000)
```

### B3. Geometry Classes in COMPAS

COMPAS provides a number of ready-to-use primitive objects. Available primitive objects include `Point`, `Vector`, `Line`, `Plane`, `Polyline`, `Polygon`, `Circle`, `Frame`, etc. All COMPAS primitives can be used interchangeably with native Python objects as input for geometry functions and object methods. For a complete overview, you can visit the [API Reference](https://compas.dev/compas/latest/api/compas.geometry.html).

\\

| Geometry Object | COMPAS Class                         |
| --------------- | ------------------------------------ |
| point           | point = Point(x, y, z)               |
| vector          | vector = Vector(x, y, z)             |
| line            | line = Line(point, point)            |
| plane           | plane = Plane(point, vector)         |
| circle          | circle = Circle(plane, radius)       |
| polyline        | polyline = Polyline(points)          |
| polygon         | polygon = Polygon(points)            |
| frame           | frame = Frame(point, vector, vector) |

\\

```python
from compas.geometry import Point, Line

line_1 = Line([0, 0, 0], [2, 0, 0])
line_2 = Line(Point(0, 0, 0), Point(2, 0, 0))

print(line_1 == line_2)
```

```
True
```

***

## C. Geometry and Visualization

### C1. Visualize a Point

The **point** we created in the last session is a virtual object, now we will visualize it. After we generate the geometry objects, we can use a visualization interface to translate the information into a visual context. Firstly, we need a "drawing surface" - a canvas in 2D, or a scene in 3D. A 2D canvas can contain a number of shapes, importantly, the **canvas** can display not only geometric data such as point coordinates, but also enhance this data with graphical elements such as color or line width. A **Graphics Context** contains computational objects that provide mechanisms for _displaying_ the geometry, such as color, width of the curve, etc..

A **Plotter** is such a graphics context. Let us use the [Compas Plotter](https://compas.dev/compas/latest/api/generated/compas\_plotters.plotter.Plotter.html#compas\_plotters.plotter.Plotter) ...

```python
from compas.geometry import Point
from compas_plotters import Plotter

my_point = Point(1, 1, 0)

# visualize the Point
plotter = Plotter(show_axes=True)
plotter.add(my_point)
plotter.show()
```

![](https://github.com/BlockResearchGroup/CSD2\_2022/blob/e80a3ce74fa5577abcca03c187181b1a9d446e55/2\_Geometry/Tutorial4/week\_4\_files/week\_4\_19\_0.png?raw=true)

### C2. Line

For all information consult the COMPAS API reference for [Line](https://compas.dev/compas/latest/api/generated/compas.geometry.Line.html#compas.geometry.Line).

```python
from compas.geometry import Line
from compas_plotters import Plotter

# create a line
my_line = Line([0, 0, 0], [1, 1, 0])

# visualize the line
plotter = Plotter(show_axes=True)
plotter.add(my_line, draw_points=False, draw_as_segment=True)
plotter.zoom_extents()
plotter.show()
```

![](https://github.com/BlockResearchGroup/CSD2\_2022/blob/e80a3ce74fa5577abcca03c187181b1a9d446e55/2\_Geometry/Tutorial4/week\_4\_files/week\_4\_21\_0.png?raw=true)

### C3. Vector

A vector is a geometric object that has magnitude and direction. In Python, it can be represented through a list of x, y, z components.

For all information consult the COMPAS API reference for [Vector](https://compas.dev/compas/latest/api/generated/compas.geometry.Vector.html#compas.geometry.Vector).

#### C3\_a. Vector Data

```python
my_vector = [1, 2, 0]  # xyz coordinates of the vector
```

A vector can be added, subtracted, multiplied by another vector. For example, here's the example to add two vectors in Python.

```python
vector1 = [1, 2, 0]
vector2 = [0, 1, 0]
#vector3 = [vector1[i] + vector2[i] for i in range(3)]
vector3 = []
for i in range(3):
    vector3.append(vector1[i] + vector2[i])
print(vector3)
```

```
[1, 3, 0]
```

#### C3\_b. Geometric Operation Functions

compas.geometry provides geometric operation functions to simplify the use of basic Python operations. These functions always return native Python objects. The last example can be realized by using `compas.geometry.add_vectors`.

```python
from compas.geometry import add_vectors
vector1 = [1, 2, 0]
vector2 = [0, 1, 0]
vector3 = add_vectors(vector1, vector2)
print(vector3)
```

```
[1, 3, 0]
```

#### C3\_c. Vector Class

COMPAS Vector class which contains useful geometric properties and methods. Now let's create a Vector object and check its length. In Vector class, `length` is an attribute of the vector `object`.

```python
from compas.geometry import Vector
my_vector = Vector(1, 2, 0)
print(my_vector)
print(round(my_vector.length,3))
```

```
Vector(1.000, 2.000, 0.000)
2.236
```

A vector can also be constructed from start and end points. COMPAS geometry types can be used interchangeably with native Python types.

In other words, **Both a COMPAS Point object or a list composed of 3 components could be used as input**.

```python
from compas.geometry import Point, Vector
my_vector = Vector.from_start_end(Point(0, 0, 0), Point(1, 2, 0))
# my_vector = Vector.from_start_end([0, 0, 0], [1, 2, 0]
print(my_vector, 'my_vector')
print(my_vector == Vector(1, 2, 0))
```

```
Vector(1.000, 2.000, 0.000) my_vector
True
```

Operators such as + or \* involving COMPAS geometry objects always return a new COMPAS geometry object. For example, scaling my\_vector by 2 can use the class method Vector.scale(n) as well as \* 2.

```python
from compas.geometry import Vector
my_vector = Vector(1, 2, 0)
my_vector.scale(2)
print(my_vector)
print(my_vector == Vector(2, 4, 0))
print(my_vector == Vector(1, 2, 0) * 2)
```

```
Vector(2.000, 4.000, 0.000)
True
True
```

#### C3\_d: Exercise: Draw Vectors

Question: Given three points: pointA: \[0, 0, 0], pointB: \[0, 1, 0], pointC: \[3, 2, 0]. You need to draw three vectors as shown in the following picture.

![](https://github.com/BlockResearchGroup/CSD2\_2022/blob/6e83888362c6734355d5abf42e9e573c3afb3052/2\_Geometry/Tutorial4/img/vectors.jpg?raw=true)

```python
from compas.geometry import Point
from compas_plotters import Plotter

# Point Geometry
point1 = Point(0, 0, 0)
point2 = Point(0, 1, 0)
point3 = Point(3, 2, 0)

# Plottor
plotter = Plotter(show_axes=True)

plotter.add(point1)
plotter.add(point2)
plotter.add(point3)

plotter.zoom_extents()
plotter.show()
```

![](https://github.com/BlockResearchGroup/CSD2\_2022/blob/e80a3ce74fa5577abcca03c187181b1a9d446e55/2\_Geometry/Tutorial4/week\_4\_files/week\_4\_35\_0.png?raw=true)

```python
from compas.geometry import Point
from compas_plotters import Plotter

# Point Geometry
point1 = Point(0, 0, 0)
point2 = Point(0, 1, 0)
point3 = Point(3, 2, 0)

vector1 = point2 - point1
vector2 = point3 - point2
vector3 = point3 - point1

# Plottor 
plotter = Plotter(show_axes=True)

plotter.add(point1)
plotter.add(point2)
plotter.add(point3)

plotter.add(vector1, point=point1, color=(1, 0, 0))
plotter.add(vector2, point=point2, color=(0, 1, 0))
plotter.add(vector3, point=point1, color=(0, 0, 1))

plotter.zoom_extents() 
plotter.show()
```

![](https://github.com/BlockResearchGroup/CSD2\_2022/blob/e80a3ce74fa5577abcca03c187181b1a9d446e55/2\_Geometry/Tutorial4/week\_4\_files/week\_4\_36\_0.png?raw=true)

### C4. Polygon

A Polygon can be represented by an ordered collection of points in space connected by straight line segments forming a closed boundary around the interior space. Its closed boundary separates its interior from the exterior.

For all information consult the COMPAS API reference for [Polygon](https://compas.dev/compas/latest/api/generated/compas.geometry.Polygon.html#compas.geometry.Polygon).

```python
from compas.geometry import Polygon
from compas_plotters import Plotter

my_polygon = Polygon([[0, 0, 0], [1, 1, 0], [2, 1, 0], [1, -1, 0]])

plotter = Plotter(show_axes=True)
plotter.add(my_polygon, edgecolor=(0, 0, 1), facecolor=(1, 1, 0))
plotter.zoom_extents()
plotter.show()
```

![](https://github.com/BlockResearchGroup/CSD2\_2022/blob/e80a3ce74fa5577abcca03c187181b1a9d446e55/2\_Geometry/Tutorial4/week\_4\_files/week\_4\_38\_0.png?raw=true)

```python
from compas.geometry import Polygon
from compas_plotters import Plotter

# Construct a regular polygon from a number of sides and a radius.
my_polygon = Polygon.from_sides_and_radius_xy(5, 2.0) 

plotter = Plotter(show_axes=True)
plotter.add(my_polygon, edgecolor=(0, 0, 1), facecolor=(0.7, 0.7, 1.0))
plotter.zoom_extents()
plotter.show()
```

![](https://github.com/BlockResearchGroup/CSD2\_2022/blob/e80a3ce74fa5577abcca03c187181b1a9d446e55/2\_Geometry/Tutorial4/week\_4\_files/week\_4\_39\_0.png?raw=true)

### C5. Polyline

A Polyline is a sequence of points connected by line segments. In contrast to a Polygon, a Polyline **does not** have an interior and an exterior.

For all information consult the COMPAS API reference for [Polyline](https://compas.dev/compas/latest/api/generated/compas.geometry.Polyline.html#compas.geometry.Polyline).

```python
from compas.geometry import Polyline
from compas_plotters import Plotter

my_polyline = Polyline([[0, 0, 0], [1, 1, 0], [2, 1, 0], [1, -1, 0]])

plotter = Plotter(show_axes=True)
plotter.add(my_polyline, color=(1, 0, 0), linewidth=3)
plotter.zoom_extents()
plotter.show()
```

![](https://github.com/BlockResearchGroup/CSD2\_2022/blob/e80a3ce74fa5577abcca03c187181b1a9d446e55/2\_Geometry/Tutorial4/week\_4\_files/week\_4\_41\_0.png?raw=true)

### C6. Circle

For all information consult the COMPAS API reference for [Circle](https://compas.dev/compas/latest/api/generated/compas.geometry.Circle.html#compas.geometry.Circle).

```python
from compas.geometry import Plane, Circle
from compas_plotters import Plotter

my_plane = Plane([2, 1, 0], [0, 0, 1])  # center and normal
my_circle = Circle(my_plane, 2)

plotter = Plotter(show_axes=True)
plotter.add(my_circle, edgecolor=(0, 0, 1), facecolor=(0, 1, 1), linewidth=3)

plotter.zoom_extents()
plotter.show()
```

![](https://github.com/BlockResearchGroup/CSD2\_2022/blob/e80a3ce74fa5577abcca03c187181b1a9d446e55/2\_Geometry/Tutorial4/week\_4\_files/week\_4\_43\_0.png?raw=true)

### C7. Pointcloud

For all information consult the COMPAS API reference for [Pointcloud](https://compas.dev/compas/latest/api/generated/compas.geometry.Pointcloud.html#compas.geometry.Pointcloud).

```python
from random import random

from compas.geometry import Pointcloud
from compas.utilities import i_to_rgb
from compas_plotters import Plotter

# Pointcloud Geometry
pcl = Pointcloud.from_bounds(10, 5, 0, 100)

# Plotter
plotter = Plotter(show_axes=True)

for point in pcl.points:
    plotter.add(point, facecolor = i_to_rgb(random(), normalize=True))

plotter.zoom_extents()
plotter.show()
```

![](https://github.com/BlockResearchGroup/CSD2\_2022/blob/e80a3ce74fa5577abcca03c187181b1a9d446e55/2\_Geometry/Tutorial4/week\_4\_files/week\_4\_45\_0.png?raw=true)

### &#x20;<a href="#operations" id="operations"></a>

## D. Geometry Operations

### D1. Transformation

Transformation means changes in geometric shape, which is represented by a 4x4 transformation matrix. Here we will learn 3 typical transformations in COMPAS: translation, rotation and scale. A COMPAS geometry object can be transformed by calling the method .transform() or .transformed(). The former modifies the object in place, whereas the latter returns a new object.

For all information consult the COMPAS API reference for [Transformations](https://compas.dev/compas/latest/api/compas.geometry.html#transformations-1).

#### D1\_a. Translation

Translation is to move the geometry, one of the most basic transformation types. The shape, size and orientation of the geometry remain the same.

For all information consult the COMPAS API reference for [Translation](https://compas.dev/compas/latest/api/generated/compas.geometry.Translation.html#compas.geometry.Translation).

```python
from compas.geometry import Translation
T = Translation.from_vector([1, 2, 3])
print(T)
```

```
[[    1.0000,    0.0000,    0.0000,    1.0000],
 [    0.0000,    1.0000,    0.0000,    2.0000],
 [    0.0000,    0.0000,    1.0000,    3.0000],
 [    0.0000,    0.0000,    0.0000,    1.0000]]
```

```python
from compas.geometry import Polygon, Translation
from compas_plotters import Plotter

# Construct a regular polygon from a number of sides and a radius.
my_polygon = Polygon.from_sides_and_radius_xy(5, 2.0) 
my_polygon.transform(T)

plotter = Plotter(show_axes=True)
plotter.add(my_polygon, edgecolor=(0, 0, 1), facecolor=(0.7, 0.7, 1.0))
plotter.zoom_extents()
plotter.show()
```

![](https://github.com/BlockResearchGroup/CSD2\_2022/blob/e80a3ce74fa5577abcca03c187181b1a9d446e55/2\_Geometry/Tutorial4/week\_4\_files/week\_4\_50\_0.png?raw=true)

.transformed() creates a new polygon.

```python
from compas.geometry import Polygon, Translation
from compas_plotters import Plotter

# Construct a regular polygon from a number of sides and a radius.
my_polygon = Polygon.from_sides_and_radius_xy(5, 2.0) 
my_polygon.transform(T)

my_polygon = Polygon.from_sides_and_radius_xy(5, 2.0)
T1 = Translation.from_vector([1, 2, 0])
T2 = Translation.from_vector([2, 1, 0])
my_polygon.transform(T1)
my_polygon2 = my_polygon.transformed(T2)

plotter = Plotter(show_axes=True)
plotter.add(my_polygon, edgecolor=(0, 0, 1), facecolor=(0.7, 0.7, 1.0))
plotter.add(my_polygon2, edgecolor=(0, 0, 1), facecolor=(1.0, 0.7, 1.0))

plotter.zoom_extents()
plotter.show()
```

![](https://github.com/BlockResearchGroup/CSD2\_2022/blob/e80a3ce74fa5577abcca03c187181b1a9d446e55/2\_Geometry/Tutorial4/week\_4\_files/week\_4\_52\_0.png?raw=true)

#### D1\_b. Rotation

Rotation is to rotate the geometry by a certain amount in **degrees** or **radians**.

For all information consult the COMPAS API reference for [Rotation](https://compas.dev/compas/latest/api/generated/compas.geometry.Rotation.html#compas.geometry.Rotation).

```python
import math as m
from compas.geometry import Polygon, Rotation
from compas_plotters import Plotter

# Construct a regular polygon from a number of sides and a radius.
my_polygon = Polygon.from_sides_and_radius_xy(5, 2.0) 
my_polygon.transform(T)

R = Rotation.from_axis_and_angle([0, 0, 1], m.radians(15))
my_polygon.transform(R)

plotter = Plotter(show_axes=True)
plotter.add(my_polygon, edgecolor=(0, 0, 1), facecolor=(0.7, 0.7, 1.0))
plotter.zoom_extents()
plotter.show()
```

![](https://github.com/BlockResearchGroup/CSD2\_2022/blob/e80a3ce74fa5577abcca03c187181b1a9d446e55/2\_Geometry/Tutorial4/week\_4\_files/week\_4\_54\_0.png?raw=true)

#### D1\_c. Scaling

Scaling is a **linear transformation** to **enlarge** or **shrink** objects by a **scale factor**. Scaling can either be **uniform**, by the same scale factor along all axes, or **non-uniform**, by different scale factors along the axes.

For all information consult the COMPAS API reference for [Scaling](https://compas.dev/compas/latest/api/generated/compas.geometry.Scale.html#compas.geometry.Scale).

```python
from compas.geometry import Polygon, Scale
from compas_plotters import Plotter

# Construct a regular polygon from a number of sides and a radius.
my_polygon = Polygon.from_sides_and_radius_xy(5, 2.0) 
my_polygon.transform(T)

S = Scale.from_factors([0.5, 1, 1])  # scale factors along X, Y, Z
my_polygon.transform(S)

plotter = Plotter(show_axes=True)
plotter.add(my_polygon, edgecolor=(0, 0, 1), facecolor=(0.7, 0.7, 1.0))
plotter.zoom_extents()
plotter.show()
```

![](https://github.com/BlockResearchGroup/CSD2\_2022/blob/e80a3ce74fa5577abcca03c187181b1a9d446e55/2\_Geometry/Tutorial4/week\_4\_files/week\_4\_56\_0.png?raw=true)

#### D1\_d. Frame

A **Frame** plays an important role in Transformation, especially in 3D. A frame defines a local coordinate system enabling transformation between different coordinate systems represented by frames. Note that **Frame** is different from a **Plane**. A frame is defined by an origin and two axes, while a plane is defined by an origin and a normal vector.

For all information consult the COMPAS API reference for [Frame](https://compas.dev/compas/latest/api/generated/compas.geometry.Frame.html#compas.geometry.Frame).

```python
from compas.geometry import Frame, Transformation
f1 = Frame([1, 1, 1], [0.68, 0.68, 0.27], [-0.67, 0.73, -0.15])
T = Transformation.from_frame(f1)
print(T)
```

```
[[    0.6808,   -0.6688,   -0.2988,    1.0000],
 [    0.6808,    0.7282,   -0.0788,    1.0000],
 [    0.2703,   -0.1498,    0.9511,    1.0000],
 [    0.0000,    0.0000,    0.0000,    1.0000]]
```

```python
f2 = Frame([1, 1, 1], [0.68, 0.68, 0.27], [-0.67, 0.73, -0.15])
T = Transformation.from_frame_to_frame(f1, f2)
f1.transform(T)
print(f1 == f2)
```

```
True
```
