# 104. Merge K Sorted Lists

**Description**

Merge `k` sorted linked lists and return it as one sorted list.

> **Analyze and describe its complexity.**
 
**Example**

```
Example 1:
	Input:   [2->4->null,null,-1->null]
	Output:  -1->2->4->null

Example 2:
	Input: [2->6->null,5->null,7->null]
	Output:  2->5->6->7->null
```


**三种不同的解法**

- `mergeHelper_v1_minHeap` 小顶堆（优先队列）
- `mergeHelper_v2_Divide_Conquer` 分治思想，递归
- `mergeHelper_v3_Non_Recursive` 两两合并，非递归

时间复杂度均为 `O(nlogk)`


三道相似题目

- 104.Merge K Sorted Lists
- 486.Merge K Sorted Arrays
- 577.Merge K Sorted Interval Lists

实质上是一个问题，均可以采用 `v1`, `v2`, `v3` 三种不一样的解法


```java
/**
* 本参考程序来自九章算法，由 @Roger 提供。版权所有，转发请注明出处。
* - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
* - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
* - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
* - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code
*/ 

public class Solution {
    /**
     * @param lists: a list of ListNode
     * @return: The head of one sorted list.
     */
    public ListNode mergeKLists(List<ListNode> lists) {  
        // write your code here
        if (lists == null || lists.size() == 0) {
            return null;
        }

        return mergeHelper_v1_minHeap(lists);
        return mergeHelper_v2_Divide_Conquer(lists, 0, lists.size() - 1);
        return mergeHelper_v3_Non_Recursive(lists);
    }

    // version 1: min heap
    private ListNode mergeHelper_v1_minHeap(List<ListNode> lists) {
        // initialize priorityQueue
        Queue<ListNode> pq = new PriorityQueue<ListNode>(lists.size(), new Comparator<ListNode>() {
            @Override
            public int compare(ListNode o1, ListNode o2) {
                return o1.val - o2.val;
            }
        });

        for (ListNode head : lists) {
            if (head != null) {
                pq.offer(head);
            }
        }

        ListNode dummy = new ListNode(0), tail = dummy;

        while (!pq.isEmpty()) {
            ListNode top = pq.poll();
            tail.next = top;
            tail = top;
            if (top.next != null) {
                pq.offer(top.next);
            }
        }

        return dummy.next;
    }


    // version 2 Divide and Conquer
    private ListNode mergeHelper_v2_Divide_Conquer(List<ListNode> lists, int start, int end) {
        if (start == end) {
            return lists.get(start);
        }

        int mid = start + (end - start) / 2;
        ListNode left = mergeHelper_v2_Divide_Conquer(lists, start, mid);
        ListNode right = mergeHelper_v2_Divide_Conquer(lists, mid + 1, end);
        return mergeTwoSortedList(left, right);
    }


    // version 3: Non Recursion
    private ListNode mergeHelper_v3_Non_Recursive(List<ListNode> lists) {
        while (lists.size() > 1) {
            // merge
            List<ListNode> tmp = new ArrayList<ListNode>();
            for (int i = 0; i < lists.size() && i + 1 < lists.size(); i += 2) {
                ListNode head = mergeTwoSortedList(lists.get(i), lists.get(i + 1));
                tmp.add(head);
            }

            if (lists.size() % 2 == 1) {
                tmp.add(lists.get(lists.size() - 1));
            }

            lists = tmp;
        }
        return lists.get(0);
    }


    // helper function
    private ListNode mergeTwoSortedList(ListNode L1, ListNode L2) {
        ListNode dummy = new ListNode(0), tail = dummy;
        
        while (L1 != null && L2 != null) {
            if (L1.val <= L2.val) {
                tail.next = L1;
                L1 = L1.next;
            } else {
                tail.next = L2;
                L2 = L2.next;
            }
            tail = tail.next;
        }

        tail.next = (L1 != null) ? L1 : L2;

        return dummy.next;
    }
}
```