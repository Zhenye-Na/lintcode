# 927. Reverse Words in a String II

**Description**

Given an input character array, reverse the array word by word. A word is defined as a sequence of non-space characters.

The input character array does not contain leading or trailing spaces and the words are always separated by a single space.


**Example**

Example1

```
Input: s = "the sky is blue"
Output: "blue is sky the"
```

Example2

```
Input: "a b c"
Output: "c b a"
```

**Challenge**

Could you do it in-place without allocating extra space?


no extra space, 三步翻转法

```java
public class Solution {
    /**
     * @param str: a string
     * @return: return a string
     */
    public char[] reverseWords(char[] str) {
        if(str == null || str.length == 0){
            return str;
        }

        // 翻转整个数组
        reverse(str, 0, str.length - 1);
        
        int index = 0;

        // 翻转每一个单词
        for(int i = 0; i < str.length; i++){
            if (str[i] == ' ') {
                reverse(str, index, i - 1);
                index = i + 1;
            }
        }

        // 翻转最后一个单词
        reverse(str, index, str.length - 1);
    
        return str;
    }

    private void reverse(char[] str, int start, int end){
        while(start <= end){
            char temp = str[start];
            str[start] = str[end];
            str[end] = temp;
            start++;
            end--;
        }
    }
}
```

one-line solution

```python
class Solution:
    """
    @param s: a string
    @return: return a string
    """
    def reverseWords(self, s):
        # write your code here
        return " ".join(reversed(s.strip().split(" ")))
```

