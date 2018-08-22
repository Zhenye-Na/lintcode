# 136. Palindrome Partitioning

- **Description**
    - Given a string `s`, partition `s` such that every substring of the partition is a palindrome.
    - Return all possible palindrome partitioning of `s`.
- **Example**
    - Given s = "aab", return:

    ```java
    [
      ["aa","b"],
      ["a","a","b"]
    ]
    ```


## Solution

分割回文字符串：

- 本题和 `subsets` 以及 `combination sum` 基本类似，只不过不是很明显。字符串每一个字母之间都是可以拆开的候选位置（高中数学）。
- 同时，跟 permutations 不同，不可以选择之前的字母（需要一个 `startIndex`）
- 其他就是套模板即可



### Code

```java
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
```


**九章题解：**


```java
/**
* 本参考程序来自九章算法，由 @九章算法 提供。版权所有，转发请注明出处。
* - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
* - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
* - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
* - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code
*/ 

// version 1: shorter but slower
public class Solution {
    /**
     * @param s: A string
     * @return: A list of lists of string
     */
    public List<List<String>> partition(String s) {
        List<List<String>> results = new ArrayList<>();
        if (s == null || s.length() == 0) {
            return results;
        }
        
        List<String> partition = new ArrayList<String>();
        helper(s, 0, partition, results);
        
        return results;
    }
    
    private void helper(String s,
                        int startIndex,
                        List<String> partition,
                        List<List<String>> results) {
        if (startIndex == s.length()) {
            results.add(new ArrayList<String>(partition));
            return;
        }
        
        for (int i = startIndex; i < s.length(); i++) {
            String subString = s.substring(startIndex, i + 1);
            if (!isPalindrome(subString)) {
                continue;
            }
            partition.add(subString);
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




// version 2: longer but faster
public class Solution {
    List<List<String>> results;
    boolean[][] isPalindrome;
    
    /**
     * @param s: A string
     * @return: A list of lists of string
     */
    public List<List<String>> partition(String s) {
        results = new ArrayList<>();
        if (s == null || s.length() == 0) {
            return results;
        }
        
        getIsPalindrome(s);
        
        helper(s, 0, new ArrayList<Integer>());
        
        return results;
    }
    
    private void getIsPalindrome(String s) {
        int n = s.length();
        isPalindrome = new boolean[n][n];
        
        for (int i = 0; i < n; i++) {
            isPalindrome[i][i] = true;
        }
        for (int i = 0; i < n - 1; i++) {
            isPalindrome[i][i + 1] = (s.charAt(i) == s.charAt(i + 1));
        }
        
        for (int i = n - 3; i >= 0; i--) {
            for (int j = i + 2; j < n; j++) {
                isPalindrome[i][j] = isPalindrome[i + 1][j - 1] && s.charAt(i) == s.charAt(j);
            }
        }
    }
    
    private void helper(String s,
                        int startIndex,
                        List<Integer> partition) {
        if (startIndex == s.length()) {
            addResult(s, partition);
            return;
        }
        
        for (int i = startIndex; i < s.length(); i++) {
            if (!isPalindrome[startIndex][i]) {
                continue;
            }
            partition.add(i);
            helper(s, i + 1, partition);
            partition.remove(partition.size() - 1);
        }
    }
    
    private void addResult(String s, List<Integer> partition) {
        List<String> result = new ArrayList<>();
        int startIndex = 0;
        for (int i = 0; i < partition.size(); i++) {
            result.add(s.substring(startIndex, partition.get(i) + 1));
            startIndex = partition.get(i) + 1;
        }
        results.add(result);
    }
}







/**
* 本参考程序来自九章算法，由 @DIng 提供。版权所有，转发请注明出处。
* - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
* - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
* - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
* - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code
*/ 

public class Solution {
    /*
     * @param s: A string
     * @return: A list of lists of string
     */
    public List<List<String>> partition(String s) {
        // write your code here
        List<List<String>> results = new ArrayList<>();
        if (s == null || s.length() == 0) {
            results.add(new ArrayList<>());
            return results;
        }
        Map<String, List<List<String>>> memo = new HashMap<>();
        return dfs(memo, s);
    }
    
    private List<List<String>> dfs(Map<String, 
                                   List<List<String>>> memo,
                                   String s) {
        
        if (s.length() == 0) {
            List<List<String>> list = new ArrayList<List<String>>();
            list.add(new ArrayList<>());
            return list;
        }
        
        // memoization
        if (memo.containsKey(s)) {
            return memo.get(s);
        } else {
            List<List<String>> list = new ArrayList<List<String>>();
            memo.put(s, list);
        }
        
        for (int i = 1; i <= s.length(); i++) {
            String sub = s.substring(0, i);
            if (!isPalindrome(sub)) {
                continue;
            }
            List<List<String>> next = dfs(memo, s.substring(i, s.length()));
            for (List<String> path : next) {
                List<String> list = new ArrayList<>();
                list.add(sub);
                list.addAll(path);
                memo.get(s).add(list);
            }
        }
        return memo.get(s);
    }
    
    private boolean isPalindrome(String s) {
        boolean[][] f = new boolean[s.length()][s.length()];
        f[0][0] = true;
        for (int i = 1; i < s.length(); i++) {
            f[i][i] = true;
            if (s.charAt(i) == s.charAt(i - 1)) {
                f[i - 1][i] = true;
            }
        }
        
        for (int i = s.length() - 3; i >= 0; i--) {
            for (int j = i + 2; j < s.length(); j++) {
                if (s.charAt(i) == s.charAt(j) && f[i + 1][j - 1]) {
                    f[i][j] = true;
                }
            }
        }
        return f[0][s.length() - 1];
    }
    
}
```