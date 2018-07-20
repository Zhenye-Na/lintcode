public class Solution {
    /**
     * @param s: A string
     * @return: Whether the string is a valid palindrome
     */
    public boolean isPalindrome(String s) {
        // write your code here
        s = rmSigns(s);
        if (s == null || s.length() == 0 || s.length() == 1) {
            return true;
        }

        int left = 0, right = s.length() - 1;
        while (left < right) {
            if (s.charAt(left) != s.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }

    private String rmSigns(String s) {
        String wow = s.replaceAll("[^a-zA-Z0-9]", "").trim().toUpperCase();
        return wow;
    }
    
    
}