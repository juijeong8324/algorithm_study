#include <iostream>

using namespace std;

void change(int &a, int &b); // int a int b이면 원래 배열에 적용 안됨 따라서 int &a 로 원본 a의 주소에 해당하는 값을 얻게 된다. 

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

/* 다른 분의 풀이 
* min max 이용 
#include <bits/stdc++.h>
using namespace std;

int main(void){
  ios::sync_with_stdio(0);
  cin.tie(0);

  int a, b, c; // 입력
  cin >> a >> b >> c;
  int d, e, f; // 크기 순으로 출력할 세 수
  d = min({a,b,c});
  f = max({a,b,c});
  e = a+b+c-d-f;
  cout << d << ' ' << e << ' ' << f;
}

sort함수 이용 
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