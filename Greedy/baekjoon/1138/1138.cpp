#include <bits/stdc++.h>
using namespace std;

int main(void) {
	int N;
	cin >> N;

	int arr[10];
	fill(arr, arr + 10, 11); // 11�� �ʱ�ȭ

	for (int i = 1; i <= N; i++) {
		/*�ʱ�ȭ*/
		int temp = 0;
		int count = 0; // ������ ���ʿ� �ִ� ��� ����
		int j = 0; // �ε��� 

		cin >> temp; // ���ڸ� �ޱ� 

		while (true) {

			if (count == temp) { // count�� temp�� ���� �� 
				if (arr[j] != 11) { // �� �ڸ��� �ƴϸ� 
					j++;
				}
				else { // ���ڸ��� 
					break;
				}
			}
			else { // count�� temp�� ���� ���� �� 
				if (arr[j] == 11) { // �ڱ� ���� ū �ְ� ������ 
					count++;// ū �� count 
					j++; // �ε��� ����
				}
				else { // �ڱ⺸�� ū �ְ� �ƴϸ� 
					j++; //�ε��� ���� 
				}

			}
		}

		arr[j] = i; // �Ҵ� 

	}

	for (int i = 0; i < N; i++) {
		cout << arr[i] << " ";
	}

}