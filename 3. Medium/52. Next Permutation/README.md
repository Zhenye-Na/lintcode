# 52. Next Permutation

Description

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Example
Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.


`1,2,3` → `1,3,2`  
`3,2,1` → `1,2,3`  
`1,1,5` → `1,5,1`  


## Solution

### [Next lexicographical permutation algorithm](https://www.nayuki.io/page/next-lexicographical-permutation-algorithm)

We will use the sequence `(0, 1, 2, 5, 3, 3, 0)` as a running example.

The key observation in this algorithm is that when we want to compute the next permutation, we must "increase" the sequence as little as possible. Just like when we count up using numbers, we try to modify the rightmost elements and leave the left side unchanged. For example, there is no need to change the first element from `0` to `1`, because by changing the prefix from (0, 1) to (0, 2) we get an even closer next permutation. In fact, there is no need to change the second element either, which brings us to the next point.

Firstly, identify the longest suffix that is non-increasing (i.e. weakly decreasing). In our example, the suffix with this property is (5, 3, 3, 0). This suffix is already the highest permutation, so we can’t make a next permutation just by modifying it – we need to modify some element(s) to the left of it. (Note that we can identify this suffix in O(n) time by scanning the sequence from right to left. Also note that such a suffix has at least one element, because a single element substring is trivially non-increasing.)

Secondly, look at the element immediately to the left of the suffix (in the example it’s 2) and call it the pivot. (If there is no such element – i.e. the entire sequence is non-increasing – then this is already the last permutation.) The pivot is necessarily less than the head of the suffix (in the example it's 5). So some element in the suffix is greater than the pivot. If we swap the pivot with the smallest element in the suffix that is greater than the pivot, then the prefix is minimized. (The prefix is everything in the sequence except the suffix.) In the example, we end up with the new prefix `(0, 1, 3)` and new suffix `(5, 3, 2, 0)`. (Note that if the suffix has multiple copies of the new pivot, we should take the rightmost copy – this plays into the next step.)

Finally, we sort the suffix in non-decreasing (i.e. weakly increasing) order because we increased the prefix, so we want to make the new suffix as low as possible. In fact, we can avoid sorting and simply reverse the suffix, because the replaced element respects the weakly decreasing order. Thus we obtain the sequence `(0, 1, 3, 0, 2, 3, 5)`, which is the next permutation that we wanted to compute.

Condensed mathematical description:

1. Find largest index `i` such that `array[i − 1] < array[i]`. (If no such `i` exists, then this is already the last permutation.)
2. Find largest index `j` such that `j ≥ i` and `array[j] > array[i − 1]`.
3. Swap `array[j]` and `array[i − 1]`.
4. Reverse the suffix starting at `array[i]`.


![](https://www.nayuki.io/res/next-lexicographical-permutation-algorithm/next-permutation-algorithm.svg)


### Python

```python
class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers
    """
    def nextPermutation(self, nums):
        # write your code here
        if len(nums) <= 1:
            return nums

        i = len(nums) - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1
        if i <= 0:
            nums.sort()
            return nums

        # Find successor to pivot
        j = len(nums) - 1
        while nums[j] <= nums[i - 1]:
            j -= 1
        nums[i - 1], nums[j] = nums[j], nums[i - 1]

        # Reverse suffix
        nums[i : ] = nums[len(nums) - 1 : i - 1 : -1]

        return nums
```

### Java

```java
/**
 * Computes the next lexicographical permutation of the specified
 * array of integers in place, returning whether a next permutation
 * existed. (Returns {@code false} when the argument is already the
 * last possible permutation.)
 * @param array the array of integers to permute
 * @return whether the array was permuted to the next permutation
 */
public static boolean nextPermutation(int[] array) {
    // Find non-increasing suffix
    int i = array.length - 1;
    while (i > 0 && array[i - 1] >= array[i])
        i--;
    if (i <= 0)
        Arrays.sort(array)
        return array;

    // Find successor to pivot
    int j = array.length - 1;
    while (array[j] <= array[i - 1])
        j--;
    int temp = array[i - 1];
    array[i - 1] = array[j];
    array[j] = temp;

    // Reverse suffix
    j = array.length - 1;
    while (i < j) {
        temp = array[i];
        array[i] = array[j];
        array[j] = temp;
        i++;
        j--;
    }
    return array;
}
```
