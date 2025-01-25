'''
Given two strings, one is a text string txt and the other is a pattern string pat. The task is to print the indexes of all the occurrences of the pattern string in the text string. Use 0-based indexing while returning the indices. 
Note: Return an empty list in case of no occurrences of pattern.

Examples :

Input: txt = "abcab", pat = "ab"
Output: [0, 3]
Explanation: The string "ab" occurs twice in txt, one starts at index 0 and the other at index 3. 
Input: txt = "abesdu", pat = "edu"
Output: []
Explanation: There's no substring "edu" present in txt.
Input: txt = "aabaacaadaabaaba", pat = "aaba"
Output: [0, 9, 12]
Explanation:

Constraints:
1 ≤ txt.size() ≤ 106
1 ≤ pat.size() < txt.size()
Both the strings consist of lowercase English alphabets.
'''
class Solution:
    def search(self, pat, txt):
        def computeLPSArray(pat, M, lps):
            length = 0
            lps[0] = 0
            i = 1
            while i < M:
                if pat[i] == pat[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1

        result = []
        M = len(pat)
        N = len(txt)
        lps = [0] * M
        j = 0
        computeLPSArray(pat, M, lps)
        i = 0
        while i < N:
            if pat[j] == txt[i]:
                i += 1
                j += 1
            if j == M:
                result.append(i - j)
                j = lps[j - 1]
            elif i < N and pat[j] != txt[i]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return result
            