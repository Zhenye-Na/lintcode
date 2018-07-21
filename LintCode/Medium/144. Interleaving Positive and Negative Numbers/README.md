# 144. Interleaving Positive and Negative Numbers

- **Description**
- Given an array with positive and negative integers. Re-range it to interleaving with positive and negative integers.
- You are not necessary to keep the original order of positive integers or negative integers.
- **Example**
- Given `[-1, -2, -3, 4, 5, 6]`, after re-range, it will be `[-1, 5, -2, 4, -3, 6]` or any other reasonable answer.
- **Challenge**
- Do it in-place and **without extra memory**.


## Solution

```java
public class Solution {
    /*
     * @param A: An integer array.
     * @return: nothing
     */
    public void rerange(int[] A) {
        // write your code here
        int positive = 0;
        int negative = 0;
        
        Arrays.sort(A);

        for (int i = 0; i < A.length; i++) {
            if (A[i] < 0) {
                negative++;
            }

            if (A[i] > 0) {
                positive++;
            }
        }
        
        if (positive > negative){
            reverse(A);
        }

        for (int left = 0; left < A.length; left++) {
            int right = left + 1;
            while(right < A.length && A[left] * A[right] > 0) {
                right++;
            }
            
            if (right < A.length && A[left] * A[right] < 0) {
                int tmp = A[left + 1];
                A[left + 1] = A[right];
                A[right] = tmp;
            }

        }

    }

    public  void reverse(int[] A) {
        int left = 0;
        int right = A.length - 1;
        while (left <= right) {
            int tmp = A[left];
            A[left] = A[right];
            A[right] = tmp;
            left++;
            right--;
        }
    }

}
```