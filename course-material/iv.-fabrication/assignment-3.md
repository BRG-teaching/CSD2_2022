# Assignment 3

{% hint style="warning" %}
Complete the tasks below, and submit a zipped folder that includes&#x20;

1. the completed files or other deliverables&#x20;
2. and the PDF&#x20;

by **15:00 on Thursday, May 19th**.&#x20;

Please follow the file naming convention as shown in the [**Syllabus**](../../syllabus.md).  \


### [Submit assignment 3 here.](https://www.dropbox.com/request/8eLJIcF0pSEq9rELs0FT)
{% endhint %}

## 1.Design Brief

![© Roland Fischer](<../../.gitbook/assets/image (1).png>)

In order to apply the knowlege acquire throughout the CSD2  in a realistic design scenario, you will be asked to use all the techniques we will have presented throughout the course to design a shell structure in the public space of the Sechseläutenplatz in Zurich, Switzerland.&#x20;

![](../../.gitbook/assets/Opera4.jpeg)

Design a free-form shell for [Sechseläutenplatz in Zurich](https://goo.gl/maps/JaMvwPPMruYewLMFA). The surface of the shell may have a maximum area of 200 square meters and a maximum 16 meter span. The shell may land around, but not in or on the existing site obstacles (umbrellas, trees and dark grey areas). The shell must be inside the red area shown in the second image below. The height of the shell should be at least 2.5 meters, so that it can be used as a passageway as well as a covering for the plaza.

![](../../.gitbook/assets/Opera2.jpeg)

Tips and design considerations

* For my given site and my design intent, which method of RV2 pattern generation is appropriate?
* What types of existing boundary condition constraints do I need to taken into account?
* How does my pattern generation and modification strategies influence my choice of material and other fabrication and construction schemes?
* How can I control and modify the geometry of the force diagram to refine the shape of the Thrust Diagram?
* Have I considered how the landings and openings of the Thrust Diagram relate to the program and the intended use of the space underneath?

**Use the following 3Dmodel to develop your design.**

{% file src="../../.gitbook/assets/Sechselautenplatz_CSD2-2022.3dm.zip" %}
3Dmodel of the site in Zurich
{% endfile %}

## 2.Geometry, Rationalisation, and Materialisation Brief

Use the Tutorial 7 workflow on the form-found resulting mesh.

Hint: Follow a similar workflow as in  [Assignment 2 Jupyter Notebook](https://colab.research.google.com/github/BlockResearchGroup/CSD2\_2022/blob/main/2\_Geometry/Tutorial3/week\_3\_assignment.ipynb) to develop your answer.

In this part of the assignment, we will generate polygon blocks for the form-found funicular shell**.**

****

### Steps:

* **A. Load Your form-found Mesh**
* **B. Compute Tessellation Pattern**\
  The input mesh is a quad mesh, A hexagonal polygon can be generated with the vertices around two adjacent quad faces. You can modify the vertex coordinates in the quadmesh. Serialize the modified quad mesh.\
  Secondly, find the correct vertices in each block. Create a list,`block_faces`, and save the vertices on each block as a list in `block_faces`. Serialize the `block_faces`.\
  Visualize the blocks as `Polygon` in the viewer.\

* **C. Generate Blocks**\
  Create a function `generate_block`. The input parameter is **the modified quad mesh**, **vertices on one block**, and **thickness of the block**. The function should return a 3D block, which has a planar top surface.\
  Call the function to generate all the blocks for the barrel vault. Serialize the blocks and visualize them in the viewer.



## 3. Fabrication Brief

### 4a. Deliverables for the Form finding and Geometry, Rationalisation, and Materialisation

On the last CSD2 Course session, on May 19th, you will be asked to present your design proposals to the instructors . Before the start of Friday's 1st session, please compile the material below into a zip file (Your\_GroupName.zip), and upload it using the link in the header of this page.

### 1. Images(5-7)

* 16x9 format, 1920x1080 resolution min
* These images may include but are not limited to:
  * Site strategy diagrams
  * Concept sketches and design development
  * Pattern generation techniques and development
  * evolution and refinement of form and force diagrams
  * block generation, rationalization, and materialisation snapshots
  * fabrication strategies and development
  * perspectives/renderings
* Your\_Group\_Name\_\_##.png

### 2. Presentation board

* Presentation board (16x9 format, 1920x1080 resolution min.) summarising the the design project
* This board can be an organized compilation or a collage of the 8-10 images from above
* Your\_Group\_Name\_board.pdf (or jpg/png)

### 3. .rv2 session file (s)

* Final or a series of .rv2 session files&#x20;
* Your\_Group\_Name\_##.rv2

### 4. .3dm rhino file

Include Rhino files of the final design, including the shell geometry as well as any materialisation and fabrication developments.

* The Rhino file may be used interactively in your presentation
* To give an overview of materialization and fabrication developments
