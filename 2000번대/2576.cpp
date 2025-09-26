#include <iostream>

using namespace std;

int main(void) {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int sum = 0; // 합계
	int min = 100; // 주어지는 자연수는 10보다 작다  
	int temp = 0;

	for (int i = 0; i < 7; i++) {
		cin >> temp;

		if (temp % 2 != 0) { // 홀수면 
			sum += temp;
			if (min > temp) {
				min = temp;
			}
		}
	}

	if (sum == 0) return -1;
	else {
		cout << sum << "\n" << min;
	}
}

/*
bit 단위 연산 AND(&)를 사용해보자 
1100 & 1 -> 0 이 나온다 즉, 2진수에서 2^0이 1이면 홀수 임을 이용하자 
#include <bits/stdc++.h>
using namespace std;

int main(void){
  ios::sync_with_stdio(0);
  cin.tie(0);

  int x, odd = 0, sum = 0, min = 100;

  for (int i = 0; i < 7; i++) {
	cin >> x;

	if (x & 1) {
	  odd += 1;
	  sum += x;

	  if (x < min) {
		min = x;
	  }
	}
  }

  if (odd) cout << sum << "\n" << min;
  else cout << "-1";
}

*/