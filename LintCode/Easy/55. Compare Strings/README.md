# 55. Compare Strings

- **Description**
    - Compare two strings A and B, determine whether A contains all of the characters in B.
    - The characters in string A and B are all Upper Case letters.
The characters of B in A are not necessary continuous or ordered.
- **Example**
    - For `A = "ABCD"`, `B = "ACD"`, return `true`.
    - For `A = "ABCD"`, `B = "AABC"`, return `false`.

## Solution

HashMap的解法，先把A的所有char放到hashMap里边，然后对B进行遍历，逐个减去，如果找不到key，返回false；如果key都存在，value变成0说明B里边有多余的char, 返回false即可

### HashMap

```Java
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

```

### Array

开一个数组用来存储char的个数，本质上和第一个方法相同，但是不需要额外的进行 Map 的 get 和 put

```java
/**
* 本参考程序来自九章算法，由 @九章算法 提供。版权所有，转发请注明出处。
* - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
* - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
* - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
* - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code
*/

public class Solution {
    /**
     * @param A : A string includes Upper Case letters
     * @param B : A string includes Upper Case letter
     * @return :  if string A contains all of the characters in B return true else return false
     */
    public boolean compareStrings(String A, String B) {
        int[] counts = new int[26];
        for (int i = 0; i < 26; i++) {
            counts[i] = 0;
        }
        for (int i = 0; i < A.length(); i++) {
            counts[A.charAt(i) - 'A']++;
        }
        for (int i = 0; i < B.length(); i++) {
            counts[B.charAt(i) - 'A']--;
            if (counts[B.charAt(i) - 'A'] < 0) {
                return false;
            }
        }
        return true;
    }
}
```
