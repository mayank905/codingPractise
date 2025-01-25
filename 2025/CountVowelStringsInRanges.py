'''
You are given a 0-indexed array of strings words and a 2D array of integers queries.

Each query queries[i] = [li, ri] asks us to find the number of strings present in the range li to ri (both inclusive) of words that start and end with a vowel.

Return an array ans of size queries.length, where ans[i] is the answer to the ith query.

Note that the vowel letters are 'a', 'e', 'i', 'o', and 'u'.

 

Example 1:

Input: words = ["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]]
Output: [2,3,0]
Explanation: The strings starting and ending with a vowel are "aba", "ece", "aa" and "e".
The answer to the query [0,2] is 2 (strings "aba" and "ece").
to query [1,4] is 3 (strings "ece", "aa", "e").
to query [1,1] is 0.
We return [2,3,0].
Example 2:

Input: words = ["a","e","i"], queries = [[0,2],[0,1],[2,2]]
Output: [3,2,1]
Explanation: Every string satisfies the conditions, so we return [3,2,1].
 

Constraints:

1 <= words.length <= 105
1 <= words[i].length <= 40
words[i] consists only of lowercase English letters.
sum(words[i].length) <= 3 * 105
1 <= queries.length <= 105
0 <= li <= ri < words.length
'''
from typing import List


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowel=[]
        def isvowel(ch):
            return ch in "aeiou"
        for i in range(len(words)):
            st=words[i]
            if isvowel(st[0]) and isvowel(st[-1]):
                vowel.append(1)
            else:
                vowel.append(0)
        prev=vowel[0]
        for i in range(1,len(vowel)):
            vowel[i]+=prev
            prev=vowel[i]
        result=[]
        for i in range(len(queries)):
            l,r=queries[i]
            if l==0:
                result.append(vowel[r])
            else:
                result.append(vowel[r]-vowel[l-1])
        return result
sol=Solution()
words=["aba","bcb","ece","aa","e"]
words=["a","e","i"]
queries=[[0,2],[1,4],[1,1]]
queries=[[0,2],[0,1],[2,2]]
print(sol.vowelStrings(words,queries))#[2,3,0]