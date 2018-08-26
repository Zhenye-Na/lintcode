class Solution {
public:
    /**
     * @param A: A positive integer which has N digits, A is a string
     * @param k: Remove k digits
     * @return: A string
     */
    string DeleteDigits(string &A, int k) {
        // write your code here
        string res;
        int keep = A.size() - k;
        for (int i=0; i<A.size(); i++) {
            while (res.size()>0 && res.back()>A[i] && k>0) {
                res.pop_back();
                k--;
            }
            res.push_back(A[i]);
        }
        res.erase(keep, string::npos);

        // trim leading zeros
        int s = 0;
        while (s<(int)res.size()-1 && res[s]=='0')  s++;
        res.erase(0, s);

        return res=="" ? "0" : res;
    }
};
