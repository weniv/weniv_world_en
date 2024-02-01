# Convincing the Tribes

## Convincing the Tribes `Comprehension` `Ternary Operator` `Lambda Function` `JSON`

Javadog has returned to his hometown where he had met Licat. He sent a letter to each trustworthy friend in the tribes and invited them. They were top-notch technicians who were forcibly conscripted by Lion and struggled with arduous tasks.

Mind Stone gave Javadog a keen insight. During the conversations with the technicians, he sensed their desire for the restoration of daily life, precious time with family, and peaceful weekends.

Javadog prepared dinner for them with all his heart. With heartfelt treats, they were touched. But everything couldn't be solved in an instant, and it shouldn't have been either. Javadog patiently began to change the village little by little.

After these efforts, many people came to know Javadog’s sincerity and gained the courage to face the truth and the determination to bring about change.

> "A project without pressure or arguing, a dinner with family, a life with a weekend… Our hopes are not that big. But look. In a society where even a small wish can't be fulfilled, what it will look like in 30, 50 years if you don't act for it!"

Javadog showed his sincerity through the Mind Stone, presenting them with a new vision. Then skilled engineers began to take action.

![Javadog giving a speech](./story19-1.jpg)

> "Not for our future, but for the future of our children!" 

Javadog’s words resonated deeply with the villagers, leading to change.

### Mission
Determine if a specific dish can be made based on the freshness and quantity of each ingredient in the given JSON data. This mission involves understanding the JSON, extracting and processing data according to conditions, and using `any` and `all` functions. Determine whether the freshness and quantity of the required ingredients for a specific dish are sufficient, and print the result as `True` or `False` in the terminal.

### Basic Data
```python
# Check conditions for cooking
required_ingredient = ["carrot", "lettuce", "onion", "tomato"]
required_freshness = 5
# A list to see if carrots, lettuce, onions and tomatoes meet the conditions
required = [False, False, False, False]

items = [
    {"name": "carrot", "freshness": 7},
    {"name": "apple", "freshness": 5},
    {"name": "carrot", "freshness": 6},
    {"name": "grape", "freshness": 4},
    {"name": "carrot", "freshness": 8},
    {"name": "lettuce", "freshness": 8},
    {"name": "onion", "freshness": 5},
    {"name": "tomato", "freshness": 5},
]
```

### Target Dish and Required Ingredients
- Dish: Fresh carrot salad
- Required Ingredients: 4 carrots with freshness of 5 or higher

### Output
```python
True or False
```

## Hints
Complete the mission by combining the codes below.

```python
filter()
all()
any()
sum()
and
or
[item for item in items]
result = 'hello' if True else 'world'
required[required_ingredient.index(야채)]
```