# 101. Remove Duplicates from Sorted Array II

- **Description**
    - Follow up for "Remove Duplicates":
    - What if duplicates are allowed **at most twice**?
- **Example**
    - Given sorted array `A = [1,1,1,2,2,3]`,
    - Your function should return `length = 5`, and `A` is now `[1,1,2,2,3]`.


## Solution

### TreeMap


```java
public class Solution {
    /**
     * @param A: a array of integers
     * @return : return an integer
     */
    public int removeDuplicates(int[] nums) {
        // write your code here
        if (nums == null || nums.length == 0) {
            return 0;
        }

        Map<Integer, Integer> mapping = new TreeMap<>();
        int length = nums.length;
        for (int i = 0; i < length; i++) {
            if (!mapping.containsKey(nums[i])) {
                mapping.put( nums[i], 1 );
            } else {
                mapping.put( nums[i], mapping.get(nums[i]) + 1 );
            }
        }

        int index = 0;
        for (Map.Entry<Integer, Integer> entry : mapping.entrySet()) {
            int occurence = Math.min(2, entry.getValue());
            System.out.println(occurence);
            for (int num = 0; num < occurence; num++ ) {
                nums[index++] = entry.getKey();
            }
        }

        return index;
    }
}
```


### Two Pointers

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
     * @param A: a array of integers
     * @return : return an integer
     */
    public int removeDuplicates(int[] nums) {
        if (nums == null || nums.length == 0) {
            return 0;
        }
        int index = 0, count = 1;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] == nums[index]) {
                if (count < 2) {
                    nums[++index] = nums[i];
                    count ++;
                }
            } else {
                nums[++index] = nums[i];
                count = 1;
            }
        }
        return index + 1;
    }
}
```
