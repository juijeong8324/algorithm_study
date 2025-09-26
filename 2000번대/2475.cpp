#include <iostream>

using namespace std;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int sum = 0;
    int temp = 0;
    for (int i = 0; i < 5; i++) {
        cin >> temp;
        sum = sum + temp * temp;
    }

    cout << sum % 10;
}