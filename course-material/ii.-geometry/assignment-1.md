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

Use the [Assignment1 Jupyter Notebook](https://colab.research.google.com/github/BlockResearchGroup/CSD2\_2022/blob/main/2\_Geometry/Tutorial3/week\_3\_assignment.ipynb) to develop your answer.

Then answer the questions on the following document:

{% file src="../../.gitbook/assets/CSD2_2022_Assignment-1_template.docx" %}

## Question: <a href="#question" id="question"></a>

Now you have fabricated all your voussoirs. You have a cargo van which can carry a maximum of 900 kg in one turn. It is your task to transport all your pieces from the factory to the site. How many transportation turns do you need?





## Answers: <a href="#steps" id="steps"></a>

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

![Check first turn diagram](<../../.gitbook/assets/Assignment1-Diagram-0 CSD2-2022.png>)

```python
# Solution for the Check Voussoirs first turn
# ==============================================================================
# Input
# ==============================================================================
# voussoir weight list
voussoirs = [10.88, 24.71, 10.16, 18.85, 19.45, 24.24, 20.33, 17.52, 20.65, 18.72, 17.65, 13.99, 14.34, 22.85, 11.33, 13.53, 17.53, 13.22, 21.14, 12.96, 16.75, 12.87, 19.28, 13.49, 12.78, 20.07, 20.37, 24.32, 16.16, 14.45, 13.87, 10.9, 17.06, 15.04, 20.8, 20.19, 19.71, 12.46, 13.87, 19.87, 11.52, 13.67, 18.47, 14.43, 23.56, 23.28, 10.42, 24.41, 12.54,
             24.27, 24.71, 12.36, 12.63, 19.32, 20.46, 18.24, 24.12, 12.17, 11.9, 24.88, 22.36, 21.76, 19.69, 17.84, 18.64, 14.5, 16.67, 11.13, 18.81, 22.36, 13.41, 19.1, 11.28, 10.66, 18.43, 20.32, 11.15, 12.09, 17.09, 20.91, 13.52, 23.54, 21.28, 10.97, 22.39, 10.57, 19.17, 19.18, 20.67, 24.76, 13.33, 19.91, 14.57, 14.92, 14.17, 21.26, 11.42, 19.58, 14.77, 13.81]
# index list to store the voussoirs on the truck
index = []
# remaining weight on the truck
remaining_weight = 900

# ==============================================================================
# Check voussoirs on the truck and the remainings
# ==============================================================================
for i, voussoir in enumerate(voussoirs):
    if voussoir <= remaining_weight:
        remaining_weight -= voussoir
        index.append(i)
print("Turn one would take voussoir", index)

voussoirs = [voussoir for i, voussoir in enumerate(voussoirs) if i not in index]

# ==============================================================================
# Output
# ==============================================================================
print("Remaining voussoirs", voussoirs)
```



### C. `check_left_voussoirs` Function <a href="#c.-check_left_voussoirs-function" id="c.-check_left_voussoirs-function"></a>

![Turn Check First Turn into a function](<../../.gitbook/assets/Assignment1-Diagram-1 CSD2-2022.png>)

```python
# Solution for Turn Check First into a function
def check_left_voussoirs(voussoirs, max_load=900):
    
    """
    Given the voussoirs and max load of the truck,
    Check the remaining voussoirs after truck is fully loaded

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
    # index list to store the voussoirs on the truck
    index = []
    # initiate remaining weight on the truck with the max load capacity
    remaining = max_load

    # check voussoirs on the truck and the remainings
    for i, voussoir in enumerate(voussoirs):
        if voussoir <= remaining:
            remaining -= voussoir
            index.append(i)
    voussoirs = [voussoir for i, voussoir in enumerate(voussoirs) if i not in index]

    return voussoirs
```



### D. Call the Function to Calculate Transportation Turns <a href="#d.-call-the-function-to-calculate-transportation-turns" id="d.-call-the-function-to-calculate-transportation-turns"></a>

```python
# Solution for Turn Check First into a function
turns = 0
while voussoirs:
    turns += 1
    voussoirs = check_left_voussoirs(voussoirs, 900)

print("The truck needs", turns, "turns.")
```

