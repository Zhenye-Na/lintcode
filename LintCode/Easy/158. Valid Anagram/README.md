# 158. Valid Anagram

- **Description**
    - Write a method `anagram(s,t)` to decide if two strings are anagrams or not.
- **Clarification**
    - What is Anagram?
    - **Two strings are anagram if they can be the same after change the order of characters**.
- **Example**
    - Given `s = "abcd"`, `t = "dcab"`, return `true`.
    - Given `s = "ab"`, `t = "ab"`, return `true`.
    - Given `s = "ab"`, `t = "ac"`, return `false`.
- **Challenge**
    - `O(n)` time, `O(1)` extra space


## Solution

### HashMap

```java
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

```

### Array

通过使用一个数组的方式进一步降低了空间复杂度，同时也加快的运行速度。

```java
/**
* 本参考程序来自九章算法，由 @J同学 提供。版权所有，转发请注明出处。
* - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
* - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
* - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
* - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code
*/

public class Solution {
    /**
     * @param s: The first string
     * @param t: The second string
     * @return: true or false
     */
    public boolean anagram(String s, String t) {
        // write your code here
        if(s==null || t==null ||s.length()!=t.length()){
            return false;
        }

        int[] container = new int[128];
        for(char c: s.toCharArray()){
            container[c]++;
        }
        for(char c: t.toCharArray()){
            container[c]--;
        }

        for(int i=0;i<container.length;i++){
            if(container[i]!=0){
                return false;
            }
        }

        return true;

    }
}
```




```python
# 本参考程序来自九章算法，由 @J同学 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code


class Solution:
    """
    @param s: The first string
    @param t: The second string
    @return: true or false
    """
    def anagram(self, s, t):
        return collections.Counter(s) == collections.Counter(t)
```
