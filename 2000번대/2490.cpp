#include <iostream>

using namespace std;

int main(void) {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int result = 0; // ���� ������ ��� �迭 
	int temp = 0; // �ӽ� ���� 

	for (int i = 0; i < 3; i++) {
		for (int j = 0; j < 4; j++) {
			cin >> temp;
			result = result + temp;
		}

		switch (result)
		{
		case 0:
			cout << "D" << "\n";
			break;
		case 1:
			cout << "C" << "\n";
			break;
		case 2:
			cout << "B" << "\n";
			break;
		case 3:
			cout << "A" << "\n";
			break;
		case 4:
			cout << "E" << "\n";
			break;

		}
		result = 0;
	}


}

/*

#include <bits/stdc++.h>
using namespace std;

int result, input;
string res = "DCBAE";

int main(void){
  ios::sync_with_stdio(0);
  cin.tie(0);

  for(int r = 0; r < 3; r++) {
	result = 0;
	for(int c = 0; c < 4; c++) {
	  cin >> input;
	  result += input;
	}
	cout << res[result] << '\n'; ���� �ٸ� �� �� string�� Ư¡�� �̿��߳� ���ƴ�. 
  }
}

*/