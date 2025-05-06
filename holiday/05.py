## 실용문제 (41-50)

##41 : 비밀번호 강도 검사 
#print("비밀번호를 입력하시오")
#password =input()
#len_ok =len(password) >= 8
#number =any(str.isdigit() for str in password) ##숫자포함 여부부
#word =any(str.isalpha() for str in password) ##문자포함여부부
#if (len_ok) and (number) and (word ):
 #   print("안전한 비밀 번호 입니다.")
#else :
 #   print("안전하지 않은은 비밀 번호 입니다.")



##42:단어 뒤집기
#print("문장을 입력하시오")
#text =input().split()
#str1 =text[0]
#str2 =text[1]
#str3 =text[2]

#print(f"{str1[::-1]} {str2[::-1]} {str3[::-1]}")

##43:문자 카운터

#print("문장을 입력하세요")
#text = input().lower()

#li =['a','e','i','o','u']  ##리스트 만들기
#a= 0
#b=0
#for ch in text :
#   if ch.isalpha():
#      if ch in li:
 #        a +=1
     
#      else :
#      b += 1
#print(f"모음 개수 {a}")
#print(f"자음 개수:{b}")


##44:근삿값 계산

#print("실수를 입력하시오 ")
#number =float(input())
#number1 =round(number)
#print(f"가장 가까운 정수: {number1}")

##45.날짜 유효성 검사 

#print("년-월-일을 입력하시오")
#text = input().split('-')
#year,month,day = int(text[0]),int(text[1]),int(text[2])

## 월의 일수 

#if month == '1,3,5,7,8,10,12':
#    day <=31
#elif month =='4,6,9,11':
 #   day <=30
#elif month =='2':   
#    if year %4==0:
 #     day <=29
 #   else :
 #      day <=28
#else : 
 #print("유효하지 않는 날짜 입니다.")

###46: 파일 확장자 추출
#print("파일명을 입력하시오")
#text =input().split(".")
#name = text[0]
#pro_name =text[1]

#print(f"확장자:{pro_name}")


##47:문자열 압축
#print("문자를 입력하시오")
#text =input()
#compress = ""##결과 저장할 변수
#count_number =1 ##무조건 1개부터 시작
#for ch in range(1,len(text)) :
#    if text[ch] == text[ch-1]:
#        count_number +=1
#    else:
#        compress +=text[ch -1] +str(count_number)
#        count_number =1
#
#compress += text [-1]+str(count_number)

#print(f"압축된 문자열 :{compress}")

###48 :팰린드롬 검사
#print("문자를 입력하시오")
#text =input()
#if text == text[::-1]:
#    print(f"'{text}'은 팰린드롬 입니다.")
#else:
#    print(f"'{text}'은 팰린드롬이 아닙니다.")

##49 :간단한 암호화 
#print("문자열을 입력하세요:")
#text = input().upper()  # 대문자로 변환

#result = ""
#for ch in text:
#  if ch.isalpha():  # 알파벳일 때만 처리
#        shifted = (ord(ch) - ord('A') + 3) % 26 + ord('A')
#        result += chr(shifted)
#    else:
#        result += ch  # 알파벳이 아니면 그대로 추가

#print("암호화:", result)





###50 :ip주소 검증

#print("ip 주소를 입력하세요.")
#ip_adress =input().split(".")
#number1 =int(ip_adress[0])
#number2 =int(ip_adress[1])
#number3 =int(ip_adress[2])
#number4 =int(ip_adress[3])
#if len (ip_adress) != 4:
#    print("유효하지 않은 ip 주소 입니다.")
#ch_number1 = 0<=number1<=255
#ch_number2 = 0<=number2<=255
#ch_number3 = 0<=number3<=255
#ch_number4 = 0<=number4<=255
#if ch_number1 and ch_number2 and ch_number3 and ch_number4:
#    print("유효한 ip 주소 입니다.")

#else : 
#    print("유효하지 않은 ip 주소 입니다.")