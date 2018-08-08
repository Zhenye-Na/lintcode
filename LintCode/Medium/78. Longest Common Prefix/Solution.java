public class Solution {
    /**
     * @param strs: A list of strings
     * @return: The longest common prefix
     */
    public String longestCommonPrefix(String[] strs) {
        // write your code here
        if (strs == null || strs.length == 0) return "";
        Map<Integer, Character> mapping = new HashMap<>();

        int index = 0, length = strs.length;
        boolean flag = false, diffFlag = true;
        while (true) {
            int i;
            for (i = 0; i < length; i++) {

                // IndexOutOfBounds
                if (index >= strs[i].length()) {
                    flag = true;
                    break;
                } else {
                    char buffer = strs[i].charAt(index);
                    if (index + 1 > mapping.size()) {
                        // new Character
                        mapping.put(index, buffer);
                    } else if (index + 1 == mapping.size() && buffer != mapping.get(index)) {
                        // There is different Character
                        flag = true;
                        diffFlag = true;
                        break;
                    }
                }
            }

            // Check whether iterate to end or break
            if (flag) {
                break;
            } else {
                index++;
            }

        }

        int prefixLength = diffFlag ? index - 1 : index;

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i <= prefixLength; i++) {
            sb.append(mapping.get(i));
        }

        return sb.toString();
    }
}
