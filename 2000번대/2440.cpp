#include <iostream>

using namespace std;

int main(void) {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int num = 0;
	cin >> num;
	int temp = num;

	for (int i = 0; i < num; i++) {
		for (int j = temp; j > 0; j--) {
			cout << "*";
		}
		cout << "\n";
		temp--;
	}
}

/*
#include <bits/stdc++.h>
using namespace std;

int main(void){
  ios::sync_with_stdio(0);
  cin.tie(0);

  int N;
  cin >> N;

  for(int i = 0; i < N; i++) {
	for(int j = 0; j < N - i; j++)  cout << '*'; // 즉 i변수를 이용했음 
	cout << "\n";
  }
*/