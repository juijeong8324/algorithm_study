#include <iostream>
#include <vector>
using namespace std;

int main(void) {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int M, N = 0;
	int min = 0;
	int sum = 0;

	cin >> M >> N;

	vector<int> s; // 소수가 담겨있다. 
	s.push_back(2);

	for (int i = 1; i < N + 1; i++) {
		int j = 0;
		for (; j < s.size(); j++) {
			if (i % s[j] == 0 || i == 1) { // 1은 기각 
				if (i == 2) {
					continue;
				}
				break;
			}
		}

		if (j == s.size()) {
			s.push_back(i);
			if (i >= M) {
				if (sum == 0) {
					min = i;
				}
				sum += i;
			}
		}
	}

	if (sum == 0) {
		cout << -1;
	}
	else {
		cout << sum << "\n" << min;
	}
}