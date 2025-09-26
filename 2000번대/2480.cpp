#include <iostream>
#include <algorithm>

using namespace std;

int main(void) {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int c[3];
	cin >> c[0] >> c[1] >> c[2];

	sort(c, c+3);

	if (c[0] == c[2]) {
		cout << 10000 + c[2] * 1000;
	}
	else {
		if (c[1] == c[0] || c[1] == c[2]) {
			cout << 1000 + c[1] * 100;
		}
		else {
			cout << c[2] * 100;
		}
	}
}

/* 다른 분들의 풀이 
같은 값을 비교한 후에 max 사용 
int main(void){
  ios::sync_with_stdio(0);
  cin.tie(0);

  int a, b, c;
  cin >> a >> b >> c;
  if(a == b && b == c) cout << 10000 + a*1000;
  else if(a == b || a == c) cout << 1000 + a*100;
  else if(b == c) cout << 1000 + b*100;
  else cout << max({a,b,c}) * 100;
}

*/