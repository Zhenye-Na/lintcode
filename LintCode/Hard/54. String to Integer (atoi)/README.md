# 54. String to Integer (atoi)
Description
Implement function atoi to convert a string to an integer.
If no valid conversion could be performed, a zero value is returned.
If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.

Example

```
"10" => 10
"-1" => -1
"123123123123123" => 2147483647
"1.0" => 1
```


## Solution

Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.

Requirements for atoi:
The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of representable values, `INT_MAX (2147483647)` or `INT_MIN (-2147483648)` is returned.

```java
public class Solution {
    /**
     * @param str: A string
     * @return: An integer
     */
    public int atoi(String str) {
        // write your code here
        if(str == null) {
            return 0;
        }
        str = str.trim();
        if (str.length() == 0) {
            return 0;
        }

        char first = str.charAt(0);
        int length = str.length(), index = 0, sign = 1, num;
        if (first == '-') {
            sign = -1;
            index++;
        } else if (first == '+') {
            index++;
        }

        long result = 0;
        for (int i = index; i < length; i++) {
            if (str.charAt(i) - '0' > 9 || str.charAt(i) - '0' < 0) {
                break;
            }
            num = str.charAt(i) - '0';
            result = result * 10 + num;
            if (sign * result >= Integer.MAX_VALUE || sign * result <= Integer.MIN_VALUE) {
                break;
            }
        }


        if (sign * result >= Integer.MAX_VALUE) {
            return Integer.MAX_VALUE;
        } else if (sign * result <= Integer.MIN_VALUE) {
            return Integer.MIN_VALUE;
        } else {
            return (int) (sign * result);
        }

    }
}
```

```java
/**
* 本参考程序来自九章算法，由 @S同学 提供。版权所有，转发请注明出处。
* - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
* - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
* - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
* - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code
*/

public class Solution {
    /**
     * @param str: A string
     * @return: An integer
     */
    public int atoi(String str) {
        // write your code here
        boolean isPos = true;
        char[] sc = (str.trim() + " ").toCharArray();
        int i = 0;

        if (sc[0] == '-') {
            isPos = false;
            i++;
        } else if (sc[0] == '+') {
            isPos = true;
            i++;
        }

        long value = 0;

        while (i < sc.length && Character.isDigit(sc[i])) {
            value = value * 10 + (sc[i] - '0');
            i++;

            if (value > Integer.MAX_VALUE) {
                return isPos ? Integer.MAX_VALUE : Integer.MIN_VALUE;
            }
        }


        value = isPos ? value : -value;

        return (int) value;
    }
}
```
