class Solution:
    """
    @param words: the n strings
    @param target: the target string
    @return: The ans
    """
    def the_longest_common_prefix(self, words, target):
        # write your code here
        ans = 0
        for word in words:
            same = 0

            for j in range(0, len(target)):
                if j > len(word) - 1 or target[j] != word[j]:
                    break
                same += 1

            ans = max(ans, same)

        return ans