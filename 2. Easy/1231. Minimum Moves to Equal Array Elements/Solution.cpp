class Solution {
public:
    /**
     * @param nums: an array
     * @return: the minimum number of moves required to make all array elements equal
     */
    int minMoves(vector<int> &nums) {
        // Write your code here
        int mn = INT_MAX, res = 0;
        for (int num : nums) mn = min(mn, num);
        for (int num : nums) res += num - mn;
        return res;
    }
};




class Solution {
public:
    int minMoves(vector<int>& nums) {
        int mn = INT_MAX, sum = 0, res = 0;
        for (int num : nums) {
            mn = min(mn, num);
            sum += num;
        }
        return sum - mn * nums.size();
    }
};
