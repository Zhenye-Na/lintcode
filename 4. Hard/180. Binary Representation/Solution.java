public class Solution {
    /**
     * @param n: Given a decimal number that is passed in as a string
     * @return: A string
     */

    public String binaryRepresentation(String n) {
        // write your code here
        StringBuilder sb = new StringBuilder();
        String[] number = n.split("\\.");

        int length = number[1].length();
        long integer = Long.parseLong(number[0]);

        double division = Math.pow(10, length);
        double fraction = Long.parseLong(number[1]) / division;

        if (fraction != 0.0) {
            while (fraction > 0) {
                if (fraction * 2 >= 1) {
                    sb.append(1);
                    fraction = fraction * 2 - 1;
                } else {
                    sb.append(0);
                    fraction = fraction * 2;
                }
                if (sb.length() > 32) {
                    return "ERROR";
                }
            }

            return Long.toBinaryString(integer) + "." + sb.toString();

        } else {
            return Long.toBinaryString(integer);
        }

    }

}
