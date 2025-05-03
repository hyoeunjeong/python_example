#2025 05 03
#입력과 출력

##1. 인사하기
#name = input()
#print("안녕하세요,",name,"님!") #이렇게 하면 띄어쓰기 됨 
#print(f"안녕하세요,{name}님!")

##2 에코 프로그램

#str1=input()
#print(str1*3) # 문자열 반복출력시 ((반복할 문자열)*(반복할 수))


##3 나이 계산기

#year =input()
#year =int(year)
#age =(2025-year)
#print(f"당신의 나이는 {age}세 입니다.")


##4 원의 넓이 계산

#r =input()
#r=float(r)
#PI =3.14
#area =(r**2*PI)
#print(f"반지름이 {r:.0f}인 원의 넓이:{area}") #r정수일 경우
#print(f"반지름이 {r}인 원의 넓이:{area}") #아닐 경우

##5 여행거리 계산
#print("시속 (km/h )과 시간 (hour)를 입력하시오")
#speed=int(input())
#hour =int(input())

#distance =speed*hour

#print(f"총 이동 거리: {distance}km ")


##6.문장합치기
#first =input()
#second =input()

#print(first + second)


##7. 인치 -센티미터 변환

#inch = float(input())

#cm =inch *2.54
#print(f"{inch}인치는 {cm}센티미터 입니다.") #실수일 경우
#print(f"{inch:.0f}인치는 {cm}센티미터 입니다.") #정수 일경우

##8.팁계산기

#price =int(input())
#tip_percent = int(input())

#tip =price*(tip_percent /100)

#total_price =price + tip
#print (f"팁 금액: {int(tip)}원") # 정수형으로 
#print(f"총 지불 금액:{int(total_price)}원")

##9 BMI 계산기
#print("키를 입력하시오")
#cm = float(input())
#cm_m =cm/100    ##cm ----> m
#print("몸무게를 입력하시오")
#kg = float(input())

#BMI = kg/cm_m**2  # **2 제곱 
#print(f"BMI:{BMI:.2f}")

#10 다중입력
#print(" 숫자를 공백으로 입력하시오 .")
#number =input().split()
#number1 =int(number[0]) #첫번째
#number2 =int(number[-1]) #마지막
#print(f"첫번째 숫자:{number1}")
#print(f"마지막 숫자:{number2}")