# Tutorial 2


### Computational Structural Design II Intro to coding in Python and the Jupyter notebook I

**Code Link**
* [Introduction to Jupyter Notebook](https://mybinder.org/v2/gh/BlockResearchGroup/CSD2_2022.git/ca2aada?labpath=2_Geometry%2FIntroduction%2FIntroductionToJupyterNotebook.ipynb)

* [Tutorial 2 Notebook](https://mybinder.org/v2/gh/BlockResearchGroup/CSD2_2022.git/ca2aada?labpath=2_Geometry%2FTutorial2%2Fweek_2_lecture.ipynb)

* [Tutorial 2 Notebook (full)](https://mybinder.org/v2/gh/BlockResearchGroup/CSD2_2022.git/ca2aada?labpath=2_Geometry%2FTutorial2%2Fweek_2.ipynb)


**Learning Goals:**

* develop your procedural thinking
* draw a logic diagram or flowchart
* translate the flowchart to pseudocode using comments in Python
* write basic Python script including: variables, object types, conditionals,for loops, while loops, lists, mathematical operators, print statements

**Content:**

* [Gridshell Cost I](tutorial2a.md#ex1)
* [Voussoir Weight](tutorial2a.md#ex2)

**Exercise:**

* [Gridshell Cost II](tutorial2a.md#tut1\_ex)

**Reference:**
* [Python Tutorial](https://docs.python.org/3/tutorial/)

---


#### Question:

Suppose you have designed a gridshell made from steel bars. You are going to fabricate them and estimate the total cost. There are 2 different prices for bars longer than 3 meters and shorter than 3 meters, 5 Fr and 3 Fr correspondingly. Now you need to count how many bars are above 3 meters and how many are below, to calculate the cost.

![](https://github.com/BlockResearchGroup/CSD2\_2022/blob/c6f4099930d5936262cb131b4a0dd21c19d2d073/2\_Geometry/Tutorial2/img/T2\_diagram\_bars.png?raw=true)

| Bar No. | Length (m) |
| :-----: | :--------: |
|    1    |     1.6    |
|    2    |     3.6    |
|    3    |     2.4    |
|    4    |     3.4    |
|    5    |     2.7    |
|    6    |     2.8    |
|    7    |     3.3    |
|    8    |     3.1    |
|    9    |     3.7    |
|    10   |     1.8    |
|    11   |     1.8    |
|    12   |     2.6    |

#### Part A: Check Length of One Bar

Let's first break this problem down into small steps. Firstly, you could pick one bar and check whether its length is larger than 3 m. Secondly, you could repeat the first step to check all the bars, and then multiply the number of bars with the cost.

#### A\_0. Flowchart

A flowchart is a step-by-step approach until you find the answer. Flowcharts help you to visualize the processes in small steps and they are very similar to how the computer executes your instructions.

\
\


![](https://files.gitbook.com/v0/b/gitbook-28427.appspot.com/o/assets%2F-M730QpQnbAMvz44bqhc%2F-MNht34RYVKlCmOCcR92%2F-MNiECpXmHCeJT14YSZs%2Fimage.png?alt=media\&token=13c41acb-ddda-47f9-a01e-89861de8fc7c)

|   Function   |        Shape       |                                   Explanation                                   |
| :----------: | :----------------: | :-----------------------------------------------------------------------------: |
|   Start/End  | rounded rectangles | Start is required of all flowcharts, while some flowcharts may not have an end. |
|    Process   |      rectangle     |               It involves the action, to do something. e.g. add 1               |
| Input/Output |    parallelogram   |      It indicates that manual operation is needed. e.g. type in the number      |
|   Decision   |       rhombus      |                        e.g. Is the number bigger than 10?                       |
|     Arrow    |        arrow       |                       It indicates the flow of the chart.                       |

#### A\_1. Draw Flowchart

Firstly, we can draw a [**flowchart**](https://app.gitbook.com/s/-M730QpQnbAMvz44bqhc/learn-to-code/i.-my-first-python-script/cheat-sheet#flowchart).

![](https://github.com/BlockResearchGroup/CSD2\_2022/blob/5319ae679b8e41fbf62b45afee4b4c2794c35233/2\_Geometry/Tutorial2/img/week1\_ex1.png?raw=true)

**A\_2. Write pseudocode**

Firstly, we could convert our flowchart to [**pseudocode**](https://en.wikipedia.org/wiki/Pseudocode#:\~:text=In%20computer%20science%2C%20pseudocode%20is,reading%20rather%20than%20machine%20reading.), a plain-English version of the flowchart.

The pseudocode are written in Python [**comments**](https://www.w3schools.com/python/python\_comments.asp), which starts with a `#` and will not be executed when we run the code. Comments help us to organize the logic when we start to write code, as well as in the future to keep track of and to understand the code. You can type `#` in front of the line you want to comment out. If you want to comment several lines, you can select the lines that need to be commented out, and press `ctrl + /`.

<mark style="color:blue;">pick one bar</mark>

<mark style="color:blue;">if length larger than 3?</mark>

```
# long bar 
```

<mark style="color:blue;">else</mark>

<mark style="color:blue;">short bar</mark>

**A\_3. Write your code**

We could turn the pseudocode line by line into code.

```python
# pick one bar
bar_length = 1.6
# if length bigger than 3?
if bar_length > 3:
    # long bar 
    print("This is a long bar.")
# else
else:
    # short bar
    print("This is a short bar.")
```

```
This is a short bar.
```

#### Part B: Check Length of All Bars

Let's complete the program. You need to repeat the whole process of checking the bar length until you have classified all the bars. You could use another condition in your flowchart for the repetition instructions. After you have checked all the bar in your gridshell, you could count the amount in two length types and calculate the total cost.

**B\_1. Draw Flowchart**

![](https://github.com/BlockResearchGroup/CSD2\_2022/blob/75a96a6722bcc51b90424947811f8bd725eb24b7/2\_Geometry/Tutorial2/img/week1\_ex1\_2.jpg?raw=true)\\

**B\_2. Write pseudocode**

<mark style="color:blue;">pick one bar in the gridshell</mark>

<mark style="color:blue;">if length larger than 3?</mark>

<mark style="color:blue;">long bar amount + 1</mark>

<mark style="color:blue;">else</mark>

<mark style="color:blue;">short bar amount + 1</mark>

<mark style="color:blue;">repeat until the all the bars are checked</mark>

<mark style="color:blue;">calculate total cost</mark>

**B\_3. Write the code**

Here we need to input all the lengths of our bars. Instead of multiple length variables, we could store them in a collection - a [**list**](https://app.gitbook.com/s/-M730QpQnbAMvz44bqhc/learn-to-code/i.-my-first-python-script/cheat-sheet#list). List items are ordered, or in other words, indexed, the first item has index `0`, the second item has index `1` etc.

```python
gridshell = [1.6, 3.6, 2.4, 3.4, 2.7, 2.8, 3.3, 3.1, 3.7, 1.8, 1.8, 2.6]
print(gridshell[0])  # 1.6
print(gridshell[1])  # 3.6
print(gridshell[-1])  # 2.6
```

```
1.6
3.6
2.6
```

To iterate over a list, we could use a [**`for`**](https://app.gitbook.com/s/-M730QpQnbAMvz44bqhc/learn-to-code/i.-my-first-python-script/cheat-sheet#for-loop-and-while-loop) loop.

```python
for bar in gridshell:
    print(bar)
```

```
1.6
3.6
2.4
3.4
2.7
2.8
3.3
3.1
3.7
1.8
1.8
2.6
```

Now we go through the list, check the bar length one by one, and count the number of the corresponding type. Thus, we need to initiate the counter of two types at the beginning of our code. Here, we create two new variables: `long_bar_count`, `short_bar_count`, and set their initial value to `0`.

```python
# Input
gridshell = [1.6, 3.6, 2.4, 3.4, 2.7, 2.8, 3.3, 3.1, 3.7, 1.8, 1.8, 2.6]
long_bar_count = 0
short_bar_count = 0
long_bar_price = 5
short_bar_price = 3

# pick one bar in the gridshell, check its length
# repeat until the all the bars are checked
for bar in gridshell:
    # if length bigger than 3?
    if bar > 3:
        # long bar amount + 1
        long_bar_count += 1
    # else
    else:
        # short bar amount + 1
        short_bar_count += 1
# calculate total cost
total_cost = long_bar_count * long_bar_price + short_bar_count * short_bar_price

# Output
print("Total cost is", total_cost, "CHF")
```

```
Total cost is 46 CHF
```

#### Part C: Modify Bar Length

Oh, No!... You realize that you have measured the length of a bars wrongly. Don't worry. The cabarble length list we use as input can be modified because list items are changeable. You could also modify a value in the `gridshell` list by referring to the item's **index**. Note that the index always starts from **`0`**!

| Bar No. | Index | Length (m) |
| :-----: | :---: | :--------: |
|    1    |   0   |     1.6    |
|    2    |   1   |     3.6    |
|    3    |   2   |     2.4    |
|    4    |   3   |     3.4    |
|    5    |   4   |     2.7    |
|    6    |   5   |     2.8    |
|    7    |   6   |     3.3    |
|    8    |   7   |     3.1    |
|    9    |   8   |     3.7    |
|    10   |   9   |     1.8    |
|    11   |   10  |     1.8    |
|    12   |   11  |     2.6    |

For example, we find out the **3rd** bar has the wrong length, whose corresponding index is `2` in the list. Find it, and change its value.

```python
gridshell[2] = 2.5
print(gridshell)
```

```
[1.6, 3.6, 2.5, 3.4, 2.7, 2.8, 3.3, 3.1, 3.7, 1.8, 1.8, 2.6]
```

If we realize that we have omitted one bar that is 4 m, we could use `append` to add it at the end of our list.

```python
print("We have", len(gridshell), "bars.")
print(gridshell)
gridshell.append(4.0)
print("After adding the new bar, we have", len(gridshell), "bars.")
print(gridshell)
```

```
We have 12 bars.
[1.6, 3.6, 2.5, 3.4, 2.7, 2.8, 3.3, 3.1, 3.7, 1.8, 1.8, 2.6]
After adding the new bar, we have 13 bars.
[1.6, 3.6, 2.5, 3.4, 2.7, 2.8, 3.3, 3.1, 3.7, 1.8, 1.8, 2.6, 4.0]
```

If you need to delete a bar you could either delete it by its index. For example, we want to delete the 4th bar in the list, whose index is `3`.

```python
gridshell.pop(3)
print(gridshell)
```

```
[1.6, 3.6, 2.5, 2.7, 2.8, 3.3, 3.1, 3.7, 1.8, 1.8, 2.6, 4.0]
```

The bar can also be deleted by its value. If there are duplicated values, this method only removes the first matching element.

```python
gridshell.remove(3.1)
print(gridshell)
```

```
[1.6, 3.6, 2.5, 2.7, 2.8, 3.3, 3.7, 1.8, 1.8, 2.6, 4.0]
```

#### Exercise: Bars of 3 different Lengths

Suppose there are three different prices for the bars: 2 Fr. for bars shorter than 2 m; 3 Fr. for bars between 2 m and 3 m; 5 Fr. for bars longer than 3 m. Could you modify your code and calculate the total cost?

Hint:\
You need to classify 3 types of bars. When you run into a situation where you have several conditions, you can place as many elif conditions as necessary between the if condition and the else condition.
If you don't know how to add more conditions to the ``if`` statement, try to use google to search for the answer or our reference material: https://docs.python.org/3/tutorial/controlflow.html#if-statements. 

```python
# Input
# bar length of the gridshell
gridshell = [1.6, 3.6, 2.4, 3.4, 2.7, 2.8, 3.3, 3.1, 3.7, 1.8, 1.8, 2.6]

# please write down your answer here
```

***

Check Voussoir Weight\\

#### Question A:

You have designed a freeform masonry vault and all the stone pieces are unique. You want to assemble the vault manually. However, on the construction site, the manual handling weight limit is 25 kg. Thus, you have to find the pieces that are too heavy and export their index.

| CabVoussoirle No. | Weight (kg) |
| :---------------: | :---------: |
|         1         |      15     |
|         2         |      20     |
|         3         |      54     |
|         4         |      18     |
|         5         |      26     |
|         6         |      18     |

\\

**A\_1. Draw Flowchart**

![](https://github.com/BlockResearchGroup/CSD2\_2022/blob/75a96a6722bcc51b90424947811f8bd725eb24b7/2\_Geometry/Tutorial2/img/week1\_ex2.png?raw=true)\\

**A\_2. Write pseudocode**

<mark style="color:blue;">pick one voussoir in the vault</mark>

<mark style="color:blue;">if weight heavier than 25</mark>

<mark style="color:blue;">mark it as problematic voussoir</mark>

<mark style="color:blue;">repeat until all the voussoirs are checked</mark>

<mark style="color:blue;">output the problmatic voussoirs</mark>

**A\_3. Write your code**

Here, we will use the `enumerate` method of a list, which adds a counter when we iterate over the list.

```python
voussoir_weight_list = [15, 20, 34, 18, 26, 18]
for i, voussoir in enumerate(voussoir_weight_list):
    print("index", i, "value", voussoir)
```

```
index 0 value 15
index 1 value 20
index 2 value 34
index 3 value 18
index 4 value 26
index 5 value 18
```

We can create an empty list and add the index of the problematic voussoir in the list during our iteration. In the end, we can export the list. The `*` operator unpacks the list.

```python
voussoir_weight_list = [15, 20, 34, 18, 26, 18]
problem_index = []

# enumerate voussoirs in the vault:
for i, voussoir in enumerate(voussoir_weight_list):
    # check whether the weight is bigger than 25 kg
    if voussoir >= 25:
        problem_index.append(i)

print("Voussoir ", *problem_index, "are too heavy.")
```

```
Voussoir  2 4 are too heavy.
```

#### Question B: Optimize Voussoir Weight

Now you would optimize all the voussoirs that are too heavy by cutting them into two pieces while keeping the sequence of the voussoirs.

**B\_1. Draw Flowchart**

We can continue from the last example. When the voussoir is too heavy, we need to first cut it in half, then check the weight of the half one. If the new weight is still too heavy, keep cutting. After cutting, we need to add the new cut stones back, so the sequence of the original voussoirs will not change.

![](https://github.com/BlockResearchGroup/CSD2\_2022/blob/75a96a6722bcc51b90424947811f8bd725eb24b7/2\_Geometry/Tutorial2/img/week1\_ex2\_2.png?raw=true)\\

**B\_2. Write pseudocode**

<mark style="color:blue;">pick one voussoir in the vault</mark>

<mark style="color:blue;">if weight heavier than 25</mark>

<mark style="color:blue;">cut it the voussoir in half until the weight is below 25</mark>

<mark style="color:blue;">replace the problematic voussoir with the new ones</mark>

<mark style="color:blue;">repeat until all the voussoirs are checked</mark>

<mark style="color:blue;">output the problmatic voussoirs</mark>

**B\_3. Write your code**

Here, we will use a **`while`** loop, which keeps executing the code inside if the condition is True. The loop will stop when the condition is not fulfilled any more. For example, here we pick a voussoir that is 54 kg and the count is 1. The weight is too heavy. In the first iteration of the while loop, the voussoir will be cut in half, so the weight is divided by 2 and the count is multiplied by 2. Now, the while loop checks the new voussoir weight, which is 54 / 2 = 27. 27 is still bigger than 25, so the loop will keep running. The 27 kg voussoir is further cut in half and the count is multiplied by 2. Now the new weight is 27 / 2 = 13.5, which is smaller than 25. Thus, the while loop stops. Inside the while loop, we redeclare the value of the variable voussoir, variable count in every iteration. So, we can print the final value.

```python
voussoir = 54
count = 1
while voussoir >= 25:
    voussoir /= 2
    count *= 2
print("Weight of the voussoir is", voussoir, 
      "and the total number of voussoirs is", count)
```

```
Weight of the voussoir is 13.5 and the total number of voussoirs is 4
```

Now let's solve the problem. To notice that, when we iterate over the list, the items of the list cannot be modified. Thus, we create a new empty list: `new_voussoir_weights`. After checking each voussoir, we can add the original voussoir or the processed smaller ones to the list.

```python
# Input
voussoir_weight_list = [15, 20, 54, 18, 26, 18]
new_voussoir_weights = []

# enumerate voussoirs in the vault:
for i, voussoir in enumerate(voussoir_weight_list):
    # check whether the weight is bigger than 25 kg
    if voussoir >= 25:
        count = 1
        # cut the voussoir by half until it it less than 25 kg
        while voussoir >= 25:
            voussoir /= 2
            count *= 2
        new_voussoir_weights.extend([voussoir] * count)
    else:
        new_voussoir_weights.append(voussoir)

# Output
print(new_voussoir_weights)
```

```
[15, 20, 13.5, 13.5, 13.5, 13.5, 18, 13.0, 13.0, 18]
```

**Working with Functions**

In computer programming, a function is a named section of a code that performs a specific task. This typically involves taking some input, manipulating the input and returning an output. Next, we will define a simple python function and use it to extract some information from our fabrication data on the gridshell.

```python
def visualize_bar_lengths(bars):
    """
    visulalizes the list of bars

    Parameters
    ----------
    bars: list
        A list containing the bar length of the gridshell

    Returns
    -------
    prints the contents of the list: print output
       A human-readable rendition of the contents of the list
    
    """
    # print the gridshell bars list

    print(bars, 'information on the fabrication data')
    #return bars

# call the function

gridshell = [1.6, 3.6, 2.4, 3.4, 2.7, 2.8, 3.3, 3.1, 3.7, 1.8, 1.8, 2.6]
voussoir_weight_list = [15, 20, 54, 18, 26, 18]

visualization = visualize_bar_lengths(voussoir_weight_list)
```

***

#### Answer to Bar Cost Exercise:

```python
# Input
# bar length of the gridshell
gridshell = [1.6, 3.6, 2.4, 3.4, 2.7, 2.8, 3.3, 3.1, 3.7, 1.8, 1.8, 2.6]


# initiate the bar amount
long_bar_amount = 0
mid_bar_amount = 0
short_bar_amount = 0

# price of bar
short_bar_price = 2
mid_bar_price = 3
long_bar_price = 5


# check length of the bar
for bar in gridshell:
    if bar < 2:
        short_bar_amount += 1
    elif 2 <= bar <= 3:
        mid_bar_amount += 1
    else:
        long_bar_amount += 1

# calculate total cost
total_cost = long_bar_amount * long_bar_price + mid_bar_amount * mid_bar_price + short_bar_amount * short_bar_price

# Output
print("Total cost of the gridshell is", total_cost, "CHF")
```

```
Total cost of the gridshell is 43 CHF
```
