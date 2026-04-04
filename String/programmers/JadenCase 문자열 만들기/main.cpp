#include <bits/stdc++.h>

using namespace std;

string solution(string s) {
    string answer = "";
    bool new_world = true;
    
    for(auto& c : s){
        if(c == ' '){
            new_world = true;
        }
        else if(new_world){
            c = toupper(c);
            new_world = false;
        }
        else{
            c = tolower(c);
        }
    }
    
    return s;
}