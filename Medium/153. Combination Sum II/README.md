# 153. Combination Sum II

- **Description**
    - Given a collection of candidate numbers (**C**) and a target number (**T**), find all unique combinations in **C** where the candidate numbers sums to **T**.
    - Each number in **C** may only be used once in the combination.
    - All numbers (including target) will be positive integers.
    - Elements in a combination (`a1, a2, … , ak`) must be in non-descending order. (ie, `a1 ≤ a2 ≤ … ≤ ak`).
    - The solution set must not contain duplicate combinations. 
- **Example**
- Given candidate set `[10,1,6,7,2,1,5]` and target `8`,
- A solution set is:

    ```
    [
      [1,7],
      [1,2,5],
      [2,6],
      [1,1,6]
    ]
    ```




## Solution

与 135. Combination Sum 基本类似，唯一不同的是不能重复。

添加这一行判断即可：  
> 当前选中的 element 和 相邻的 element 不相等，并且 不是可以选择的第一个值（其实相当于不让 `i - 1` "out of bounds"）

```java
if (i != startIndex && nums[i - 1] == nums[i]) {
    continue;
}
```


### Code

```java
public class Solution {
    /**
     * @param nums: Given the candidate numbers
     * @param target: Given the target number
     * @return: All the combinations that sum to target
     */
    public List<List<Integer>> combinationSum2(int[] nums, int target) {
        // write your code here
        List<List<Integer>> results = new ArrayList<>();
        if (nums == null || nums.length == 0) {
            return results;
        }
        
        Arrays.sort(nums);
        helper(nums, 0, target, new ArrayList<>(), results);
        return results;
    }

    
    private void helper(int[] nums,
                        int startIndex,
                        int target,
                        List<Integer> combinations,
                        List<List<Integer>> results) {
        
        // Definition: Recursively find combinations that sum up to target
        
        // Exit:
        if (target == 0) {
            results.add(new ArrayList<>(combinations));
            return;
        }
        
        // Split:
        for (int i = startIndex; i < nums.length; i++) {
            
            if (i != startIndex && nums[i - 1] == nums[i]) {
                continue;
            }
            
            if (nums[i] > target) {
                break;
            }
            
            combinations.add(nums[i]);                                     // add element
            helper(nums, i + 1, target - nums[i], combinations, results);  // 从当前位置的下一个位置开始，与 subsets 类似，但与 permutations 不同，因为不是要去除所有的 element，而是要求 `combination.sum() == target`
            combinations.remove(combinations.size() - 1);                  // remove element，算法继续执行

        }

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

public class Solution {
    /**
     * @param num: Given the candidate numbers
     * @param target: Given the target number
     * @return: All the combinations that sum to target
     */
    public List<List<Integer>> combinationSum2(int[] candidates,
            int target) {
        List<List<Integer>> results = new ArrayList<>();
        if (candidates == null || candidates.length == 0) {
            return results;
        }

        Arrays.sort(candidates);
        List<Integer> combination = new ArrayList<Integer>();
        helper(candidates, 0, combination, target, results);

        return results;
    }

    private void helper(int[] candidates,
                        int startIndex,
                        List<Integer> combination,
                        int target,
                        List<List<Integer>> results) {
        if (target == 0) {
            results.add(new ArrayList<Integer>(combination));
            return;
        }

        for (int i = startIndex; i < candidates.length; i++) {
            if (i != startIndex && candidates[i] == candidates[i - 1]) {
                continue;
            }
            if (target < candidates[i]) {
                break;
            }
            combination.add(candidates[i]);
            helper(candidates, i + 1, combination, target - candidates[i], results);
            combination.remove(combination.size() - 1);
        }
    }
}
```