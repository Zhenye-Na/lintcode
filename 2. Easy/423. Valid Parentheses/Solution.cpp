class Solution {
public:
    /**
     * @param s: A string
     * @return: whether the string is a valid parentheses
     */
    bool isValidParentheses(string &s) {
        // write your code here
        if (s.empty()) {
            return true;
        }

        if (s.length() % 2 != 0) {
            return false;
        }

        stack<char> stack;
        for (int i = 0; i < s.length(); i++) {

            char c = s[i];
            if (c == '(' || c == '[' || c == '{') {
                stack.push(c);
            } else {
                // return false if stack is empty because the next char is closing
                // brackets but there is no opening brackets
                if (stack.empty()) {
                    return false;
                }

                // top element (nearest brackets) is not in pair
                if ((c == ')' && stack.top() != '(') ||
                    (c == ']' && stack.top() != '[' ) ||
                    (c == '}' && stack.top() != '{')) {
                    return false;
                }

                // pop the top element
                stack.pop();
            }
        }

        // if stack is empty, then there is no remaining brackets
        return stack.empty();
    }
};
