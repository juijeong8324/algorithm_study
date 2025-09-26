#include <iostream>
#include <string>
#include <cmath>

using namespace std;

void sort(struct Coordinate* a, int left, int right);
void swap(struct Coordinate& a, struct Coordinate& b);
double ClosetsPair(struct Coordinate* s, int start, int end);
double dist(struct Coordinate* s, int a, int b);
double findMin(double a, double b);

struct Coordinate{
	double x;
	double y;
};

int main(void) {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int num; // 좌표 개수
	cin >> num;

	Coordinate* c = new Coordinate[num];  

	string s_x; // 임시 방편

	for (int i = 0; i < num; i++) {
		cin >> s_x >> c[i].y;
		c[i].x = stoi(s_x); // int로 바꾸면서 자동으로 , 삭제!!!!! 
	}

	sort(c, 0, num - 1); // x좌표에 대해서 정렬 

	printf("%.6f\n", ClosetsPair(c, 0, num-1));

	delete[] c;
}

void sort(struct Coordinate* a, int left, int right) {
	if (left >= right) {
		return;
	}

	int p = left;
	int i = left+1; 
	int j = right;

	while (i <= j) {
		while (i <= right && a[i].x <= a[p].x) {
			i++;
		}
		while (j > left && a[j].x > a[p].x) {
			j--;
		}

		if (i > j) {
			break; // 잘 배열되었으니 나가기
		}
		else {
			swap(a[i], a[j]);
		}
		
	}
	swap(a[p], a[j]);

	sort(a, left, j - 1); // j위치가 이제 피벗임
	sort(a, j + 1, right);
}

void swap(struct Coordinate& a, struct Coordinate& b) {
	Coordinate temp = a;
	a = b;
	b = temp;
}

double ClosetsPair(struct Coordinate* s, int start, int end) { // 최근접 쌍 찾는 문제 
	int divide = 0;
	int sizeHalf = (int)((end - start + 1)/2); // size의 반을 측정
	int size = end - start + 1;

	if (size > 3) { // 3개 이상이라면 
		divide = (int)((start + end) / 2); // divide는 첫 번째 분할의 마지막 index가 된다
		if ((size) % 2 == 0) { // 짝수일 때 시작
			start = divide - sizeHalf + 1;
		}
		else { // 홀수일 때 시작
			start = divide - sizeHalf;
		}
	}


	if (size == 2) {
		return dist(s, start, end);
	}
	else if (size == 3) {
		double dist1 = dist(s, start, start + 1);
		double dist2 = dist(s, start, end);
		double dist3 = dist(s, start + 1, end);

		double min = findMin(dist1, dist2);
		double min1 = findMin(dist3, dist1);
		return findMin(min, min1);
	}
	else { // 4개 이상일 때 
		double cpL = ClosetsPair(s, start, divide);
		double cpR = ClosetsPair(s, divide+1,divide+sizeHalf);
		double d = findMin(cpL, cpR);

		// 중간단계 
		Coordinate* temp = new Coordinate[size];

		double cpC = d; 
		int temp_s = 0;

		for (int i = start; i < end+1; i++) {
			if (fabs(s[i].x - s[divide].x) < d) {
				temp[temp_s].x = s[i].x;
				temp[temp_s].y = s[i].y;
				temp_s++;
			}
		}

		for (int i = 0; i < temp_s; i++)
		{
			for (int j = i + 1; j < temp_s; j++)
			{
				if (fabs(temp[i].y - temp[j].y) < d) // y의 크기를 먼저 비교하고 
				{
					double distC = dist(temp, i, j);

					if (distC < cpC)
					{
						cpC = distC;
					}
				}
			}
		}
      
		// 거리비교 및 결과 
		return cpC == d ? d : cpC; // cpC가 d랑 같다는 것은 d보다 작은 중간범위가 없다는 뜻 
		
		delete[] temp;
	}
}

double dist(struct Coordinate* s, int a, int b) {
	double x_l = (s[a].x - s[b].x) * (s[a].x - s[b].x);
	double y_l = (s[a].y - s[b].y) * (s[a].y - s[b].y);
	return sqrt(x_l + y_l);
}

double findMin(double a, double b) {
	if (a > b) {
		return b;
	}
	else {
		return a;
	}
}
