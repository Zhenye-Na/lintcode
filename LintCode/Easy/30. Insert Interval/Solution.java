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
        List<Interval> result = new ArrayList<>();

        boolean startFlag = false, endFlag = false;
        int length = intervals.size(), foundIndex = 0;

        for (int i = 0; i < length; i++) {
            // first interval that overlaps, skip this interval
            if (isStartIn(intervals.get(i), newInterval)) {
                startFlag = true;
                foundIndex = i;
                continue;
            }

            if (isEndIn(intervals.get(i), newInterval) && startFlag == true) {
                endFlag = true;
                result.add(new Interval(intervals.get(foundIndex).start, intervals.get(i).end));
            } else if (isEndIn(intervals.get(i), newInterval)) {
                endFlag = true;
                result.add(new Interval(newInterval.start, intervals.get(i).end));
            } else {
                // no overlapping intervals
                result.add(intervals.get(i));
            }
        }

        if (!endFlag) {
            intervals.get(foundIndex).end = newInterval.end;

        }

        return result;

    }


    private boolean isStartIn(Interval interval, Interval newInterval) {
        return (newInterval.start >= interval.start && newInterval.start <= interval.end);
    }

    private boolean isEndIn(Interval interval, Interval newInterval) {
        return (newInterval.end >= interval.start && newInterval.end <= interval.end);
    }

}
