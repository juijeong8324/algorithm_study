#include <iostream>

using namespace std;

int main(void) {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int N = 0;

	cin >> N;

	for (int i = N; i > 0; i--) {
		for (int j = i; j < N  ; j++) {
			cout << " ";
		}

		for(int j = 0; j < 2 *i-1; j++) {
			cout << "*";
		}
		cout << "\n";
	}
}