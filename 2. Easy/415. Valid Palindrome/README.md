# 415. Valid Palindrome

- **Description**
    - Given a string, determine if it is a palindrome, **considering only alphanumeric characters and ignoring cases**.
    - **Have you consider that the string might be empty? This is a good question to ask during an interview.**
    - For the purpose of this problem, we define **empty string as valid palindrome**.
- **Example**
    - `"A man, a plan, a canal: Panama"` is a palindrome.
    - `"race a car"` is **not** a palindrome.
- **Challenge**
    - `O(n)` time without extra memory.


## Solution

### Recursion

```cpp
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
        s.erase(remove_if(s.begin(), 
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
```


### Two Pointers

```java
public class Solution {
    /**
     * @param s: A string
     * @return: Whether the string is a valid palindrome
     */
    public boolean isPalindrome(String s) {
        // write your code here
        s = rmSigns(s);
        if (s == null || s.length() == 0 || s.length() == 1) {
            return true;
        }

        int left = 0, right = s.length() - 1;
        while (left < right) {
            if (s.charAt(left) != s.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }

    private String rmSigns(String s) {
        String wow = s.replaceAll("[^a-zA-Z0-9]", "").trim().toUpperCase();
        return wow;
    }
}
```
