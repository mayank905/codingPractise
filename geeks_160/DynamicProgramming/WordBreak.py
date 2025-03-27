'''
You are given a string s and a list dictionary[] of words. Your task is to determine whether the string s can be formed by concatenating one or more words from the dictionary[].

Note: From dictionary[], any word can be taken any number of times and in any order.

Examples :

Input: s = "ilike", dictionary[] = ["i", "like", "gfg"]
Output: true
Explanation: s can be breakdown as "i like".
Input: s = "ilikegfg", dictionary[] = ["i", "like", "man", "india", "gfg"]
Output: true
Explanation: s can be breakdown as "i like gfg".
Input: s = "ilikemangoes", dictionary[] = ["i", "like", "man", "india", "gfg"]
Output: false
Explanation: s cannot be formed using dictionary[] words.
Constraints:
1 ≤ s.size() ≤ 3000
1 ≤ dictionary.size() ≤ 1000
1 ≤ dictionary[i].size() ≤ 100
'''
#My Solution using top-down approach
'''class Solution:
    def wordBreak(self, s, dictionary):
        # code here
        set1=set()
        def dp(index):
            if index in set1:
                return True
            if index==len(s):
                return True
            for word in dictionary:
                len1=len(word)
                if s[index:index+len1]==word:
                    if dp(index+len1):
                        set1.add(index)
                        return True
            return False
        return dp(0)'''
#Bottom-up approach using set as data structure
'''class Solution:
    def wordBreak(self, s, dictionary):
        # Convert the dictionary to a set for O(1) lookups
        word_set = set(dictionary)
        n = len(s)

        # dp[i] represents whether the substring s[0:i] can be segmented into words from the dictionary
        dp = [False] * (n + 1)
        dp[0] = True  # Base case: An empty string can always be segmented

        # Fill the dp array
        for i in range(1, n + 1):
            for j in range(i):
                # Check if s[j:i] is in the dictionary and dp[j] is True
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[n]
class Solution:
    def wordBreak(self, s, dictionary):
        # Convert the dictionary to a set for O(1) lookups
        word_set = set(dictionary)
        n = len(s)

        # dp[i] represents whether the substring s[0:i] can be segmented into words from the dictionary
        dp = [False] * (n + 1)
        dp[0] = True  # Base case: An empty string can always be segmented

        set2=set()
        set2.add(0)
        # Fill the dp array
        for i in range(1, n + 1):
            for j in set2:
                # Check if s[j:i] is in the dictionary and dp[j] is True
                if s[j:i] in word_set:
                    dp[i] = True
                    set2.add(i)
                    break

        return dp[n]'''
#Bottom-up approach using Trie data structure
'''class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search_prefix(self, s, start):
        node = self.root
        for i in range(start, len(s)):
            if s[i] not in node.children:
                return []
            node = node.children[s[i]]
            if node.is_end_of_word:
                yield i + 1

class Solution:
    def wordBreak(self, s, dictionary):
        # Build a Trie from the dictionary
        trie = Trie()
        for word in dictionary:
            trie.insert(word)

        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True  # Base case: An empty string can always be segmented

        # Fill the dp array
        for i in range(n):
            if dp[i]:
                for end in trie.search_prefix(s, i):
                    dp[end] = True

        return dp[n]'''
class TrieNode:
    def __init__(self):
        self.children={}
        self.is_end=False
        
class Trie:
    def __init__(self):
        self.root=TrieNode()
        
    def insert(self,word):
        node=self.root
        for char in word:
            if char not in node.children:
                node.children[char]=TrieNode()
            node=node.children[char]
        node.is_end=True
        
    def search_prefix(self,s,start):
        node=self.root
        for i in range(start,len(s)):
            if s[i] not in node.children:
                return []
            node=node.children[s[i]]
            if node.is_end:
                yield i+1
        
class Solution:
    def wordBreak(self, s, dictionary):
        # code here
        trie=Trie()
        for word in dictionary:
            trie.insert(word)
        n=len(s)
        dp=[False]*(n+1)
        dp[0]=True
        for i in range(n):
            if dp[i]:
                for end in trie.search_prefix(s,i):
                    dp[end]=True
        return dp[n]
# #{ 
#  # Driver Code Starts
# if __name__ == '__main__':
#     test_case = int(input())

#     for _ in range(test_case):
#         s = input().strip()
#         dictionary = input().strip().split()
#         ob = Solution()
#         res = ob.wordBreak(s, dictionary)
#         if res:
#             print("true")
#         else:
#             print("false")
#         print("~")
# # } Driver Code Ends
sol=Solution()
s='ilike'
dictionary=["i", "like", "gfg"]
print(sol.wordBreak(s,dictionary)) #True