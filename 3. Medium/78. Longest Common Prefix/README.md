# 78. Longest Common Prefix

- **Description**
    - Given `k` strings, find the **longest common prefix (LCP)**.
- **Example**
    - For strings `"ABCD"`, `"ABEF"` and `"ACEF"`, the LCP is `"A"`
    - For strings `"ABCDEFG"`, `"ABCEFG"` and `"ABCEFA"`, the LCP is `"ABC"`


## Solution

想到了一个**十分麻烦**但是跑起来不算慢的方法，具体思路如下：

- `String Array` 里面每一个 String `length()` 都不一定相同，一定会有一个最短的（或者 `lrngth()` 全部一样）
- 如果一直 `index++` 这样就会产生 `IndexOutOfBoundsException` 者正是我所要的，出现这种情况说明，已经到头了不要继续加 `Character` 了
- 用一个 HashMap 来存储 (Index, Character) 这个关系，也就是第一个相同的字母会被变成 (0, X) 存进 HashMap，这就产生了如何判断当前 character 是否应该被算入 return String
- 这里用到了两个 flag， 一个是 `IndexOutOfBounds` 时的 `flag`，一个是当前字母和之前的 `String.charAt(index)` 不一样时的 `diffFlag`，`flag == true` 代表已经到达某一个 String 的末尾了，LCP不能在长了，直接 break 掉所有 loop 即可； `diffFlag == true` 代表遇到了不同值，最后一个LCP应该删除（不应该算在 return String 里）
- 用 StringBuilder 把HashMap里所有的 value 取出来变成String就可以了




```java
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

```