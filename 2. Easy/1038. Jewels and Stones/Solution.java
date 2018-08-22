public class Solution {
    /**
     * @param J: the types of stones that are jewels
     * @param S: representing the stones you have
     * @return: how many of the stones you have are also jewels
     */
    public int numJewelsInStones(String J, String S) {
        // Write your code here
        if (J == null || J.length() == 0) {
            return 0;
        }

        Set<Character> set = new HashSet<>();
        for (int i = 0; i < J.length(); i++) {
            set.add(J.charAt(i));
        }

        int num = 0;
        for (int j = 0; j < S.length(); j++) {
            if (set.contains(S.charAt(j))) {
                num++;
            }
        }

        return num;
    }
}
