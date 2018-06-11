/**
 * Created by Zhenye Na on Jun, 2018
 */


// First trial 755 ms
public class Solution {
    /**
     * @param number: A 3-digit number.
     * @return: Reversed number.
     */
    public int reverseInteger(int number) {
        // write your code here
        int r = number % 10;
        int l = number / 100;
        int m = (number - (l * 100 + r)) / 10;

        return 100 * r + 10 * m + l;
    }
}


// Second trial 755 ms
public class Solution {
    /**
     * @param number: A 3-digit number.
     * @return: Reversed number.
     */
    public int reverseInteger(int number) {
        // write your code here
        int result = 0;
        int count = 0;
        while (number > 0) {
            int digit = number % 10;
            result += Math.pow(10, 2 - count) * digit;
            number = (number - digit) / 10;
            count ++;
        }
        return result;
    }
}


// Third trial 762 ms
public class Solution {
    /**
     * @param number: A 3-digit number.
     * @return: Reversed number.
     */
    public int reverseInteger(int number) {
        // write your code here
        int reversedNum = 0;

        while (number != 0) {
            reversedNum = reversedNum * 10 + number % 10;
            number = number / 10;
        }
        
        return reversedNum;
    }
}


// Weird trial 755 ms
public class Solution {
    /**
     * @param number: A 3-digit number.
     * @return: Reversed number.
     */
    public int reverseInteger(int number) {
        // write your code here
        int[] iarray = new int[3];
        for (int index = 0; index < len; index++) {
            iarray[index] = number % 10;
            number /= 10;
        }

        Collections.reverse(Ints.asList(iarray));

        int result;
        for( int temp=0; temp < 3; temp++){
          result *= 10;
          result += iarray[temp];
        }

        return result;
    }
}

