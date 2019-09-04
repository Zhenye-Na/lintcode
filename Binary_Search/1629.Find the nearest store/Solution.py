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
