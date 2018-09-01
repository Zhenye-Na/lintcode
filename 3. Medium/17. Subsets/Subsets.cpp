/*
 * cannot pass the test cases due to non-descending order
 */


class Solution {
public:
    /**
     * @param nums: A set of numbers
     * @return: A list of lists
     */
    vector<vector<int>> result;
    vector<int>::iterator it;
    vector<vector<int>> subsets(vector<int> &nums) {
        // write your code here
        vector<int> chosen;
        helper(nums, chosen);
        for (vector<int> subset : result) {
            sort(subset.begin(), subset.end());
        }
        return result;
    }


    void helper(vector<int> &nums, vector<int> &chosen) {
        if (nums.empty()) {
            // base case
            result.push_back(chosen);
        } else {
            // recursive case
            // for each possible choice
            int n = nums[0];
            nums.erase(nums.begin());

            // choose without n
            helper(nums, chosen);

            // choose with n
            chosen.push_back(n);
            helper(nums, chosen);

            // un-choose
            nums.insert(nums.begin(), n);
            chosen.pop_back();
        }
    }

};
