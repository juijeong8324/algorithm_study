#include <iostream>
#include <vector>

using namespace std;

int main(void) {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int num = 0; // 통화개수
	vector<int> v;
	int temp = 0;

	cin >> num;
	for (int i = 0; i < num; i++) {
		cin >> temp;
		v.push_back(temp);
	}

	// 영식 
	int sum1 = 0;
	for (int i = 0; i < num; i++) {
		int a = (int)(v[i] / 30);
		sum1 += 10*(a+1);
	}

	// 민식
	int sum2 = 0;
	for (int i = 0; i < num; i++) {
		int a = (int)(v[i] / 60);
		sum2 += 15 * (a + 1);
	}

	if (sum1 < sum2) {
		cout << "Y" << " " << sum1;
	}
	else if (sum1 > sum2) {
		cout << "M" << " " << sum2;
	}
	else {
		cout << "Y" << " " << "M" << " " << sum1;
	}
}

/*
#include <bits/stdc++.h>
using namespace std;

int phone[10000], Y, M;

int main(void){
  ios::sync_with_stdio(0);
  cin.tie(0);

  int N;
  cin >> N;

  for(int n = 0; n < N; n++) cin >> phone[n];

  for(int n = 0; n < N; n++) Y += ((phone[n] / 30) + 1) * 10;

  for(int n = 0; n < N; n++) M += ((phone[n] / 60) + 1) * 15;

  if(Y < M) cout << "Y " << Y;
  else if(Y > M) cout << "M " << M;
  else cout << "Y M " << Y;
}
*/