#### 반복문
##순회하는 것 [1,2,3,4,5]

#s ='hello'

#for i in s : ##s 변수 i 는 바뀧수 있다 for문안에 내가 지정한 변수(i) 사용가능능
 #   print(i)

#a=[1,2,3,4,5,6,"good"]
#for i in a:
#    print(i)

#for i in range(50): ##0 부터 -1 숫자자 까지의 순회가능한 데이터를 만든다 라고 보면됨
# print(i) ##  range 범위

##range(10,51) 10부터 50까지의 길이를 만든다
#for i in range(10,51):
 #  print(i)

#range (1,11,2)
#for i in range (1,11,2):
#    print(i)    ##11부터 11 까지 2계단씩

##range(5000)  ##range(0,5000,1)

##음수로 만들기 

for i in range(10,-8,-1):
    print(i)


"""
1 부터 100까지 출력
2 부터 50까지 짝수만 출력
10 부터 -1까지 출력력
"""

#for i in range(1,101):
# print(i)


#for j in range(2,51,2):
 #print(j)

#for c in range (10,-2,-1):
 #print(c) 

# for i in range(1,100):
 #  if i %3 ==0 :
  #   print(i) 

## 구구단 만들기 
for i in range(2,10):    ###1번 시작할떄 
  
  for j in range(1,10): ## 위에  for 문에 종속되어 있음 ##9번 실행   둘 곱하면 반복 가능
     print(f"{i}*{j}={i*j}")
     
     if i*j ==9 :
        print(9)
