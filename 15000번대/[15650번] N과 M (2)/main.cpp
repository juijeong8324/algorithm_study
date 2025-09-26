#include <bits/stdc++.h>

using namespace std;

int N, M = 0;
void permutation(int depth, int b);
vector<int> ans;
vector<bool> visited;

int main(void) {
	ios::sync_with_stdio(0);
	cin.tie(0);

	cin >> N >> M;
	for (int i = 1; i <= N + 1; i++) {
		visited.push_back(false);
	}
	permutation(1, 0);

}

void permutation(int depth, int b) {
	// 종료 조건
	if (depth > M) {
		for (int j = 0; j < ans.size(); j++) {
			cout << ans[j] << " ";
		}
		cout << "\n";
		return;
	}

	for (int i = 1; i <= N; i++) {
		if (visited[i] == false && b < i) { // b는 방금 담은 숫자를 의미 
			ans.push_back(i);
			visited[i] = true;
			permutation(depth + 1, i);
			ans.pop_back();
			visited[i] = false;
		}
	}
}
