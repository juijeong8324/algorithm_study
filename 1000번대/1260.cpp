#include <bits/stdc++.h>

using namespace std; // std라는 클래스의 이름 공간을 사용하겠다~~~
bool compare(const pair<int, int>& a, const pair<int, int>& b); // sort

int main(void) {
	ios::sync_with_stdio(0); // c++ stream과 c stream의 동기화 제거 -> 입출력 시 시간 이득
	cin.tie(0); // cin 수행 전에 buffer 지우지 않도록 해줌  

	int N, M, V = 0;
	cin >> N >> M >> V;

	vector<vector<int>> graph; // 그래프 
	vector<int> v; // 각 노드 간 연결
	int* visit = new int[N + 1]; // 동적 생성
	memset(visit, 0, sizeof(int) * (N + 1)); // 초기화 


	// 초기화 
	for (int i = 0; i < N + 1; i++) {
		graph.push_back(v); // 노드마다 생성 
	}
	// 입력
	for (int i = 0; i < M; i++) {
		int f, s = 0;
		cin >> f >> s;

		graph[s].push_back(f); // 간선 추가 
		graph[f].push_back(s); // 간선 추가 하나만 추가하면 간선 그래프 끊길 수도 있음 
	}

	/*정렬*/
	for (int i = 1; i < graph.size(); i++) {
		sort(graph[i].begin(), graph[i].end()); // 정렬 
	}

	/*DFS*/
	stack<int> next;
	next.push(V); // 초기값 넣기 
	while (!next.empty()) // 비워질 때까지 반복 
	{
		int p = next.top(); // 맨 위에 값 꺼내고
		next.pop();

		if (visit[p] != 1) { // 방문이 안 된 노드에 대해서만 
			visit[p] = 1; // 방문 표시  
			cout << p << " ";

			for (int i = graph[p].size() - 1; i >= 0; i--) {
				next.push(graph[p][i]); // 해당 노드들 모두넣기 
			}
		}

	}
	cout << "\n";

	memset(visit, 0, sizeof(int) * (N + 1)); // 초기화 
	/*BFS*/
	queue<int> next_b;
	next_b.push(V); // 초기값 대입
	visit[V] = 0; //방문 표시 
	while (!next_b.empty()) // 비워질 때까지 반복 
	{
		int p = next_b.front(); // 맨 위에 값 꺼내고
		next_b.pop();

		if (visit[p] != 1) { // 방문이 안 된 노드에 대해서만 
			visit[p] = 1; // 방문 표시  
			cout << p << " ";

			for (int i = 0; i < graph[p].size(); i++) {
				next_b.push(graph[p][i]); // 해당 노드들 모두넣기 
			}
		}

	}

	delete[] visit;

	return 0;
}

