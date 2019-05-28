public class Solution {
    /**
     * @param n: a decimal number
     * @param k: a Integer represent base-k
     * @return: a base-k number
     */

    char[] dict = {'0', '1', '2', '3', '4', '5', '6', '7',
                   '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'
                  };
    public String hexConversion(int n, int k) {
        // write your code here
        LinkedList<Character> l = new LinkedList<>();
        char[] digits = new char[k];

        int q = n / k;
        int r = n % k;
        l.add(0, dict[r]);

        while (q != 0) {
            n = q;
            q = n / k;
            r = n % k;
            l.add(0, dict[r]);
        }

        StringBuilder sb = new StringBuilder();

        for (char d : l) {
            sb.append(d);
        }

        return sb.toString();
    }
}
