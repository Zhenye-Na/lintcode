# 50. Product of Array Exclude Itself
Description
Given an integers array A.

Define B[i] = A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1], calculate B WITHOUT divide operation.

Have you met this question in a real interview?  
Example
For A = [1, 2, 3], return [6, 3, 2].


## Solution

### For loop

```java
public class Solution {
    /*
     * @param nums: Given an integers array A
     * @return: A long long array B and B[i]= A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]
     */
    public List<Long> productExcludeItself(List<Integer> nums) {
        // write your code here
        List<Long> result = new ArrayList<>();
        if (nums == null || nums.size() == 0 || nums.size() == 1) {
            result.add( (long) 1);
            return result;
        }

        int[] mask = new int[nums.size()];
        Arrays.fill(mask, 1);

        int size = nums.size();
        for (int index = 0; index < size; index++) {
            mask[index] = 0;
            result.add(calculateProduct(nums, mask));
            mask[index] = 1;
        }
        return result;
    }


    private long calculateProduct(List<Integer> nums, int[] mask) {
        long result = 1;
        for (int i = 0; i < mask.length; i++) {
            if (mask[i] != 0) {
                int mul = nums.get(i);
                result = result * (long) mul;
            }
        }

        return result;

    }
}

```

### "Dynamic Programming"


```java
public class Solution {
    /**
     * @param A: Given an integers array A
     * @return: A Long array B and B[i]= A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]
     */
    public ArrayList<Long> productExcludeItself(ArrayList<Integer> A) {
        // write your code
        //DP
        ArrayList<Long> res = new ArrayList<Long>();
        if(A == null || A.size() == 0){
            return res;
        }

        int n = A.size();
        //f[i]:product from i to end
        long[] f = new long[n];
        f[n - 1] = A.get(n - 1);
        for(int i = n - 2; i >= 0; i--){
            f[i] = A.get(i) * f[i + 1];
        }

        //从开头到当前元素之前的元素之积
        long now = 1;
        //从开头到当前元素之积
        long temp = 1;
        for(int i = 0; i < n; i++){
            now = temp;
            if(i + 1 < n){
                res.add(now * f[i + 1]);
            }else{
                res.add(now);
            }
            temp = now * A.get(i);
        }

        return res;
    }
}
```
