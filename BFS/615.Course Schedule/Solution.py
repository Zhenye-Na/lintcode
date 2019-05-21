from collections import deque, defaultdict

class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """
    def canFinish(self, numCourses, prerequisites):
        # write your code here
        courseIndegree = self._getCourseIndegree(prerequisites)
        neighbors = self._getNeighbors(prerequisites)

        start_courses = [course for course in range(numCourses) if courseIndegree[course] == 0]
        queue = deque(start_courses)
        count = 0

        while queue:
            course = queue.popleft()
            count += 1

            for neighbor in neighbors[course]:

                courseIndegree[neighbor] -= 1
                if courseIndegree[neighbor] == 0:
                    queue.append(neighbor)
        return count == numCourses

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
