# 58. 4Sum

- **Description**
    - Given an array `S` of `n` integers, are there elements `a`, `b`, `c`, and `d` in `S` such that `a + b + c + d = target`?
    - Find all unique quadruplets in the array which gives the sum of target.
    - Elements in a quadruplet `(a,b,c,d)` must be in **non-descending** order. (ie, `a ≤ b ≤ c ≤ d`)
    - The solution set **must not contain duplicate quadruplets**.
- **Example**
    - Given array `S = {1 0 -1 0 -2 2}`, and `target = 0`.
    - A solution set is:

    ```
    (-1, 0, 0, 1)
    (-2, -1, 1, 2)
    (-2, 0, 0, 2)
    ```


## Solution

4Sum -> 3Sum -> 2Sum

```java
public class Solution {
    /**
     * @param numbers: Give an array
     * @param target: An integer
     * @return: Find all unique quadruplets in the array which gives the sum of zero
     */
    public List<List<Integer>> fourSum(int[] numbers, int target) {
        // write your code here
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        if (numbers == null || numbers.length < 4) {
            return result;
        }

        Arrays.sort(numbers);

        for (int i = 0; i < numbers.length; i++) {
            // First number: a
            if (i > 0 && numbers[i] == numbers[i - 1]) {
                continue;
            }
            
            for (int j = i + 1; j < numbers.length; j++) {
                // Second number: b
                if (j > i + 1 && numbers[j] == numbers[j - 1]) {
                    continue;
                }

                // Third and Fourth number: c, d
                int start = j + 1, end = numbers.length - 1;
                
                while (start < end) {
                    int total = numbers[i] + numbers[j] + numbers[start] + numbers[end];
                    if (total == target) {
                        List<Integer> tmp = new ArrayList<>();
                        tmp.add(numbers[i]);
                        tmp.add(numbers[j]);
                        tmp.add(numbers[start]);
                        tmp.add(numbers[end]);
                        result.add(tmp);

                        start++;
                        while (start < end && numbers[start] == numbers[start - 1]) {
							start++;
						}

						end--;
						while (start < end && numbers[end] == numbers[end + 1]) {
							end--;
						}
                    } else if (total > target) {
                        end--;
						while (start < end && numbers[end] == numbers[end + 1]) {
							end--;
						}
                    } else {
                        start++;
                        while (start < end && numbers[start] == numbers[start - 1]) {
							start++;
						}
                    }
                }

            }

        }
        return result;
    }

}
```