# 20250430 오전강의

#a =9
#b =21

#if a>10:
 #   print("good")
#elif b == 20: #if 첫 if 가 거짓이면 elif 로 들어간다.
#    print("20입니다.")
#elif a ==10:
#    print("10입니다.")  #값이 20입니다 나옴
#else: 
  #print("이도저도 아니다")
'''
    20나오는 이유 코드는 위에서 아래 로 읽는다 즉 위에 실행되는 
    if가 있다면 그것 이 실행된다.
    
 '''

    #조건문에서 이도저도 아닌 상황은 --->  else 를 사용한다.   

    
#split() 활용
#a,b 변수를 활용,
#키,몸무게를 입력받는다.

#키와 몸무게를 나눈 나머지를 출력한다.

#조건문을 활용해서

#키(a)가 130 이상이면 a, 150이상이면 b, 170 이상이면 c 180 이상면이면 d를 출력하세요요 


#print("키 와 몸무게를 입력하시오")

#answer=input().split(" ")
#cm,kg =int(answer[0]),int(answer[1])

#c=cm % kg

#print(c)
#if cm >= 130:
#    print("a")
#elif cm >= 150:
#    print("b")
#elif cm >= 170:
#    print("c")
#elif cm >= 180:
#    print("d")


#a= 185

#f a>= 130:
 #  print("130 이상입니다.")

#if a>= 180:
#    print("d")
#elif a>=170:
# print("c")
#elif a>=150:
# print("b")
#else:
#  print("a")


#score=input("점수를 입력하세요.")
#score =int(score)

#score =int(input("점수를 입력해주세요"))
#if 90<= score <=100 :
#    print("A")
#elif 80<= score <=89:
#    print("B")
#elif 70<= score <=79:
#    print("C")
#elif 60<= score <=69:
#     print("D")
#else:
#    print("F")

#들여쓰기 오류나는 이유
#why??? 콜론 뒤(들여쓰기 블록 )
#뒤에  주석처리를 한다면 말이 안된다.--> 즉 에러발생

#and or 연산활용

#a=10
#b=20

#if a ==10  and b ==20:
 #print("good")

#else:
 #print("no")

'''
a,b,c 를 입력받는다.
a가 100이고 b가 200이상이면 "a"를 출력
b가 1이면 "b"를 출력
이도저도 아니면 c를 출력
'''
print("숫자를 입력해주세요")
a,b,c = input().split(" ")  
#강사님예시 a,b,c =int(input()),int(input()),int(input())
a,b,c=int(a),int(b),int(c)

if a ==100 and b >=200:
    print("a")

elif b ==1 :
    print("b")

else :
 print("c")

 #elif로 마무리 해도 가능 하지만 만약 참이 아닌경우 거짓이 나왔을때 처리가 어려움
 #가능은 하지만 (이도저도 아닐떄)힘듬---> 요구사항에 따라 달라지긴한다다


 #a,b,c =input().split(" ")
#a,b,c=int(a),int(b),int(c)

#if a==b==c: #모두 같을때  
#    print( 10000+a*100)

#elif a ==b or a==c or c==b: #두개만 같으때
   
#   if a ==b: 
#    print(1000+a*1000)
#   elif a==c:
#     print(1000+a*100)
#   else:
#    print(1000+b*100)


#else: #모두 다를때

 #   print(max(a,b,c)*100)

#강사님 시범 (max 안쓴 버전)
#중첩 if문 
#a,b,c=input().split()
#a,b,c =int(a),int(b),int(c)

#if a==b==c:
#    price =10000+a*1000

#같은 눈 2개일 경우
#elif a ==b:
#    price =1000 + a*100
#elif a ==c:
#    price =1000 + a*100
#elif b ==c:
    #price =1000 + a*100

#else:
#    price =0 #이도저도 아닌경우 (위에처 참이 아니라면 문제가 발생한다.)
#혹시 모를 오류를 대비하여서 초기화 해주는 것


#모두 다른 눈일때 최댓값 찾기기
#if a!=b and b !=c and a!=c:
#    temp =a
#    if b>temp:
#        temp =b
#    if c>temp:
#        temp =c
#    price =temp *100
#print(f"상금:{price}원원")