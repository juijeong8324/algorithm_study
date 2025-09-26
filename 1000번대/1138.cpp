#include <bits/stdc++.h>
using namespace std;

int main(void) {
	int N;
	cin >> N;

	int arr[10];
	fill(arr, arr + 10, 11); // 11로 초기화

	for (int i = 1; i <= N; i++) {
		/*초기화*/
		int temp = 0;
		int count = 0; // 나보다 왼쪽에 있는 사람 세기
		int j = 0; // 인덱스 

		cin >> temp; // 숫자를 받기 

		while (true) {

			if (count == temp) { // count와 temp가 같을 때 
				if (arr[j] != 11) { // 빈 자리가 아니면 
					j++;
				}
				else { // 빈자리면 
					break;
				}
			}
			else { // count와 temp가 같지 않을 때 
				if (arr[j] == 11) { // 자기 보다 큰 애가 있을때 
					count++;// 큰 애 count 
					j++; // 인덱스 증가
				}
				else { // 자기보다 큰 애가 아니면 
					j++; //인덱스 증가 
				}

			}
		}

		arr[j] = i; // 할당 

	}

	for (int i = 0; i < N; i++) {
		cout << arr[i] << " ";
	}

}