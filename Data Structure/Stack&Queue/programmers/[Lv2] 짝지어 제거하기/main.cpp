#include <stack>
#include <string>
using namespace std;

/*
    stack 
        - push()
        - pop()
        - top()
*/

int solution(string s)
{
    stack<int> st;
    
    st.push(s[0]); 
    for(int i= 1; i <s.size();i++){
        if(st.empty() || st.top() != s[i]){
            st.push(s[i]);
        }
        else{
            st.pop();
        }
    }

    return int(st.empty());
}