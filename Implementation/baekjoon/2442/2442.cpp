#include <iostream>

using namespace std;

int main(void) {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int N=0;

	cin >> N;

	for (int i = 0; i < N; i++) {
		for (int j=1; j < N-i; j++) { //������ ���ʵ� ����� ��... 
			cout << " ";
		}
		for (int j=N-i; j < N+i+1; j++) {
			cout << "*";
		}
		// ������ ������ ������� ���ƾ� �� 
		cout << "\n";
	}

}