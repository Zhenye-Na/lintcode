class Solution:
    """
    @param s: a string
    @return: an integer
    """
    def lengthOfLongestSubstring(self, s):
        # write your code here
        if not s or len(s) == 0:
            return 0

        char = [ch for ch in s]
        visited = [0 for _ in range(256)]
        visited[ord(s[0])] = 1
        max_string, current = [], [char[0]]
        right = 1

        for left in range(len(char)):
            while right < len(char) and self._isUnique(visited, char[right]):
                current.append(char[right])
                visited[ord(char[right])] = 1
                right += 1

            if len(current) > len(max_string):
                max_string = current[:]

            visited[ord(current[0])] = 0
            current = current[1:]

        return len(max_string)


    def _isUnique(self, visited, target_str):
        return visited[ord(target_str)] == 0
