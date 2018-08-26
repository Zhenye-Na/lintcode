# 184. Largest Number

**Description**
Given a list of non negative integers, arrange them such that they form the largest number.
The result may be very large, so you need to return a string instead of an integer.
**Example**
Given [1, 20, 23, 4, 8], the largest formed number is 8423201.
**Challenge**
Do it in `O(nlogn)` time complexity.


## Solution

The idea here is basically implement a String comparator to decide which String should come first during concatenation. Because when you have 2 numbers (let's convert them into String), you'll face only 2 cases:

For example:

```java
String s1 = "9";
String s2 = "31";

String case1 = s1 + s2;  // 931
String case2 = s2 + s1;  // 319
```

Apparently, **case1** is greater than **case2** in terms of value.

So, we should always put `s1` in front of `s2`.


```java
public class Solution {
    /**
     * @param nums: A list of non negative integers
     * @return: A string
     */
    public String largestNumber(int[] num) {
        // write your code here
		if (num == null || num.length == 0)
		    return "";

		// Convert int array to String array, so we can sort later on
		String[] s_num = new String[num.length];
		for (int i = 0; i < num.length; i++) {
		    s_num[i] = String.valueOf(num[i]);
		}

		// Comparator to decide which string should come first in concatenation
		Comparator<String> comp = new Comparator<String>() {
		    @Override
		    public int compare(String str1, String str2) {
		        String s1 = str1 + str2;
    			  String s2 = str2 + str1;
    			  return s2.compareTo(s1); // reverse order here, so we can do append() later
		    }
    };

		Arrays.sort(s_num, comp);

    // An extreme edge case by lc, say you have only a bunch of 0 in your int array
    if (s_num[0].charAt(0) == '0') return "0";

		StringBuilder sb = new StringBuilder();
		for (String s: s_num) {
		    sb.append(s);
    }
		return sb.toString();
    }
}
```

In terms of Time and Space Complexity:
Let's assume:

```
the length of input array is n,
average length of Strings in s_num is k,
Then, compare 2 strings will take O(k).
Sorting will take O(nlgn)
Appending to StringBuilder takes O(n).
So total will be O(nklgnk) + O(n) = O(nklgnk).
```

Space is pretty straight forward: `O(n)`.
