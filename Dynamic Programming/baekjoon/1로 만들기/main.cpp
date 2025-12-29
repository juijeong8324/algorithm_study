#include <bits/stdc++.h>

using namespace std;

int d[1000001]; // 전역에 선언하면 0으로 초기화! 
int n;

int main(void){
		ios::sync_with_stdio(0);
		cin.tie(0);
		cin >> n;
		d[1] = 0;
		for(int i = 2; i <= n; i++){ // for문을 돌면서 확인! 
				d[i] = d[i-1] + 1; // 1을 뺀 것은 무조건 존재하므로 
				if(i%3 == 0) d[i] = min(d[i], d[i/3]+1);
				if(i%2 == 0) d[i] = min(d[i], d[i/2]+1);
		}

		cout << d[n];
}