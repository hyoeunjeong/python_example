# 비교연산

#x,y =10,100
#print(x==y) #.x랑 y 값이 같나요 다르나요 -->다르기에 
#false 출력
#x,y =10,11
#print(x>y) #초과
#print(x>=y) #이상 
#print(x<y) #미만
#print(x<=y)# 이하

#print('apple'<"banana") #결과 :ture
#알파벳으로는 a 가 b 보다 먼저 이여서 더 작은것으로 생각된다.

#print(5<x<15) #결과 ture



#input() 으로 키와 몸무게를 입력받는다. (숫자형으로 변환)
#키가 130 이하이면 "키 미만"을 출력하고,
#몸무게가 10 이상이면 "정상"을 출력하세요
#print (" 키와 몸무게를 입력하여 주세요.")
#answer =input()
#height1,weight1 =answer.split(' ')
#height = float(height1)
#weight = float(weight1)

#print(height <=130,"키 미만")
#print(weight>=10,"정상")



#a= "good"


#예제 문제제
#print(len(a)) #len(변수)는 뱐숭의 문자를 수를 가져온다

#input() 두 번을 사용하여, 두개의 변수의 임의의 문자열을 넣고,
#len() 을 사용하여 문자의 수를 변수에 넣는다.

#'첫번째 변수의 문자 수는 {문자의 수} 입니다.'
#'두번째 변수의 문자 수는 {문자의 수} 입니다.'


#print("첫번째 문자를 입력하세요")
#first =input()
#print("두번째 문자를 입력하세요")
#second =input()

#str1=len(first)
#str2=len(second)

#print(f"첫번째 변수의 문자 수는 {str1} 입니다")
#print(f"두번째 변수의 문자 수는 {str2} 입니다")


#s1 =input()   #s1이라는 변수에 문자열을 입력 받는다
#s2 = input()  #s2이라는 변수에 문자열을 입력 받는다

#s3 = len(s1) # len() 을통해 s1 변수의 문자열 수를 가져온다.
#s4 = len(s2) # len() 을통해 s2 변수의 문자열 수를 가져온다.

#print(f"첫번째 변수의 문자 수는 {s3} 입니다.")
#print(f"첫번째 변수의 문자 수는 {s4} 입니다.")



#i =10
#j=10.5555555

#print(f"j의 값은 {j:.2f}") #f=float  소수점 둘째자리까지 표현한다 
#j의 값은 10.56


#콤마 3개 1000씩 끊어
#money =100000000000000000
#print(f"{money:,}") #디폴트가 3이다


#PI =3.141592

#print(f"{PI:.2f}") #f말고 float를 입력하면 오류가 난다.