#include <iostream>

using namespace std;

int main(void) {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int N, K = 0;
	int count = 0;

	cin >> N >> K;

	for (int i = 1; i <= N; i++) {
		if (N % i == 0) {
			count++;
			if (count == K)
			{
				cout << i;
				return 0;
			}
			if (count > K) break;
		}
	}

	cout << 0;

}