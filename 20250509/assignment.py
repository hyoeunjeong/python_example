##1.
#my_tuple = (1, 2, 3, 4, 5)
#print(my_tuple[1:4])

 ##2
#total = 0
#for i in range(1, 5):
#    total += i
#print(total)


##3
#score = 75
#if score >= 90:
#    result = "A"
#elif score >= 80:
#    result = "B"
#elif score >= 70:
#    result = "C"
#else:
#    result = "D"
#print(result)


##3
#text = "Python Programming"
#print(text[7:13])

##4
#student = {"name": "Kim", "age": 20, "grade": "A"}
#student["age"] = 21
#print(student["age"])
##5
#result = 0
#for i in range(3):
#    for j in range(2):
#        result += i + j
#print(result)

##6
#a = 5
#b = 10
#c = 15
#if a > b:
#    print("A")
#elif b > c:
#    print("B")
#elif a + b == c:
#    print("C")
#else:
#    print("D")

##7

#numbers = [2, 4, 6, 8, 10]
#result = []
#for num in numbers:
#    if num > 5:
#        result.append(num // 2)
#print(result)
##8
#data = {"a": [1, 2, 3], "b": [4, 5, 6]}
#result = 0
#for key in data:
#    for num in data[key]:
#        if num % 2 == 0:
#            result += num
#print(result)

'''다음 코드의 빈칸을 채워 리스트 numbers에서 
짝수만 골라내 새로운 리스트 even_numbers에 
저장하는 코드를 완성하세요.'''


#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#even_numbers = []

#for num in numbers:
#    if num %2 ==0:
#        even_numbers.append(num) ##  추가하기 위해서서
#print(even_numbers)  # 출력: [2, 4, 6, 8, 10]



'''
온도에 따라 상태를 출력하는 프로그램을 작성하세요.

온도가 0도 미만이면 "얼음" 온도가 0도 이상 100도 미만이면 
"물" 온도가 100도 이상이면 "수증기" 를 출력합니다.
사용자로부터 온도를 입력받고 위 조건에 맞게 
상태를 출력하는 코드를 작성하세요.
'''

#print("온도를 입력하시오:")
#c =int(input())

#if  0> c :
#    print("얼음")
#elif 0<= c<100:
#    print("물")
#elif c>=100:
#    print("수증기")
#else:
#    print("온도를 다시 입력하시오")


''' 
다음의 학생 점수 딕셔너리에서
평균 점수를 계산하는 코드를 작성하세요.  
'''

#scores = {"국어": 85, "영어": 90, "수학": 78, "과학": 92}

#total =sum(scores.values())
#count =len(scores.keys())
#average = total/count

#print(average)

'''
문자열에서 공백을 제거하고 모두 
소문자로 변환하는 코드를 작성하세요.
입력 문자열은 "Python Programming"이며,
결과는 "pythonprogramming"이 되어야 합니다.
'''
#print("문자열을 입력하시오")
#str_1 = input().split()
#str_2 = str(str_1[0])
#str_3 = str(str_1[1])
#text =''.join(str_2+str_3)
#text_2=text.lower()
#print(text_2)


'''
1부터 사용자가 입력한 숫자까지의 합을
계산하는 프로그램을 작성하세요. 
단, 3의 배수는 제외하고 합을 계산합니다.
'''
#11번
#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#even_numbers = []

#for num in numbers:
#    if num %2 ==0:
#        even_numbers.append(num) ##  추가하기 위해서서
#print(even_numbers)  # 출력: [2, 4, 6, 8, 10]

#12번 
#print("온도를 입력하시오:")
#c =int(input())

#if  0> c :
#    print("얼음")
#elif 0<= c<100:
#    print("물")
#elif c>=100:
#    print("수증기")
#else:
#    print("온도를 다시 입력하시오")

#13번
#scores = {"국어": 85, "영어": 90, "수학": 78, "과학": 92}

#total =sum(scores.values())
#count =len(scores.keys())
#average = total/count

#print(average)


#print("문자열을 입력하시오")
#str_1 = input().split()
#str_2 = str(str_1[0])
#str_3 = str(str_1[1])
#text =''.join(str_2+str_3)
#text_2=text.lower()
#print(text_2)

#15번
print ("숫자를 입력하시오")
numbers =input().split()
total =0
for i in range (1,numbers+1): 
 if i %3 != 0 :
    total += i
print ("1부터", numbers, "까지의 합 (3의 배수 제외):", total)
