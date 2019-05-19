class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: node: insert this node into the binary search tree
    @return: The root of the new binary search tree.
    """
    def insertNode(self, root, node):
        # write your code here
        return self.__helper(root, node)
    
     # helper函数定义成私有属性   
    def __helper(self, root, node):     
        if root is None:
            return node
        if node.val < root.val:
            root.left = self.__helper(root.left, node)
        else:
            root.right = self.__helper(root.right, node)
        return root