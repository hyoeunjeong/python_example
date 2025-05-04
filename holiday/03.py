##문자열 다루기 (21 ~30)


##21 :문자열 다루기
#str1 =input()

#print(f"대문자:{str1.upper()}") #모두 대문자로로
#print(f"소문자:{str1.lower()}")  #모두 소문자로로
#print(f"첫글자만 대문자:{str1.title()}") #맨 앞자리만 대문자로로


##문제22: 문자열 슬라이싱

#text=input()

#str1 =text[0:3] ## 앞에서 세번째 까지 
#str2 =text[-3:] ##뒤에서 세번째 까지 인덱싱
#str3 =text[::-1] ## 거꾸로로

#print(f"앞 3글자:{str1}")
#print(f"뒤 세글자:{str2}")
#print(f"거꾸로:{str3}")

##문제23:단어 위치 찾기      ####문제지에서는 14 ---> 답은 17

#text =input("문장을 입력하시오.")
#word =input("찾으실 단어를 입력하시오.")

#index=text.find(word)

#if index != -1: ##찾는 단어가 문장안에 있다면 이라는 뜻이다다
#    print(f"단어'{word}'의 위치:{index}")

#else:
#    print("단어가 존재하지 않습니다.")

##24: 문자 교체
#print("문장을 입력해주세요.")
#text = input()
#print("교체할 문자를 입력해주세요.")
#old_word =input()
#print("새 문자를 입력해주세요")
#new_word =input()

#changed = text.replace(old_word,new_word)  ##문자교체
### .replace(변경될될것,변경할것)

#print(changed)


##25 :문자 출현 횟수
#print("문장을 입력하세요.")
#text = input()
#print("찾으실 문자를 입력하세요.")
#find =input()
#number =text.count(find)  ##특정문자 출현 횟수 계산산

#print(f"문자 '{find}'의 출현 횟수 :{number}")


##26 :이메일 유효성 검사

#print("당신의 이메일을 작성해주세요.")
#email = input()
#if "@" in email: ## 이메일 안에 @ 이 있는가 
#    print ("유효한 이메일 주소 입니다")

#else :
#    print("유효한 이메일 주소가 아닙니다.")


##27 : 문자열 패딩

#print("문자를 입력하시오")
#text =input()
#print("원하시는 길이를 입력하시오")
#length =int(input())

#if len(text) <length:
#    add ='*'* (length -len(text))
#    text += add

#print(text)



### 28:문자열 중앙 문자

#print("문자열을 입력하시오")
#text = input()
#length =len(text)
#center1 =text[length//2]
#center2 =text[length//2-1]
#if len(text) % 2 == 1 :
#    print(f"중앙 문자:{center1}")

#elif len(text) %2 ==0:
#    print(f"중앙문자:{center1},{center2}")




##29 :특수문자 제거
#print("문자열을 입력하시오")
#text =input()

#special ='!@#$%^&*?'
#if special in text:
 #text =text.replace(special," ")
#print(text)

##30:이스케이프 시퀸스 연습
