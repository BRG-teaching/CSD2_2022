# Introduction

{% embed url="https://mybinder.org/v2/gh/BlockResearchGroup/CSD2_2022.git/f057575?labpath=%2F2_Geometry%2FIntroduction%2FIntroductionToJupyterNotebook.ipynb" %}
Introduction to Jupyter Notebook
{% endembed %}


{% embed url="https://mybinder.org/v2/gh/BlockResearchGroup/CSD2_2022.git/f057575?labpath=2_Geometry%2FIntroduction%2FJupyter_Notebook_Markdown_Guide.ipynb" %}
Markdown
{% endembed %}

{% embed url="https://mybinder.org/v2/gh/BlockResearchGroup/CSD2_2022/f057575?labpath=2_Geometry%2FIntroduction%2Fhello_world.ipynb" %}
Hello World
{% endembed %}

---

## Introduction to Jupyter Notebook

Some of you might be familiar with using an IPython shell to run the code line by line or creating custom Python Scripts in CAD applications. This is great, but for more elaborate use of coding in Architecture, and especially, for learning and sharing your coding knowlege we will introduce another tool: The Jupyter Notebook.

The Jupyter Notebook is an open source web application that you can use to create and share documents that contain live code, equations, visualizations, and text. The name itself comes from the core supported programming languages: Julia, Python, and R.

For more information on the project itself, visit [Project Jupyter](https://jupyter.org).

### Jupyter in CSD2

Throughout the CSD2 course, Jupyter notebooks will be used to in all the next sessions, for teaching and coding together.

The notebook is the perfect tool because it is built as an interactive web application that allows us to develop and run our code block by block and immediatily see results without worrying on instally additional software packages.

Before this class you have received a weblink to a Jupyter notebook that the CSD2 team has created and is running using your browser, it could just as well run locally on your computer as a local server or remotely on a server. The reason it is called notebook is because it can contain live code, rich text elements such as equations, links, images, tables, and so on.

#### Create a Jupyter Notebook

When you navigate to the link you received, you will see a dashboard. In this dashboard, you can see some important features that are labeled in red: you can see all the files in the current folder, show all the running notebooks, and create a new notebook or others such as text file, folder and a terminal. Now let us create a new Python notebook by selecting the Python 3, usually this is called Python kernel. We will use the Python kernel, therefore, choose Python 3 kernel.

![](<../../.gitbook/assets/220206-jupyter\_dashboard-01\_ISB (1).png>)

Alternatively, use the "Launcher" to create the file, as shown below:

![](../../.gitbook/assets/220206-jupyter\_dashboard-02\_ISB.png)

**Create a new notebook and give it the name "hello\_world.ipynb"**

And open the new notebook.

![](../../.gitbook/assets/220206-jupyter\_dashboard-04\_ISB.png)

#### Use a Jupyter Notebook for interactive coding in Python

After you create a new Jupyter Notebook, it will look like the following figure. The toolbar and menu is self-explanatory and you can explore that on your own. We will cover only basic information here, to get you started.

![](../../.gitbook/assets/220206-jupyter\_dashboard-03\_ISB.png)

See this [Markdownguide](https://www.markdownguide.org/basic-syntax/#links) for an indepth look at styling your Jupyter Notebook content

Hovering your cursor to the toolbar shows you the function of the tool and if you press the menu, it will show you the drop down list. The most important things to know is that Jupyter notebook uses _cells_ and the different types. The _cell_ is a place where you can write your code or text. Cells can be run one at a time. You will be pacticing this way of running and testing your code throughout the course. Two important cell types are _code_ and _markdown_. The _code cell_ is where we type or paste our code and can run the code in it. The _markdown cell_ is a place you can type descriptions such as _pseudocode_(we will get to that later) in rich text format, see the following figure as an example. You can search for _‘Markdown cheatsheet’_ to get a quick start with markdown.

**To run the code or renter the markdown in the notebook is simple, just press Shift + Enter.**

Now create a _code cell_ and type the following code:

```python
print ('Hello CSD2!!')
```

Run the code by pressing the play sign left of the code cell. Doing this will create the following result:

```
Hello CSD2!!
```

![](../../.gitbook/assets/220206-jupyter\_dashboard-05\_ISB.png)

#### Saving your changes

To save the changes you have made click the floppy icon on the Jupyter Notebook menu. The current notebook will be changes locally.

#### Sharing with others

### Method: Through the menu

You can export your currently running Notebook by going to the File menu and choosing the Download as option.

This option allows you to download in all the formats that nbconvert supports. This quick method allows you to convert the running notebook directly. However, for converting multiple notebooks at once please use the "nbconvert" method described in the "How to Use nbconvert" section of [this tutorial](https://realpython.com/jupyter-notebook-introduction/#exporting-notebooks).

#### Shut down the Jupyter notebook

Closing the browser will not close the Jupyter notebook, since the server is still running. You can reopen the previous address in a browser. To completely shut down it, we need to close the associated terminal that you launch the Jupyter noteobok.

#### Close a notebook

If you close the notebook browser tab, the notebook actually is not closed, it is still running in the background. To close the notebook completely, go to the dashboard, and check the box before the notebook, and you can see a shutdown option in the toolbar above, this is the correct way you close a notebook completely.

**Ok, now you have the basic knowledge to launch and run a Jupyter notebook, and it is time to continue to learn Python.**

#### Jupyter Notebook Documentation

[PythonNumericalMethods](https://pythonnumericalmethods.berkeley.edu/notebooks/chapter01.05-Logial-Expressions-and-Operators.html)

[RealPython](https://realpython.com/jupyter-notebook-introduction/#adding-rich-content)

```python
```
