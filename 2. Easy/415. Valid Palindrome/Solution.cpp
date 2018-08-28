class Solution {
public:
    /**
     * @param s: A string
     * @return: Whether the string is a valid palindrome
     */
    bool isPalindrome(string &s) {
        // write your code here
        return validPalindrome(remove_rubbish(s));
    }

    string remove_rubbish(string s) {
        auto is_rubbish = [](char c) { 
            return ispunct(c) || isspace(c); 
        };
        
        // remove spaces and puctuations
        s.erase(std::remove_if(s.begin(), 
                               s.end(), 
                               is_rubbish), 
                s.end());
        return s;
    }


    bool validPalindrome(string s) {
        // base case -> "" or "x" is palindrome
        if (s.length() < 2) {
            return true;
        } else {
            char first = s[0];
            char last  = s[s.length() - 1];
            
            // first and last is same or one is lowercase, the other is not
            if (first == last || abs(first - last) == 32) {
                string substr = s.substr(1, s.length() - 2);
                return validPalindrome(substr);
            } else {
                return false;
            }
        }
    }
};