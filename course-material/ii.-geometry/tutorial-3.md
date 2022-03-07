# Tutorial 3

## Tutorial 3

### Computational Structural Design II Intro to coding in Python and the Jupyter notebook II

**Learning Goal:**

* understand how to write a function
* understand how to use built-in functions in Python
* understand `dictionary`s

#### Content:

* A. bar Length
  * A1. [Find the Longest Bar](tutorial-3.md#a1.-find-the-longest-bar)
  * A2. [Sort the Bars](tutorial-3.md#a2.-sort-the-bars)
* B. Data Management
  * B1. [Gridshell Data](tutorial-3.md#b1.-gridshell-data)
  * B2. [Calculate Voussoir Volume](tutorial-3.md#b2.-calculate-voussoir-volume)

#### Exercise:

* [Calculate Voussoir Weight](tutorial-3.md#b2.-calculate-voussoir-volume)

#### Assignment:

* [Calculate Transportation Turns](assignment-1.md)

A. bar Length\



### A1. Find the Longest Bar

#### Question:

You are still working on your grid-shell. You want to find the longest bar in your grid-shell. How can you find i

#### Answer:

You can pick one bar, and suppose it is the longest bar. Then, pick the second one. If it is longer than the first one, then the longest one is the second one. Keep repeating this process until you have compared all the bars. Then you will find the longest bar.

#### A1\_a. Flowchart

![](../../2\_Geometry/Tutorial3/img/A1\_a.png)

#### A1\_b. Code

```python
# Input
# bar length of the grids-shell
gridshell = [1.6, 3.6, 2.4, 3.4, 2.7, 2.8, 3.3, 3.1, 3.7, 1.8, 1.8, 1.8, 2.6]

# initiate longest bar, suppose the first bar is the longest
longest = gridshell[0]  
index = 0  

# Compare Bar Length
# if the bar is longer than the longest bar
# assign the longest bar the new bar length
for i, bar in enumerate(gridshell):
    if bar >= longest:
        longest = bar
        index = i

# Output
print("The longest bar is bar", index + 1, "and its length is", longest, "m.")
```

***

### A2. Sort the bars

#### Question:

Now you want to sort the bars from the longest to the shortest. How can you do it?

#### Answer:

One way to solve this problem is to go through all the bars, and find the longest one. Add the longest one to a new list.

| Sorted bars | Length (m) |
| :---------: | :--------: |
|      1      |     3.7    |

Then do it again and find the next-longest bar.

| Sorted bars | Length (m) |
| :---------: | :--------: |
|      1      |     3.7    |
|      2      |     3.6    |

Keep doing and you would get the sorted bars from longest to shortest.

#### A2\_a. Flowchart

![](../../2\_Geometry/Tutorial3/img/A1\_b.png)

#### A2\_b. Write the Function

To find one element in the sorted bar list, we need to find the longest bar in the remaining bar list. We could turn this part of the statements into a [function](https://docs.python.org/3/tutorial/controlflow.html#defining-functions), which we could reuse when needed. A function always start with a keyword `def`, followed by the function name and the parameters. When we write a function, it's suggested to write a short doc describing the function.

```python
def find_longest_bar(bars):
    """
    to find the longest bar in the gridshell
    Parameters
    ----------
    bars : list
        A list containing the bar length of the gridshell

    Returns
    -------
    index: int
        Index of the longest bar in the bar list
    longest: float
        Length of the longest bar in the bar list
    """

    # check the list is not empty
    if bars == []:
        return

    # initiate longest bar, suppose the first bar is the longest
    longest = bars[0]  
    index = 0  

    # compare every bar with the longest bar
    for i, bar in enumerate(bars):
        if bar >= longest:
            longest = bar
            index = i

    return index, longest
```

#### A2\_c. Call the Function

Now we could use `find_longest_bar` function to sort our bars from longest to shortest. Every time we find the longest bar, we will delete it from the gridshell list and add it to the sorted\_bars list.

```python
# Input
# bar length of the bar-net
gridshell = [1.6, 3.6, 2.4, 3.4, 2.7, 2.8, 3.3, 3.1, 3.7, 1.8, 1.8, 1.8, 2.6]
# create empty bar list
sorted_bars = []

# Program
while gridshell != []:
    # find the longest bar in the remaining of the bar list
    i, longest = find_longest_bar(gridshell)
    # remove the longest item from the bar list
    gridshell.pop(i)
    # add the longest item to the sorted bar list
    sorted_bars.append(longest)

# Output
print("The sorted bar list is", sorted_bars)
```

#### A2\_d. Turn Sorting into a Function

We could also turn the sorting into a function `sort_bar_length`, which means the `sort_bar_length` function will include the `find_longest_bar` function. It is allowed in Python. This sorting method is also called [`selecting sorting` algorithm](https://en.wikipedia.org/wiki/Selection\_sort).

```python
def sort_bar_length(bars):
    """
    sort the bars in descending order

    Parameters
    ----------
    bars: list
        A list containing the bar length of the gridshell

    Returns
    -------
    sorted_bars: list
        A list containing the bar length of the gridshell in descending order
    
    """
    # create empty bar list
    sorted_bars = []

    while bars != []:
        # find the longest bar in the remaining of the bar list
        i, longest = find_longest_bar(bars)
        # remove the longest item from the bar list
        bars.pop(i)
        # add the longest item to the sorted bar list
        sorted_bars.append(longest)

    return sorted_bars
```

#### A2\_d. Python List Functions

Python has built-in method `sorted()` that could sort a list easily. `max()` and `min()` would find the largest and smallest item in the list.

```python
barnet = [1.6, 3.6, 2.4, 3.4, 2.7, 2.8, 3.3, 3.1, 3.7, 1.8, 1.8, 1.8, 2.6]

print("Longest bar is", max(barnet), "m.")
print("Shortest bar is", min(barnet), "m.")
print("bars in ascending order:", sorted(barnet))
print("bars in descending order:", sorted(barnet, reverse=True))
print("Total bar length is", sum(barnet), "m.")
```

```
Longest bar is 3.7 m.
Shortest bar is 1.6 m.
bars in ascending order: [1.6, 1.8, 1.8, 1.8, 2.4, 2.6, 2.7, 2.8, 3.1, 3.3, 3.4, 3.6, 3.7]
bars in descending order: [3.7, 3.6, 3.4, 3.3, 3.1, 2.8, 2.7, 2.6, 2.4, 1.8, 1.8, 1.8, 1.6]
Total bar length is 34.6 m.
```

***

B. Data Management\



### B1. Gridshell Data

#### Question:

While digging deep into the design and fabrication, you start to accumulating information about the bars, including the length, dimension, bar stress, etc. How would you hold your information?

| bar No. | Length (m) | Dimension (mm) | Stress (N/mm2) |
| :-----: | :--------: | :------------: | :------------: |
|    1    |     1.6    |        2       |       275      |
|    2    |     3.6    |        2       |       185      |
|    3    |     2.4    |        2       |       105      |
|    4    |     3.4    |        2       |       134      |
|    5    |     2.7    |        2       |       155      |
|    6    |     2.8    |        2       |       265      |
|    7    |     3.3    |        2       |       150      |
|    8    |     3.1    |        2       |       185      |
|    9    |     3.7    |        2       |       124      |
|    10   |     1.8    |        2       |       234      |
|    11   |     1.8    |        2       |       259      |
|    12   |     2.6    |        2       |       201      |

#### Answer:

In this case, we can create three lists, containing information of length, dimension, and stress respectively. However, this solution is not efficient nor clear, especially when our data set is big. Here we would introduce a new collection type - [dictionary](https://docs.python.org/3/tutorial/datastructures.html#dictionaries).

#### B1\_a. Create a Dictionary

First, let's create a dictionary to save all the lengths of the bars. The key is the index of the bar, and the item is the length.

```python
bar_length_list = [1.6, 3.6, 2.4, 3.4, 2.7, 2.8, 3.3, 3.1, 3.7, 1.8, 1.8, 2.6]

# create an empty dictionary
gridshell_dict = {}

for i in range(len(bar_length_list)):
    gridshell_dict[i] = bar_length_list[i]
    
print(gridshell_dict)
```

```
{0: 1.6, 1: 3.6, 2: 2.4, 3: 3.4, 4: 2.7, 5: 2.8, 6: 3.3, 7: 3.1, 8: 3.7, 9: 1.8, 10: 1.8, 11: 2.6}
```

Note that dictionaries are indexed by keys, which can be not only numbers, but also other immutable type, such as strings.

```python
bar_length_list = [1.6, 3.6, 2.4, 3.4, 2.7, 2.8, 3.3, 3.1, 3.7, 1.8, 1.8, 2.6]

# create an empty dictionary
gridshell_dict = {}

for i in range(len(bar_length_list)):
    key = "bar_{}".format(i)
    gridshell_dict[key] = bar_length_list[i]
    
print(gridshell_dict)
```

#### B1\_b. Add Values to Dictionary

Now let's save more information.

```python
bar_length_list = [1.6, 3.6, 2.4, 3.4, 2.7, 2.8, 3.3, 3.1, 3.7, 1.8, 1.8, 2.6]
bar_stress_list = [275, 185, 105, 134, 155, 265, 150, 185, 124, 234, 259, 201]

# create an empty dictionary
# key is index of the bar, item is infomation of the bar
gridshell_dict = {}

for i in range(len(bar_length_list)):
    # for each bar, we create another dictionary
    # key: category, item: value of the category
    gridshell_dict[i] = {}
    gridshell_dict[i]["length"] = bar_length_list[i]
    gridshell_dict[i]["dimension"] = 2
    gridshell_dict[i]["stress"] = bar_stress_list[i]

print(gridshell_dict)
```

#### B1\_c. Access a Dictionary

We could easily find the information on a specific bar. For example, let's find the information on bar `3`.

```python
index = 3
print("bar", index, "information", gridshell_dict[index])
```

#### B1\_d. Modify a Dictionary

Similar to the list, we can modify information in the dictionary. If we find the stress of bar 3 is incorrect, we could modify it.

```python
gridshell_dict[index]["stress"] = 154
print("bar", index, "information", gridshell_dict[index])
```

***

### B2. Calculate Voussoir Volume

#### Question:

You have a dictionary containing the surface area and thickness of the voussoir. Now you want to calculate the volume of each piece, and add the number to the dictionary.

$$
volume = area * thickness
$$

```python
# vault dictionary
vault = {
    0: {"area": 2590, "thickness": 51},
    1: {"area": 3420, "thickness": 46},
    2: {"area": 2940, "thickness": 48},
    3: {"area": 4210, "thickness": 38},
    4: {"area": 3890, "thickness": 58},
    5: {"area": 4000, "thickness": 60}
}
```

#### Answer:

```python
# iterate through the dictionary
for key in vault.keys():
    # get the area and thickness of the voussoir
    v_area = vault[key]["area"]
    v_thickness = vault[key]["thickness"]
    # calculate the volume
    v_volume = round(v_area * v_thickness, 2)
    print("Voussior", key, "volume:", v_volume)
    # add the volume to the dictionary
    vault[key]["volume"] = v_volume
```

#### Exercise: Calculate Voussoir Weight

Now you decide the voussoir would be cut from limestone, and its density is 2160 kg/m3, could you calculate the weight of each piece and add it to the dictionary?

$$
weight = volume * thickness
$$

```python
density = 2160  # kg/m3

# iterate through the dictionary
for key in vault.keys():
    # please write down your answer here
```

***

#### Answer:

```python
density = 2160  # kg/m3

# iterate through the dictionary
for key in vault.keys():
    # get the area and thickness of the voussoir
    v_area = vault[key]["area"]
    v_thickness = vault[key]["thickness"]
    # calculate the volume and weight
    v_volume = v_area * v_thickness
    v_weight = v_volume * density / 1000 ** 3
    v_weight = round(v_weight, 2)  # limit the number to 2 decimals
    print("Voussior", key, "volume:", v_volume, "weight:", v_weight)
    # add the volume to the dictionary
    vault[key]["volume"] = v_volume
    vault[key]["weight"] = v_weight
```
