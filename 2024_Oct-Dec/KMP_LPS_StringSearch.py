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

sol = Solution()
pat = 'geeksforgeeks'
txt = 'geeksforgeekssjfhisbcugeeksforgeekssfjakncsuigeeksforgeeksforgeeksforgeeksafejepngeggeeksforgeeks'
print(sol.search(pat, txt))