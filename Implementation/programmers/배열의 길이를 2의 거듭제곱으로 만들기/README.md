## 첫 번째 방법
### 1차 시도 
```c++
#include <string>
#include <vector>
#include <array>

using namespace std;

vector<int> solution(vector<int> arr) {
    array<int, 10> pow = {2, 4, 8, 16, 32, 64, 128, 256, 512, 1024};
    int zero = 0;
    
    for(int i = 0; i < pow.size(); i++){
        if(arr.size() <= pow[i]){
            zero = pow[i] - arr.size();
            break;
        }
    }
    arr.insert(arr.end(), zero, 0);
    return arr;
}
```
1. 문제에서 arr의 길이가 1000까지라 2의 거듭제곱을 담은 배열을 만들어준다.
2. 배열의 크기보다 2의 거듭제곱 값이 크거나 같은 경우를 조건문으로 체크하여 그 간격을 구해준다
3. 해당 간격만큼 0을 추가해준다.

### 문제 발생 
![image](https://user-images.githubusercontent.com/63052097/236430482-55eae9dc-0932-4e6d-a531-23f0ea8d2a5d.png)
아니 대체 어디가 문제인거지?!!? Test case 22 번째가 실패로 뜬다.

<br>

### 문제해결
문제를 잘 읽어보니 길이가 **2의 정수 거듭제곱이 되도록** 만든다고 했다. 즉 2^0 = 1도 2의 정수 거듭제곱이라는 것!!
```c++
#include <string>
#include <vector>
#include <array>

using namespace std;

vector<int> solution(vector<int> arr) {
    array<int, 11> pow = {1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024};
    int zero = 0;
    
    for(int i = 0; i < pow.size(); i++){
        if(arr.size() <= pow[i]){
            zero = pow[i] - arr.size();
            break;
        }
    }
    arr.insert(arr.end(), zero, 0);
    return arr;
}
```
통과했지롱~~ 

<br>
<br>

---

<br>

## 두 번째 방법 : < cmath > header pow(2, ceil(log2(arr.size())))이용
### [ceil(double x)](https://cplusplus.com/reference/cmath/ceil/)
- The smallest integral value that is not less than x (as a floating-point value).
- 즉 x보다 작지 않은 가장 작은 정수 값을 반환한다. 

### 예시
```c++
/* ceil example */
#include <stdio.h>      /* printf */
#include <math.h>       /* ceil */

int main ()
{
  printf ( "ceil of 2.3 is %.1f\n", ceil(2.3) );
  printf ( "ceil of 3.8 is %.1f\n", ceil(3.8) );
  printf ( "ceil of -2.3 is %.1f\n", ceil(-2.3) );
  printf ( "ceil of -3.8 is %.1f\n", ceil(-3.8) );
  return 0;
}
```
```
ceil of 2.3 is 3.0
ceil of 3.8 is 4.0
ceil of -2.3 is -2.0
ceil of -3.8 is -3.0
```

<br>

### [pow(double base, double exponent)](https://cplusplus.com/reference/cmath/pow/)
- base를 exponent 승만큼 제곱한 값을 리턴한다.
```c++
/* pow example */
#include <stdio.h>      /* printf */
#include <math.h>       /* pow */

int main ()
{
  printf ("7 ^ 3 = %f\n", pow (7.0, 3.0) );
  printf ("4.73 ^ 12 = %f\n", pow (4.73, 12.0) );
  printf ("32.01 ^ 1.54 = %f\n", pow (32.01, 1.54) );
  return 0;
}
```
```
7 ^ 3 = 343.000000
4.73 ^ 12 = 125410439.217423
32.01 ^ 1.54 = 208.036691
```
자세한 알고리즘은 위의 Second.cpp를 확인해보자!
