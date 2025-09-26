// Link : https://www.acmicpc.net/problem/18222
// int로 쓰면 시간 초과난다. long으로 쓰면 넘어감!!!
// WHY? 연산을 수행해야 할 때 CPU에게 필요한 클럭 수도 다르고, 메모리와 CPU 사이에 오고가야 하는 데이터의 양도 다르기 때문입니다.
#include <iostream>

using namespace std;

long find(long num);

int main() {
	long n;
	cin >> n;

	cout << find(n);
	return 0;
}

long find(long num)
{   if (num == 1) return 0;
	if (num == 2) return 1;
	
	long temp = 2;
	while (temp + temp < num) { // num에 가까운 2의 제곱 구하기 
		temp *= 2;
	}

	return 1 - find(num - temp);
}
