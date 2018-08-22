public class Solution {
    /*
     * @param s: A string
     * @return: A list of lists of string
     */
    public List<List<String>> partition(String s) {
        // write your code here
        List<List<String>> results = new ArrayList<>();
        if (s == null || s.length() == 0) return results;

        helper(s, 0, new ArrayList<String>(), results);
        return results;
    }


    private void helper(String s,
                        int startIndex,
                        List<String> partition,
                        List<List<String>> results) {
        
        // Definition: Recursively find all palidrome substring

        // Exit
        if (s.length() == startIndex) {
            results.add(new ArrayList<String>(partition));
            return;
        }


        // Split
        for (int i = startIndex; i < s.length(); i++) {
            String substring = s.substring(startIndex, i + 1);
            if (!isPalindrome(substring)) {
                continue;
            }
            
            partition.add(substring);
            helper(s, i + 1, partition, results);
            partition.remove(partition.size() - 1);
        }

    }


    private boolean isPalindrome(String s) {
        for (int i = 0, j = s.length() - 1; i < j; i++, j--) {
            if (s.charAt(i) != s.charAt(j)) {
                return false;
            }
        }
        return true;
    }
    
}