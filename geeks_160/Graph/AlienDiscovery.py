'''
A new alien language uses the English alphabet, but the order of letters is unknown. You are given a list of words[] from the alien language’s dictionary, where the words are claimed to be sorted lexicographically according to the language’s rules.

Your task is to determine the correct order of letters in this alien language based on the given words. If the order is valid, return a string containing the unique letters in lexicographically increasing order as per the new language's rules. If there are multiple valid orders, return any one of them.

However, if the given arrangement of words is inconsistent with any possible letter ordering, return an empty string ("").

A string a is lexicographically smaller than a string b if, at the first position where they differ, the character in a appears earlier in the alien language than the corresponding character in b. If all characters in the shorter word match the beginning of the longer word, the shorter word is considered smaller.

Note: Your implementation will be tested using a driver code. It will print true if your returned order correctly follows the alien language’s lexicographic rules; otherwise, it will print false.

Examples:

Input: words[] = ["baa", "abcd", "abca", "cab", "cad"]
Output: true
Explanation: A possible corrct order of letters in the alien dictionary is "bdac".
The pair "baa" and "abcd" suggests 'b' appears before 'a' in the alien dictionary.
The pair "abcd" and "abca" suggests 'd' appears before 'a' in the alien dictionary.
The pair "abca" and "cab" suggests 'a' appears before 'c' in the alien dictionary.
The pair "cab" and "cad" suggests 'b' appears before 'd' in the alien dictionary.
So, 'b' → 'd' → 'a' → 'c' is a valid ordering.
Input: words[] = ["caa", "aaa", "aab"]
Output: true
Explanation: A possible corrct order of letters in the alien dictionary is "cab".
The pair "caa" and "aaa" suggests 'c' appears before 'a'.
The pair "aaa" and "aab" suggests 'a' appear before 'b' in the alien dictionary. 
So, 'c' → 'a' → 'b' is a valid ordering.
Input: words[] = ["ab", "cd", "ef", "ad"]
Output: ""
Explanation: No valid ordering of letters is possible.
The pair "ab" and "ef" suggests "a" appears before "e".
The pair "ef" and "ad" suggests "e" appears before "a", which contradicts the ordering rules.
Constraints:
1 ≤ words.length ≤ 500
1 ≤ words[i].length ≤ 100
words[i] consists only of lowercase English letters.
'''
class Solution:
    def findOrder(self,words):
        # code here
        graph = {}
        indegree = {}
        for word in words:
            for char in word:
                if char not in graph:
                    graph[char] = []
                    indegree[char] = 0
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            min_length = min(len(word1), len(word2))
            bol=False
            for j in range(min_length):
                if word1[j] != word2[j]:
                    graph[word1[j]].append(word2[j])
                    indegree[word2[j]] += 1
                    break
            if not bol and len(word1)>len(word2):
                return ""
        queue = []
        for char in indegree:
            if indegree[char] == 0:
                queue.append(char)
        order = ""
        while queue:
            current = queue.pop(0)
            order += current
            for neighbor in graph[current]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        if len(order) != len(indegree):
            return ""
        return order
sol = Solution()
# words=["baa", "abcd", "abca", "cab", "cad"]
# print(sol.findOrder(words)) # bdac
# words=["caa", "aaa", "aab"]
# print(sol.findOrder(words)) # cab
# words=["ab", "cd", "ef", "ad"]
# print(sol.findOrder(words)) # ""
words=["abc", "ab"]
print(sol.findOrder(words)) # ""
