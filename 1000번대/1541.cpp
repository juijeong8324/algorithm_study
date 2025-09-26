#include <iostream>
#include <string>

using namespace std;

int main(void) {

	string temp;
	string s;
	bool m = false;

	int result = 0;
	cin >> s; // 수식 입력 

	for (int i = 0; i < 50; i++)
	{
		if (s[i] == '+' || s[i] == '-' || s[i] =='\0') { 
			if (m) {
				// 음수값이 참
				result -= stoi(temp);
			}
			else {
				// +면
				result += stoi(temp);
			}
			temp = ""; // 초기화
			if (s[i] == '-') {
				m = true;
			}
		}
		else {
			temp += s[i]; // 문자열을 만들어준다. 
		}
	
	}
	
	cout << result;

}