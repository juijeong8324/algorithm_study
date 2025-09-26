#include <iostream>

using namespace std;

int main(void) {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int N=0;

	cin >> N;

	for (int i = 0; i < N; i++) {
		for (int j=1; j < N-i; j++) { //심지어 이쪽도 맞춰야 함... 
			cout << " ";
		}
		for (int j=N-i; j < N+i+1; j++) {
			cout << "*";
		}
		// 오른쪽 공백은 출력하지 말아야 함 
		cout << "\n";
	}

}