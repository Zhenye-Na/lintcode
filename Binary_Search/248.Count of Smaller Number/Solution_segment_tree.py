class Solution:
    """
    @param A: A list of integer
    @return: The number of element in the array that 
             are smaller that the given integer
    """
    class SegmentTreeNode:
        def __init__(self, start, end, count):
            self.start, self.end, self.count = start, end, count
            self.left, self.right = None, None

    def countOfSmallerNumber(self, A, queries):
        # write your code here
        
        # build segmeng tree
        root = self.build(0, 10000)
        result = []
        
        # modify count value for each
        for num in A:
            self.modify(root, num, 1)
        
        for i in queries:
            count = 0
            if i > 0:
                count = self.query(root, 0, i - 1)
            result.append(count)
        
        return result
    
    def build(self, start, end):
        if start >= end:
            return SegmentTreeNode(start, end, 0)
        root = SegmentTreeNode(start, end, 0)
        mid = start + (end - start) / 2
        root.left = self.build(start, mid)
        root.right = self.build(mid + 1, end)
        return root
    
    def modify(self, root, index, value):
        if root.start == index and root.end == index:
            root.count += value
            return
        # query
        mid = root.start + (root.end - root.start) / 2
        if index <= mid:
            self.modify(root.left, index, value)
        
        if mid < index:
            self.modify(root.right, index, value)
        root.count = root.left.count + root.right.count
    
    def query(self, root, start, end):
        if start == root.start and end == root.end:
            return root.count
        
        mid = root.start + (root.end - root.start) / 2
        if end <= mid:
            return self.query(root.left, start, end)
        
        if start > mid:
            return self.query(root.right, start, end)
            
        return self.query(root.left, start, mid) + \
            self.query(root.right, mid + 1, end)