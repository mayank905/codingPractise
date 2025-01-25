'''
You are given a list of strings of the same length words and a string target.

Your task is to form target using the given words under the following rules:

target should be formed from left to right.
To form the ith character (0-indexed) of target, you can choose the kth character of the jth string in words if target[i] = words[j][k].
Once you use the kth character of the jth string of words, you can no longer use the xth character of any string in words where x <= k. In other words, all characters to the left of or at index k become unusuable for every string.
Repeat the process until you form the string target.
Notice that you can use multiple characters from the same string in words provided the conditions above are met.

Return the number of ways to form target from words. Since the answer may be too large, return it modulo 109 + 7.

 

Example 1:

Input: words = ["acca","bbbb","caca"], target = "aba"
Output: 6
Explanation: There are 6 ways to form target.
"aba" -> index 0 ("acca"), index 1 ("bbbb"), index 3 ("caca")
"aba" -> index 0 ("acca"), index 2 ("bbbb"), index 3 ("caca")
"aba" -> index 0 ("acca"), index 1 ("bbbb"), index 3 ("acca")
"aba" -> index 0 ("acca"), index 2 ("bbbb"), index 3 ("acca")
"aba" -> index 1 ("caca"), index 2 ("bbbb"), index 3 ("acca")
"aba" -> index 1 ("caca"), index 2 ("bbbb"), index 3 ("caca")
Example 2:

Input: words = ["abba","baab"], target = "bab"
Output: 4
Explanation: There are 4 ways to form target.
"bab" -> index 0 ("baab"), index 1 ("baab"), index 2 ("abba")
"bab" -> index 0 ("baab"), index 1 ("baab"), index 3 ("baab")
"bab" -> index 0 ("baab"), index 2 ("baab"), index 3 ("baab")
"bab" -> index 1 ("abba"), index 2 ("baab"), index 3 ("baab")
 

Constraints:

1 <= words.length <= 1000
1 <= words[i].length <= 1000
All strings in words have the same length.
1 <= target.length <= 1000
words[i] and target contain only lowercase English letters.
'''
from typing import List


class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        dp = [[-1] * len(target) for _ in range(len(words[0]))]
        char_frequency = [[0] * 26 for _ in range(len(words[0]))]

        for i in range(len(words)):
            for j in range(len(words[0])):
                character = ord(words[i][j]) - 97
                char_frequency[j][character] += 1
        return self.__get_words(words, target, 0, 0, dp, char_frequency)

    def __get_words(
        self, words, target, words_index, target_index, dp, char_frequency
    ):
        if target_index == len(target):
            return 1
        if (
            words_index == len(words[0])
            or len(words[0]) - words_index < len(target) - target_index
        ):
            return 0

        if dp[words_index][target_index] != -1:
            return dp[words_index][target_index]

        count_ways = 0
        cur_pos = ord(target[target_index]) - 97
        count_ways += self.__get_words(
            words, target, words_index + 1, target_index, dp, char_frequency
        )
        count_ways += char_frequency[words_index][cur_pos] * self.__get_words(
            words, target, words_index + 1, target_index + 1, dp, char_frequency
        )

        dp[words_index][target_index] = count_ways % 1000000007
        return dp[words_index][target_index]
