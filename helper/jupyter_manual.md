# Jupyter Notebook
Jupyter Notebook is a web-based interactive computational environment for creating Jupyter notebook documents.

## `JupyterNotebook` & `JupyterLab`
`JupyterLab` is the next-generation user interface **including notebooks**. It has a modular structure where several notebooks or files can be opened as tabs simultaneously. According [JupyterLab official documentation](https://jupyterlab.readthedocs.io/en/stable/getting_started/overview.html#jupyterlab-releases),<br/>
> JupyterLab will eventually replace the classic Jupyter Notebook. Throughout this transition, the same notebook document format will be supported by both the classic Notebook and JupyterLab. 
> 
So there is no need to use `JupyterNotebook`. 

## Installation
`JupyterLab` can be installed using `conda` with:<br/>
```python
conda install -c conda-forge jupyterlab
```





## Start
1. Open Terminal
2. change the current working directory `cd [directory]`
3. change the environment `conda activate [env]`
4. open jupyter notebook `jupyter lab`

Jupyter notebook will be opened in the browser. It’s being hosted and run on your local machine.

## Cell types:
- Code
- Markdown
- Raw: A raw cell is independent of the kernel that execute code. 

## 

## Output 
`$ jupyter nbconvert <input notebook> --to <output format>`
e.g. `$ jupyter nbconvert py_examples.ipynb --to pdf`
