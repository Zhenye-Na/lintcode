import java.util.Set;
import java.util.HashSet;

public class Solution {
    
    /*
     * @param nums1: an integer array
     * @param nums2: an integer array
     * @return: an integer array
     */
    public int[] intersection(int[] nums1, int[] nums2) {
        // write your code here
        if (nums1 == null && nums2 == null) return null;
        
        Set<Integer> s1 = new HashSet<>();
        for (int i = 0; i < nums1.length; i++) {
            s1.add(nums1[i]);
        }
        
        Set<Integer> result = new HashSet<>();
        for (int j = 0; j < nums2.length; j++) {
            if (s1.contains(nums2[j]) && !result.contains(nums2[j])) {
                result.add(nums2[j]);
            }
        }
        
        int[] num = new int[result.size()];
        int index = 0;
        for (Integer nums : result) {
            num[index++] = nums;
        }
        

        return num;

    }
    
}