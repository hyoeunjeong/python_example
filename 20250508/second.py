##insert 

#a =[1,2,3,4,5]

#a.insert(0,0) ##(인덱스,값)
#print(a)

##pop() ## 제일 끝에 있는 추출
##리스트 값이 비어있으면 index:pop from emty list
#b= a.pop()
#print(a)
##뽑은뒤 ---> 저장
# 미연에 방지하려면??
#if len(a) >=1 :
 #   a.pop()
#else:
 #   print("리스트가 비었습니다다")

    ##remove(값을 찾아서 지우는 것)
#c=[1,2,3,1,1]
#c.remove(1)
#print(c)
#c.remove(1)
#print(c)


## 예시문제
'''
기존에 데이터가 있는 리스트를 만든다.
insert를 활용해서 데이터를 넣는다.
pop을 사용하여 꺼낸 데이터를 출력한다.
remove를 사용하여 특정 데이터를 제거해본다.
                  
'''

#li =["봄","가을","겨울"]
##li.insert(1,"여름")
#print(li)

#li.pop()
#print(li)

#li.remove("봄")
#print(li)
#``` python
#```


##   리버스

#[1,2,3]
#[3,2,1,]

#a=[1,2,3,4,5]
#a.reverse() ##[5,4,3,2,1] ##원본 데이타 변경 권장 ㄴㄴ

#print(a)
#b= a.append(1)   ##행위를 하지만 결과값을 반환하지 않는다다

##print(b)

#a=[1,2,3,4,5]
#print(list(reversed(a)))  ##괄호 안에서 부터 해결결
#print(a)
#print (b)


##sort sorted  
#a =[5,4,3,2,1]
#a.sort() ##rever 와 똑같
#print(a)
#print(b)
#### 오름 차순순
#a =[5,4,3,2,1]     
#b=list(sorted(a)) ##rever 와 똑같
#print(a)
#print(b)

####내림 차순
#c=[1,2,3,4,5]
##sorted(리스트 ,reverse = bool)
#d= sorted(c,reverse = False) # dorted(a)
#d =list(sorted(c,reverse = True))
#print(d)

##튜플 tuple list  ##읽고 사용만 가능 
a =(1,2,3)  ##수정할수 없음 수정이 안될뿐 가져더 쓸수 있음

print(type(a))
print(a[2]) ##인덱싱 쌉가능
b=a[0:2]## 슬라이싱 사용가능
print(b)

numbers =(3,1,4,1,5,9,2,6,5,3)
print(numbers.count(5))
print(numbers.index(5))