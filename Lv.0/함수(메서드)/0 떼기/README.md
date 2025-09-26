## [string.substr(int)](https://modoocode.com/235)
- 문자열의 pos부터 count까지를 반환한다. 
- count의 default는 npos로 npos는 문자열의 끝을 의미한다. 

`c++
 basic_string substr(size_type pos = 0, size_type count = npos) const;
`

### 예시
```c++
#include <iostream>
#include <string>

int main() {
  std::string a = "0123456789abcdefghij";

  // count 가 npos 이므로 pos 부터 문자열 끝까지 리턴한다.
  std::string sub1 = a.substr(10);
  std::cout << sub1 << '\n';

  // pos 와 pos + count 모두 문자열 범위 안이므로, 해당하는 부분 문자열을
  // 리턴한다.
  std::string sub2 = a.substr(5, 3);
  std::cout << sub2 << '\n';
  ```
  ```
  abcdefghij
  567
  ```
