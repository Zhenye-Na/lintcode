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