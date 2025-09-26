// 몬스터의 목숨이 0이 아니라면 최댓값 찾기 + 그리디 알고리즘 
#include <iostream>

using namespace std;

int find(struct Attack* data, int size);

struct Attack { // 기존의 Attack 구조체에서 
    int power;
    int hp;
    bool check; // 체크 변수를 추가
};
int main(void) {
    int monster; // 몬스터 목숨
    int count; // 무기 개수 
    int num = 0; // 공격 횟수 

    cin >> monster >> count;
    Attack* monster_a = new Attack[count];

    for (int i = 0; i < count; i++) { // 배열에 값 저장
        cin >> monster_a[i].power >> monster_a[i].hp;
        monster_a[i].check = true;
    }

    // 몬스터가 작을 때까지 계산          
    while (monster > 0) {
        int index = find(monster_a, count); // 무기 공격력 최댓값 찾기!! 
        int c = monster / (monster_a[index].power);

        if (c >= monster_a[index].hp) {
            monster = monster - monster_a[index].power * monster_a[index].hp;
            num = num + monster_a[index].hp;
        }
        else { // c < monster_a[i].hp
            if (monster % monster_a[index].power != 0) {
                monster = monster - monster_a[index].power * (c + 1);
                num = num + (c + 1);
            }
            else {
                monster = monster - monster_a[index].power * c;
                num = num + c;
            }

        }
    }

    delete[]monster_a;

    cout << num;

    return 0;
}

int find(struct Attack* data, int size) {
    int max = 0;
    int max_i = 0; // index

    for (int i = 0; i < size; i++) {
        if (max < data[i].power && data[i].check == true) { // 체크가 true로 되어 있는 것들 중 최댓값 찾기 
            max = data[i].power;
            max_i = i;
        }
    }

    data[max_i].check = false;
    return max_i;
}
