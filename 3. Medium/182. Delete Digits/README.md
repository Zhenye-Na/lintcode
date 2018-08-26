# 182. Delete Digits

> *LeetCode 402. Remove K Digits*

Description

Given string `A` representative a positive integer which has `N` digits, remove any `k` digits of the number, the remaining digits are arranged according to the original order to become a new positive integer.

Note:
The length of `num` is less than `240` and will be `≥ k`.
The given num does not contain any leading zero.

Example
Example 1:

Input: `num = "1432219"`, `k = 3`
Output: `"1219"`
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.


Example 2:

Input: `num = "10200"`, `k = 1`
Output: `"200"`
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.


Example 3:

Input: `num = "10"`, `k = 2`
Output: `"0"`
Explanation: Remove all the digits from the number and it is left with nothing which is `0`.


## Solution

### `O(k * N)`

The first algorithm is straight-forward. Let's think about the simplest case: how to remove 1 digit from the number so that the new number is the smallest possible？ Well, one can simply scan from left to right, and remove the first "peak" digit; **the peak digit is larger than its right neighbor**. One can repeat this procedure k times, and obtain the first algorithm:

#### Python

```python
class Solution:
    """
    @param A: A positive integer which has N digits, A is a string
    @param k: Remove k digits
    @return: A string
    """
    def DeleteDigits(self, A, k):
        # write your code here
        A = list(A)
        stack = []
        length = len(A) - k

        # push into stack, check whether top element is greater than A[i]
        for i in xrange(len(A)):
            while k > 0 and len(stack) > 0 and stack[-1] > A[i]:
                stack.pop()
                k -= 1
            stack.append(A[i])

        stack = stack[:length]

        # trim leading zeroes
        i = 0
        while i < len(stack) and stack[i] == "0":
            i += 1

        result = "".join(stack[i:])
        return "0" if result == "" else result
```

#### C++

```cpp
class Solution {
public:
    /**
     * @param A: A positive integer which has N digits, A is a string
     * @param k: Remove k digits
     * @return: A string
     */
    string removeKdigits(string num, int k) {
            while (k > 0) {
                int n = num.size();
                int i = 0;
                while (i+1<n && num[i]<=num[i+1])  i++;
                num.erase(i, 1);
                k--;
            }
            // trim leading zeros
            int s = 0;
            while (s<(int)num.size()-1 && num[s]=='0')  s++;
            num.erase(0, s);

            return num=="" ? "0" : num;
        }
};
```

### Stack

The above algorithm is a bit inefficient because it frequently remove a particular element from a string and has complexity `O(k*n)`.

One can simulate the above procedure by using a stack, and obtain a `O(n)` algorithm. Note, when the result stack (i.e. res) pop a digit, it is equivalent as remove that "peak" digit.

#### C++

```cpp
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
```
