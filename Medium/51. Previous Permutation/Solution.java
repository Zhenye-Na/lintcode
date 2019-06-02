boolean previousPermutation(int[] array) {
    // Find longest non-decreasing suffix
    int i = array.length - 1;
    while (i > 0 && array[i - 1] <= array[i])
        i--;
    // Now i is the head index of the suffix

    // Are we at the first permutation already?
    if (i <= 0)
        return false;

    // Let array[i - 1] be the pivot
    // Find rightmost element that is below the pivot
    int j = array.length - 1;
    while (array[j] >= array[i - 1])
        j--;
    // Now the value array[j] will become the new pivot
    // Assertion: j >= i

    // Swap the pivot with j
    int temp = array[i - 1];
    array[i - 1] = array[j];
    array[j] = temp;

    // Reverse the suffix
    j = array.length - 1;
    while (i < j) {
        temp = array[i];
        array[i] = array[j];
        array[j] = temp;
        i++;
        j--;
    }

    // Successfully computed the previous permutation
    return true;
}
