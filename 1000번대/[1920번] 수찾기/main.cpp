// Link : https://www.acmicpc.net/problem/1920
// 퀵 정렬과 이분 탐색 사용한 매우 원초적인 알고리즘이다. 
// 최대한 printf와 scanf,\n 쓰자.. 안 하면 시간초과 뜬다!!!! 아니 왜이리 허무한 것이여 %참고: cout,cin,endl은 시간이 오래걸린다%
// sort 함수에서 등호 주의 메모리초과 뜸. 
// scanf, printf를 안 쓰고 싶으면 아래 main함수 첫 두 줄 참고 

#include <iostream>

void sort(int* arr, int left, int right);
void swap(int& a, int& b);
bool find(int* arr, int answer, int start, int end);

int main(void) {
    //ios_base::sync_with_stdio(false); 
    //cin.tie(null);

    int n, m;
    scanf("%d", &n);

    int* a = new int[n];

    int temp = 0;
    for (int i = 0; i < n; i++) {
        scanf("%d", &temp);
        a[i] = temp;
    }
    sort(a, 0, n - 1);

    scanf("%d", &m);
    int find_a = 0;
    for (int j = 0; j < m; j++) {
        scanf("%d", &find_a);
        printf("%d", (int)find(a, find_a, 0, n - 1));
        printf("\n");
    }

    delete[] a;
    return 0;
}

void sort(int* arr, int left, int right) {
    if (left >= right) {
        return;
    }

    int p = left;
    int i = p + 1;
    int j = right;

    while (i <= j) {
        while (i <= right && arr[i] <= arr[p]) {
            i++;
        }
        while (j > left && arr[j] > arr[p]) { // 등호를 넣어주니 메모리초과가 뜬다!! 
            j--;
        }

        if (i > j) {
            break;
        }
        else {
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[p], arr[j]);

    sort(arr, j + 1, right);
    sort(arr, left, j - 1);
}

void swap(int& a, int& b) {
    int temp = a;
    a = b;
    b = temp;
}

bool find(int* arr, int answer, int start, int end) { // end 대신 size 매개변수를 넣었음
    if (start > end) { // 재귀 함수 주의할 점 : 항상 break 포인트를 만들어주자!!
        return 0;
    }
    /* int temp = start + size / 2; 나의 잘 못된 코드 */

    int p = (start + end) / 2;

    if (arr[p] == answer) {
        return 1;
    }
    else if (arr[p] > answer) {
        return find(arr, answer, start, p - 1); // 만약에 짝수면 4/2 =  2 이때 양쪽 크기가 모두 2가 되서 더 많은 연산 필요 
    }
    else {
        return find(arr, answer, p + 1, end);
    }

}
