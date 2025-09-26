#include <iostream>

using namespace std;

int main(void) {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int year;
	cin >> year;
	
	if (year % 4 == 0 && year % 100 != 0) {
		cout << 1;
	}
	else if (year % 400 == 0) {
		cout << 1;
	}
	else {
		cout << 0;
	}
}

/* �ٸ� ���� Ǯ�� 
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);

  int year;
  cin >> year;

  if(year % 4 == 0){
	// 4�� ����̸鼭 400�� ���
	if(year % 400 == 0)  cout << 1;
	// 4�� ����̸鼭 100�� ���
	else if(year % 100 == 0)  cout << 0;
	// 4�� ����̸鼭 100, 400�� ����� �ƴ� ��
	else  cout << 1;
  }
  // 4�� ����� �ƴ� ��
  else  cout << 0;
}
*/