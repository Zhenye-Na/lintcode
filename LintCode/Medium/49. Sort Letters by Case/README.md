# 49. Sort Letters by Case

- **Description**
    - Given a string which contains only letters. Sort it by lower case first and upper case second.
    - It's **NOT** necessary to keep the original order of lower-case letters and upper case letters.
- **Example**
    - For `"abAcD"`, a reasonable answer is `"acbAD"`
- **Challenge**
    - Do it in one-pass and in-place.


## Solution


```java
public class Solution {
    /*
     * @param chars: The letter array you should sort by Case
     * @return: nothing
     */
    public void sortLetters(char[] chars) {
        // write your code here
        if (chars == null || chars.length == 0) {
            return;
        }

        int left = 0, right = chars.length - 1;

        while (left < right) {
            while (left < right && isLowercase(chars[left])) {
                left++;
            }

            while (left < right && !isLowercase(chars[right])) {
                right--;
            }

            if (left < right) {
                char temp = chars[left];
                chars[left] = chars[right];
                chars[right] = temp;
            }
        }
    }

    private boolean isLowercase(char character) {
        if (character >= 'a' && character <= 'z') {
            return true;
        }
        return false;
    }

}
```



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
     *@param chars: The letter array you should sort by Case
     *@return: void
     */
    public void sortLetters(char[] chars) {
        int i = 0, j = chars.length - 1;
    	char tmp ;
		while ( i <= j) {
			while (i <= j && Character.isLowerCase(chars[i]) ) i++;
			while (i <= j && Character.isUpperCase(chars[j]) ) j--;
			if (i <= j) {
				tmp = chars[i];
				chars[i] = chars[j];
				chars[j] = tmp;
				i++; j--;
			}
		}
        //write your code here
		return ;
    }
}
```