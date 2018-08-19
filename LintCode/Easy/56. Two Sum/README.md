# 56. Two Sum


- **Description**
    - Given an array of integers, find two numbers such that they add up to a specific target number.
    - The function twoSum should return indices of the two numbers such that they add up to the target, where **index1 must be less than index2**. Please note that your returned answers (both index1 and index2) are zero-based.
    - **You may assume that each input would have exactly one solution**
- **Example**
    - `numbers = [2, 7, 11, 15]`, `target = 9`
    - return `[0, 1]`
- **Challenge**
    - Either of the following solutions are acceptable:
    - `O(n)` Space, `O(nlogn)` Time
    - `O(n)` Space, `O(n)` Time



## Solution

### `O(n)` Space, `O(nlogn)` Time

#### Two Pointers

```python
class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        start, end = 0, len(numbers) - 1

        # Copy a new array without messing the original array
        newNumbers = numbers[:]

        # sort new array -> Two Pointers need it
        newNumbers.sort()

        # Two Pointers
        while start < end:

            # sum is greater than target,
            if newNumbers[start] + newNumbers[end] > target:
                end -= 1
            elif newNumbers[start] + newNumbers[end] < target:
                start += 1
            else:
                # solution found
                break

        firstNum = newNumbers[start]
        lastNum  = newNumbers[end]
        result = [-1] * 2


        # If the two numbers are not same, just find them
        if firstNum != lastNum:
            for i in range(len(numbers)):
                if firstNum == numbers[i]:
                    result[0] = i
                if lastNum == numbers[i]:
                    result[1] = i

        # If they are the same, then the second one must appear after the first
        else:
            for i in range(len(numbers)):
                if firstNum == numbers[i]:
                    result[0] = i

                    for j in range(i + 1, len(numbers)):
                        if lastNum == numbers[i]:
                            result[1] = i

        # Return sorted array -> in case they are not in ascending order
        return sorted(result)
```


### `O(n)` Space, `O(n)` Time

#### Java `HashMap<>()`

```java
public class Solution {
    /**
     * @param numbers: An array of Integer
     * @param target: target = numbers[index1] + numbers[index2]
     * @return: [index1, index2] (index1 < index2)
     */
    public int[] twoSum(int[] numbers, int target) {
        // write your code here

        HashMap<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < numbers.length; i++) {
            if (map.get(numbers[i]) != null) {
                int[] result = {map.get(numbers[i]), i};
                return result;
            }
            map.put(target - numbers[i], i);
        }

        int[] result = {};
        return result;

    }
}
```

#### Python `{}`

```python
class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        dict = {}
        for i in range(len(numbers)):

            if numbers[i] in dict:
                return [dict[numbers[i]] , i]

            dict[target - numbers[i]] = i

        return []
```
