# Computational Structural Design II <br/> Intro to coding in Python and the Jupyter notebook II

### Learning Goal: 
- understand how to write a function
- understand how to use built-in functions in Python
- understand `dictionary`

### Content:
- [A. Strut Length](#exA)
    - A1. Find the Longest Cable
    - A2. Sort the cables
- [B. Data Management](#exB)
    - B1. Cable-net Data
    - B2. Calculate Voussoir Volume

### Exercise:
- [Calculate Voussoir Weight](#exB2)

<a id='exA'></a>

# A. Strut Length <br/>
## A1. Find the Longest Cable
### Question: 
You are still working on your grid shell. You want to find the longest strut in your grid shell. How can you find it?

### Answer:
You can pick one cable, and suppose it is the longest cable. Then, pick the second one. If it is longer than the first one, then the longest one is the second one. Keep repeating this process until you have compared all the cables. Then you will find the longest cable. 

### A1_a. Flowchart
<img src="https://files.gitbook.com/v0/b/gitbook-28427.appspot.com/o/assets%2F-M730QpQnbAMvz44bqhc%2F-MMRUovKxE5lvzBXWGn6%2F-MMRYft9oXZpioSHn49-%2Fweek1_dia%20(2).png?alt=media&token=0e484961-4ab7-4f24-855d-abb21916f9b2" style="margin-left:auto; margin-right:auto"/>


### A1_b. Code


```python
# Input
# cable length of the cable-net
cablenet = [1.6, 3.6, 2.4, 3.4, 2.7, 2.8, 3.3, 3.1, 3.7, 1.8, 1.8, 1.8, 2.6]

# initiate longest cable, suppose the first cable is the longest
longest = cablenet[0]  
index = 0  

# Compare Cable Length
# if the cable is longer than the longest cable
# assign the longest cable the new cable length
for i, cable in enumerate(cablenet):
    if cable >= longest:
        longest = cable
        index = i

# Output
print("The longest cable is cable", index + 1, "and its length is", longest, "m.")
```

    The longest cable is cable 9 and its length is 3.7 m.


## A2. Sort the cables
### Question:
Now you want to sort the cables from the longest to the shortest. How can you do it?

### Answer:
One way to solve this problem is to go through all the cables, and find the longest one. Add the longest one to a new list. 

| Sorted Cables | Length (m) |
| :---: | :---: |
| 1 | 3.7 |

Then do it again and find the next-longest cable. 

| Sorted Cables | Length (m) |
| :---: | :---: |
| 1 | 3.7 |
| 2 | 3.6 |

Keep doing and you would get the sorted cables from longest to shortest.

### A2_a. Flowchart
<img src="https://files.gitbook.com/v0/b/gitbook-28427.appspot.com/o/assets%2F-M730QpQnbAMvz44bqhc%2F-MMRwMy-a-u_usu0jZWc%2F-MMSbXFPpSLZty5V4M-r%2Fweek1_dia%20(3).png?alt=media&token=f1cd130f-cecd-40ae-846a-ddc96deb26d5" style="margin-left:auto; margin-right:auto"/>


### A2_b. Write the Function
To find one element in the sorted cable list, we need to find the longest cable in the remaining cable list. We could turn this part of the statements into a function, which we could reuse when needed. When we write a function, it's suggested to write a short doc describing the function.


```python
def find_longest_cable(cablenet):
    """
    to find the longest cable in the cable list
    Parameters
    ----------
    cables : list
        A list containing the cable length of the cable-net

    Returns
    -------
    index: int
        Index of the longest cable in the cable list
    longest: float
        Length of the longest cable in the cable list
    """

    # check the list is not empty
    if cablenet == []:
        return

    # initiate longest cable, suppose the first cable is the longest
    longest = cablenet[0]  
    index = 0  

    # compare every cable with the longest cable
    for i, cable in enumerate(cablenet):
        if cable >= longest:
            longest = cable
            index = i

    return index, longest
```

### A2_c. Call the Function
Now we could use `find_longest_cable` function to sort our cables from longest to shortest. Every time we find the longest cable, we will delete it from the cablenet list and add it to the sorted_cables list. 


```python
# Input
# cable length of the cable-net
cablenet = [1.6, 3.6, 2.4, 3.4, 2.7, 2.8, 3.3, 3.1, 3.7, 1.8, 1.8, 1.8, 2.6]
# create empty cable list
sorted_cables = []

# Program
while cablenet != []:
    # find the longest cable in the remaining of the cable list
    i, longest = find_longest_cable(cablenet)
    # remove the longest item from the cable list
    cablenet.pop(i)
    # add the longest item to the sorted cable list
    sorted_cables.append(longest)

# Output
print("The sorted cable list is", sorted_cables)
```

    The sorted cable list is [3.7, 3.6, 3.4, 3.3, 3.1, 2.8, 2.7, 2.6, 2.4, 1.8, 1.8, 1.8, 1.6]


### A2_d. Turn Sorting into a Function
We could also turn the sorting into a function. We can call a function in another function. This sorting method is also called `selecting sorting` algorithm.  


```python
def sort_cable_length(cables):
    """
    sort the cables in descending order

    Parameters
    ----------
    cables: list
        A list containing the cable length of the cable-net

    Returns
    -------
    sorted_cables: list
        A list containing the cable length of the cable-net in descending order
    
    """
    # create empty cable list
    sorted_cables = []

    while cables != []:
        # find the longest cable in the remaining of the cable list
        i, longest = find_longest_cable(cables)
        # remove the longest item from the cable list
        cables.pop(i)
        # add the longest item to the sorted cable list
        sorted_cables.append(longest)

    return sorted_cables
```

### A2_d. Python List Functions

Python has built-in method `sorted()` that could sort a list easily. `max()` and `min()` would find the largest and smallest item in the list. 


```python
cablenet = [1.6, 3.6, 2.4, 3.4, 2.7, 2.8, 3.3, 3.1, 3.7, 1.8, 1.8, 1.8, 2.6]

print("Longest cable is", max(cablenet), "m.")
print("Shortest cable is", min(cablenet), "m.")
print("Cables in ascending order:", sorted(cablenet))
print("Cables in descending order:", sorted(cablenet, reverse=True))
print("Total cable length is", sum(cablenet), "m.")
```

    Longest cable is 3.7 m.
    Shortest cable is 1.6 m.
    Cables in ascending order: [1.6, 1.8, 1.8, 1.8, 2.4, 2.6, 2.7, 2.8, 3.1, 3.3, 3.4, 3.6, 3.7]
    Cables in descending order: [3.7, 3.6, 3.4, 3.3, 3.1, 2.8, 2.7, 2.6, 2.4, 1.8, 1.8, 1.8, 1.6]
    Total cable length is 34.6 m.


---

<a id='exB'></a>

# B. Data Management <br/>
## B1. Cable-net Data
### Question: 
While digging deep into the design and fabrication, you start to accumulating information about the cables, including the length, dimension, cable stress, etc. How would you hold your information?

| Cable No. | Length (m) | Dimension (mm) | Stress (N/mm<sup>2</sup>) |
| :---: | :---: | :---: | :---: |
| 1 | 1.6 | 2 | 275 |
| 2 | 3.6 | 2 | 185 |
| 3 | 2.4 | 2 | 105 |
| 4 | 3.4 | 2 | 134 |
| 5 | 2.7 | 2 | 155 |
| 6 | 2.8 | 2 | 265 |
| 7 | 3.3 | 2 | 150 |
| 8 | 3.1 | 2 | 185 |
| 9 | 3.7 | 2 | 124 |
| 10 | 1.8 | 2 | 234 |
| 11 | 1.8 | 2 | 259 |
| 12 | 2.6 | 2 | 201 |

### Answer:
In this case, we can create three lists, containing information of length, dimension, and stress respectively. However, this solution is not so efficient and clear, especially when our data set is big. Here we would introduce a new collection type - `dictionary`. 

### B1_a. Create a Dictionary
First, let's create a dictionary to save all the lengths of the cables. The key is the index of the cable, and the item is the length.


```python
cable_length_list = [1.6, 3.6, 2.4, 3.4, 2.7, 2.8, 3.3, 3.1, 3.7, 1.8, 1.8, 2.6]

# create an empty dictionary
cables_dict = {}

for i in range(len(cable_length_list)):
    cables_dict[i] = cable_length_list[i]

print(cables_dict)
```

    {0: 1.6, 1: 3.6, 2: 2.4, 3: 3.4, 4: 2.7, 5: 2.8, 6: 3.3, 7: 3.1, 8: 3.7, 9: 1.8, 10: 1.8, 11: 2.6}


### B1_b. Add Values to Dictionary
Now let's save more information.


```python
cable_length_list = [1.6, 3.6, 2.4, 3.4, 2.7, 2.8, 3.3, 3.1, 3.7, 1.8, 1.8, 2.6]
cable_stress_list = [275, 185, 105, 134, 155, 265, 150, 185, 124, 234, 259, 201]

# create an empty dictionary
# key is index of the cable, item is infomation of the cable
cables_dict = {}

for i in range(len(cable_length_list)):
    # for each cable, we create another dictionary
    # key: category, item: value of the category
    cables_dict[i] = {}
    cables_dict[i]["length"] = cable_length_list[i]
    cables_dict[i]["dimension"] = 2
    cables_dict[i]["stress"] = cable_stress_list[i]

print(cables_dict)
```

    {0: {'length': 1.6, 'dimension': 2, 'stress': 275}, 1: {'length': 3.6, 'dimension': 2, 'stress': 185}, 2: {'length': 2.4, 'dimension': 2, 'stress': 105}, 3: {'length': 3.4, 'dimension': 2, 'stress': 134}, 4: {'length': 2.7, 'dimension': 2, 'stress': 155}, 5: {'length': 2.8, 'dimension': 2, 'stress': 265}, 6: {'length': 3.3, 'dimension': 2, 'stress': 150}, 7: {'length': 3.1, 'dimension': 2, 'stress': 185}, 8: {'length': 3.7, 'dimension': 2, 'stress': 124}, 9: {'length': 1.8, 'dimension': 2, 'stress': 234}, 10: {'length': 1.8, 'dimension': 2, 'stress': 259}, 11: {'length': 2.6, 'dimension': 2, 'stress': 201}}


### B1_c. Access a Dictionary
We could easily find the information on a specific cable. For example, let's find the information on cable `3`.


```python
index = 3
print("cable", index, "information", cables_dict[index])
```

    cable 3 information {'length': 3.4, 'dimension': 2, 'stress': 134}


### B1_d. Modify a Dictionary
Similar to the list, we can modify information in the dictionary. If we find the stress of cable 3 is incorrect, we could modify it.


```python
cables_dict[index]["stress"] = 154
print("cable", index, "information", cables_dict[index])
```

    cable 3 information {'length': 3.4, 'dimension': 2, 'stress': 154}


## B2. Calculate Voussoir Volume
### Question: 
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

### Answer:



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

    Voussior 0 volume: 132090
    Voussior 1 volume: 157320
    Voussior 2 volume: 141120
    Voussior 3 volume: 159980
    Voussior 4 volume: 225620
    Voussior 5 volume: 240000


<a id='exB2'></a>

### Exercise: Calculate Voussoir Weight
Now you decide the voussoir would be cut from limestone, and its density is 2160 kg/m<sup>3</sup>, could you calculate the weight of each piece and add it to the dictionary?
$$
weight = volume * thickness
$$


```python
density = 2160  # kg/m3

# iterate through the dictionary
for key in vault.keys():
    # please write down your answer here
```

---
### Answer:


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
