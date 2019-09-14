// Author: Huahua
// Running time: 82 ms
class Solution {
public:
  vector<int> maxSlidingWindow(vector<int>& nums, int k) {
    vector<int> ans;
    if (nums.empty()) return ans;
    multiset<int> window(nums.begin(), nums.begin() + k - 1);
    for (int i = k - 1; i < nums.size(); ++i) {
      window.insert(nums[i]);
      ans.push_back(*window.rbegin());
      if (i - k + 1 >= 0)
        window.erase(window.equal_range(nums[i - k + 1]).first);      
    }
    return ans;
  }
};