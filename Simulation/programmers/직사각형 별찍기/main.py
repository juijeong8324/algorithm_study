# Link : https://programmers.co.kr/learn/courses/30/lessons/12969

a, b = map(int, raw_input().strip().split(' '))
for i in range(b):
    print "*" * a
    
# map(적용시킬 함수, 적용할 값들) 이때 map 타입으로 결과를 리턴! for문을 대신해서 많이 쓰는듯?
# int : 데이터 타입을 변환하는 함수 
# raw_input() : 사용자로부터 string 타입의 입력을 받는다
# strip() : 문자열 끝에 .strip()을 붙이면 문자열의 맨앞과 맨뒤의 whitespace가 제거(단 중간은 제거 노노)
#split(' ') : 문자열의 중간을 ' ' 즉, space로 나누어 새로운 리스트로 리턴! 
