# Gather Your Colleagues!

## Gather Your Colleagues! `Type Casting` `Lambda Function` `Built-in Function`

![Licat's precious colleagues](./14.webp)

During his journey, Licat met many colleagues: Javadog, who loves Java and is curious about Python, Gary whom he met on a ship and solved algorithms together, and SoulGom, the last gatekeeper and a henchman of Pie and Sun.

As the number of colleagues grew, Licat wanted to see their information easily. There were too many people to rely just on his memory. Currently, this information is stored in a list in tuple format.

Licat wants to manage this data in dictionary. Your mission is to convert the given data from tuples within a list into dictionaries within a list and extract the desired data. In other words, convert the tuples within the list into dictionary format and then output only the names extracted from those dictionaries.

### Mission

Your mission is to obtain the required results using the provided data. Instead of direct printing, create and use a dictionary to output the result.

### Basic Data

```python
# Tuple-based colleague information
crew_info = [
    ("Javadog", 95, "a lifelong Java enthusiast curious about Python. When Python expert Licat suggested him to be a colleague, Javadog felt curious and gave him a small test. Impressed by Licat's wisdom in solving the problem, he became Licat's colleague. He wants to try various things with Python."),
    ("Gary", 85, "met on a ship heading to algorithmic treasures. During a discussion about who would take the remaining seat, Licat suggested the idea of considering the weak using a page replacement algorithm. Gary was impressed and became Licat's colleague."),
    ("SoulGom", 1, "a henchman of Pie and Sun. Moves with infinite power as an NPC and acts as the gatekeeper of the last gate of Pie and Sun. Disguised as a cafe owner, but easily recognized.")
]
```

### Transformed Data

The transformed data format is as follows. Use the tuple data to create it as shown below and output `Javadog`, `Gary`, `SoulGom` as a final result.

```python
crew_info = [{
    "Name": "Javadog"
    "Coding Ability": 95
    "Note": "a lifelong Java enthusiast curious about Python. When Python expert Licat suggested him to be a colleague, Javadog felt curious and gave him a small test. Impressed by Licat's wisdom in solving the problem, he became Licat's colleague. He wants to try various things with Python."
},
{
    "Name": "Gary"
    "Coding Ability": 85
    "Note": "met on a ship heading to algorithmic treasures. During a discussion about who would take the remaining seat, Licat suggested the idea of considering the weak using a page replacement algorithm. Gary was impressed and became Licat's colleague."
}
{
    "Name": "SoulGom"
    "Coding Ability": 1
    "Note": "a henchman of Pie and Sun. Moves with infinite power as an NPC and acts as the gatekeeper of the last gate of Pie and Sun. Disguised as a cafe owner, but easily recognized"
}]
```

### Output
```python
print(['Javadog', 'Gary', 'SoulGom'])
```

## Hints
Complete the mission by combining the codes below.
```python
dict()
map()
list()
print()
lambda x: x**2
```