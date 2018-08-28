class Solution {
public:
    /**
     * @param s: The first string
     * @param t: The second string
     * @return: true or false
     */
    bool anagram(string &s, string &t) {
        // write your code here
        string sorted_s = s;
        string sorted_t = t;
        sort(sorted_s.begin(), sorted_s.end());
        sort(sorted_t.begin(), sorted_t.end());
        return sorted_t == sorted_s;
    }
};