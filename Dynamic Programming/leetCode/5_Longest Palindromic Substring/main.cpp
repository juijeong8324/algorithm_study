class Solution {
public:
    string longestPalindrome(string s) {
        int N = s.size();
        int d[1000][1000] = {0,};

        int a = 0, b = 0;
        for(int r=0; r<N; r++){
            for(int l=0; l < r; l++){
                if(r-l <= 2){ // 수정한 부분 
                    d[l][r] = (s[r] == s[l]);
                }
                else{ // length = 3 over
                    d[l][r] = (s[r] == s[l]) && (d[l+1][r-1]);
                }

                if((b-a < r-l) && (d[l][r])){
                    a = l; b = r;
                }
            }
        }

        string ans = s.substr(a,b-a+1);

        return ans;
    }
};