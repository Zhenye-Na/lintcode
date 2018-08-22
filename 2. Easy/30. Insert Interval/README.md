# 30. Insert Interval

- **Description**
    - Given a **non-overlapping** interval list which is **sorted by start point**.
    - Insert a new interval into it, make sure the list is **still in order** and **non-overlapping** (merge intervals if necessary).
- **Example**
    - Insert `(2, 5)` into `[(1,2), (5,9)]`, we get `[(1,9)]`.
    - Insert `(3, 4)` into `[(1,2), (5,9)]`, we get `[(1,2), (3,4), (5,9)]`.
**Related problems**
    - 156. Merge Intervals
    - 919. Meeting Rooms II


## Solution

Same as LeetCode 57. Insert Interval [Hard]

这道题在 LeetCode 是 Hard 不知道为什么在 LintCode 是 Easy ... 解题思路跟 LeetCode 56. Merge Intervals 十分类似，建议先做 LeetCode 56. Merge Intervals (或者 LintCode 156. Merge Intervals)。

整体解题思路如下：

intervals 已经按照 start 排好序， 可以将所有的 intervals 分成三种

- 第一种是 `interval.end < newInterval.start`
- 第二种是 `interval.start > newInterval.end`
- 第三种就是两者纠缠在一起 “剪不断理还乱”的关系

然后分开处理即可

### Code

```java
/**
 * Definition of Interval:
 * public classs Interval {
 *     int start, end;
 *     Interval(int start, int end) {
 *         this.start = start;
 *         this.end = end;
 *     }
 * }
 */

public class Solution {
    /**
     * @param intervals: Sorted interval list.
     * @param newInterval: new interval.
     * @return: A new interval list.
     */
    public List<Interval> insert(List<Interval> intervals, Interval newInterval) {
        // write your code here
        if (newInterval == null) return intervals;
        List<Interval> result = new ArrayList<>();
        int index = 0, size = intervals.size();

        while (index < size && intervals.get(index).end < newInterval.start) {
            result.add(intervals.get(index++));
        }

        while (index < size && intervals.get(index).start <= newInterval.end) {
            newInterval.start = Math.min(intervals.get(index).start, newInterval.start);
            newInterval.end = Math.max(intervals.get(index).end, newInterval.end);
            index++;
        }
        result.add(newInterval);

        while (index < size) {
            result.add(intervals.get(index++));
        }

        return result;
    }

}
```

**九章算法题解如下：**

```java
/**
* 本参考程序来自九章算法，由 @九章算法 提供。版权所有，转发请注明出处。
* - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
* - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
* - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
* - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code
*/

public class Solution {
    public List<Interval> insert(List<Interval> intervals, Interval newInterval) {
        if (newInterval == null || intervals == null) {
            return intervals;
        }

        List<Interval> results = new ArrayList<Interval>();
        int insertPos = 0;

        for (Interval interval : intervals) {
            if (interval.end < newInterval.start) {
                results.add(interval);
                insertPos++;
            } else if (interval.start > newInterval.end) {
                results.add(interval);
            } else {
                newInterval.start = Math.min(interval.start, newInterval.start);
                newInterval.end = Math.max(interval.end, newInterval.end);
            }
        }

        results.add(insertPos, newInterval);

        return results;
    }
}

// version: 高频题班
public class Solution {
    /*
     * @param intervals: Sorted interval list.
     * @param newInterval: new interval.
     * @return: A new interval list.
     */
    public List<Interval> insert(List<Interval> intervals, Interval newInterval) {
        // write your code here
        List<Interval> ans = new ArrayList<>();

        int idx = 0;
        while (idx < intervals.size() && intervals.get(idx).start < newInterval.start) {
            idx++;
        }
        intervals.add(idx, newInterval);

        Interval last = null;
        for (Interval item : intervals) {
            if (last == null || last.end < item.start) {
                ans.add(item);
                last = item;
            } else {
                last.end = Math.max(last.end, item.end); // Modify the element already in list
            }
        }
        return ans;
    }
}
```
