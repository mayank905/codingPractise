'''
You are given a boolean expression s containing
    'T' ---> true
    'F' ---> false 
and following operators between symbols
   &   ---> boolean AND
    |   ---> boolean OR
   ^   ---> boolean XOR
Count the number of ways we can parenthesize the expression so that the value of expression evaluates to true.

Note: The answer is guaranteed to fit within a 32-bit integer.

Examples:

Input: s = "T|T&F^T"
Output: 4
Explaination: The expression evaluates to true in 4 ways: ((T|T)&(F^T)), (T|(T&(F^T))), (((T|T)&F)^T) and (T|((T&F)^T)).
Input: s = "T^F|F"
Output: 2
Explaination: The expression evaluates to true in 2 ways: ((T^F)|F) and (T^(F|F)).
Constraints:
1 ≤ |s| ≤ 100 
'''
'''
class Solution:
    def countWays(self, s):
        # code here
        length=len(s)
        # count=0
        dp=[[0 for _ in range(length)]for _ in range(length)]
        op={'&':lambda x,y:x and y,
            '|':lambda x,y:x or y,
            '^':lambda x,y:x ^ y}
        for i in range(length):
            dp[i][i] = 1 if s[i] == 'T' else 0
        for gap in range(1,length,2):
            for i in range(0,length-gap,2):
                j=i+gap+1
                for k in range(i+1,j,2):
                    dp[i][j]=op[s[k]](dp[i][k-1],dp[k+1][j])
                    bol=dp[i][j]
                    if i>0:
                        bol=bol and dp[0][i]
                    if j<length-1:
                        bol=bol and dp[j][length-1]
                    dp[0][length-1]+=bol
                # count+=dp[i][j]
        return dp[0][length-1]
'''
class Solution:
    def countWays(self, s):
        MOD = 10**9 + 7
        n = len(s)
        memo = {}

        def solve(i, j, isTrue):
            # Base case
            if i > j:
                return 0
            if i == j:
                if isTrue:
                    return 1 if s[i] == 'T' else 0
                else:
                    return 1 if s[i] == 'F' else 0

            # Check if the result is already computed
            if (i, j, isTrue) in memo:
                return memo[(i, j, isTrue)]

            # Initialize the count
            ways = 0

            # Partition the expression at every operator
            for k in range(i + 1, j, 2):
                operator = s[k]

                # Solve for left and right parts
                leftTrue = solve(i, k - 1, True)
                leftFalse = solve(i, k - 1, False)
                rightTrue = solve(k + 1, j, True)
                rightFalse = solve(k + 1, j, False)

                # Calculate the number of ways based on the operator
                if operator == '&':
                    if isTrue:
                        ways += leftTrue * rightTrue
                    else:
                        ways += leftTrue * rightFalse + leftFalse * rightTrue + leftFalse * rightFalse
                elif operator == '|':
                    if isTrue:
                        ways += leftTrue * rightTrue + leftTrue * rightFalse + leftFalse * rightTrue
                    else:
                        ways += leftFalse * rightFalse
                elif operator == '^':
                    if isTrue:
                        ways += leftTrue * rightFalse + leftFalse * rightTrue
                    else:
                        ways += leftTrue * rightTrue + leftFalse * rightFalse

                ways %= MOD

            # Store the result in the memo dictionary
            memo[(i, j, isTrue)] = ways
            return ways

        # Solve for the entire expression to evaluate to True
        return solve(0, n - 1, True)
    
sol=Solution()
s="T|T&F^T"
# s="T^F|F"
# s='T^T|F^F'
# s='T&T^F|T'
print(sol.countWays(s))
'''
        for gap in range(1, length):
            for i in range(length - gap):
                j = i + gap
                dp[i][j] = 0
                for k in range(i + 1, j, 2):
                    left_true = dp[i][k - 1]
                    left_false = (k - i) // 2 - left_true
                    right_true = dp[k + 1][j]
                    right_false = (j - k) // 2 - right_true

                    if s[k] == '&':
                        dp[i][j] += left_true * right_true
                    elif s[k] == '|':
                        dp[i][j] += left_true * right_true + left_true * right_false + left_false * right_true
                    elif s[k] == '^':
                        dp[i][j] += left_true * right_false + left_false * right_true
        return dp[0][length - 1]
'''