#include <string>
#include <vector>

using namespace std;

int solution(double flo) {
    int answer = 0;
    answer = (int)flo; // 명시적 형변환
    return answer;
}

/* 다른 사람의 풀이 */
#include <string>
#include <vector>

using namespace std;

int solution(double flo) {
    int answer = flo; // 묵시적 형변환
    return answer;
}
