#include <iostream>
#include <string>

using namespace std;

int main(void) {

	string temp;
	string s;
	bool m = false;

	int result = 0;
	cin >> s; // ���� �Է� 

	for (int i = 0; i < 50; i++)
	{
		if (s[i] == '+' || s[i] == '-' || s[i] =='\0') { 
			if (m) {
				// �������� ��
				result -= stoi(temp);
			}
			else {
				// +��
				result += stoi(temp);
			}
			temp = ""; // �ʱ�ȭ
			if (s[i] == '-') {
				m = true;
			}
		}
		else {
			temp += s[i]; // ���ڿ��� ������ش�. 
		}
	
	}
	
	cout << result;

}