# Let's pick out the rotten carrots!

## Let's pick out the rotten carrots! `Comprehension` `Ternary Operator`

Binky, who was the trusted companion of Pie and Sun, was guarding the treasure with SoulGom. When Licat was overcoming various challenges, Binky gave him some advice. When Licat got the jewel, Binky realized it was the last mission left by Pie and Sun.

> ‘A person who will never use an ax again after being stamped with an ax, or a person who can trust and embrace it even if he is stamped with an ax.’

This was something as heavy as the weight of a crown. Binky witnessed the faith, trust, and tolerance that Licat shared with those who overcame many obstacles. If Licat tried to claim the treasure alone, Binky was prepared to retrieve it. While contemplating, Binky received Licat’s call.

> “Binky, take it! I wouldn't have come this far without Binky!”

Binky, who never expected to receive it, was taken aback. And she found this situation amusing which is guided by destiny. Pie and Sun had entrusted Binky to guard the treasure until the right person emerged. And now Binky received the treasure from the right one. Now is the time for Binky to prove herself.

![Binky with Reality Stone](./18_1.webp)

- Reality Stone: Can manipulate people's vision to create illusions resembling reality.

Binky moved to her hometown, where she had been away for a long time. She worked hard to enhance her ability to use the Reality Stone and pondered on what kind of power she could gather with it.

Upon arriving, Binky found a village that had changed a lot. The old hills were gone, and only tall buildings remained due to industrialization.

Starving rabbits lay by the roadside, and rotten carrots were scattered in the fields. Well-dressed lions and hyenas were entering the tall buildings, while rabbits were working at the construction site.

![](./18_2.webp)

> "I'll recreate the village where there was clearer water, a garden to rest, and a fresh carrot to eat at any time. The air is clear, and people come out and run around. Then, people will know how precious it is to lose them."

### Mission
Exclude carrots with low freshness and items other than carrots from the given list, and select only carrots with a freshness score of 5 or higher. Lastly, output them to the terminal. The list is structured with `['item name', freshness score]` for each item. Use `list comprehension` and the `ternary operator` to complete this mission.

### Basic Data
```python
items = [['carrot', 3], ['apple', 5], ['carrot', 6], ['grape', 4], ['carrot', 7]]
```

### Output
```python
['carrot', 6], ['carrot', 7]
```

## Hints
Complete the mission by combining the codes below.

```python
result = [item for item in items]
result = 'hello' if True else 'world'
if item[0] == 'carrot' and item[1] >= 5
```