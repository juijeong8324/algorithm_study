# Input
# s = input string (1~20, only lowercase letters)
# p = pattern (1~20)
# '.': Matches any single character
# '*': Matches zero or more of the preceding element
# Output
# The matching should cover the entire input string (not partial)!
# Note) Guarantee.. x is valid character in 'x*' 
# Hint
# dp[i][j]: s의 i번째 까지와 p의 j번째까지 패턴이 맞는지 여부 
# Why DP?
# 이전까

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)

        dp = [[False]*(m+1) for _ in range(n+1)]

        dp[0][0] = True # index 0 means ""

        for k in range(2, m+1): # s = "", p 'x*' 
            if p[k-1] == '*': 
                dp[0][k] = dp[0][k-2] # It is ok zero! 

        for i in range(1,n+1): # Note dp[i][j] = s[i-1]p[j-1]
            for j in range(1,m+1):
                if p[j-1] == '*':
                    # * 사용 안 함: dp[i][j-2]
                    # * 사용: 이전 문자와 매칭되면 dp[i-1][j] 확인
                    dp[i][j] = dp[i][j-2] or dp[i-1][j] and (s[i-1] == p[j-2] or p[j-2] == '.') 
                    # 이전까지 and s의 i번째와 p의 j-1번째 문자 일치 여부 혹은 p[j-2]가 any
                    # 여기서의 이전은 *가 사용되었다는 가정 하에 이전임
                    # 아 그러니까... *를 사용했다 가정하면 이전에도 사용이 되어야 하는거구나?!
                else: 
                    dp[i][j] = dp[i-1][j-1] and (s[i-1] == p[j-1] or p[j-1] == '.') # 이전까지 and (현재 위치 같아야 함 or any)
        
        return dp[n][m]
