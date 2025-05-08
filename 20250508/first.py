#food = input()

#if food.find("짜장") != -1:
#    if "쟁반" in food:
#        print("쟁반짜장입니다.")
#else:
#    print("짬뽕입니다.")

##리스트 복습
## like 장바구니
#a =[1,2,3,4,5] ## 요소의 개수---> 5개 
##요소의 갯수 len() --길이찾는거
#len은 문자열에 도 사용 가능 '순서가 있는 리스트 시퀀스 자료형
#인덱스  -->0번 부터
#print (len(a))
#print(a[0])##  인덱싱
#print(a[-1]) ##마지막 부터터

#print(a[1:3])##슬라이싱 뒤에 숫자는 포함 ㄴㄴ 결과 2,3

#b=[1,"2","good",4]
#리스트 안에 리스트 넣기 중첩 리스트트

##1.
c = [1, "2", "good", 4, [1, 2, 3, [123, "good"],31],2]

print(c[2]) 
print(c[4][3][1])
print(c[4][3][0:2])



###a = stack  last in  first out
## stack Queeve 


#a =[1,2,3,"good"]
#a[0] =3
#print("aaa")
#print(a)
#a[3]="aaa"
#print(a)

##a[3][1] ="g" #str 문자열의 특정 값을 새로운 값으로대체 할수 없다다
##자료구조의 중복을 허용한다.


##메소드 
##데이터 추가가
#li = []
#li.append(1) 
#li.append(2) 
#li.append([1,2,3,4])
#print(li)
#li[2].append("good")
#print(li)



###데이터 삭제

#li.clear()#####리스트는 남아있고 안에 있는 데이터만 삭제 되는것
#print(li)


#b=[1,2,3]
#c=b
#c.append(123)
#print(b)


#c=b.copy()
#c.append(2)
#print(b)
#print(c)

#1.빈리스트를 만든다.
#2.append를 사용하여 이중 리스트를 만든다.
#3.출력한다.
#4.리스트의 데이터를 다 지운다.
#5.출력한다.
#6.copy를 활용한다.
#7.카피를 활용한 리스트에 append를 사용하여 출력한다.

#### 연습문제 
#li=[]
#li.append(1)
#li.append("good")
#li.append([1,2,3])


#print (li)

#li.clear()
#print(li)

#lili=li.copy()
#lili.append("haha")
#print(li)
#print(lili)


####count
a =[1,2,3,'okey',1,1,1,]
print(a.count(1))##4


b=[1,2,3,[1,2,3,1]]
print(b.count(1)) ##리스트 안에 ㄴㄴㄴ


print(b.count(1))

print(b.count(1)+b[3].count(1))

#Windows : Shift + Alt + F
#macOS : Shift(⇧) + Option(⌥) + F
#Linux : Ctrl + Shift + I
#formatter

#extend
a=[1,2,3,4]
b=[5,6,7,8]

#[1,2,3,4,5,6,7,8]   ##순회가 되어야 한다다
a.extend(b)
print(a)
c="good"
b.extend(c)
print(b)

###인덱스

a=["good","okey"]
b= a.index("good")
print(b)

try:
    a.index('aaa')
except:
    print("에러")


##