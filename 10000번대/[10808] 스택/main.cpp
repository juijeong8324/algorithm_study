// LINK : https://www.acmicpc.net/problem/10828
#include <iostream>

using namespace std;

void push(int x);
int pop();
int size();
int empty();
int top();

// 전역변수 
int idx = 0; // 현재 원소 개수 
int arr[10000];

int main(void) {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int inputOrder = 0;
	string inputString = "";
	cin >> inputOrder;

	for (int i = 0; i < inputOrder; i++) {
		cin >> inputString;
		if (inputString == "push") {
			int inputX = 0;
			cin >> inputX;
			push(inputX);
		}
		else if (inputString == "pop") {
			cout << pop() << "\n";
		}
		else if (inputString == "size") {
			cout << size() << "\n";
		}
		else if (inputString == "empty"){
			cout << empty() << "\n";
		}
		else {
			// top
			cout << top() << "\n";
		}
	}
}

void push(int x) {
	arr[idx] = x;
	idx++;
}

int pop() {
	if (idx == 0) {
		return -1;
	}
	else {
		int top = arr[idx - 1];
		idx--;
		return top;
	}
	
}

int size() {
	return idx;
}

int empty() {
	if (idx == 0) return 1;
	else return 0;
}

int top() {
	if (idx == 0) return -1;
	else {
		return arr[idx - 1];
	}
}
