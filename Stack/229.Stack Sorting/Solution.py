"""
In python, you can use list as stack
stack = [1,2,3,4]
Get top element: stack[-1]  -> 4
Pop element: stack.pop()   -> 4
Push element: stack.append(5)
check the size of stack: len(stack)
"""


class Solution:
    """
    @param: stk: an integer stack
    @return: void
    """
    def stackSorting(self, stk):
        # write your code here
        if not stk or len(stk) == 0:
            return stk

        stack = []
        stack.append(stk.pop())

        while stk:
            temp = stk.pop()
            while stack and temp > stack[-1]:
                stk.append(stack.pop())
            stack.append(temp)

        while stack:
            stk.append(stack.pop())