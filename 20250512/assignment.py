##1.
# 문제1: 두 수를 더하는 함수를 만드세요.
def solution(a, b):
 return  a + b 
print(solution(5, 3))  # 결과: 8

##2
# 문제2: 두 수를 곱하는 함수를 만드세요.
def solution(a, b):
 return a*b
print(solution(4, 7))  # 결과: 28


##3
# 문제3: 리스트의 모든 숫자를 더하는 함수를 만드세요. ##이코드가 더 엘레강스스

def solution(numbers):
    return sum(numbers)

print(solution([1, 2, 3, 4, 5]))  # 출력: 15

##3
# 문제3: 리스트의 모든 숫자를 더하는 함수를 만드세요.
def solution(numbers):
    result = 0
    for i in numbers:
        result += i
    return result

solution([1, 2, 3, 4, 5])  # 결과: 15
##4

# 문제4: 리스트의 평균값을 계산하는 함수를 만드세요.
def solution(numbers):
    return sum(numbers)/len(numbers)

print(solution([10, 20, 30, 40]))  # 결과: 25.0
##

##5

# 문제5: 문자열의 길이를 반환하는 함수를 만드세요.
def solution(text):
    return len(text)

print(solution("파이썬"))  # 결과: 3


##6

# 문제6: 리스트에서 가장 큰 수를 찾는 함수를 만드세요.
#실제문제는 이렇게 풀지 않는다.
#원리에 다가간다는 의의가 있다.
# 최댓값 ==> 최솟값 먼저 저장
#최솟값 최댓값이 먼저저
def solution(numbers):
    return max(numbers)

print(solution([7, 12, 3, 8, 4]))  # 결과: 12

## 이방법을 주로 사용하자!
def solution(numbers):
    max_value = float('-inf')
    for i in numbers:
        if i >max_value:
            max_value = i
        return max(numbers)

print(solution([7, 12, 3, 8, 4]))  # 결과: 12

####
float('inf') > 10
float('-inf') > 10
##7
# 문제7: 리스트에서 가장 작은 수를 찾는 함수를 만드세요.
def solution(numbers):
    return min(numbers)

print(solution([7, 12, 3, 8, 4]))  # 결과: 3


##8


##8
# 문제8: 문자열을 n번 반복하는 함수를 만드세요.
def solution(text, n):
    return text*n

solution("안녕", 3)  # 결과: "안녕안녕안녕"

##9 
# 문제9: 주어진 숫자가 짝수인지 확인하는 함수를 만드세요. (짝수면 True, 홀수면 False 반환)
def solution(number):
    return number %2 ==0

print(solution(6))  # 결과: True
print(solution(9))  # 결과: False

