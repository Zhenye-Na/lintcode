# 607. Two Sum III - Data structure design

**Description**

Design and implement a `TwoSum` class. It should support the following operations: `add` and `find`.

```
add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.
```

**Example**

Example 1:

```
add(1); add(3); add(5);
find(4) // return true
find(7) // return false
```

**Two Pointers**

```python
class TwoSum:
    def __init__(self):
        self.pool = []

    """
    @param number: An integer
    @return: nothing
    """
    def add(self, number):
        # write your code here
        self.pool.append(number)


    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        # write your code here
        if len(self.pool) < 2:
            return False

        left, right = 0, len(self.pool) - 1
        self.pool.sort()
        while left < right:
            if self.pool[left] + self.pool[right] == value:
                return True
            elif self.pool[left] + self.pool[right] < value:
                left += 1
            else:
                right -= 1

        return False
```
