# 172. Remove Element

- **Description**
    - Given an array and a value, remove all occurrences of that value **in place and return the new length**.
    - **The order of elements can be changed, and the elements after the new length don't matter**.
- **Example**
    - Given an array `[0,4,4,0,0,2,4,4]`, `value=4`
    - return `4` and front four elements of the array is `[0,0,0,2]`




## Solution

最开始没有读懂题意，这道题是“只要把不一样的放在前面并给出有多少个不一样的，OJ 只会去检查前半部分，后半部分无所谓”


```java
public class Solution {
    /*
     * @param A: A list of integers
     * @param elem: An integer
     * @return: The new length after remove
     */
    public int removeElement(int[] A, int elem) {
        // write your code here
        int i = 0;
        int pointer = A.length - 1;

        while(i <= pointer){
            if(A[i] == elem){
                A[i] = A[pointer];
                pointer--;
            } else {
                i++;
            }
        }

        return pointer + 1;
    }
}
```