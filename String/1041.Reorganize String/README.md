1041. Reorganize String
Description
中文
English
Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

If possible, output any possible result. If not possible, return the empty string.

S will consist of lowercase letters and have length in range [1, 500].

Have you met this question in a real interview?  
Example
Example 1:

Input: S = "aab"
Output: "aba"
Example 2:

Input: S = "aaab"
Output: ""


先统计每个字母出现的数，如果有一个超过一半了，直接返回空；不然进行交错排列即可



