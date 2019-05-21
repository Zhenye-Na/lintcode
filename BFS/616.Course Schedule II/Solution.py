from collections import deque, defaultdict

class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: the course order
    """
    def findOrder(self, numCourses, prerequisites):
        # write your code here
        courseIndegree = self._getCourseIndegree(prerequisites)
        neighbors = self._getNeighbors(prerequisites)

        start_courses = [course for course in range(numCourses) if courseIndegree[course] == 0]
        queue = deque(start_courses)
        order = []

        while queue:
            course = queue.popleft()
            order.append(course)

            for neighbor in neighbors[course]:
                courseIndegree[neighbor] -= 1
                if courseIndegree[neighbor] == 0:
                    queue.append(neighbor)

        return order if len(order) == numCourses else []


    def _getCourseIndegree(self, prerequisites):
        courseIndegree = defaultdict(int)

        for i, j in prerequisites:
            courseIndegree[i] += 1

        return courseIndegree

    def _getNeighbors(self, prerequisites):
        neighbors = defaultdict(list)

        for i, j in prerequisites:
            neighbors[j].append(i)

        return neighbors
