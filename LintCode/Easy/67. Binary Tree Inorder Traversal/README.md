# 67. Binary Tree Inorder Traversal


Description
Given a binary tree, return the inorder traversal of its nodes' values.

Example
Given binary tree {1,#,2,3},

```
   1
    \
     2
    /
   3
```

return [1,3,2].

Challenge
Can you do it without recursion?


## Solution

### Stack: non-recursion **[Recommended]**

```python
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        # write your code here
        result = []
        stack  = []

        if root is None:
            return result

        # 1. 添加所有最左边节点到栈
        while root:
            stack.append(root)
            root = root.left

        while stack:
            # 2. pop stack 然后添加到结果
            node = stack.pop()
            result.append(node.val)

            # 3. 查找当前node的右边节点是否为空，如果不为空，重复 step 1
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left

        return result
```

### Divide & Conquer

```python
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        # write your code here
        result = []

        if root is None:
            return result

        left = self.inorderTraversal(root.left)
        right = self.inorderTraversal(root.right)

        result.extend(left)
        result.append(root.val)
        result.extend(right)

        return result
```

### Traverse helper function

```python
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        # write your code here
        result = []
        self.inorderHelper(root, result)
        return result


    def inorderHelper(self, root, result):
        if root is None:
            return result

        if root.left is not None:
            self.inorderHelper(root.left, result)

        result.append(root.val)

        if root.right is not None:
            self.inorderHelper(root.right, result)
```

## Analysis

**From LintCode @Leon**

我感觉这是一道非常有趣的题目，这里提供了三种不同的python解法，思路是完全不一样的。
总的来讲，中序遍历和前序遍历相比，难点就在于，左-中-右 顺序中‘中’的处理。不止要保存‘中’节点的信息，而且还要保存是否已经访问‘中’节点的左节点。
其实对于一个非空节点，可能出现的情况有以下几种：

有左节点：这种情况继续分两种情况：

左节点没有被访问，那么应该继续向左
左节点已经被访问，这种情况相当于2‘ 没有左节点
没有左节点：这个时候首先要print 这个节点，然后看右节点

有右节点：那么向右节点走，这个时候注意，这个有右节点的节点，已经被printed了
没有右节点：那么返回这个节点的先驱节点（进入这个节点的上一个节点）
所以难点就在于，如何寻找先驱节点。在中序遍历里，寻找左子树的先驱节点很容易，它的父辈就是了；但是右子树的先驱节点就麻烦了，因为进入右子树之前，父节点已经printed过了，真正的先驱节点应该是第一个没有被print的父节点。
接下来可以从下面三种题解中看看如何寻找/标记先驱节点

第一个解法的本质，其实是利用None的次数来标记父节点。第一次向stack填入None的时候，都代表进入情况2（没有左节点了），这个时候pop 掉stack 并print，进入这个被print 节点的右子树，然后第二次出现None的时候，是情况2.2（右子树也空了），这个时候pop出来的就是真正的先驱节点。那个已经被printed的先驱节点，在第一次出现None的时候已经被pop掉了

第二个解法，九章给出来的标准做法。其实我个人感觉有点绕。这个算法包括了两种操作：第一个操作是把一整条向左的path都存入到stack里面，第二个操作是寻找先驱节点。这个算法用到的一个重要的性质是：对于一个右子树，先驱节点到达它的方式一定是，先向左一下，（到达进入右子树，但却已经被访问过的那个节点），再向右进入右子树，所以利用这个性质，所有stack[-1] == node的节点其实都是已经被printed的节点了，不是真正的先驱节点。

第三个解法（morris），是我最喜欢的，逻辑上很直接。这个算法的根本是：把一个子树的最右边的节点（最后一个被访问的节点）的右节点，连到它的先驱节点上。这样就避免了找先驱节点的麻烦，相当于反向的思维解决了问题。算法是对于每一个节点，第一步是找它是谁的先驱节点，方法和2类似，就是找它左子树的最右边，首先如果没有左子树，直接print 然后向右走就行。然后要分两种情况

发现它左子树最右边是None，就把这个None改成它自己，向左走；
如果左子树的最右边是它自己，说明我要找的就是它，print 它，然后向右走
最后总结一下这道题的思想，是用iteraton 方式来做DFS 遍历，所以同样类别的题，如果面试问到，都可以去思考如何得到先驱节点的方法。
花了一些时间整理了一下自己对于这道题的理解，如果有同学看到的话可以一起讨论。

```python
# 本参考程序来自九章算法，由 @Leon 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code


class Solution:
    """
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal1(self, root):
        # write your code here
        ans = []
        stack = []
        curr = root
        while curr or stack:
            if not curr:
                curr = stack.pop(-1)
                ans.append(curr.val)
                curr = curr.right
            else:
                stack.append(curr)
                curr = curr.left
        return ans

    def inorderTraversal2(self,root):
        ans = []
        stack = []
        while root:
            stack.append(root)
            root = root.left
        # Now root is the most left node
        while stack:
            node = stack[-1]
            # stack[-1] is always the most left node
            ans.append(node.val)
            if node.right: # has right, repeat pushing all left nodes to stack
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
            if not node.right:
                # if no right node, pop this node out and find the precessor
                node = stack.pop(-1)
                while stack and stack[-1].right == node:
                    node = stack.pop(-1)
        return ans    

    def inorderTraversal3(self,root):
        ans = []
        stack = []
        curr = root
        while stack or curr:
            if curr.left:
                pre = curr.left
                while pre.right and pre.right!=curr:
                    pre = pre.right
                if pre.right!=curr:
                    pre.right = curr
                    curr = curr.left
                else:
                    pre.right = None
                    ans.append(curr.val)
                    curr = curr.right
            else:
                ans.append(curr.val)
                curr = curr.right
        return ans
```
