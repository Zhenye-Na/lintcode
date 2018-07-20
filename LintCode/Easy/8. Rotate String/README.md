# 8. Rotate String
Description
Given a string and an offset, rotate string by offset. (rotate from left to right)

Have you met this question in a real interview?  
Example
Given "abcdefg".

offset=0 => "abcdefg"
offset=1 => "gabcdef"
offset=2 => "fgabcde"
offset=3 => "efgabcd"
Challenge
Rotate in-place with O(1) extra memory.




```
public class Solution {
    /**
     * @param str: An array of char
     * @param offset: An integer
     * @return: nothing
     */
    public void rotateString(char[] str, int offset) {
        // write your code here
        if (str == null || str.length == 0 || offset == 0) {
            return;
        }

        offset = offset % str.length;
        int left = str.length - 2, right = str.length - 1, count = 0;

        while (count < offset) {

            while (left >= 0) {
                swap(str, left, right);
                left--;
                right--;
            }

            left = str.length - 2;
            right = str.length - 1;
        }

        private void swap(char[] str, int left, int right) {
            int temp = str[left];
            str[left] = str[right];
            str[right] = temp;
        }

    }
}
```






```
public class Solution {
    /**
     * @param str: An array of char
     * @param offset: An integer
     * @return: nothing
     */
    public void rotateString(char[] str, int offset) {
        // write your code here
        if (str == null || str.length == 0 || offset == 0) {
            return;
        }

        int length = str.length;
        offset = offset % length;
        reverse(str, 0, length - offset - 1);
        reverse(str, length - offset, length - 1);
        reverse(str, 0, length - 1);
    }
    
    private void reverse(char[] str, int start, int end) {
        for (int i = start, j = end; i < j; i++, j--) {
            char temp = str[i];
            str[i] = str[j];
            str[j] = temp;
        }
    }
}
```