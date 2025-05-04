####연산자

##31:사칙연산 계산기

#print("숫자를 입력하시오:")
#number1 = int(input())
#print("연산자를 입력하시오:")
#operator =input()
#print("숫자를 입력하시오:")
#number2 = int(input())
#result1 = number1 + number2
#result2 = number1 - number2
#result3 = number1 * number2
#result4 = number1 / number2

#if operator == '+':
#    print (f"{number1}{operator}{number2} ={result1}")

#elif operator == '-':
#    print (f"{number1}{operator}{number2} ={result2}")

#elif operator == '*':
#    print (f"{number1}{operator}{number2} ={result3}")

#elif operator == '/':
#    print (f"{number1}{operator}{number2} ={result4}")


## 32:세금 계산기

#print("금액을 입력하시오")
#money = float(input())
#print("세율을 입력하시오")
#tax_per = float(input())

#tax =money *(tax_per/100)
#af_tex = money -tax

#print(f"세금:{tax}원")
#print(f"세후 금액:{af_tex}원")


##33: 논리 연산 테이블



###34 할인계산기

#print("원래 가격을 입력하시오")
#price = float(input())
#print("할인율을 입력하시오")
#discount =float(input())

#discount_price =price *(discount/100)
#af_price =price -discount_price

#print(f"할인 금액:{discount_price}원")
#print(f"최종금액:{af_price}원")


##35 큰수 판별 (max()사용)

#print("숫자를 입력하시오")
#number1 = int(input())
#print("숫자를 입력하시오")
#number2 = int(input())
#print("숫자를 입력하시오")
#number3 = int(input())

#print(max(number1,number2,number3))


##35-1 :큰수 판별(조건문 활용)


#print("숫자를 입력하시오")
#number1 = int(input())
#print("숫자를 입력하시오")
#number2 = int(input())
#print("숫자를 입력하시오")
#number3 = int(input())

#if number1 > number2:
#    print(number1)

#elif number2 > number3:
#    print(number2)

#elif number1 > number3:
#    print(number1)

#elif number3 > number1:
#    print(number3)

#elif number2 > number1:
#    print(number2)
#elif number3 > number2:
#    print(number3)



##36 :윤년 판별

#print("년도를 입력하시오")
#year =int(input())

#if (year %4 == 0 and year % 100 !=0 )or year %400 ==0 :
#    print(f"{year}년 은 윤년입니다.")

#else:
#    print("윤년이 아닙니다.")


##37 : 문자열 포함 여부

#print("문자열을 입력하여 주시오:")
#str1 = input()
#print("문자열을 입력하여 주시오:")
#str2 = input()

#if str2 in str1 : 
#    print(f'"{str1}"에"{str2}"이(가)포함되어 있습니다.')
#else :
#     print(f'"{str1}"에"{str2}"이(가)포함되어 있지 않습니다.')




##38:조건부 출력

#print("점수를 입력하시오:")
#score =int(input())

#if score >= 90:
#    print("학점:A")
#elif score >=80:
#    print("학점:B")
#elif score >=70:
#    print("학점:C")
#elif score >=60:
#    print("학점:D")
#else:
#    print("학점:F")


##39 :자릿수 합계

#print("양의 정수를 입력하시오") 
#number =int(input())

#number = str(number)



##40 :복합조건

#print("나이와 회원여부(Y/N)을 입력해주세요.")
#text= input().split()
#age= int(text[0])
#membership = str(text[1])

#if age >=19 and membership == 'N' :
#    print("입장료:10000원")

#elif age >=19 and membership == 'Y' :
#    print("입장료:8000원")

#else:
#    print ("입장료: 5000원")

