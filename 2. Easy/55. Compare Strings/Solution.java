public class Solution {
    /**
     * @param A: A string
     * @param B: A string
     * @return: if string A contains all of the characters in B return true else return false
     */
    public boolean compareStrings(String A, String B) {
        // write your code here
        if (A.length() == 0 && B.length() != 0) return false;
        if (A.length() == 0 && B.length() == 0) return true;

        int Alength = A.length();
        int Blength = B.length();

        Map<Character, Integer> mapping = new HashMap<>();
        for (int i = 0; i < Alength; i++) {
            if (mapping.containsKey(A.charAt(i))) {
                mapping.put(A.charAt(i), mapping.get(A.charAt(i)) + 1);
            } else {
                mapping.put(A.charAt(i), 1);
            }
        }

        for (int j = 0; j < Blength; j++) {
            if (!mapping.containsKey(B.charAt(j)) || mapping.get(B.charAt(j)) == 0){
                return false;
            } else {
                mapping.put(B.charAt(j), mapping.get(B.charAt(j)) - 1);
            }
        }

        return true;

    }
}
