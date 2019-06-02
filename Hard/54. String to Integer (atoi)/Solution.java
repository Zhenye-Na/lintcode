public class Solution {
    /**
     * @param str: A string
     * @return: An integer
     */
    public int atoi(String str) {
        // write your code here
        if(str == null) {
            return 0;
        }
        str = str.trim();
        if (str.length() == 0) {
            return 0;
        }

        char first = str.charAt(0);
        int length = str.length(), index = 0, sign = 1, num;
        if (first == '-') {
            sign = -1;
            index++;
        } else if (first == '+') {
            index++;
        }

        long result = 0;
        for (int i = index; i < length; i++) {
            if (str.charAt(i) - '0' > 9 || str.charAt(i) - '0' < 0) {
                break;
            }
            num = str.charAt(i) - '0';
            result = result * 10 + num;
            if (sign * result >= Integer.MAX_VALUE || sign * result <= Integer.MIN_VALUE) {
                break;
            }
        }


        if (sign * result >= Integer.MAX_VALUE) {
            return Integer.MAX_VALUE;
        } else if (sign * result <= Integer.MIN_VALUE) {
            return Integer.MIN_VALUE;
        } else {
            return (int) (sign * result);
        }

    }
}
