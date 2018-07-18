# 138. Subarray Sum


- **Description**
    - Given an integer array, find a subarray where the sum of numbers is zero. Your code should return the index of the first number and the index of the last number.
    - There is at least one subarray that it's sum equals to zero.
- **Example**
    - Given `[-3, 1, 2, -3, 4]`, return `[0, 2]` **or** `[1, 3].
    

## Solution

比较简单，但是思路还是要明确。

用到了 **PrefixSum** 的思想，但是要思考，什么情况下才会表示 `subarraySum == 0` ？
即：prefixSum 出现两个相同的 value 时，说明存在 `subarraySum == 0`
题目指出 **"or"**，所以我用了 `break`，也可以直接 `return`

举个🌰：  
`[-3, 1, 2, -3, 4]` 的 prefixSum 是 `[0, -3, -2, 0, -3, 1]` 可以观察到 `-3` 和 `0` 都出现了两次，所以 example 给出的 return value 有**两组**。


```java
public class Solution {
    /**
     * @param nums: A list of integers
     * @return: A list of integers includes the index of the first number and the index of the last number
     */
    public List<Integer> subarraySum(int[] nums) {
        // write your code here
        List<Integer> result = new ArrayList<>();
        if (nums == null || nums.length == 0) return result;
        
        // prefix sum -> array index
        Map<Integer, Integer> mapping = new HashMap<>();
        
        // first prefix sum = 0;
        mapping.put(0, -1);
        
        int sum = 0;
        int length = nums.length;

        for (int i = 0; i < length; i++) {
            sum += nums[i];
            
            if (mapping.containsKey(sum)) {
                result.add(mapping.get(sum) + 1);
                result.add(i);
                break;
            } else {
                mapping.put(sum, i);
            }
        }
        
        return result;
    }
}
```

**@九章算法题解：**

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
     * @param nums: A list of integers
     * @return: A list of integers includes the index of the first number and the index of the last number
     */
    public ArrayList<Integer> subarraySum(int[] nums) {
        // write your code here
       
        int len = nums.length;
       
        ArrayList<Integer> ans = new ArrayList<Integer>();
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
       
        map.put(0, -1);
       
        int sum = 0;
        for (int i = 0; i < len; i++) {
            sum += nums[i];
           
            if (map.containsKey(sum)) {
                ans.add(map.get(sum) + 1);
                ans.add(i);
                return ans;
            }
            
            map.put(sum, i);
        }
       
        return ans;
    }
}
```