#include <iostream>

using namespace std;

int main(void) {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int sum = 0; // �հ�
	int min = 100; // �־����� �ڿ����� 10���� �۴�  
	int temp = 0;

	for (int i = 0; i < 7; i++) {
		cin >> temp;

		if (temp % 2 != 0) { // Ȧ���� 
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
bit ���� ���� AND(&)�� ����غ��� 
1100 & 1 -> 0 �� ���´� ��, 2�������� 2^0�� 1�̸� Ȧ�� ���� �̿����� 
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