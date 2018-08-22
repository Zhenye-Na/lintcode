/**

substring

public String substring(int startIndex): This method returns new String object
    containing the substring of the given string from specified startIndex (inclusive).

public String substring(int startIndex, int endIndex): This method returns new
    String object containing the substring of the given string from specified
    startIndex to endIndex.

In case of string:
    startIndex: inclusive
    endIndex: exclusive

*/

public class Solution {
    /**
     * Returns a index to the first occurrence of target in source,
     * or -1  if target is not part of source.
     * @param source string to be scanned.
     * @param target string containing the sequence of characters to match.
     */
    public int strStr(String source, String target) {
        // write your code here
        if (source == null || target == null || target.length() > source.length()) {
            return -1;
        }

        for (int i = 0; i <= source.length() - target.length(); i++) {
            if (source.substring(i, i + target.length()).equals(target)) {
                return i;
            }
        }

        return -1;
    }
}





/**

While/For loop only

*/

/**
* 本参考程序来自九章算法，由 @九章算法 提供。版权所有，转发请注明出处。
* - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
* - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
* - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
* - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code
*/

class Solution {
    /**
     * Returns a index to the first occurrence of target in source,
     * or -1  if target is not part of source.
     * @param source string to be scanned.
     * @param target string containing the sequence of characters to match.
     */
    public int strStr(String source, String target) {
        if (source == null || target == null) {
            return -1;
        }

        for (int i = 0; i < source.length() - target.length() + 1; i++) {
            int j = 0;
            for (j = 0; j < target.length(); j++) {
                if (source.charAt(i + j) != target.charAt(j)) {
                    break;
                }
            }
            // finished loop, target found
            if (j == target.length()) {
                return i;
            }
        }
        return -1;
    }
}






/**

KMP: Knuth-Morris-Pratt (Optional)

    O(m+n)

*/

public class Solution {
    int[] KMPpreprocessing(String needle) {
        int n = needle.length();
        int[] match = new int[n];
        Arrays.fill(match, -1);
        int j = -1;
        for (int i = 1; i < n; ++i) {
            while (j >= 0 && needle.charAt(i) != needle.charAt(j + 1))
                j = match[j];
            if (needle.charAt(i) == needle.charAt(j + 1))
                j++;
            match[i] = j;
        }
        return match;
    }

    public int strStr(String haystack, String needle) {
        int lengthOfHaystack = haystack.length();
        int lengthOfNeedle = needle.length();
        if (lengthOfNeedle == 0)
            return 0;
        if (lengthOfNeedle > lengthOfHaystack)
            return -1;
        int[] match = KMPpreprocessing(needle);
        int j = -1;
        for (int i = 0; i < lengthOfHaystack; i++) {
            while (j >= 0 && haystack.charAt(i) != needle.charAt(j + 1))
                j = match[j];
            if (haystack.charAt(i) == needle.charAt(j + 1))
                j++;
            if (j == lengthOfNeedle - 1)
                return (i - lengthOfNeedle + 1);
        }
        return -1;
    }
}
