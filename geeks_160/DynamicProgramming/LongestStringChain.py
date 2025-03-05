'''
You are given an array of words where each word consists of lowercase English letters.
wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA without changing the order of the other characters to make it equal to wordB. For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".

A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, where word1 is a predecessor of word2, word2 is a predecessor of word3, and so on. A single word is trivially a word chain with k = 1.

Return the length of the longest possible word chain with words chosen from the given list of words in any order.

Examples:

Input: words[] = ["ba", "b", "a", "bca", "bda", "bdca"]
Output: 4
Explanation: One of the longest word chains is ["a", "ba", "bda", "bdca"].
Input: words[] = ["abc", "a", "ab"]
Output: 3
Explanation: The longest chain is {"a", "ab" "abc"}
Input: words[] = ["abcd", "dbqca"]
Output: 1
Explanation: The trivial word chain ["abcd"] is one of the longest word chains.
Constraint:
1 <= words.length <= 104
1 <= words[i].length <= 10
 words[i] only consists of lowercase English letters.
'''
class Solution:
    def longestStringChain(self, words):
        # Code here
        global val
        val=1
        visited=dict()
        def dp(st,length):
            global val
            if st in visited and visited[st]>length:
                return
            visited[st]=length
            val=max(val,length)
            for i in range(len(st)):
                cur=st[:i]+st[i+1:]
                if cur in words1:
                    dp(cur,length+1)
            
        words.sort(key=len,reverse=True)
        words1=set(words)
        for i in range(len(words)):
            dp(words[i],1)
        return val
sol=Solution()
with open('geeks_160/DynamicProgramming/fileInput.txt', 'r') as file:
    words = file.read().split()

print(sol.longestStringChain(words))