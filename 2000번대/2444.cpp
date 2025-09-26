#include <iostream>

using namespace std;

int main(void) {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int N;
	cin >> N;

	for (int i = 1; i < N+2; i++) {
		for (int j = 0; j < abs(N-i);j++) {
			cout << " ";
		}
		for (int j = 0; j < 2*(abs(N-i))-1;j++) {
			cout << "*";
		}
		cout << "\n";
	}

}