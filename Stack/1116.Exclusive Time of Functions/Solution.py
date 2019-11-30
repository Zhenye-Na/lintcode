class Solution:
    """
    @param n: a integer
    @param logs: a list of integers
    @return: return a list of integers
    """
    def exclusiveTime(self, n, logs):
        # write your code here
        stack = []
        result = [0 for _ in range(n)]
        last_timestamp = 0

        for log in logs:
            log = log.split(":")
            thread_id, status, timestamp = int(log[0]), log[1], int(log[2])

            if status == "start":
                if stack:
                    result[stack[-1]] += timestamp - last_timestamp
                stack.append(thread_id)
            else:
                timestamp += 1
                result[stack.pop()] += timestamp - last_timestamp

            last_timestamp = timestamp

        return result
