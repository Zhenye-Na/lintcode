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