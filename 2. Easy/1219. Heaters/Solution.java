public class Solution {
    /**
     * @param houses: positions of houses
     * @param heaters: positions of heaters
     * @return: the minimum radius standard of heaters
     */
    public int findRadius(int[] houses, int[] heaters) {
        // Write your code here
        Arrays.sort(houses);
        Arrays.sort(heaters);

        int i = 0;
        int radius = 0;

        for (int house : houses) {
            while (i < heaters.length - 1 && heaters[i] + heaters[i + 1] <= house * 2) {
                i++;
            }
            radius = Math.max(radius, Math.abs(heaters[i] - house));
        }
        return radius;

    }


}