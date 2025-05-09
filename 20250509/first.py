## 복습 

a =(1,10,1,2,3)


#슬라이싱
b=a[2:5] #123
c =a[1] #1

#기능
c =a.count(1) #2
d= a.index(1) #0 처음 걸리는 위치를 나타낸다.
##모든 1의 위치를 찾고 싶다면

#set 자료구조

a={1,2,3,2}  #중복을 허용하지 않는다
print(a)
print(len(a)) ##중복 허용 하지 않음

#set 생성 

#형변환 list __>set \
a =[1,1,1,2,2,3]
b=set(a)
print(b)

c= list(b)

a ={1,2,3}
##print(a[0])  ##set 은 인덱스로 읽을수 없다다#
d = {"a", 1, 2, 3, 1, "a"}
print(d)

e = list(d)
print(e)
set1 ={1,2,3,4,5}
set2 ={4,5,6,7,8}
print   (f"합집합 {set1|set2}") 
#합집합 {1, 2, 3, 4, 5, 6, 7, 8} 중복 카운트 하지 않음

print   (f"교집합 {set1&set2}")


print   (f"차집합 {set1-set2}")
print   (f"차집합 {set2-set1}")

#대칭 차집합합
print(f"대칭차집합{set1.symmetric_difference(set2)}")
print   (f"여집합 {set1&set2}")

#set 수정

##추가가
fruits ={'apple','banana','cherry'}
fruits.add('orange') ##append 아님님
print(fruits)

##삭제
fruits.remove('apple')
print(fruits)

print(f"set1이 set2의 부분집합인가{set1.issubset(set2)}")

##딕셔너리 dict()

#key:value (키:벨류류)
my_dict ={"me":"길동"}
my_dict2 =dict()
my_dict_1 =dict([("one","하나"),("Two","둘")])
my_dict ={"me":[1,2,3]} ## 키 만 알면 여러 데이터가 들어갈 수 있다다
my_dict3 ={'me':[1,2,3],"me":"good"}
print(my_dict)

### 데이터 추가 

dict4 =dict()
dict4["max"] ="노잼"
dict4["max"] =[1,2,3,4] ##데이터 삽입
print(dict4)

##키는 문자열 인게 보통...


### 예제
'''
dict() 를통해 빈 딕셔너리를 만든 후

데이터 삽입을 하여 키가 4개 , 각각의 밸류에는 다른 타입의 데이터를 넣어서

그 딕셔너리를 출력
'''
#new_dict =dict()
#new_dict["open"] ="열려라"
#new_dict["a"] =[1,9,5,4]
#new_dict["b"] ={"안녕":[8,2,8,2]}
#new_dict["c"] ={"배고파","밥줘"}

#print(new_dict)

#dict5 = dict()
#dict5["age"] = 27
#dict5["b"] = (3, 27, 18)
#dict5["from"] = "busan"
#dict5["a"] = [0, 1, "sim"]
#print(dict5)

##딕셔너리는 데이터가 방대할 때 쓰면 좋다 but 적제적소 
### 데이터 읽기
#a = dict4["Max"]
#person = {'name': 'licat', 'age': 25, 'height': 165.5}
#print(f"일름은:{person["name"]}")
#print(f"나이이:{person["age"]}")

##print(f"나이이:{person["agoo"]}")  Key Error :'good'

##데이터 수정

#person["age"] =30
#print(person)

#person = {'name': 'licat', 'age': 25, 'height': 165.5}
#person["name"]="hyoeun"
##person["age"]=1000

#print(person)


##데이터 삭제
#del  person["height"]
#person["age"]=""
#person["age"]="" #None 키를 남기고 값을 없애고 싶을떼
#print(person)

## 일부만 교체

g = {"good1": {"good2": [1, 2, 3, [1, 2, 3]]}}

#b = {"good1": {"good2": [1, 2, 3, [1, 2, 3, 4]]}}
g["good1"]["good2"][3].append(4) ##1에 접급 --->2에 접근(key) --> 인덱스 찾기(3)-->데이터 추가 -->append(추가하고 싶운거거)
print(g)


person ={'name':"licat","age":25,"city":"seoul"}
#get(키,키가 없을 경우 value)
city = person.get('city',"없는데")
print(city)
city2 = person.get('city2',"없는데") ##내가 찾는 키가 없을 떄 대체값으로 정하는 것을 .get 이라 한다
print(city2)

person ={'name':"licat","age":25,"city":"seoul"}
#키만 가져오는 경우
person_keys =person.keys()
print(person_keys)
#형변환환
a=list(person_keys)
print(a)

##벨류만 추출
person_valuse =person.values() ##벨류값만
print(person_valuse)
b =list(person_valuse)


##전체 추출
person_items =person.items()
print(person_items)  #dict_items([('name', 'licat'), ('age', 25), ('city', 'seoul')])
c=list(person_items)
print(c)

## del person['age'] #지우는것  (권장 x)
a=person.pop("age")  ##지워야 하는데 지우는 값을 알아야 할때 사용용
##값을 지우고 그 지워진 값을  a 에 저장
##제거된 값을 다시사용 할 때 pop

# 전체를 추출
person_items = person.items()
print(person_items) #dict_items([('name', 'licat'), ('age', 25), ('city', 'seoul')])
c = list(person_items) #[('name', 'licat'), ('age', 25), ('city', 'seoul')]
print(c)
print(type(person_items))
#del person['age'] 권장 x
a = person.pop("age") # age라는 키에 있는 값을 a에 저장장
print(a)