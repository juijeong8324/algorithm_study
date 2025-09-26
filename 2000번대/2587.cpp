#include <iostream>
#include <algorithm>

using namespace std;


int main(void) {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int num[5]; // 담을 배열 
	int sum = 0;

	for (int i = 0; i < 5; i++) {
		cin >> num[i];
		sum += num[i];
	}
	cout << sum/5 << "\n";

	sort(num, num + 5);
	cout << num[2];

}
