#include <iostream>

using namespace std;

struct Graph {
	long int x;
	long int y;
	long int w; // 가중치 
};

// 크루스칼 알고리즘 관련 
void Union(long int* root, long int a, long int b); // 같은 집합으로 합치기  
void sort(struct Graph* v, long int left, long int right); // 가중치에 대해 정렬 
long int find(long int* root, long int a); // root 찾기 
void swap(struct Graph& a, struct Graph& b);

int main(void) {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	long int n, m;
	cin >> n >> m;

	long int* root = new long int[n+1]; // 집합
	for (long int i = 1; i < n + 1; i++) {
		root[i] = i; // 집합에 자기 자신을 포함 
	}

	Graph* v = new Graph[m]; // edge
	for (long int i = 0; i < m; i++) {
		// 간선의 개수만큼 돌려야 함 
		cin >> v[i].x >> v[i].y >> v[i].w;
	}

	sort(v, 0, m - 1); // 정렬
	
	long int t = 0; // 최소 신장 가중치의 합을 반환
	long int count = 0; // 가중치 개수  

	for (long int i = 0; i < m; i++) {
		if (find(root, v[i].x) != find(root, v[i].y)) {
			// x점과 y점이 같은 집합이 아닌경우에만 
			t += v[i].w; // 가중치 더함
			Union(root, v[i].x, v[i].y); //집합 합쳐주기
			count++;
		}
		if (count == n - 1) {
			break;
		}
	}

	cout << t;

	delete[] root;
	delete[] v;
}

void Union(long int* root, long int a, long int b) {
	long int aRoot = find(root,a);
	long int bRoot = find(root,b);

	if (aRoot == bRoot) { // 같은 트리이므로 처리할 필요 없음
		return;
	}
	else {
		root[aRoot] = bRoot; //  root를 같게 해주기
	}
}

long int find(long int* root, long int a) {
	if (root[a] == a) { // root면 자기자신을 반환
		return a;
	}
	else {
		return root[a] = find(root, root[a]); // root로 고고
	}
}

void sort(struct Graph* v, long int left, long int right) {
	if (left >= right) {
		return;
	}

	long int p = left;
	long int i = left + 1;
	long int j = right;

	while (i <= j) {
		while (v[p].w >= v[i].w && i <= right) {
			i++;
		}
		while (v[p].w < v[j].w && j > left) {
			j--;
		}

		if (i > j)
			break;
		else {
			swap(v[i], v[j]);
		}
	}
	swap(v[j], v[p]);

	sort(v, left, j - 1);
	sort(v, j + 1, right);

}

void swap(struct Graph& a, struct Graph& b)
{
	Graph temp = a;
	a = b;
	b = temp;
}
