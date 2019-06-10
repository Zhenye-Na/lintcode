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
     * @param intervals: the given k sorted interval lists
     * @return:  the new sorted interval list
     */
    public List<Interval> mergeKSortedIntervalLists(List<List<Interval>> intervals) {
        // write your code here
        if (intervals == null || intervals.isEmpty()) {
            return new ArrayList<Interval>();
        }

        return DivideConquer(intervals, 0, intervals.size() - 1);
    }

    private List<Interval> DivideConquer(List<List<Interval>> intervals, int low, int high) {
        if (low >= high) {
            return intervals.get(low);
        }

        int mid = low + (high - low) / 2;
        List<Interval> left = DivideConquer(intervals, low, mid);
        List<Interval> right = DivideConquer(intervals, mid + 1, high);

        return mergeTwoInterval(left, right);
    }

    private List<Interval> mergeTwoInterval(List<Interval> list1, List<Interval> list2) {
        // write your code here
        if (list1 == null || list1.isEmpty()) {
            return list2;
        }
        
        if (list2 == null || list2.isEmpty()) {
            return list1;
        }
        
        List<Interval> merge = new ArrayList<>();
        Interval last = null;
        
        int i = 0, j = 0;
        while (i < list1.size() && j < list2.size()) {
            Interval cur;               
            if (list1.get(i).start <= list2.get(j).start) {
                cur = list1.get(i);
                i++;
            } else {
                cur = list2.get(j);
                j++;
            }
            
            if (last == null || last.end < cur.start) {
                merge.add(cur);
                last = cur;
            } else {
                last.end = Math.max(last.end, cur.end);
            }
        }
        
        while (i < list1.size()) {
            Interval cur = list1.get(i);               
            i++;
            
            if (last == null || last.end < cur.start) {
                merge.add(cur);
                last = cur;
            } else {
                last.end = Math.max(last.end, cur.end);
            }
        }
        
        while (j < list2.size()) {
            Interval cur = list2.get(j);               
            j++;
            
            if (last == null || last.end < cur.start) {
                merge.add(cur);
                last = cur;
            } else {
                last.end = Math.max(last.end, cur.end);
            }
        }
        
        return merge;
    }

}