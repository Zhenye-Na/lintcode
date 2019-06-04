/**
 * Definition of Interval:
 * classs Interval {
 *     int start, end;
 *     Interval(int start, int end) {
 *         this->start = start;
 *         this->end = end;
 *     }
 * }
 */

class Solution {
public:
    /**
     * @param intervals: interval list.
     * @return: A new interval list.
     */
    vector<Interval> merge(vector<Interval> &intervals) {
        // write your code here
        if (intervals.empty())
            return {};
        
        sort(intervals.begin(), intervals.end(), 
             [](const Interval & l, const Interval & r) { 
                 return l.start < r.start;
             });
        
        vector<Interval> res;
        for (const auto & interval: intervals) {
            if (res.empty() || interval.start > res.back().end)
                res.push_back(interval);
            else
                res.back().end = max(res.back().end, interval.end);
        }
        return res;
    }
};