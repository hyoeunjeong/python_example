# 20250428 수업 내용

#정수

a = 10
b =20
c = 0
d = -40

print(type(a),type(b),type(c),type(d))
print(int(9.33333))
#<class 'int'> <class 'int'> <class 'int'> <class 'int'> 따라서 , 는 띄어쓰기 가된다


#실수 
print
number1 =3.12
number2 =-0.12
print(type(number1),type(number2))

#float() 실수형
#int() 정수형 

print(float(3))



#무한대  infinity - (inf)라고 사용한다.
x=float("inf") #양의 무한대
x=float("-inf") #음의 무한대 


#문자열

str1 ="abcd"
str1 ='abcd'
str3 = '''   오늘은 4월 28일 한달뒤면 내 생일'''  

print(type(str3))
print(str3)
#파이썬에서는 두개를 같은것으로생각한다



'''문자와 문자열의 차이점 


'''

#문자열 이어 붙이기

str6 = "modu"
str7 ="lab"

print(str6+str7)
str8 =str6+str7


print(str8)

# if  str7 +str6 라고쓰면 ladmodu 라고 출력됨


#
# 개인정보 출력해보기기
## 1. 성 ,이름 변수 따로 만들어서 +로 합친후 출력
##2. 주민번호도 1번과 같이
##3. 이메일 {아이디}{@} {네이버 구글}


#1
name1 ="kim"
name2 ="nana"
print(name1 +name2)

#2 
birth ="123456"
code="1234567"
print (birth+"-"+code)

#3 
name11 = "abcd"
name12 =  "naver.com"
print(name11+"@"+name12)

#문자열 반복 

str10 = str1* 10
test2 = "30"
print(str10)

#print(str1 *test2)
print(str10 + "입니다"+"어쩌고 쩌고고")
#오늘은 4월 28일 입니다. 
a ="4"
b="28"

#기본방식 
print ("오늘은"+a+"월"+b+"일입니다.")
#f-string 문자열 안에 변수 사용할수 있도록 한다. 실무에서 많이 사용한다.

print(f"오늘은{a}월{b*10}일 입니다.")

#순서는 무조건 0번 부터 왼---> 오오
#index 
'''인덱싱 내가 위치를 알고 있고 인덱스를 통해서 가져오는 것
특정위치에 있는 값을 알려면면 인덱스를 알아야한다 
문자열 개수가 많다면 너무 길잖음 그래서 보통은 문자열 마지막 값을 -1이라고 한다 그래서 
그 앞의 값을 -2 라 한다.<--- 마이너스 ----> 0부터터'''


#문자열 인덱싱

s = "life is good" #띄어쓰기 포함함
print(s[0]) #s의 0번 째 인덱싱
print(s[3]) #e를 출력하는 법
print(s[-1]) #마지막 자리
#print(s[400]) #string index out of range -- 범위를 벗어남
#주민등록번호가 13 자리
#print(s[13])
#print("good!")# 이게 위에가 오류가 나면 밑에 전체가 실행이 안된 
# 그래서 예외 처리를 하여서 오류를 방어한다. 왜냐 엄청 크리티컬한 오류이기 떄문이다.


#문자열 슬라이싱  [start:stop:setp] step은 생략가능 -부터 -까지 스텝텝

'''슬라이싱 vs 인덱싱
인덱싱은 하나만 가능하다면 슬라이싱은 여러단어 가져올수 있다다'''
print(s[0:3]) #e가 출력이 안된다. #s[0:3:1] 0부터 3까지 1씩 증가가
print(s[0:4:2]) #값 lf (0번째 부터 4번까지 2스텝텝)


#다양한 슬라이싱 방법

s ='weniv ceo licat'
print(1,s[0:5]) #출력 :weniv
print(2,s[6:]) # 끝까지 출력
print(3,s[:]) #모두 출력
print(4,s[::-1])#역순으로 출력
print(5,s[::2]) #스텝 건너 뛰면서

#테스트
## ip address = 172.100.200.100

'''
1.ip address문자열을 슬라이싱 기법을 활용해 변수에 담아 출력
2.a,b,c,d 라는 변수에 슬라이싱 기법을 통해 .을 기준으로 각각 담는다.
3.step 을 활용해서 172100200100 이 나오게 하기기

'''
s = "ip address = 172.100.200.100"
#1

print(1,s[0:11])
#2

a=(s[13:16])
b=(s[17:20])
c=(s[21:24])
d=(s[25:])

print(2,a,b,c,d)

#3
# s = "ip address = 172.100.200.100"

print(f"3.IP address{a}{b}{c}{d}")


#