#include <iostream>

using namespace std;

int main(void) {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int temp;
	int index = 0;
	int max = 0;

	for (int i = 0; i < 9; i++) {
		cin >> temp;

		if (max < temp) {
			max = temp;
			index = i+1;
		}
	}

	cout << max << "\n";
	cout << index;

}