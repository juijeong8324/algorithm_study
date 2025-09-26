#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(void) {
	ios::sync_with_stdio(0);
	cin.tie(0);

	vector<int> num;
	int temp = 0;
	int sum = 0;
	int a = 0; // �ӽ� ����
	int b = 0;

	for (int i = 0; i < 9; i++) {
		cin >> temp;
		num.push_back(temp);
		sum += temp;
	}

	a = sum - 100; // ��ȩ ������ �� - 100

	for (int i = 0; i < 9; i++) {
		if (a > num[i]) { // ���� �ش� ������ Ŀ�� Ȯ�� ����
			auto it = find(num.begin(), num.end(), a - num[i]); // ������ �ش� ���� ������ �迭�� �ִ�?

			if (it != num.end() && it-num.begin() != i) { // ���ų� �ڱ��ڽ��� ����Ű�� �ʴ´ٸ�? ��) ���� 40�̰� �ش� ���� 20�� ���...
				num[i] = 0;
				num[it - num.begin()] = 0; // �� 0���� �ٲٱ�
				break; // break ���ֱ�! �ֳ��ϸ� �ٸ� ����� ���� ã�� �� �ִµ� �ϳ��� ã���ָ� �ȴ�. 
			}
		}
	}

	sort(num.begin(), num.end());
	for (int i = 2; i < 9; i++) {
		cout << num[i] << "\n";
	}
}

/*
�׳� ������ Ǯ���� 
#include <bits/stdc++.h>
using namespace std;

int num[9], result[7];

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);

  for(int i = 0; i < 9; i++) cin >> num[i];

  // 9�� �� 2���� �� ��� ���� ���
  for(int a = 0; a < 8; a++) {
	int total = 0;

	for(int b = a + 1; b < 9; b++) {
	  total = 0;

	  // ������ 7�� ����
	  for(int c = 0, i = 0; c < 9; c++) if(c != a && c != b) result[i++] = num[c];
	  for(int i = 0; i < 7; i++) total += result[i];

	  // 7�� Ű�� ���� 100�� ���
	  if(total == 100) break;
	}
	if(total == 100) break;
  }

  // ���� �� ���
  sort(result, result + 7);
  for(int i = 0; i < 7; i++) cout << result[i] << "\n";
}
*/