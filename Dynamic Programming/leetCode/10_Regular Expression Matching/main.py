class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)

        dp = [[False]*(m+1) for _ in range(n+1)]

        dp[0][0] = True # index 0 means ""

        for k in range(2, m+1): # s = "", p = "x*" 
            if p[k-1] == '*': 
                dp[0][k] = dp[0][k-2]  

        for i in range(1,n+1): # Note dp[i][j] = s[:i] matches p[:j]; current chars are s[i-1], p[j-1]
            for j in range(1,m+1):
                if p[j-1] == '*': # p[j-2] = char, p[j-1] = *
                    # * not use -> depends on dp[i][j-2]
                    # * use -> check previous and current matching
                    dp[i][j] = dp[i][j-2] or dp[i-1][j] and (s[i-1] == p[j-2] or p[j-2] == '.') 
                else: 
                    # check previous and current matching
                    dp[i][j] = dp[i-1][j-1] and (s[i-1] == p[j-1] or p[j-1] == '.') 
        
        return dp[n][m]
