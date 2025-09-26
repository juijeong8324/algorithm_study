### 함수 및 메서드 

|문제 이름| ✏️KeyPoint✏️| 원본링크 |        
| :-----: | :-----: | :-----: |         
| <a href="https://github.com/juijeong8324/codingStudy/tree/programmers/Lv.0/%ED%95%A8%EC%88%98(%EB%A9%94%EC%84%9C%EB%93%9C)/%EB%AC%B8%EC%9E%90%EC%97%B4%EB%A1%9C%20%EB%B3%80%ED%99%98">문자열로 변환</a> | < string > header의 ```to_string(int)``` 함수 이용 |[링크](https://school.programmers.co.kr/learn/courses/30/lessons/181845)|
| <a href="">정수 부분</a> |1️⃣ 묵시적 형변환 : 선언시 int로 <br> 2️⃣ 명시적 형변환 : (int)변수이름 |[링크](https://school.programmers.co.kr/learn/courses/30/lessons/181850)|
| <a href="">문자열을 정수로 변환하기</a> |1️⃣ < string > header의 ```stoi(string)``` 함수 이용 <br> 2️⃣ '0'의 ASCII code가 48임을 이용(48을 빼면 됨) or 해당 숫자에 '0'을 빼면 해당 숫자값이 나옴을 이용|[링크](https://school.programmers.co.kr/learn/courses/30/lessons/181848)|
| <a href="">배열의 길이에 따라 다른 연산하기</a> |```arr.size()```와 ```for문``` 이용|[링크](https://school.programmers.co.kr/learn/courses/30/lessons/181854)|
| <a href="">문자열 정수의 합</a> |```for문```을 이용해서 각 문자열을 접근하고 '0'을 빼어 실제 숫자값을 구하여 더하기|[링크](https://school.programmers.co.kr/learn/courses/30/lessons/181849)|
| <a href="">뒤에서 5등까지</a> |1️⃣ < algorithm > header의 `sort()` 함수를 이용해서 정렬하고 for문으로 5번째 배열 얻기 <br> 2️⃣ 정렬 후 ```insert()```함수 이용 <br> 3️⃣ 정렬 후 ```vector 초기화```|[링크](https://school.programmers.co.kr/learn/courses/30/lessons/181853)|
| <a href="">뒤에서 5등 위로</a> |뒤에서 5등까지 문제와 동일|[링크](https://school.programmers.co.kr/learn/courses/30/lessons/181852)|
| <a href="">배열의 길이를 2의 거듭제곱으로 만들기</a> |1️⃣ 2의 거듭제곱이 담긴 array를 만들어주고 arr.size()와 해당 거듭제곱 값을 비교  ```insert()```로 추가 <br> 2️⃣ < cmath > header의 `pow` 함수와 `ceil` 함수 이용 <br> 3️⃣ while 문으로 arr.size()보다 큰 2의 거듭제곱 만큼 곱해준 후 추가|[링크](https://school.programmers.co.kr/learn/courses/30/lessons/181857)|
| <a href="">0 떼기</a> |1️⃣ 해당 문자열을 `stoi(string)`를 이용해서 int로 바꿔 0을 떼고 `to_string(int)`로 문자열로 만들어주기 <br> 2️⃣ 0을 다른 숫자가 올때까지 count하고 `substr(int)`로 문자열 자르기 |[링크](https://school.programmers.co.kr/learn/courses/30/lessons/181847)|
| <a href="">배열 비교하기</a> |1️⃣ < numeric > header의 `accumulate()` 이용해서 배열의 합 구하고 단순 대소 비교 <br> 2️⃣ 대소 비교시 삼항 연산자 이용하면 더 simple한 코드 완|[링크](https://school.programmers.co.kr/learn/courses/30/lessons/181856)|

<br>

---

<br>

### 문자열 

|문제 이름| ✏️KeyPoint✏️ | 원본링크 |        
| :-----: | :-----: | :-----: |     
| <a href="">대문자로 바꾸기</a> | 1️⃣ ```toupper(char)``` 함수 이용 (소문자로 변환 시 ```tolower(char)``` 함수 이용) <br> 2️⃣ ASCII 값이 A-Z는 65-90 a-z는 97-122임을 이용(97-65=`32를 더하거나 빼면 됨`) <br> 3️⃣ 현재 문자와 'a'와의 차를 계산한 후 'A'를 더하기 (```char-'a'+'A'```)|[링크](https://school.programmers.co.kr/learn/courses/30/lessons/181877)|

<br>

---

<br>

### 리스트(배열)
|문제 이름| ✏️KeyPoint✏️ | 원본링크 |        
| :-----: | :-----: | :-----: |    
|||[링크]()|

<br>

---

<br>

### 연산
|문제 이름| ✏️KeyPoint✏️ | 원본링크 |        
| :-----: | :-----: | :-----: |    
|||[링크]()|
