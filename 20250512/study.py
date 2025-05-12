##1. 양수, 음수, 0 구분하기
'''
문제: 주어진 숫자가 양수, 음수, 0인지 구분하는 함수를 만드세요.

양수이면 "양수"를 출력하고,

음수이면 "음수"를 출력하고,

0이면 "0"을 출력하세요.

'''

def solution(number):
    if number > 0:
       return"양수"
    elif number < 0:
       return "음수"
    else :
       return "0"
print(solution(5))   # 출력: 양수
print(solution(-3))  # 출력: 음수
print(solution(0))   # 출력: 0

##2.배수 판별하기 
'''
문제: 주어진 숫자가 3의 배수인지 확인하는 함수를 만드세요.

3의 배수이면 "True"를 출력하고,

아니라면 "False"를 출력하세요.
'''
def solution(number):
     return number % 3 ==0
print(solution(9))   # 출력: True
print(solution(10))  # 출력: False

##3. 짝수 또는 홀수 구분하기 (범위 지정)

'''
문제: 주어진 숫자가 짝수인지 홀수인지 구분하고,

숫자가 10보다 작으면 "작다",

숫자가 **10보다 크면 "크다"**라고 출력하세요.
'''
def solution(number):
 if number% 2== 0 :
    if number <10:
       return "짝수 작다"
    else :
       return "짝수 크다"
 else :
    if number <10:
       return "홀수 작다"
    else:
       return "홀수 크다"
  

print(solution(6))   # 출력: 짝수 작다
print(solution(15))  # 출력: 홀수 크다
print(solution(12))  # 출력: 짝수 크다
print(solution(7))   # 출력: 홀수 작다

##4 윤년 확인하기

'''
문제: 주어진 연도가 윤년인지 아닌지 확인하는 함수를 만드세요.
윤년의 조건:

4로 나누어 떨어지면 윤년,

100으로 나누어 떨어지면 윤년이 아니지만,

400으로 나누어 떨어지면 윤년.
'''

def solution(year):
    if year %400 ==0 :
       return "윤년"
    elif year % 100 == 0 :
       return "평년"
    elif year % 4 ==0 :
       return "윤년"
    

print(solution(2020))  # 출력: 윤년
print(solution(1900))  # 출력: 평년
print(solution(2000))  # 출력: 윤년


##5. 숫자 범위 확인하기
'''
문제: 주어진 숫자가 1에서 100까지의 범위 안에 있는지 확인하는 함수를 만드세요.

범위 안에 있으면 "범위 안"을 출력하고,

범위 밖에 있으면 "범위 밖"을 출력하세요.
'''

def solution(number):
    return 1<= number<=100

print(solution(50))   # 출력: 범위 안
print(solution(150))  # 출력: 범위 밖
