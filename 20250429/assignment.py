#6025

#a1,a2 = input().split()
#a1 ,a2=int(a1) ,int(a2) 
#b=a1+a2
#print(b)


#6026

#a1=input()
#a2 =input()
#a1,a2 =float(a1),float(a2)
#b= a1+a2
#print(b)


#6032

#a =input()
#a =int(a)
#print(-a)

#6033
#a = input()  # 예: 'A', 'z', '0' 등
#print(chr(ord(a + 1)))  
## ord(a) → 입력받은 문자를 유니코드 숫자로 바꿈


#6034 다시공부하기 
#a =input().split(" ") #문자열러 입력이됨됨
#a1,a2 =int(a[0]), int(a[1]) #-->문자열을 정수로 바꿔줌 -->인덱스 사용용
#b= a1-a2
#print(b)

#6035
#a = input().split(" ")
#a1,a2=float(a[0]),float(a[1])
#b =a1*a2
#print (b)

#6036

#a,b =input().split(" ")
#b= int(b)
#print(a*b)

#6037

#a=input()
#b=input()

#a= int(a)
#print(a*b)

#6038

#a =input().split(" ")
#a1,a2 =int(a[0]),int(a[1])
#b=a1**a2
#print(b)

#6039 #추가공부 하기기
#a= input()
#a= int(a)
#print(a<<1)

'''
예시
n = 10
print(n<<1)  #10을 2배 한 값인 20 이 출력된다.
print(n>>1)  #10을 반으로 나눈 값인 5 가 출력된다.
print(n<<2)  #10을 4배 한 값인 40 이 출력된다.
print(n>>2)  #10을 반으로 나눈 후 다시 반으로 나눈 값인 2 가 출력된다.
'''
#6039

#a =input().split(" ")
#a1 ,a2 =float(a[0]),float(a[1])
#b = a1**a2
#print(b)

#6040
#a =input().split(" ")
#a1,a2 =int(a[0]),int(a[1])
#b= a1//a2
#print(b)

#6041

#a =input().split(" ")
#a1,a2 =int(a[0]),int(a[1])
#b= a1%a2
#print(b)

#6043
#a =input().split(" ")
#a1,a2 =float(a[0]),float(a[1])
#b= a1/a2
#print(f"{b:.3f}")

#6044

#a = input().split()
#a1,a2 =int(a[0]),int(a[1])
#b =a1+a2
#c=a1-a2
#d= a1*a2
#e=a1//a2
#h=a1 %a2
#g= a1/a2

#print(b) 

#print(c) 

#print(d) 

#print(e) 

#print(h) 

#print(f"{g:.2f}")

#6047 #추가공부하기
#a= input().split(" ")
#a1,a2 =int(a[0]),int(a[1])

#print(a1<<a2)  #<< 2제곱표현현

#6048
#a =input().split()
#a1,a2 =int(a[0]),int(a[1])

#if a1 < a2:
  #  print("True")
#else:
 #   print("False")


#6049

#a =input().split(" ")
#a1,a2=int(a[0]),int(a[1])

#if a1 == a2:
#    print("True")

#else:
#    print("False")

#6050

#a =input().split(" ")
#a1,a2=int(a[0]),int(a[1])

#if a1<= a2:
#   print("True")

#else:
#    print("False")


#6051
#a=input().split(" ")

#a1,a2 =int(a[0]),int(a[1])

#if a1!=a2:
#    print("True")

#else :
#    print("False")



#6052

#a =input()
#a=int(a)

#if a == 0 :
# print("False")
#else:
# print(True)


#6053 (멘토님께 질문하기 bool 타입 )

a =bool(int(input()))

if a == False:
    print ( not a)
else:
   print ( a)