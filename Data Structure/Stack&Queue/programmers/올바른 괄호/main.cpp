#include<bits/stdc++.h>

using namespace std;

bool solution(string s)
{
    bool answer = true;
    vector<int> st;
    
    for(auto c : s){
        if(c == '('){
            st.push_back(1);
        }
        else{
            if(st.empty()){
                return false;
            }
            
            st.pop_back();
        }
    }
    
    if(st.empty()){
        return true;
    }
    else{
        return false;
    }

}