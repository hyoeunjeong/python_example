#논리 연산자 

'''
1. and
2. or
3. not
'''
##다른언어에서는
## a &&b
## python -->



#논리곱 연산자 (and)
#a = True
#b = True

#c = a and b


#d = 10>5 and 10 <5 # d ture and false ---? 0 (즉 flase)
##print(d)

#논리합 연산자 -- 하나라도 일이라면 1 이라면 ture (or)

#f =10 >=10 or False #앞에 이미 1(ture가 나와서 뒤에 값에 상관없이 1,ture 가 출력된다.)

#print(f)


#세개 항

#f = False and True and True #0 11

#print(f)

#f2 =(False or True) and True

#print(f2)


#not -->. 반대 not Ture (반대값)

#f3 =not((False or True)and True)

#print(f3)


#a=10
#b =20

#c = a!=b #다르니?? 라고 물어보는 것
#c = a==b #같니???  라고 물어보는 것 

'''
실무에서는 저렇게 까지 장황하게 쓰지는 않음 
나중에 조건문 =논리와 함께 사용된다
실무에서는 조금더 어렵게 사용된다.
'''


### 예시 문제
#a =int(input())
#b =int(input())
#c =int(input())

### 항은 3개 이상 and ,or  는 마음대로 연결하여 결과 출력

#a =int(input("첫번째 숫자를 입력해 주세요 :"))
#b =int(input("두번째 숫자를 입력해 주세요 :"))
#c =int(input("세번째 숫자를 입력해 주세요 :"))

#result =( (a<10) or(b>=6)  and (c<=15))
#print(result)



#할당연산자
'''기본적 할당 연산자는 = 입니다.'''

#=10

# =a+ 10   # == a+= 10 (덧셈 대입입)
 #r계산이 완료된 이후 a에 할당된다.

#멤버 연산

#st ="modulabs is good"

#sta =" good"in st # good 이 st 안에 있다
#sta =" good" not in st # good 이 st 안에 없다.


#6042
#[기초-값변환] 실수 1개 입력받아 소숫점이하 자리 변환하기(설명)(py)

#a= input()
#a= float(a)
#print(format(a,".2f"))



#6045
# [기초-산술연산] 정수 3개 입력받아 합과 평균 출력하기(설명)(py)

#a =input()
#a1,a2,a3  =a.split(" ")
#a4=int(a1)
#a5=int(a2)
#a6=int(a3)
#b=a4+a5+a6
#c= b/3
#print(f"{b} {c:.3f}")


#if 문
'''
조건문 :조건문은 특정 조건에 따라 코드를 실행할 수 있게
프로그램 해주는 조건의 문이다.

'''


#age =19
#height =140
#if age > 18 and height >=150:  #참이면 밑에것 실행,거짓이면 통과한다
 #   print("성인입니다")


#print("안녕하세요")

#if =10 #이것은 예약어 여서 변수로 사용할수 없다.


#age =19
#height =140
#if age > 18 or height >=150:  #참이면 밑에것 실행,거짓이면 통과한다
   # print("성인입니다")


#print("안녕하세요")


'''
if 입력한 비밀번'''

#if ~ else 
#구문 if 가 참이 아니라면 else 구문을 실행

#age =20

#if age>=30:
   # print("30대 이상입니다.")
#else:
#    print("30대가 아닙니다다")

#if ~else ~else 구문

#age =30

#if age <=19:
   # print("청소년 입니다.")

#elif age <30:
 #   print("성인 입니다.")

#else:
 #   print("30대 입니다")
    



#예제 문제

#한줄에 생년월일(yyyy) 월(mm) 일(dd) 가 공백을 기준으로 입력된다.
#년도가 짝수라면 "짝수 년도에 태어났습니다." 아니라면 "홀수 년도에 태어났습니다 를 출력)

#a=input()
#yyyy,mm,dd =a.split()
#yyyy =int(yyyy) #int 로 받는 다는거 꼭 기억하자 
#mm =int(mm)
#dd =int(dd)
#if yyyy % 2 == 0:
#    print("짝수 년도에 태어났습니다.")

#else:
#    print("홀수 년도에 태어났습니다.")




#강사님 시범

yyyy,mm,dd =input().split()
yyyy,mm,dd =int(yyyy),int(mm),int(dd)

if yyyy % 2 == 0:
    print("짝수 년도에 태어났습니다.")
else:
    print("홀수 년도에 태어났습니다.")