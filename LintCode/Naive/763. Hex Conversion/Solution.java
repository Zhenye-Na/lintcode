import java.util.LinkedList;

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
        
        char[] digits = new char[k];
        System.arraycopy(dict, 0, digits, 0, k);
        
        int q = n / k;
        int r = n % k;
        LinkedList<Character> l = new LinkedList<>();
        l.add(0, digits[r]);
        
        while (q != 0) {
            n = q;
            q = n / k;
            r = n % k;
            l.add(0, digits[r]);
        }
        
        StringBuilder sb = new StringBuilder();
        for (char d : l) {
            sb.append(d);
        }
        
        return sb.toString();
    }
}