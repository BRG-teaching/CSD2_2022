# Tutorial 3



Computational Structural Design II\
Intro to coding in Python and the Jupyter notebook II
-----------------------------------------------------

#### Learning Goal:

* understand how to write a function
* understand how to use built-in functions in Python
* understand `dictionary`

#### Content:

* A. bar Length
  * A1. Find the Longest bar
  * A2. Sort the bars
* B. Data Management
  * B1. bar-net Data
  * B2. Calculate Voussoir Volume

#### Exercise:

* Calculate Voussoir Weight

A. bar Length\



### A1. Find the Longest bar

#### Question:

You are still working on your grid shell. You want to find the longest bar in your grid shell. How can you find it?

#### Answer:

You can pick one bar, and suppose it is the longest bar. Then, pick the second one. If it is longer than the first one, then the longest one is the second one. Keep repeating this process until you have compared all the bars. Then you will find the longest bar.

#### A1\_a. Flowchart

![](https://files.gitbook.com/v0/b/gitbook-28427.appspot.com/o/assets%2F-M730QpQnbAMvz44bqhc%2F-MMRUovKxE5lvzBXWGn6%2F-MMRYft9oXZpioSHn49-%2Fweek1\_dia%20\(2\).png?alt=media\&token=0e484961-4ab7-4f24-855d-abb21916f9b2)

#### A1\_b. Code

```python
# Input
# bar length of the bar-net
barnet = [1.6, 3.6, 2.4, 3.4, 2.7, 2.8, 3.3, 3.1, 3.7, 1.8, 1.8, 1.8, 2.6]

# initiate longest bar, suppose the first bar is the longest
longest = barnet[0]  
index = 0  

# Compare bar Length
# if the bar is longer than the longest bar
# assign the longest bar the new bar length
for i, bar in enumerate(barnet):
    if bar >= longest:
        longest = bar
        index = i

# Output
print("The longest bar is bar", index + 1, "and its length is", longest, "m.")
```

```
The longest bar is bar 9 and its length is 3.7 m.
```

### A2. Sort the bars

#### Question:

Now you want to sort the bars from the longest to the shortest. How can you do it?

#### Answer:

One way to solve this problem is to go through all the bars, and find the longest one. Add the longest one to a new list.

| Sorted bars | Length (m) |
| :-----------: | :--------: |
|       1       |     3.7    |

Then do it again and find the next-longest bar.

| Sorted bars | Length (m) |
| :-----------: | :--------: |
|       1       |     3.7    |
|       2       |     3.6    |

Keep doing and you would get the sorted bars from longest to shortest.

#### A2\_a. Flowchart

![](https://files.gitbook.com/v0/b/gitbook-28427.appspot.com/o/assets%2F-M730QpQnbAMvz44bqhc%2F-MMRwMy-a-u\_usu0jZWc%2F-MMSbXFPpSLZty5V4M-r%2Fweek1\_dia%20\(3\).png?alt=media\&token=f1cd130f-cecd-40ae-846a-ddc96deb26d5)

#### A2\_b. Write the Function

To find one element in the sorted bar list, we need to find the longest bar in the remaining bar list. We could turn this part of the statements into a function, which we could reuse when needed. When we write a function, it's suggested to write a short doc describing the function.

```python
def find_longest_bar(barnet):
    """
    to find the longest bar in the bar list
    Parameters
    ----------
    bars : list
        A list containing the bar length of the bar-net

    Returns
    -------
    index: int
        Index of the longest bar in the bar list
    longest: float
        Length of the longest bar in the bar list
    """

    # check the list is not empty
    if barnet == []:
        return

    # initiate longest bar, suppose the first bar is the longest
    longest = barnet[0]  
    index = 0  

    # compare every bar with the longest bar
    for i, bar in enumerate(barnet):
        if bar >= longest:
            longest = bar
            index = i

    return index, longest
```

#### A2\_c. Call the Function

Now we could use `find_longest_bar` function to sort our bars from longest to shortest. Every time we find the longest bar, we will delete it from the barnet list and add it to the sorted\_bars list.

```python
# Input
# bar length of the bar-net
barnet = [1.6, 3.6, 2.4, 3.4, 2.7, 2.8, 3.3, 3.1, 3.7, 1.8, 1.8, 1.8, 2.6]
# create empty bar list
sorted_bars = []

# Program
while barnet != []:
    # find the longest bar in the remaining of the bar list
    i, longest = find_longest_bar(barnet)
    # remove the longest item from the bar list
    barnet.pop(i)
    # add the longest item to the sorted bar list
    sorted_bars.append(longest)

# Output
print("The sorted bar list is", sorted_bars)
```

```
The sorted bar list is [3.7, 3.6, 3.4, 3.3, 3.1, 2.8, 2.7, 2.6, 2.4, 1.8, 1.8, 1.8, 1.6]
```

#### A2\_d. Turn Sorting into a Function

We could also turn the sorting into a function. We can call a function in another function. This sorting method is also called `selecting sorting` algorithm.

```python
def sort_bar_length(bars):
    """
    sort the bars in descending order

    Parameters
    ----------
    bars: list
        A list containing the bar length of the bar-net

    Returns
    -------
    sorted_bars: list
        A list containing the bar length of the bar-net in descending order
    
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



### B1. bar-net Data

#### Question:

While digging deep into the design and fabrication, you start to accumulating information about the bars, including the length, dimension, bar stress, etc. How would you hold your information?

| bar No. | Length (m) | Dimension (mm) | Stress (N/mm2) |
| :-------: | :--------: | :------------: | :------------: |
|     1     |     1.6    |        2       |       275      |
|     2     |     3.6    |        2       |       185      |
|     3     |     2.4    |        2       |       105      |
|     4     |     3.4    |        2       |       134      |
|     5     |     2.7    |        2       |       155      |
|     6     |     2.8    |        2       |       265      |
|     7     |     3.3    |        2       |       150      |
|     8     |     3.1    |        2       |       185      |
|     9     |     3.7    |        2       |       124      |
|     10    |     1.8    |        2       |       234      |
|     11    |     1.8    |        2       |       259      |
|     12    |     2.6    |        2       |       201      |

#### Answer:

In this case, we can create three lists, containing information of length, dimension, and stress respectively. However, this solution is not so efficient and clear, especially when our data set is big. Here we would introduce a new collection type - `dictionary`.

#### B1\_a. Create a Dictionary

First, let's create a dictionary to save all the lengths of the bars. The key is the index of the bar, and the item is the length.

```python
bar_length_list = [1.6, 3.6, 2.4, 3.4, 2.7, 2.8, 3.3, 3.1, 3.7, 1.8, 1.8, 2.6]

# create an empty dictionary
bars_dict = {}

for i in range(len(bar_length_list)):
    bars_dict[i] = bar_length_list[i]

print(bars_dict)
```

```
{0: 1.6, 1: 3.6, 2: 2.4, 3: 3.4, 4: 2.7, 5: 2.8, 6: 3.3, 7: 3.1, 8: 3.7, 9: 1.8, 10: 1.8, 11: 2.6}
```

#### B1\_b. Add Values to Dictionary

Now let's save more information.

```python
bar_length_list = [1.6, 3.6, 2.4, 3.4, 2.7, 2.8, 3.3, 3.1, 3.7, 1.8, 1.8, 2.6]
bar_stress_list = [275, 185, 105, 134, 155, 265, 150, 185, 124, 234, 259, 201]

# create an empty dictionary
# key is index of the bar, item is infomation of the bar
bars_dict = {}

for i in range(len(bar_length_list)):
    # for each bar, we create another dictionary
    # key: category, item: value of the category
    bars_dict[i] = {}
    bars_dict[i]["length"] = bar_length_list[i]
    bars_dict[i]["dimension"] = 2
    bars_dict[i]["stress"] = bar_stress_list[i]

print(bars_dict)
```

```
{0: {'length': 1.6, 'dimension': 2, 'stress': 275}, 1: {'length': 3.6, 'dimension': 2, 'stress': 185}, 2: {'length': 2.4, 'dimension': 2, 'stress': 105}, 3: {'length': 3.4, 'dimension': 2, 'stress': 134}, 4: {'length': 2.7, 'dimension': 2, 'stress': 155}, 5: {'length': 2.8, 'dimension': 2, 'stress': 265}, 6: {'length': 3.3, 'dimension': 2, 'stress': 150}, 7: {'length': 3.1, 'dimension': 2, 'stress': 185}, 8: {'length': 3.7, 'dimension': 2, 'stress': 124}, 9: {'length': 1.8, 'dimension': 2, 'stress': 234}, 10: {'length': 1.8, 'dimension': 2, 'stress': 259}, 11: {'length': 2.6, 'dimension': 2, 'stress': 201}}
```

#### B1\_c. Access a Dictionary

We could easily find the information on a specific bar. For example, let's find the information on bar `3`.

```python
index = 3
print("bar", index, "information", bars_dict[index])
```

```
bar 3 information {'length': 3.4, 'dimension': 2, 'stress': 134}
```

#### B1\_d. Modify a Dictionary

Similar to the list, we can modify information in the dictionary. If we find the stress of bar 3 is incorrect, we could modify it.

```python
bars_dict[index]["stress"] = 154
print("bar", index, "information", bars_dict[index])
```

```
bar 3 information {'length': 3.4, 'dimension': 2, 'stress': 154}
```

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

```
Voussior 0 volume: 132090
Voussior 1 volume: 157320
Voussior 2 volume: 141120
Voussior 3 volume: 159980
Voussior 4 volume: 225620
Voussior 5 volume: 240000
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
