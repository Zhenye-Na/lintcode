class Solution {
public:
    /**
     * @param gas: An array of integers
     * @param cost: An array of integers
     * @return: An integer
     */
    int canCompleteCircuit(vector<int> &gas, vector<int> &cost) {
        // write your code here
        int start  = 0;  // 起始位置
        int remain = 0;  // 当前剩余燃料
        int debt   = 0;  // 前面没能走完的路上欠的债

        for (int i = 0; i < gas.size(); i++) {
            remain += gas[i] - cost[i];
            if (remain < 0) {
                debt  += remain;
                start  = i + 1;
                remain = 0;
            }
        }

        return remain + debt >= 0 ? start : -1;
    }
};
