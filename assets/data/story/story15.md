# Forward to the Final Gateway!

## Forward to the Final Gateway! `Built-in Function` `Lambda Function`

The team Licat overcame every challenge and finally arrived deep within the cavern. The cavern was deep and vast. After walking for a while, they reached a crossroads. There was a sign that read `max, potion`, along with glass bottles containing potions.

> "This is a potion, meow! Since it says `max`, I guess we should move towards the path with more potions!"

Licat started moving towards the path that had more potions. At the end of the cavern, there was a massive door.

![End of the cavern](./story15-1.png)

When Gary pressed a decoration attached to the door, the decoration went inside. The pressed decoration could be restored by pressing it again.

![Door buttons](./story15-2.png)

Upon closer look, the following guidance message was found:

```text
Among the potions you have consumed so far, add up the number of potions that are more than 3 and less than 6. Then shout out the sum!
```

When Licat said the number of potions consumed so far, patterns slowly appeared on the door.

![Patterns on the door](./story15-3.png)

### Mission
While moving along the path with more potions, you need to record the number of potions Licat has consumed so far. When you reach the end of the path, calculate the total sum of potions that are more than 3 and less than 6. Print the exact calculated number.

### Basic Data
There are a total of 4 crossroads.

```python
# Number of potions Licat has consumed
potion_counts = [0, 0, 0, 0]
```


## Hints
Complete the mission by combining the codes below.
```python
filter()
sum()
lambda x: x**2
```