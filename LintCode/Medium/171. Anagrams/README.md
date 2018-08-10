# 171. Anagrams
Description
Given an array of strings, return all groups of strings that are anagrams.

All inputs will be in lower-case

Have you met this question in a real interview?  
Example
Given ["lint", "intl", "inlt", "code"], return ["lint", "inlt", "intl"].

Given ["ab", "ba", "cd", "dc", "e"], return ["ab", "ba", "cd", "dc"].

Challenge
What is Anagram?

Two strings are anagram if they can be the same after change the order of characters.


## Solution

```java
public class Solution {
    /**
     * @param strs: A list of strings
     * @return: A list of strings
     */
    public List<String> anagrams(String[] strs) {
        // write your code here
        List<String> result = new ArrayList<String>();
        if (strs == null || strs.length == 0) {
            return result;
        }
        Map<String, ArrayList<String>> map = new HashMap<String, ArrayList<String>>();
        for (int i = 0; i < strs.length; i++) {
            char[] arr = strs[i].toCharArray();
            Arrays.sort(arr);
            String s = String.valueOf(arr);
            if (!map.containsKey(s)) {
                ArrayList<String> list = new ArrayList<String>();
                map.put(s, list);
            }
            map.get(s).add(strs[i]);
        }
        for (Map.Entry<String, ArrayList<String>> entry : map.entrySet()) {
            if (entry.getValue().size() >= 2) {
                result.addAll(entry.getValue());
            }
        }
        return result;
    }

}
```
