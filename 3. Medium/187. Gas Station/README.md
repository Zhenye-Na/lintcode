# 187. Gas Station

- **Description**
    - There are N gas stations along a circular route, where the amount of gas at station i is `gas[i]`.
    - You have a car with an unlimited gas tank and it costs `cost[i]` of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.
    - Return the starting gas station's index if you can travel around the circuit once, otherwise return `-1`.
    - The solution is guaranteed to be unique.
- **Example**

    - **Example 1:**
    
        **Input**:
        
        ```c
        gas  = [1,2,3,4,5]
        cost = [3,4,5,1,2]
        ```
        
        **Output**: `3`
        
        **Explanation**:
        
        Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
        Travel to station 4. Your tank = 4 - 1 + 5 = 8
        Travel to station 0. Your tank = 8 - 2 + 1 = 7
        Travel to station 1. Your tank = 7 - 3 + 2 = 6
        Travel to station 2. Your tank = 6 - 4 + 3 = 5
        Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
        Therefore, return 3 as the starting index.
    
    - **Example 2:**
    
        **Input**:
        
        ```c
        gas  = [2,3,4]
        cost = [3,4,3]
        ```
        
        **Output**: `-1`
        
        **Explanation**:
        
        You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
        Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
        Travel to station 0. Your tank = 4 - 3 + 2 = 3
        Travel to station 1. Your tank = 3 - 3 + 3 = 3
        You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
        Therefore, you can't travel around the circuit once no matter where you start.

- **Challenge**
    - `O(n)` time and `O(1)` extra space




## Solution

### O(n)

非常经典的一道题。可以转换成求最大连续和做，但是有更简单的方法。基于一个数学定理：

```
如果一个数组的总和非负，那么一定可以找到一个起始位置，从他开始绕数组一圈，累加和一直都是非负的
```

有了这个定理，判断到底是否存在这样的解非常容易，只需要把全部的油耗情况计算出来看看是否大于等于 `0` 即可。

那么如何求开始位置在哪？

注意到这样一个现象：

1. 假如从位置 `i` 开始，`i+1，i+2...`，一路开过来一路油箱都没有空。说明什么？说明从 `i` 到 `i+1，i+2，...` 肯定是正积累。
2. 现在突然发现开往位置 `j` 时油箱空了。这说明什么？说明从位置 `i` 开始没法走完全程(废话)。那么，我们要从位置 `i+1` 开始重新尝试吗？不需要！为什么？因为前面已经知道，位置 `i` 肯定是正积累，那么，如果从位置 `i+1` 开始走更加没法走完全程了，因为没有位置 `i` 的正积累了。

同理，也不用从 `i+2，i+3，...` 开始尝试。所以我们可以放心地从位置 `j+1` 开始尝试。


**References:**

- https://www.cnblogs.com/boring09/p/4248482.html


```python
class Solution:
    """
    @param gas: An array of integers
    @param cost: An array of integers
    @return: An integer
    """
    def canCompleteCircuit(self, gas, cost):
        # write your code here
        if not gas or not cost or len(gas) == 0 or len(cost) == 0 or len(gas) != len(cost):
            return -1

        if sum(gas) < sum(cost):
            return -1

        length = len(gas)
        diff = 0
        summation  = 0
        startIndex = -1

        for idx in range(length):
            diff      += gas[idx] - cost[idx]
            summation += gas[idx] - cost[idx]

            if diff < 0:
                startIndex = idx
                diff  = 0

        return startIndex + 1 if summation >= 0 else -1
```



### [Failed] O(n^2)

`O(n^2)` 的算法思路如下

- 首先排除异常情况 `not gas or not cost or len(gas) == 0 or len(cost) == 0 or len(gas) != len(cost)`
- 明确如果能够走一圈那么 sum(gas) > sum(cost) 是必须的，否则肯定是走不完的
- 然后循环每一个 gas station，作为 `startIndex` ，看是否能够让每一个之后的 station `gasSum - costSum > 0`
- 如果不能那么就 break， iterate 下一个



```python
class Solution:
    """
    @param gas: An array of integers
    @param cost: An array of integers
    @return: An integer
    """
    def canCompleteCircuit(self, gas, cost):
        # write your code here
        if not gas or not cost or len(gas) == 0 or len(cost) == 0 or len(gas) != len(cost):
            return -1

        if sum(gas) < sum(cost):
            return -1

        length = len(gas)

        # Start index of gas station
        for startIndex in range(len(gas)):

            endPoint = startIndex
            gasSum, costSum = 0, 0

            while startIndex < length:

                gasSum  += gas[startIndex]
                costSum += cost[startIndex]

                if gasSum < costSum:
                    break
                startIndex += 1

            if startIndex == length:
                startIndex = 0

                while startIndex < endPoint:

                    gasSum  += gas[startIndex]
                    costSum += cost[startIndex]

                    if gasSum < costSum:
                        break
                    startIndex += 1

                if startIndex == endPoint:
                    return endPoint

        return -1
```
