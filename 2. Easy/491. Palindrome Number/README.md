# 491. Palindrome Number

- **Description**
    - Check a **positive number** is a palindrome or not.
    - A palindrome number is that if you reverse the whole number you will get exactly the same number.
    - It's guaranteed the input number is a **32-bit integer**, but after reversion, the number may exceed the **32-bit integer**.
- **Example**
    - `11`, `121`, `1`, `12321` are palindrome numbers.
    - `23`, `32`, `1232` are not palindrome numbers.

## Solution

```python
class Solution:
    """
    @param num: a positive number
    @return: true if it's a palindrome or false
    """
    def isPalindrome(self, num):
        # write your code here
        if num / 10 == 0:
            return True

        numString = str(num)
        start, end = 0, len(numString) - 1
        while start < end:
            if numString[start] != numString[end]:
                return False
            start += 1
            end -= 1

        return True

```
