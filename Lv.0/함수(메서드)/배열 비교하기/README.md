## [< numeric > header의 accumulate()](https://torbjorn.tistory.com/253)
- first 부터 last 원소까지 더한 값을 리턴한다. 이때 first와 last는 iterator
- init을 설정해줘야 한다.
- 주의할 점!! init의 Type에 따라 return의 Type이 달라진다. (해당 함수를 init이 int면 int 타입으로 리턴! )
```c++
template< class InputIt, class T >
T accumulate( InputIt first, InputIt last, T init );
```

<br>

---

<br>

## 삼항 연산자
- C++만 존재하는 독특한 연산자 
- 피연산자가 3개인 연산자는 C++에서 삼항 연산자가 유일!
- 물음표(?) 앞의 조건식에 따라 결괏값이 참(true)이면 반환값1을 반환하고, 결괏값이 거짓(false)이면 반환값2를 반환합니다.
```c++
조건식 ? 반환값1 : 반환값2
```
