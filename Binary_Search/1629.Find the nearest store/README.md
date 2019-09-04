# 1629. Find the nearest store

**Description**


There are some stores and houses on a street. Please find the nearest store to each house.

You are given two array represent the location of the stores and houses.

Return an array with the location of the nearest store to each house. If there are two stores that are the same distance from the house return the left one.

Tips: 

1. There are multiple stores and houses in the same location. And the locations in array are disordered.
2. The array of location must not be empty.


**Example**

Example 1:

```
stores: [4,7,8,1,6,6,2]
houses: [1, 8, 5]
return: [1, 8, 4]

Input:
4 7 8 1 6 6 2
1 8 5
Output:
1 8 4
```

Example 2:

```
stores: [2,3,5,5,6,10]
houses: [4,11,7]
return: [3,10,6]

Input:
2 3 5 5 6 10
4 11 7
Output:
3 10 6
```


```python
class Solution:
    """
    @param stores: The location of each store.
    @param houses: The location of each house.
    @return: The location of the nearest store to each house.
    """

    def findNearestStore(self, stores, houses):
        sorted_stores = sorted(stores)
        results = []

        for house in houses:
            results.append(self._findClosest(house, sorted_stores))

        return results

    def _findClosest(self, target, stores):
        start, end = 0, len(stores) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if stores[mid] <= target:
                start = mid
            else:
                end = mid

        return stores[start] if abs(target - stores[start]) <= abs(target - stores[end]) else stores[end]
```