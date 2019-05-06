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