public class Solution {
    /**
     * @param L: Given n pieces of wood with length L[i]
     * @param k: An integer
     * @return: The maximum length of the small pieces
     */
    public int woodCut(int[] L, int k) {
        // write your code here
        if (L == null || L.length == 0) return 0;

        Arrays.sort(L);
        
        if (k == 0) return L[L.length - 1];
        
        int end = L[L.length - 1], start = 1;
        
        while (start + 1 < end) {
            
            int mid = (end - start) / 2 + start;
            int num = 0;

            for (int l : L) {
                num += (l / mid);

            }

            if (num >= k) {
                start = mid;
            } else if (num < k) {
                end = mid;
            }

        }
        
        int num = 0;
        int num2 = 0;
        for (int l : L) {
            num += (l / end);
            num2 += (l / start);
        }
        if (num >= k) {
            return end;
        } else if (num2 >= k) {
            return start;
        } else {
            return 0;
        }
        
    }
}