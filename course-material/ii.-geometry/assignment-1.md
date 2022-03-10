# Assignment 1

{% hint style="warning" %}
Complete the tasks below, and submit a zipped folder that includes&#x20;

1. the completed files or other deliverables&#x20;
2. and the PDF&#x20;

by **15:00 on Thursday, March 31st**.&#x20;

Please follow the file naming convention as shown in the [**Syllabus**](../../syllabus.md).  \


### [Submit assignment 1 here.](https://www.dropbox.com/request/2TnOS9cruALW0ItTIWD6)
{% endhint %}

## Tasks

Complete the following Assignment following the steps below:

Use the [Assignment1 Jupyter Notebook](https://mybinder.org/v2/gh/BlockResearchGroup/CSD2\_2022.git/21935a3?labpath=2\_Geometry%2FTutorial3%2Fweek\_3\_assignment.ipynb) to develop your answer.

Then answer the questions on the following document:

{% file src="../../.gitbook/assets/CSD2_2022_Assignment-1_template.docx" %}

## Question: <a href="#question" id="question"></a>

Now you have fabricated all your voussoirs. You have a cargo van which can carry a maximum of 900 kg in one turn. It is your task to transport all your pieces from the factory to the site. How many transportation turns do you need?





## Steps: <a href="#steps" id="steps"></a>

1. Let's break the question down by initially checking the first turn. You want to put as many voussoirs as possible on the truck, for maximum efficiency. Pick one voussoir. If the truck's load capacity is not filled, the voussoir can be placed in the truck. You can repeat the process until the truck is full **or** you have checked all the voussoirs and no one fits the truck anymore.
2. You can create a function that checks how many voussoirs can be loaded in one turn.
3. Now you can keep calling the function until all the voussoirs are on the truck. Note: every time we reach the truck's capacity, we need to update the remaining voussoir list.

### A. Generate Voussoir List <a href="#a.-generate-voussoir-list" id="a.-generate-voussoir-list"></a>

Please replace the value of the variable `name` with your name.

```python
import random

name = "CSD2-2022 Student X"  # please replace here with your name
n = []
for x in name:
   n.append(ord(x) - 96)
seed = sum(n)

voussoirs = []
random.seed(seed)
for i in range(200):
    voussoirs.append(round(random.uniform(12.5, 25), 2))
print("The voussoir list is: ", voussoirs)
```



### B. Check the First Turn <a href="#b.-check-the-first-turn" id="b.-check-the-first-turn"></a>

```python
# add your code here...
```



### C. `check_left_voussoirs` Function <a href="#c.-check_left_voussoirs-function" id="c.-check_left_voussoirs-function"></a>

```python
def check_left_voussoirs(voussoirs, max_load=900):
    """
    Given the voussoirs and max load of the truck,
    Check the remaining voussoirs after the truck is fully loaded.

    Parameters
    ----------
    voussoirs: list
        A list containing the weight of voussoirs
    max_load: int (optional)
        default: 900
        The maximum load capacity of the truck

    Returns
    -------
    voussoirs: list
        A list containing the weight of remaining voussoirs.

    """
    
    # your code here...
    return voussoirs
```



### D. Call the Function to Calculate Transportation Turns <a href="#d.-call-the-function-to-calculate-transportation-turns" id="d.-call-the-function-to-calculate-transportation-turns"></a>

```python
# add your code here...
```

