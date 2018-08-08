# 548. Intersection of Two Arrays II
Description
Given two arrays, write a function to compute their intersection.

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.

Example
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Challenge
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to num2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?


## Solution

### HashMap

#### HashMap solution 1

```java
public class Solution {
    /**
     * @param nums1: an integer array
     * @param nums2: an integer array
     * @return: an integer array
     */
    public int[] intersection(int[] nums1, int[] nums2) {
        // write your code here
        if (nums1 == null || nums2 == null || nums1.length == 0 || nums2.length == 0) {
            return new int[0];
        }

        int length1 = nums1.length, length2 = nums2.length;
        Map<Integer, Integer> map1 = new HashMap<>();
        Map<Integer, Integer> map2 = new HashMap<>();
        List<Integer> result = new ArrayList<>();

        for (int i = 0; i < length1; i++) {
            if (!map1.containsKey(nums1[i])) {
                map1.put( nums1[i], 1 );
            } else {
                map1.put( nums1[i], map1.get(nums1[i]) + 1 );
            }
        }

        for (int j = 0; j < length2; j++) {
            if (!map2.containsKey(nums2[j])) {
                map2.put( nums2[j], 1 );
            } else {
                map2.put( nums2[j], map2.get(nums2[j]) + 1 );
            }
        }

        for (Integer num : map1.keySet()) {
            if (map2.containsKey(num)) {
                int k = Math.min( map2.get(num), map1.get(num) );
                for (int j = 0; j < k; j++) {
                    result.add(num);
                }
            }
        }

        int[] res = new int[result.size()];

        for (int index = 0; index < result.size(); index++) {
            res[index] = result.get(index);
        }

        return res;
    }
}
```

#### HashMap solution 1

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
     * @param nums1 an integer array
     * @param nums2 an integer array
     * @return an integer array
     */
    public int[] intersection(int[] nums1, int[] nums2) {
        // Write your code here
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        for(int i = 0; i < nums1.length; ++i) {
            if (map.containsKey(nums1[i]))
                map.put(nums1[i], map.get(nums1[i]) + 1);
            else
                map.put(nums1[i], 1);
        }

        List<Integer> results = new ArrayList<Integer>();

        for (int i = 0; i < nums2.length; ++i)
            if (map.containsKey(nums2[i]) && map.get(nums2[i]) > 0) {
                results.add(nums2[i]);
                map.put(nums2[i], map.get(nums2[i]) - 1);
            }

        int result[] = new int[results.size()];
        for(int i = 0; i < results.size(); ++i)
            result[i] = results.get(i);

        return result;
    }
}
```

### Binary Search

```java
public int[] intersect(int[] nums1, int[] nums2) {
    Arrays.sort(nums1);
    Arrays.sort(nums2);
    List<Integer> list = new ArrayList<>();
    for (int i = 0, idx1 = 0, idx2 = 0; i < nums1.length; ) {
        int count1 = 0;
        while (idx1 < nums1.length && nums1[idx1] == nums1[i]) {
            idx1++;
            count1++;
        }

        idx2 = firstGE(nums2, nums1[i], idx2, nums2.length);
        int count2 = 0;
        while (idx2 < nums2.length && nums2[idx2] == nums1[i]) {
            idx2++;
            count2++;
        }

        int count = Math.min(count1, count2);
        for (int k = 0; k < count; k++) list.add(nums1[i]);

        i = idx1;
    }

    int[] res = new int[list.size()];
    int i = 0;
    for (int d : list) res[i++] = d;
    return res;
}

private int firstGE(int[] nums, int target, int lo, int hi) {
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if (nums[mid] < target)
            lo = mid + 1;
        else
            hi = mid;
    }
    return lo;
}
```
