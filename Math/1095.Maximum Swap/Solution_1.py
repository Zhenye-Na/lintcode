class Solution:
    """
    @param num: a non-negative intege
    @return: the maximum valued number
    """
    def maximumSwap(self, num):
        # Write your code here
        digits = list(reversed([i for i in str(num)]))
        
        swappingFrom, swappingTo = 0, 0
        runningMaxIndex, runningMax = 0, digits[0]
        for i in range(1, len(digits)):
            print(swappingFrom, swappingTo)
            if digits[i] < runningMax:
                swappingFrom = runningMaxIndex
                swappingTo = i 
            elif digits[i] > runningMax:
                runningMaxIndex, runningMax = i, digits[i]

        if swappingTo != 0:
            digits[swappingTo], digits[swappingFrom] = digits[swappingFrom], digits[swappingTo]
        
        return int("".join(reversed(digits)))
