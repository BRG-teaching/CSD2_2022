# Introduction to Jupyter Notebook

Some of you might be familiar with using an IPython shell to run the code line by line or creating custom Python Scripts in CAD applications. 

In the previous session you were introduced to computational structural design.
Let's recap: 

For computational design an algorithmic language must be developed, the language is procedural. In other words geometric operations are introduced an described in discrete steps.

<img src="https://github.com/BlockResearchGroup/CSD2_2022/blob/20676eaf165a73675433f284799f874a45835718/2_Geometry/Introduction/Files/Introduction/IntroToJupyterNB_Comp1.png?raw=true" style="margin-left:auto; margin-right:auto"/>

These steps are defined by computer programming which utlizes hardware and software to execute computations. In our case, these computations are useful for structural design.

<img src="https://github.com/BlockResearchGroup/CSD2_2022/blob/20676eaf165a73675433f284799f874a45835718/2_Geometry/Introduction/Files/Introduction/IntroToJupyterNB_Comp2.png?raw=true" style="margin-left:auto; margin-right:auto"/>

The elements of algorithms are:
- variables
- loops 
- conditionals
- functions
- objects

<img src="https://github.com/BlockResearchGroup/CSD2_2022/blob/20676eaf165a73675433f284799f874a45835718/2_Geometry/Introduction/Files/Introduction/IntroToJupyterNB_Comp3.png?raw=true" style="margin-left:auto; margin-right:auto"/>

These elements can be used in different form of programming:
- visual programming i.e. Grasshopper
- procedural programming - Scripting
- object-oriented programming - OOP

<img src="https://github.com/BlockResearchGroup/CSD2_2022/blob/20676eaf165a73675433f284799f874a45835718/2_Geometry/Introduction/Files/Introduction/IntroToJupyterNB_Comp4.png?raw=true" style="margin-left:auto; margin-right:auto"/>

The Computational Structural Design Class will introduce Scripting and Object-Oriented Programming through the Jupyter Notebook. 

The Jupyter Notebook is an open source web application that you can use to create and share documents that contain live code, equations, visualizations, and text. The name itself comes from the core supported programming languages: Julia, Python, and R.

For more information on the project itself, visit [Project Jupyter](https://jupyter.org).

## Jupyter in CSD2

Throughout the CSD2 course, Jupyter notebooks will be used to in all the next sessions, for teaching and coding together. 

The notebook is the perfect tool because it is built as an interactive web application that allows us to develop and run our code block by block and immediatily see results without worrying on instally additional software packages.

Before this class you have received an [Introduction to Jupyter](https://mybinder.org/v2/gh/BlockResearchGroup/CSD2_2022.git/HEAD?labpath=%2F2_Geometry%2FIntroduction%2FIntroductionToJupyterNotebook.ipynb) link to a Jupyter notebook that the CSD2 team has created and is running using your browser. 

The reason it is called notebook is because it can contain live code, rich text elements such as equations, links, images, tables, and so on.



### Create a Jupyter Notebook

When you navigate to the link you received, you will see a dashboard. In this dashboard, you can see some important features that are labeled in red: you can see all the files in the current folder, show all the running notebooks, and create a new notebook or others such as text file, folder and a terminal. Hovering your cursor to the toolbar shows you the function of the tool and if you press the menu, it will show you the drop down list.


<img src="https://github.com/BlockResearchGroup/CSD2_2022/blob/20676eaf165a73675433f284799f874a45835718/2_Geometry/Introduction/Files/Introduction/IntroToJupyterNB_Slide1.png?raw=true" style="margin-left:auto; margin-right:auto"/>

Next, open the notebook Jupyter_Notebook_Markdown_Guide.ipynb , which has already been created for you. Doubleclick the name of the Notebook in the File Data Tree, to the left of your screen.

<img src="https://github.com/BlockResearchGroup/CSD2_2022/blob/20676eaf165a73675433f284799f874a45835718/2_Geometry/Introduction/Files/Introduction/IntroToJupyterNB_Slide2.png?raw=true" style="margin-left:auto; margin-right:auto"/>

letr us look at the existing cells

<img src="https://github.com/BlockResearchGroup/CSD2_2022/blob/20676eaf165a73675433f284799f874a45835718/2_Geometry/Introduction/Files/Introduction/IntroToJupyterNB_Slide4.png?raw=true" style="margin-left:auto; margin-right:auto"/>

Let us run the existing cells.
#### To run the code or renter the markdown in the notebook is simple, just press Shift + Enter.

<img src="https://github.com/BlockResearchGroup/CSD2_2022/blob/20676eaf165a73675433f284799f874a45835718/2_Geometry/Introduction/Files/Introduction/IntroToJupyterNB_Slide3.png?raw=true" style="margin-left:auto; margin-right:auto"/>

<img src="https://github.com/BlockResearchGroup/CSD2_2022/blob/20676eaf165a73675433f284799f874a45835718/2_Geometry/Introduction/Files/Introduction/IntroToJupyterNB_Slide5.png?raw=true" style="margin-left:auto; margin-right:auto"/>

See this [Markdownguide](https://www.markdownguide.org/basic-syntax/#links)  for an indepth look at styling your Jupyter Notebook content 

The most important things to know is that Jupyter notebook uses *cells* and the different types. 
The *cell* is a place where you can write your code or text. Cells can be run one at a time. You will be pacticing this way of running and testing your code throughout the course. Two important cell types are *code* and *markdown*. 
The *code cell* is where we type or paste our code and can run the code in it. 
The *markdown cell* is a place you can type descriptions such as *pseudocode*(we will get to that later) in rich text format, see the following figure as an example. 
You can search for *‘Markdown cheatsheet’* to get a quick start with markdown. 


#### Create a new notebook and give it the name "hello_world.ipynb"

Let us create a new jupyter Notebook and practice creating cells. 

And open the new notebook.

Now create a *code cell* and type the following code:

print ('Hello CSD2! )

<img src="https://github.com/BlockResearchGroup/CSD2_2022/blob/20676eaf165a73675433f284799f874a45835718/2_Geometry/Introduction/Files/Introduction/IntroToJupyterNB_Slide%208.png?raw=true" style="margin-left:auto; margin-right:auto"/>


```python
print ('Hello CSD2!!')
```

    Hello CSD2!!


### Downloading your notebook

To download the currently-open notebook go to the **Main Menu > File > Download**

<img src="https://github.com/BlockResearchGroup/CSD2_2022/blob/20676eaf165a73675433f284799f874a45835718/2_Geometry/Introduction/Files/Introduction/IntroToJupyterNB_Slide%207.png?raw=true" style="margin-left:auto; margin-right:auto"/>

### Save and export the notebook

To save and export the currently-open notebook locally go to the **Main Menu > File > Save and Export Notebook As**

<img src="https://github.com/BlockResearchGroup/CSD2_2022/blob/20676eaf165a73675433f284799f874a45835718/2_Geometry/Introduction/Files/Introduction/IntroToJupyterNB_Slide%206.png?raw=true" style="margin-left:auto; margin-right:auto"/>


### Close a notebook

If you close the notebook browser tab, the notebook actually is not closed, it is still running in the background. To close the notebook completely, right-click the name of the notebook you want to close and select 'Shut Down Kernel'.

#### Ok, now you have the basic knowledge to launch and run a Jupyter notebook, and it is time to continue to learn Python.

### Jupyter Notebook Documentation

[PythonNumericalMethods](https://pythonnumericalmethods.berkeley.edu/notebooks/chapter01.05-Logial-Expressions-and-Operators.html)

[RealPython](https://realpython.com/jupyter-notebook-introduction/#adding-rich-content)


```python

```
