class Solution:
    """
    @param houses: positions of houses
    @param heaters: positions of heaters
    @return: the minimum radius standard of heaters
    """
    def findRadius(self, houses, heaters):
        # Write your code here
        houses.sort()
        heaters.sort()

        i, radius = 0, 0

        for house in houses:
            while i < len(heaters) - 1 and heaters[i] + heaters[i + 1] <= house * 2:
                i += 1

            radius = max(radius, abs(heaters[i] - house))

        return radius
