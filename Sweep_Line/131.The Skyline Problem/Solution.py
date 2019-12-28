from heapq import heappush, heappop


class Solution:
    """
    @param buildings: A list of lists of integers
    @return: Find the outline of those buildings
    """

    def buildingOutline(self, buildings):
        # write your code here
        building_outlines = []
        for idx, building in enumerate(buildings):
            start, end, height = building
            # start position, height, is_start, building index
            building_outlines.append([start, height, True, idx])
            building_outlines.append([end, height, False, idx])
        building_outlines.sort()

        answer = []
        building_heap = []
        prev_position = None
        history = set([])

        for position, height, is_start, building_index in building_outlines:
            top_height = -building_heap[0][0] if building_heap else 0
            self.merge(answer, prev_position, position, top_height)

            if is_start:
                heappush(building_heap, (- height, building_index))
            else:
                # record which building should be removed
                history.add(building_index)

            # removed
            while building_heap and building_heap[0][1] in history:
                heappop(building_heap)

            prev_position = position

        return answer

    def merge(self, answer, start, end, height):
        if start is None or start == end or height == 0:
            return

        if len(answer) == 0:
            answer.append([start, end, height])
            return

        else:
            prev_start, prev_end, prev_height = answer[-1]
            if prev_height == height and prev_end == start:
                answer[-1][1] = end
            else:
                answer.append([start, end, height])
