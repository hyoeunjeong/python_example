'''input() #입력
코드 실행되는 동안에는 메모리에 있다'''
#입력구현

#a =input() #메모리에 값이

#print(a)

#print("okay")

'''
입력을 몇가지 변수에 담아서
f-string, 문자붙이기, 문자반복하기 등 여러 기술을 활용해 출력하세요.
'''

#name = input("당신의 이름은? ") #문자로 받는다.
#age =input("당신의 나이는?")
#ms =input ("하고 싶은말은?")
#print(f"안녕{name}아 {age}살이구나~~{ms}라니 나도 동의해해")




#형변환 
#print(type(a))
#b= int(a) # 문자를 숫자로 ----문자 입력시 오류뜸
#print(type(b))



#print(type(a))
#b= int(a) # 문자를 숫자로  
#print(type(b))

#a=1

#print(type(str(a)))

#1을 문자로 만들수 있다.1



#문자열 고유 기능 
s = 'weniv CEO licat'
print(s.lower())  #입력한 문자를 소문자로 바꿔 준다
print(s.upper())  #입력한 문자를 대문자로 바꿔 준다



s = 'weniv CEO licat'

#print(s.find("good")) #good 을 찾는것(-1)이라고 뜸 
#print(s.index("good")) #ValueError: substring not found 

print(s.find("weniv"))  #값을 못찾으면 -1출력력
print(s.find("licat"))

#위에 값 1번은 0 2번은 10이 나온다 즉 결과값은 시작위치를 의미한다.

print(s.index("weniv"))  
print(s.index("licat")) #값을 못찾으면 에러가 나온다

'''
index와 find 그 값은 동일 하지만  find는 찾지 못하면 -1을 출력하고 
index 는 에러로 뒤에 것 실행이 안됨 

index는 예외 처리를 해줘야 한다 왜냐하면 값을 찾지못한다면 코드가 실행이 아예 안되기
때문이다. 둘다 사용한다.
'''


#count()
#특정 문자열이나  숫자의개수를 셀때 사용하는 것

print(s.count("i")) #문자열에서 i를 찾아라

s2 =s.replace("CEO","CTO") # ceo를 cto로 변경하는것것

print(s2)


s3 ="weniv-corp" #split() 문자열을 나누는것
#s3.split("") # 공백으로 분리리
#s3.split("-")#-를 기준으로 나눈다. 
'''
값이 2개로 분해된다다
'''
s4,s5 =s3.split("-")
print(s4,s5)

## 입력이 들어온다. 키 몸무게 성별 나이 이름
##이것을 공백을 기준으로 쪼개어 각 변수에 담아 출력한다.
##이름을 f-string통해 세번 반복해서 출력한다.
#print("키, 몸무게, 성별 ,나이,이름을입력하시오")
#inform =input()
#inform1,inform2,inform3,inform4,inform5 =inform.split(" ")
#print(inform1,inform2,inform3,inform4,inform5)

#print(f"{inform5*3}")


## .join

s20 =["modu","labs"] #리스트 형태  바구니 같은 형태 현재 바구니 안에 2개의 값 가지고 있음
print("-".join(s20))#-.을 기준으로 합쳐라
print("".join(s20)) # 그냥 모두 합쳐서 출력
'''문자를 자르고 붙일 수 있다 어떤 값을 가지는 바구니 , 목록'''



##format

name ='licat'
age =29

print('제이름은 {}이고,나이는 {}살 입니다.'.format(name,age))
#요즘은 print(f'제이름은 {name}이고,나이는 { age}살입니다.')



print("Hello\nWorld!") # Hello와 World! 사이에 줄바꿈이 일어납니다.
print("Hello\tWorld!") # Hello와 World! 사이에 탭 간격이 생깁니다.
print("She said, \"Hello World!\"") # 큰따옴표 내부에 문자열을 출력합니다.
print('She said, \'Hello World!\'') # 작은따옴표 내부에 문자열을 출력합니다.
print("Backslash: \\") # 백슬래시를 출력합니다.
'''
("")를 출력하려면 \를 사용해야 한다 

'''


#논리(bool)과 none자료형
'''논리 자료형이란 true, false를 가지는 자료형  
참과 거짓 0과 1을 가지는 것들'''


#bool 타입
#a = 10>3 #왼쪽기준 
#b= True # 무조건 대문자
#c = False #무조선 대문자자
#print(type(a))
#print((a))

''' '''

##형변환
a=1
b=0
c=-1
d ="okay"
f=""
print(bool(a))
print(bool(b))
print(bool(c))
print(bool(d))
print(bool(f))

#0을제외한 모든 숫자의 값은  true 
#d는 왜 ?? --> d 에도 데이터가 있어서서
#f는 데이터가 아무것도 없어서 거짓

print(a==b) #a와 b 값이 같니? 거짓 출력


x=None #아무것도 없다는 뜻이다.