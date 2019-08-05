1277. Water and Jug Problem
Description
中文
English
You are given two jugs with capacities x and y litres. There is an infinite amount of water supply available. You need to determine whether it is possible to measure exactly z litres using these two jugs.

If z liters of water is measurable, you must have z liters of water contained within one or both buckets by the end.

Operations allowed:

Fill any of the jugs completely with water.
Empty any of the jugs.
Pour water from one jug into another till the other jug is completely full or the first jug itself is empty.
Have you met this question in a real interview?  
Example
Example1

Input: x = 3, y = 5, z = 4
Output: True
Example2

Input: x = 2, y = 6, z = 5
Output: False


```
Credit to Tony123's Note

这道问题其实可以转换为有一个很大的容器，我们有两个杯子，容量分别为x和y，问我们通过用两个杯子往里倒水，和往出舀
水，问能不能使容器中的水刚好为z升。那么我们可以用一个公式来表达：

z = m * x + n * y

其中m，n为舀水和倒水的次数，正数表示往里舀水，负数表示往外倒水，那么题目中的例子可以写成:
4 = (-2) * 3 + 2 * 5，
即3升的水罐往外倒了两次水，5升水罐往里舀了两次水。那么问题就变成了对于任意给定的x,y,z，存不存在m和n使得上面
的等式成立。根据裴蜀定理，ax + by = d的解为 d = gcd(x, y)，那么我们只要只要z % d == 0，上面的等式就有
解，所以问题就迎刃而解了，我们只要看z是不是x和y的最大公约数的倍数就行了，别忘了还有个限制条件x + y >= z，因
为x和y不可能称出比它们之和还多的水
```

```python
class Solution:
    """
    @param x: the given number x
    @param y: the given number y
    @param z: the given number z
    @return: whether it is possible to measure exactly z litres using these two jugs
    """

    def canMeasureWater(self, x, y, z):
        # Write your code here
        if z < 0 or x + y < z:
            return False

        def gcd(x, y):
            # Using Euclidean Algorithm
            while y:
                x, y = y, x % y
            return x

        gcd = gcd(x, y)
        if z % gcd == 0:
            return True
        return False
```