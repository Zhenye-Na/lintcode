# 105. Copy List with Random Pointer


- **Description**
    - A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
    - Return a deep copy of the list.
- **Challenge**
    - Could you solve it with `O(1)` space?



## Solution

### HashMap<RandomListNode, RandomListNode>

**deep copy**, 用 **137. Clone Graph** 的 HashMap 可解，但是无法做到 `O(1)` Space Complexity

#### Python

```python
"""
Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
"""


class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        # write your code here
        if not head:
            return head

        # Get list of nodes
        nodes = self.getNodes(head)

        # mapping from original nodes to new nodes
        mapping = {}

        # create mapping relation
        for node in nodes:
            mapping[node]        = RandomListNode(node.label)

        # update cloning nodes
        for node in nodes:
            mapping[node].next   = mapping[node.next] if node.next else None
            mapping[node].random = mapping[node.random] if node.random else None

        return mapping[head]


    def getNodes(self, head):
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        return nodes
```


#### Java

```java
/**
 * Definition for singly-linked list with a random pointer.
 * class RandomListNode {
 *     int label;
 *     RandomListNode next, random;
 *     RandomListNode(int x) { this.label = x; }
 * };
 */
public class Solution {
    /**
     * @param head: The head of linked list with a random pointer.
     * @return: A new head of a deep copy of the list.
     */
    public RandomListNode copyRandomList(RandomListNode head) {
        // write your code here
        if (head == null) return head;

        List<RandomListNode> nodes = getNodes(head);

        Map<RandomListNode, RandomListNode> relation = new HashMap<>();
        for (RandomListNode node : nodes) {
            relation.put(node, new RandomListNode(node.label));
        }

        for (RandomListNode node : nodes) {
            relation.get(node).next   = relation.get(node.next);
            relation.get(node).random = relation.get(node.random);
        }

        return relation.get(head);
    }


    private List<RandomListNode> getNodes(RandomListNode head) {
        // get all the nodes from .next
        List<RandomListNode> nodesList = new ArrayList<>();
        while (head != null) {
            nodesList.add(head);
            head = head.next;
        }
        return nodesList;
    }

}




// 这个解法比我自己写的好处：
// 1. 只有一个 while 循环
// 2. 用到了 dummy node， 并不需要把所有的 nodes 循环出来，可以一边 `.next` 一边操作

// @九章算法
// HashMap version
public class Solution {
    public RandomListNode copyRandomList(RandomListNode head) {
        if (head == null) {
            return null;
        }

        HashMap<RandomListNode, RandomListNode> map = new HashMap<RandomListNode, RandomListNode>();
        RandomListNode dummy = new RandomListNode(0);
        RandomListNode pre = dummy, newNode;
        while (head != null) {
            if (map.containsKey(head)) {
                newNode = map.get(head);
            } else {
                newNode = new RandomListNode(head.label);
                map.put(head, newNode);
            }
            pre.next = newNode;

            if (head.random != null) {
                if (map.containsKey(head.random)) {
                    newNode.random = map.get(head.random);
                } else {
                    newNode.random = new RandomListNode(head.random.label);
                    map.put(head.random, newNode.random);
                }
            }

            pre = newNode;
            head = head.next;
        }

        return dummy.next;
    }
}
```

### O(1) Space

- 下面提供 @九章 的 `O(1)` 解法， 十分巧妙，拍拍脑子自己一辈子也想不出来，记下来就好

```java
/* 第一遍扫的时候巧妙运用next指针， 开始数组是1->2->3->4. 然后扫描过程中, 先建立copy节点 1->1`->2->2`->3->3`->4->4`,
然后第二遍copy的时候去建立边的copy， 拆分节点, 一边扫描一边拆成两个链表，这里用到两个dummy node。第一个链表变回  1->2->3,
然后第二变成 1`->2`->3` */

// No HashMap version
public class Solution {
    private void copyNext(RandomListNode head) {
        while (head != null) {
            RandomListNode newNode = new RandomListNode(head.label);
            newNode.random = head.random;
            newNode.next = head.next;
            head.next = newNode;
            head = head.next.next;
        }
    }

    private void copyRandom(RandomListNode head) {
        while (head != null) {
            if (head.next.random != null) {
                head.next.random = head.random.next;
            }
            head = head.next.next;
        }
    }

    private RandomListNode splitList(RandomListNode head) {
        RandomListNode newHead = head.next;
        while (head != null) {
            RandomListNode temp = head.next;
            head.next = temp.next;
            head = head.next;
            if (temp.next != null) {
                temp.next = temp.next.next;
            }
        }
        return newHead;
    }

    public RandomListNode copyRandomList(RandomListNode head) {
        if (head == null) {
            return null;
        }
        copyNext(head);
        copyRandom(head);
        return splitList(head);
    }
}
```
