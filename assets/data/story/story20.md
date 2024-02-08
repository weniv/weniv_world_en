# Mining Ore

## Mining Ore `Class`

SoulGom didn't have a hometown as she was an NPC created by Pie and Sun! But she could gain a soul thanks to the Soul Stone. Along with it came great wisdom and the ability to see the world of souls.

SoulGom pondered over her new life and abilities.

> 'How can I be of help in this world?'

Through the wisdom gained from the Soul Stone, SoulGom could predict that a significant war fund would soon be needed.

SoulGom headed to the Arctic. Despite the extreme cold, she could move freely thanks to her nature. She went deeper and deeper into where untouched ancient treasures were hidden.

![SoulGom and treasures](./20.webp)

Unimaginable amounts of jewels adorned the walls, shimmering like starlight. SoulGom thought that when war broke out, the currency value would plummet, hyperinflation would engulf Weniv World, and as a result, the value of jewels would rise. Looking at the jewels, SoulGom chuckled faintly.

Faith, fulfillment, purpose, the reason for existence, innovation, and revolution. As she wielded her pickaxe, SoulGom transmuted them into wisdom and soul.

### Mission
Mine gold and diamond from the map to create instances of `class Treasure`. Define the `__str__` method so that when each instance is printed like "10 gold, 20 diamond". `class Treasure` should include `__init__`, `__str__`, and `get_item` method to increase the quantity of items when collected.

### Basic Data
```python
class Treasure:
    # Define class
    pass

# Create instance
gold = Treasure('gold', 0)
diamond = Treasure('diamond', 0)

# Instance list
treasure_list = [gold, diamond]

# Print each instance
for treasure in treasure_list:
    print(treasure)
```

### Output
```python
10 gold
20 diamond
```

## Hints
Complete the mission by combining the codes below.

```python
class Treasure:
    # Initialization method
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    # String representation method
    def __str__(self):
        pass

    # Method to increase item quantity
    def get_item(self):
        pass
```