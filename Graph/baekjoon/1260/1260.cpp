#include <bits/stdc++.h>

using namespace std; // std��� Ŭ������ �̸� ������ ����ϰڴ�~~~
bool compare(const pair<int, int>& a, const pair<int, int>& b); // sort

int main(void) {
	ios::sync_with_stdio(0); // c++ stream�� c stream�� ����ȭ ���� -> ����� �� �ð� �̵�
	cin.tie(0); // cin ���� ���� buffer ������ �ʵ��� ����  

	int N, M, V = 0;
	cin >> N >> M >> V;

	vector<vector<int>> graph; // �׷��� 
	vector<int> v; // �� ��� �� ����
	int* visit = new int[N + 1]; // ���� ����
	memset(visit, 0, sizeof(int) * (N + 1)); // �ʱ�ȭ 


	// �ʱ�ȭ 
	for (int i = 0; i < N + 1; i++) {
		graph.push_back(v); // ��帶�� ���� 
	}
	// �Է�
	for (int i = 0; i < M; i++) {
		int f, s = 0;
		cin >> f >> s;

		graph[s].push_back(f); // ���� �߰� 
		graph[f].push_back(s); // ���� �߰� �ϳ��� �߰��ϸ� ���� �׷��� ���� ���� ���� 
	}

	/*����*/
	for (int i = 1; i < graph.size(); i++) {
		sort(graph[i].begin(), graph[i].end()); // ���� 
	}

	/*DFS*/
	stack<int> next;
	next.push(V); // �ʱⰪ �ֱ� 
	while (!next.empty()) // ����� ������ �ݺ� 
	{
		int p = next.top(); // �� ���� �� ������
		next.pop();

		if (visit[p] != 1) { // �湮�� �� �� ��忡 ���ؼ��� 
			visit[p] = 1; // �湮 ǥ��  
			cout << p << " ";

			for (int i = graph[p].size() - 1; i >= 0; i--) {
				next.push(graph[p][i]); // �ش� ���� ��γֱ� 
			}
		}

	}
	cout << "\n";

	memset(visit, 0, sizeof(int) * (N + 1)); // �ʱ�ȭ 
	/*BFS*/
	queue<int> next_b;
	next_b.push(V); // �ʱⰪ ����
	visit[V] = 0; //�湮 ǥ�� 
	while (!next_b.empty()) // ����� ������ �ݺ� 
	{
		int p = next_b.front(); // �� ���� �� ������
		next_b.pop();

		if (visit[p] != 1) { // �湮�� �� �� ��忡 ���ؼ��� 
			visit[p] = 1; // �湮 ǥ��  
			cout << p << " ";

			for (int i = 0; i < graph[p].size(); i++) {
				next_b.push(graph[p][i]); // �ش� ���� ��γֱ� 
			}
		}

	}

	delete[] visit;

	return 0;
}

