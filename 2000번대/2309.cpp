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
	int a = 0; // 임시 저장
	int b = 0;

	for (int i = 0; i < 9; i++) {
		cin >> temp;
		num.push_back(temp);
		sum += temp;
	}

	a = sum - 100; // 아홉 난쟁이 합 - 100

	for (int i = 0; i < 9; i++) {
		if (a > num[i]) { // 차가 해당 수보다 커야 확인 가능
			auto it = find(num.begin(), num.end(), a - num[i]); // 차에서 해당 수를 뺀값이 배열에 있니?

			if (it != num.end() && it-num.begin() != i) { // 없거나 자기자신을 가르키지 않는다면? 예) 차가 40이고 해당 수가 20인 경우...
				num[i] = 0;
				num[it - num.begin()] = 0; // 다 0으로 바꾸기
				break; // break 해주기! 왜냐하면 다른 경우의 수를 찾을 수 있는데 하나만 찾아주면 된다. 
			}
		}
	}

	sort(num.begin(), num.end());
	for (int i = 2; i < 9; i++) {
		cout << num[i] << "\n";
	}
}

/*
그냥 일일이 풀었네 
#include <bits/stdc++.h>
using namespace std;

int num[9], result[7];

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);

  for(int i = 0; i < 9; i++) cin >> num[i];

  // 9명 중 2명을 뺀 모든 조합 고려
  for(int a = 0; a < 8; a++) {
	int total = 0;

	for(int b = a + 1; b < 9; b++) {
	  total = 0;

	  // 나머지 7명 저장
	  for(int c = 0, i = 0; c < 9; c++) if(c != a && c != b) result[i++] = num[c];
	  for(int i = 0; i < 7; i++) total += result[i];

	  // 7명 키의 합이 100인 경우
	  if(total == 100) break;
	}
	if(total == 100) break;
  }

  // 정렬 후 출력
  sort(result, result + 7);
  for(int i = 0; i < 7; i++) cout << result[i] << "\n";
}
*/