## 변수와 타입 (11-20)

##11.변수 교환

#a =int(input())

#b =int(input())
#print(f"교환 전:a = {a},b ={b}")

#a,b =b,a

#print(f"교환 후:a = {a},b ={b}")

##12. 문자열 정보 출력

#str1 =input()
#a =len(str1)
#str2 = str(str1[0])
#str3 = str (str1[-1])
#print(f"문자열 길이:{a}")
#print(f"첫글자:{str2}")
#print(f"마지막 글자:{str3}")


##문제13 :이니셜 만들기    ##### 질문 ########
#print("성 이름 을 입력하세요.")
#name = input().split()
#surname = str(name[0])
#first_name =str(name[1])
#initials1 = surname[0].upper()
#initials2 = first_name[0].upper()
#print(f"이니셜:{initials1}.{initials2}.")


##14:소수점 자릿수

#number =float(input())
#print(f"{number:.2f}")


##15 : 나이구간 판별

#print(" 나이를 입력하시오 .")
#age = int(input())

#if age <19:
#    print("미성년자")
#elif 19<=age<=34:
#    print("청년")
#elif 35<=age<=64:
#    print("중장년")
    
#else:
#    print("노년")


##16:문자열 분석
#print("문자열을 입력하시오.")
#text =input()

#blank_count=0
#number_count=0
#letter_count =0

#for ch in text:  ##문자열에서 한글자씩 반복
# if ch == (' ') :
#   blank_count +=1
   

# elif '0'<=ch<= '9' :  ##ch 는 문자열이여서 int 와 비교 불가가
#    number_count +=1
   
    
# else:
#    letter_count += 1
#   
#print(f"공백수:{blank_count}")
#print(f"문자의 수:{letter_count}")


##17:참/ 거짓 (bool)
number =input()

print(bool(number))



##18:홀짝 판별

#print("숫자를 입력하시오:")
#number =int(input())
#if number%2 ==0:
#    print(f"{number}은(는)짝수입니다.")

#elif number %2 ==1:
#     print(f"{number}은(는)홀수입니다.")


##19:문자열 분할
#print ("단어를 입력해주세요")
#text =input().split()

#reslt =",".join(text) #split()의 반대개념
#print(reslt)


##20 :온도 단위 변환기
#print("온도를 입력하시오")
#a =float(input())
#print("단위를 입력하시오")
#b =input()


#if b =='c':
#  f= a*9/5 +32
#  print(f"{a}°C는{f}°F입니다.")
#else :
# c= (a -32)*5/9
# print(f"{b}°C는{c}°F입니다.")