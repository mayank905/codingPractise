'''
Given an array of strings, return all groups of strings that are anagrams. The groups must be created in order of their appearance in the original array. Look at the sample case for clarification.

Note: The final output will be in lexicographic order.

Examples:

Input: arr[] = ["act", "god", "cat", "dog", "tac"]
Output: [["act", "cat", "tac"], ["god", "dog"]]
Explanation: There are 2 groups of anagrams "god", "dog" make group 1. "act", "cat", "tac" make group 2.
Input: arr[] = ["no", "on", "is"]
Output: [["is"], ["no", "on"]]
Explanation: There are 2 groups of anagrams "is" makes group 1. "no", "on" make group 2.
Input: arr[] = ["listen", "silent", "enlist", "abc", "cab", "bac", "rat", "tar", "art"]
Output: [["abc", "cab", "bac"], ["listen", "silent", "enlist"], ["rat", "tar", "art"]]
Explanation: 
Group 1: "abc", "bac", and "cab" are anagrams.
Group 2: "listen", "silent", and "enlist" are anagrams.
Group 3: "rat", "tar", and "art" are anagrams.
Constraints:
1<= arr.size() <=100
1<= arr[i].size() <=10
'''
from collections import defaultdict


class Solution:

    def anagrams(self, arr):
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''

        #code here
        result=[]
        dict1=defaultdict(list) 
        for str in arr:
            std="".join(sorted(str))
            dict1[std].append(str)
        for key in dict1:
            result.append(dict1[key])
        result.sort()
        

        return result
sol=Solution()
arr=["act", "god", "cat", "dog", "tac"]
arr=["no", "on", "is"]
arr=["listen", "silent", "enlist", "abc", "cab", "bac", "rat", "tar", "art"]
arr=['zov', 'qvdy', 'rmyq', 'qvf', 'hnw', 'cbigl', 'l', 'xogk', 'er', 'rbbt']
print(sol.anagrams(arr)) # [["act", "cat", "tac"], ["god", "dog"]]