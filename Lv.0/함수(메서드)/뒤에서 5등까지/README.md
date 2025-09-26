## [sort()](https://modoocode.com/272) 이용
- **< algorithm >** 에 정의 
- first 부터 last 전까지의 원소들을 오름차순 정렬 
- 이때 first와 last는 **임의 접근 반복자(RandomIterator)** (iterator는 말 그대로 포인터라고 생각하면 됨!) 
- list는 sort 함수 사용 할 수 없음.(순차 접근 반복자이기 때문)

```c++
// 1. default - 오름차순
void sort(RandomIt first, RandomIt last);

// 2. comp 함수를 이용한 비교 - 내림차순을 위해서 이 방법을 사용하기도 함 
bool cmp(const Type1 &a, const Type2 &b); 
void sort(RandomIt first, RandomIt last, Comp cmp); // cmp가 True가 되도록 렬렬
```

### 예시
```c++
#include <algorithm>
#include <vector>
#include <iostream>

using namespace std;

bool cmp(int a, int b){
  return a > b; // 내림차순이 True
}

int main() {
  vector<int> v = {5, 7, 4, 2, 8, 6, 1, 9, 0, 3};

  // 기본
  sort(v.begin(), v.end());
  for (auto a : v) {
    cout << v << " ";
  }
  
  // cmp를 이용한 내림차순 정렬
  sort(v.begin(), v.end(), cmp);
  for (auto a : v) {
    cout << a << " ";
  }

  // 람다 함수를 이용한 내림차순 정렬
  sort(v.begin(), v.end(), [](int a, int b) { return a > b; });
  for (auto a : v) {
    cout << a << " ";
  }
  
  // 표준 라이브러리 비교 함수 객체 greater 를 통한 정렬
  sort(v.begin(), v.end(), greater<int>());
  for (auto a : v) {
    cout << a << " ";
  }
}
```
```
0 1 2 3 4 5 6 7 8 9
9 8 7 6 5 4 3 2 1 0
9 8 7 6 5 4 3 2 1 0
9 8 7 6 5 4 3 2 1 0
```

<br>

---

## vetor의 [insert](https://modoocode.com/186)
```c++
iterator insert(iterator position, const T& x); // 해당 position에 x를 추가
void insert(iterator position, size_type n, const T& x); // 해당 position에 n개의 같은 값 x들을 추가

template <class InputIterator>
void insert(iterator position, InputIterator first, InputIterator last); // 해당 position에 first부터 last 전까지의 원소들을 추가!
```

### 예시
```c++
#include <iostream>
#include <vector>
using namespace std;

int main() {
  vector<int> myvector(3, 100);
  vector<int>::iterator it;

  it = myvector.begin();
  it = myvector.insert(it, 200); // 첫 번째 위치에 200 값 추가 후 첫 번째 iterator 반환

  myvector.insert(it, 2, 300); // 첫 번째 위치에 2개의 300 값 추가 

  int myarray[] = {501, 502, 503};
  myvector.insert(myvector.begin(), myarray, myarray + 3); // myvector의 첫 번째 위치에 myarray 0번째 부터 2번째까지 원소들을 추가 

  cout << "myvector contains:";
  for (it = myvector.begin(); it < myvector.end(); it++) cout << " " << *it;
  cout << endl;

  return 0;
}
```

```
myvector contains: 501 502 503 300 300 200 100 100 100
```

<br>

---

## [vector 생성자](https://modoocode.com/178) 
```c++
template <class InputIterator>
vector(InputIterator first, InputIterator last, const Allocator& = Allocator());
```
first 부터 last 번째 원소 전까지 반복자가 순회하며 각각의 원소들을 생성되는 vector container 원소로 복사

### 예제
```c++
#include <iostream>
#include <vector>
using namespace std;

int main() {
  int myints[] = {16, 2, 77, 29};
  vector<int> fifth(myints, myints + 3); 
  // 배열은 이름 자체가 주소값이니까 myints.begin()이 생략되어도 괜춘! 
  // myints의 첫 번째 원소와 2번째 원소까지 복사해서 vector container 생성

  return 0;
}
```
