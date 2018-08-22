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
