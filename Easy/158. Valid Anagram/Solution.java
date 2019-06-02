public class Solution {
    /**
     * @param s: The first string
     * @param t: The second string
     * @return: true or false
     */
    public boolean anagram(String s, String t) {
        // write your code here
        if (s == null || t == null || s.length() != t.length()) {
            return false;
        }

        Map<Character, Integer> map = new HashMap<>();
        int sLength = s.length(), tLength = t.length();

        for (int i = 0; i < sLength; i++) {
            if (!map.containsKey(s.charAt(i))) {
                map.put( s.charAt(i), 1 );
            } else {
                map.put( s.charAt(i), map.get(s.charAt(i)) + 1 );
            }
        }

        for (int j = 0; j < tLength; j++) {
            if ( !map.containsKey(t.charAt(j)) || map.get(t.charAt(j)) <= 0 ) {
                return false;
            } else {
                map.put( t.charAt(j), map.get(t.charAt(j)) - 1 );
            }
        }

        return true;
    }
}
