#include <iostream>

using namespace std;

void change(int &a, int &b); // int a int b�̸� ���� �迭�� ���� �ȵ� ���� int &a �� ���� a�� �ּҿ� �ش��ϴ� ���� ��� �ȴ�. 

int main(void) {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int c[3];
	cin >> c[0] >> c[1] >> c[2];
	
	change(c[0], c[1]);
	change(c[1], c[2]);
	change(c[0], c[1]);

	cout << c[0] << " " << c[1] << " " << c[2];
	
}

void change(int &a, int &b) {
	if (a > b) {
		int temp = a;
		a = b;
		b = temp;
	}
}

/* �ٸ� ���� Ǯ�� 
* min max �̿� 
#include <bits/stdc++.h>
using namespace std;

int main(void){
  ios::sync_with_stdio(0);
  cin.tie(0);

  int a, b, c; // �Է�
  cin >> a >> b >> c;
  int d, e, f; // ũ�� ������ ����� �� ��
  d = min({a,b,c});
  f = max({a,b,c});
  e = a+b+c-d-f;
  cout << d << ' ' << e << ' ' << f;
}

sort�Լ� �̿� 
#include <bits/stdc++.h>
using namespace std;

int main(void){
  ios::sync_with_stdio(0);
  cin.tie(0);

  int arr[4];
  for(int i=0;i<3;i++){
	cin>>arr[i];
  }
  sort(arr, arr+3);
  for(int i=0;i<3;i++){
	cout<<arr[i]<<" ";
  }
}
*/