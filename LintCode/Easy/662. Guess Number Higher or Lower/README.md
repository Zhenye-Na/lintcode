# 662. Guess Number Higher or Lower

- **Description**
    - We are playing the Guess Game. The game is as follows:
        - I pick a number from `1` to `n`. You have to guess which number I picked.
        - Every time you guess wrong, I'll tell you whether the number is higher or lower.
    - You call a pre-defined API guess(int num) which returns 3 possible results `(-1, 1, or 0)`
- **Example**
    - `n = 10`, I pick `4` (but you don't know)
    - Return `4`. Correct !


## Solution


### Binary Search


#### Python


```python
"""
The guess API is already defined for you.
@param num, your guess
@return -1 if my number is lower, 1 if my number is higher, otherwise return 0
you can call Guess.guess(num)
"""


class Solution:
    # @param {int} n an integer
    # @return {int} the number you guess
    def guessNumber(self, n):
        # Write your code here
        start, end = 1, n
        while start + 1 < end:
            mid = (end - start) / 2 + start

            if Guess.guess(mid) == 0:
                return mid
            elif Guess.guess(mid) > 0:
                start = mid
            else:
                end = mid

        if Guess.guess(start) == 0:
            return start
        if Guess.guess(end) == 0:
            return end
        return -1
```


#### Java

```java
/* The guess API is defined in the parent class GuessGame.
   @param num, your guess
   @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
      int guess(int num); */

public class Solution extends GuessGame {
    /**
     * @param n an integer
     * @return the number you guess
     */
    public int guessNumber(int n) {
        // Write your code here

        int start = 0, end = n;
        while(start + 1 < end) {
            int mid = start + (end - start) / 2;
            if(guess(mid) < 0) {
                end = mid;
            }else if(guess(mid) > 0) {
                start = mid;
            }else{
                return mid;
            }
        }

        if (guess(start) == 0) {
            return start;
        } else {
            return end;
        }

    }
}
```
