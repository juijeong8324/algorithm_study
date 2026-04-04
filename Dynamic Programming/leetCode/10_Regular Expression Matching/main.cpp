class Solution {
public:
    bool isMatch(string s, string p) {
        int N = s.length();
        int M = p.length();
        vector<vector<bool>> dp(N+1, vector<bool>(M+1, false));

        // s=""에 대해서 초기화 
        dp[0][0] = true;
        for(int k = 2; k <= M; k++){
            if(p[k-1] == '*'){
                dp[0][k] = dp[0][k-2];
            }
        }

        //dp
        for(int i=1; i <= N; i++){
            for(int j=1; j<=M; j++){
                if(p[j-1] == '*'){
                    dp[i][j] = dp[i][j-2] || (dp[i-1][j] && (s[i-1] == p[j-2] || p[j-2] == '.'));
                }
                else{
                    dp[i][j] = dp[i-1][j-1] && (s[i-1] == p[j-1] || p[j-1] == '.');
                }

            }
        }

        return dp[N][M];
    }
};