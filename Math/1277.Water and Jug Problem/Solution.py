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
