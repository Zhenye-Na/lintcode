/**
 * @param s: a string
 * @return: an integer
 */
 func lengthOfLongestSubstring (s string) int {
    // write your code here
    lastOccurred := make(map[byte]int)
    start := 0
    maxLength := 0

    for idx, ch := range []byte(s) {
        if lastIdx, err := lastOccurred[ch]; err && lastIdx >= start {
            start = lastIdx + 1
        }
        if idx - start + 1 > maxLength {
            maxLength = idx - start + 1
        }
        lastOccurred[ch] = idx
    }
    return maxLength
}
