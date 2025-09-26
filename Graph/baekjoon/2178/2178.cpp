#include <bits/stdc++.h>

using namespace std;

int main(void) {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int N, M; // ����
	cin >> N >> M;

	int** arr = new int* [N]; // �� �ޱ� - �̶� ũ�Ⱑ n�� INT* �迭�� ����Ű�� ������ ���� ����
	int** d = new int* [N]; // �Ÿ� �ޱ� 
	for (int i = 0; i < N; i++) {
		arr[i] = new int[M]; //���ޱ�
		d[i] = new int[M]; // �Ÿ� �� �ޱ� 
	}

	for (int i = 0; i < N; i++) {
		string temp; // �ӽ�����
		cin >> temp;
		for (int j = 0; j < M; j++) {
			arr[i][j] = temp[j] - '0'; // �� �ֱ�, �׳� int(temp[j])�� �θ� 49�� ���´�. 
			d[i][j] = 0; // �ʱ�ȭ 
		}
	}

	queue<pair<int, int>> q; // ť�� ������� 
	q.push({ 0,0 }); // �ʱ� ��ġ �� �ֱ� 
	int dx[4] = { 1,0,-1,0 }; // �ð��������
	int dy[4] = { 0,1,0,-1 };
	while (!q.empty()) {
		pair<int, int> temp = q.front(); //���� �� ������ 
		q.pop();
		for (int i = 0; i < 4; i++) {
			int x = temp.first + dx[i];
			int y = temp.second + dy[i];

			if (x < 0 || x >= N || y < 0 || y >= M) continue; // �̷� ���� ���� ���
			if (d[x][y] > 0 || arr[x][y] != 1) continue; // �̹� �����߰ų� 0�� ��� 

			// ���� ���� 
			d[x][y] = d[temp.first][temp.second] + 1; // ������ ����̹Ƿ�!
			q.push({ x,y });

		}
	}

	cout << d[N - 1][M - 1] + 1; // �˰��� ����...  

	// ���� 
	for (int i = 0; i < N; i++) {
		delete[] arr[i];
	}
	delete[] arr;

}
