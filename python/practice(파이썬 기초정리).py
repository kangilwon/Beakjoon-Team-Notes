# """
# # 숫자형(int) 자료형
# print(5)
# print(-5)
# print(3.14)
# print(1+8)
# print(1+8)
# print(1+8+10)

# # 문자열(String) 자료형
# print('풍선')
# print("나비")
# print('ㅋㅋ+22')

# # 참/거짓()
# print(5>3) # true
# print(5<3) # false
# print(True)
# print(not False)
# """
# # 변수
# import math
# from random import *
# from operator import index
# from math import *
# animal = "강아지"
# name = "연탄이"
# age = 4
# hobby = "산책"
# is_adult = age >= 3
# print("우리 "+animal+" "+name+"")
# print("나이는 "+str(age)+"살")
# print("취미는 "+hobby+"")
# print("연탄이는 어른??"+str(is_adult)+"")

# hobby = "잠"
# age = 1
# is_adult = age >= 3
# print("우리 ", animal, " ", name, "")
# print("나이는 ", age, "살")
# print("취미는 ", hobby, "")
# print("연탄이는 어른??", is_adult)
# print(1 >= 3)
# print(is_adult)
# print(age >= 3)

# # #=한줄주석이다.
# '''
# 여러줄
# 주석
# '''
# # 드래그 컨트롤+/
# # =
# # 자동 주석이다

# # 연습문제 반복문
# station = ['사당', '신도림', '인천공항']
# for i in station:
#     print(i, '행 열차가 들어오고 있습니다.')

# # 연산자 기본적인 +-*/ 가능하고
# print(2**3)  # 2^3=8 // 제곱이나
# print(5 % 3)  # 2 나머지
# print(10//3)  # 3 몫
# # >,<,<=,>=,==,!=     //    java와 같다.
# print(1 != 3)
# print(not(1 != 3))  # not 은 결과값의 반대

# print((3 > 0) and (3 < 5))  # and=&
# print((3 > 0) & (3 < 5))

# print((3 > 0) or (3 > 5))  # or=|
# print((3 > 0) | (3 > 5))

# # 간단한 수식
# print(2+3*4)  # 14
# print((2+3)*4)  # 0
# num = 2+3*4
# print(num)  # 14
# num = num+2  # 16
# print(num)  # 16

# num += 2  # 18
# print(num)  # 18

# num //= 3
# print(num)
# # +=  *=  /=  -=  %=  **=  //=  모두 가능

# # 숫자 처리 함수
# '''
# abs=절대값
# pow=제곱
# max=최대값
# min=최소값
# round=반올림

# '''
# print(abs(-5))
# print(pow(2, 3))
# print(max(5, 1, 10, 3))
# print(min(5, 1, 10, 3))

# # math 를 임폴트 해옴
# print(floor(4.99))  # 내림
# print(ceil(4.99))  # 올림
# print(sqrt(16))  # 제곱근

# # 랜덤 함수
# print(random())  # 0.0 ~ 1.0 사이의 임의값 생성
# print(random()*10)  # 0.0 ~ 10.0 사이의 임의값 생성
# print(int(random()*10))  # 0 ~ 10 사이의 임의값 생성
# print(int(random()*10))  # 0 ~ 10 사이의 임의값 생성
# print(int(random()*10))  # 0 ~ 10 사이의 임의값 생성

# print(int(random()*10)+1)  # 1 ~ 10 사이의 임의값 생성
# print(int(random()*10)+1)  # 1 ~ 10 사이의 임의값 생성
# print(int(random()*10)+1)  # 1 ~ 10 사이의 임의값 생성
# print(int(random()*10)+1)  # 1 ~ 10 사이의 임의값 생성
# print(int(random()*10)+1)  # 1 ~ 10 사이의 임의값 생성
# print(int(random()*10)+1)  # 1 ~ 10 사이의 임의값 생성

# print('로또')
# print(int(random()*45)+1)  # 1 ~ 45 사이의 임의값 생성
# print(int(random()*45)+1)  # 1 ~ 45 사이의 임의값 생성
# print(int(random()*45)+1)  # 1 ~ 45 사이의 임의값 생성
# print(int(random()*45)+1)  # 1 ~ 45 사이의 임의값 생성
# print(int(random()*45)+1)  # 1 ~ 45 사이의 임의값 생성
# print(int(random()*45)+1)  # 1 ~ 45 사이의 임의값 생성

# print('로또2')
# print(randrange(1, 46))  # 1 ~ 46 '미만'의 랜덤값출력

# # for문 응용
# roto = [randrange(1, 46), randrange(1, 46), randrange(1, 46),
#         randrange(1, 46), randrange(1, 46), randrange(1, 46)]
# a = 0
# for i in roto:

#     a += 1
#     print(a, "번째 번호는", i)

# print(randint(1, 45))  # 1 ~ 45 '이하'의 임의값

# # 연습문제
# day = randint(4, 28)
# print("오프라인 스터디 모임 날짜는 매월 "+str(day)+"일로 선정되었습니다.")

# # 문자열 출력 상세
# String1 = '따옴표 한개와'
# String2 = "따옴표 두개는"
# String3 = """
# 차이가 없습니다.,
# 하지만 "를 3개 사용하면
# 여러줄에 걸쳐 줄바꿈을 포함하여 출력합니다.
# """
# print(String1)
# print(String2)
# print(String3)

# # 슬라이싱 = 필요한 정보만 잘라서 가져오는 기능
# jumin = "951114-1234567"
# print("성별 : " + jumin[7])  # jumin변수에서 0부터 세서 7번째에 있는 정보를 가져옴
# print('연 : ' + jumin[0:2])  # jumin변수에서 0부터 2번째 전 까지 정보를 가져옴
# print('월 : ' + jumin[2:4])  # jumin변수에서 2부터 4번째 전 까지 정보를 가져옴
# print('일 : ' + jumin[4:6])  # jumin변수에서 4부터 6번째 전 까지 정보를 가져옴
# print('생년월일 : ' + jumin[:6])  # jumin변수에서 처음부터 6번째 전 까지 정보를 가져옴
# print('뒤 7자리 : ' + jumin[7:14])  # jumin변수에서 7부터 14번째 전 까지 정보를 가져옴
# print('뒤 7자리 : ' + jumin[7:])  # jumin변수에서 7부터 마지막까지 정보를 가져옴

# print('뒤 7자리(뒤에서부터) : ' + jumin[-7:])  # 맨 뒤에 문자는 -1로 시작한다.

# # 문자열 처리

# python = "Python is Amazing"
# print(python.lower())  # 모두 소문자로
# print(python.upper())  # 모두 대문자로
# print(python[0].islower())  # 변수 python의 0번째 문자가 소문자인지 알아봄, 결과값 블리언으로 반환
# print(len(python))  # 변수 python의 길이 반환(1부터 센다)
# print(python.replace("Python", "java"))  # 문자를 바꿔준다.

# index = python.index("n")  # 문자 n이 변수의 몇번째에 위치했는가?(0부터 센다)
# print(index)
# index = python.index('n', index+1)  # 처음 찾은 n 다음으로 나오는 n
# print(index)

# print(python.find("thon"))  # find는 원하는 값이 없으면 -1 반환 // hi출력
# # print(python.index("java"))#index는 원하는 값이 없으면 오류(종료)  // hi미출력
# print("hi")

# print(python.count("n"))  # 변수에 n이 몇번 나오는지

# # 문자열 포맷
# # 방법1
# print("나는 %d살입니다." % 20)  # %d는 정수가 기본이지만 다른 형식도 출력해줌
# print("나는 %s을 좋아해여." % "파이썬")  # %s는 문자열
# print("나는 %c씨에요." % "강")  # %c는 문자
# print("나는 %s와 %s를 좋아합니다" % ("노래", '영화'))

# # 방법2
# print("나는 {}살입니다.".format(20))
# print("나는 {}와 {}를 좋아합니다".format("노래", "영화"))
# print("나는 {1}와 {0}를 좋아합니다".format("노래", "영화"))

# # 방법3
# print("나는 {move}와 {sing}를 좋아합니다".format(sing="노래", move="영화"))

# # 방법4
# sing = "노래"
# move = "영화"
# print(f"나는 {move}와 {sing}를 좋아합니다")


# # 탈출문자
# print("백문이 불여일견이오\n 백견이 불여일행이니라")  # \n=줄바꿈
# print("저는 \"파이썬\"을 공부중입니다.")  # \"는 ""안에서 ""를 사용할 수 있게 해준다

# # \\는 문장 안에서 \로 표기된다.
# print("내 파이썬 경로는 : C:\\Users\\eleck\\Desktop\\pythonWorkspace> 다")

# # \r은 커서를 맨 앞으로 이동시킨 후에 \r 이후에 쓴 문자로 다시 써준다.
# print("Red Apple\rPine")

# # \b는 백스페이스(한글자삭제)
# print("Redd\bApple")

# # \t는 탭
# print("Red\tApple")

# # 연습문제

# # a="http://naver.com"
# # a=a[7:]
# # a=a[0:5]
# # b=a[0:3]
# # print(b+str(len(a))+str(a.count("e"))+"!")

# url = "http://naver.com"
# my_str = url.replace("http://", "")
# my_str = my_str[:my_str.index(".")]
# password = my_str[:3]+str(len(my_str))+str(my_str.count("e"))+"!"
# print("{0}의 비밀번호는 {1}입니다.".format(url, password))

# # 리스트 []
# subway = [10, 20, 30]
# print(subway)

# subway = ["유재석", "조세호", "박명수"]

# # 박명수가 타고있는 칸은?
# print(subway.index("박명수")+1)

# # 하하가 다음 정류장에서 다음칸에 탔다.
# subway.append("하하")  # append는 배열 마지막에 추가한다.
# print(subway)

# # 정형돈이 박명수와 하하 사이에 탐
# subway.insert(3, "정형돈")
# print(subway)

# # 지하철에 있는 사람을 뒤에서 꺼낸다.
# print(subway.pop())
# print(subway)

# # 같은 이름을 가진 사람은 몇명인가
# subway.append("유재석")
# print(subway)
# print(subway.count("유재석"))

# # 정렬
# nums = [1, 5, 23, 89, 2, 43]
# nums.reverse()  # 배열 순서 반대로 뒤집기
# print(nums)
# nums.sort()  # 오름차순 정렬
# print(nums)

# # nums.clear() # 배열의 값을 모두 지워준다.
# print(nums)

# # 배열은 다양한 자료형과 함께 사용 가능하다
# mix_list = ["유재석", 20, True]
# print(mix_list)

# # 리스트의 확장
# nums.extend(mix_list)
# print(nums)

# # 사전
# cabinet = {3: "유재석", 100: "김태호"}
# print(cabinet[100])  # 찾는값이 없으면 오류(종료)
# print(cabinet.get(3))  # 찾는값이 없으면 none출력후 다음 실행
# print(cabinet.get(5, "사용가능"))  # 찾는값이 없으면 none출력하지만 임의 값을 준다면 none대신 출력한다.

# # 사전 안에 해당 키값이 있는지 블리언 값으로 확인한다.
# print(3 in cabinet)  # true
# print(10 in cabinet)  # fales

# # update
# cabinet[3] = "김종국"  # 유재석에서 김종국으로 변경
# cabinet["ㅁ-1"] = "노홍철"  # 노홍철 추가 // 키값은 문자도 올 수 있다.
# print(cabinet)

# # 삭제
# del cabinet["ㅁ-1"]
# print(cabinet)

# # 키값만 출력
# print(cabinet.keys())
# # value만 출력
# print(cabinet.values())
# # 키와 벨류 출력
# print(cabinet.items())
# # 사전값 초기화(전체 삭제)
# cabinet.clear()
# print(cabinet)

# # 튜플  / 리스트와 다르게 변경 불가 / 리스트보다 속도가 빠름
# menu = ("왕돈까스", "왕냉면")
# print(menu[0])
# print(menu[1])

# (name, age, hobby) = ("강일원", 27, "코딩")
# print(name, age, hobby)


# # 세트set=집합 / 중복값 허용 안하고 순서가 없다.
# my_set = {1, 2, 3, 3, 3}
# print(my_set)  # 중복값 자동으로 하나만 출력

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수","유재석"])
print(type(java))
# # java와 python의 교집합
print(java & python)
print(java.intersection(python))

# # java와 python의 합집합
print(java | python)
print(java.union(python))

# # java와 python의 차집합
# print(java-python)
# print(java.difference(python))

# # set에 값 추가
# python.add("김태호")
# print(python)
# # set에 값 제거
# java.remove("김태호")
# print(java)


# # 자료구조의 변경
# menu = {"커피", "우유", "주스"}
# print(menu, type(menu))

# menu = list(menu)
# print(menu, type(menu))

# menu = tuple(menu)
# print(menu, type(menu))


# # 연습문제
# print("연습문제")
# id = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# # [id 셔플]
# shuffle(id)
# print(id)

# # [랜덤 1명 뽑음 == 치킨 당첨자 아이디]
# ch = sample(id, 1)
# print(ch)
# # 치킨당첨자 인덱스번호 확인
# # chindex=id.index(ch[0])
# # print("index",chindex)
# id.remove(ch[0])
# print(id)


# # [랜덤 3명 뽑음 == 커피 당첨자 아이디]
# cf = sample(id, 3)

# # 값 확인
# print(cf)
# print(id)

# print("-------------------------")
# print("-- 당첨자 발표 --")
# print("치킨 당첨자 : ", ch[0])
# print("커피 당첨자 : ", cf, "")
# print("-- 축하합니다 --")
# print("-------------------------")

# user = range(1, 21)  # 1부터 20까지 숫자를 생성한다.
# user = list(user)
# shuffle(user)
# print(user)

# winners = sample(user, 4)
# print("-- 당첨자 발표 --")
# print("치킨 당첨자 : {0}".format(winners[0]))
# print("커피 당첨자 : {0}".format(winners[1:]))
# print("-- 축하합니다 --")

# '''
# #if
# weather=input("오늘 날씨는 어때요?")
# if weather=="비" or weather=="눈":
#     print("우산을 챙겨주세요")
# elif weather=="미세먼지":
#     print("마스크를 챙겨주세요")
# else:
#     print("준비물이 필요 없어요.")

# temp = int(input("오늘의 기온은?"))
# if 30<= temp:
#     print("넘무더웡.. 집!")
# elif 10<=temp and temp <30:
#     print("낫벳 귀귀")
# elif 0<=temp and temp <10:
#     print("춥다.. 롱패딩!")
# else:
#     print("집집집집 전기장판")
# '''

# # for
# for waiting_no in range(0, 5):
#     print("대기번호 : {0}".format(waiting_no))

# starbucks = ["아이언맨", "토르", "그루트"]
# for customer in starbucks:
#     print("{0}님의 커피가 준비되었습니다.".format(customer))

# # while
# customer2 = "토르"
# cfindex = 5
# while cfindex >= 1:
#     print("{0}님의 커피가 준비되었습니다.{1}번 후에 커피는 버려집니다ㅠㅠ".format(customer2, cfindex))
#     cfindex -= 1
#     if cfindex == 0:
#         print("커피는 버려졌습니다...ㅜ")

# # 무한루프.. 컨트롤 c = 무한루프 종료
# '''
# customer3="아이언맨"
# cfindex2=1
# while True:
#     print("{0}님의 커피가 준비되었습니다. 호출{1}회".format(customer3,cfindex2))
#     cfindex2+=1
# '''
# # customer4="그루트"
# # person="unknown"
# # while person != customer4:
# #     print("{0}님 커피가 준비되었습니다.".format(customer4))
# #     person=input("이름이??")


# # continue 와 break
# absent = [2, 5]  # 결석
# no_book = [7]  # 책없음
# for student in range(1, 11):  # 1번 ~ 10번
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("수업끝 {0}은 교무실로".format(no_book))
#         break
#     print("{0}, 책을 읽어봐".format(student))

# #한 줄 for#
# # 학생번호 변경
# students = list(range(1, 6))
# print(students)
# students = [i+100 for i in students]
# print(students)

# # 길이값
# hiro = ["Iron man", "Thor", "Groot"]
# # hiro=[len(i) for i in hiro]
# print(hiro)

# # 대문자로
# hiro = [i.upper() for i in hiro]
# print(hiro)

# # 연습문제
# print("연습문제")

# '''
# #손님 1번 부터 50번
# man=1
# yes="o"
# count=0
# while man!=50:
#     #운행 소요 시간
#     mtime=int(random()*45)+5
    
#     if mtime>=5 and mtime<=15:
#         yes="o"    
#         print("[{0}] {1}번째 손님 (소요시간 : {2}분)".format(yes,man,mtime))
#         count+=1
#     else:
#         yes=" "
#         print("[{0}] {1}번째 손님 (소요시간 : {2}분)".format(yes,man,mtime))
#     #다음 손님으로
#     man+=1
# print("\n 총 탑승 승객 : {0}분".format(count))
# '''

# # 정답
# cnt = 0  # 탑승 수
# for i in range(1, 51):  # 1~50명
#     time = randrange(5, 50)  # 5~50분
#     if 5 <= time <= 15:  # 5분~15분 사이 손님 , 탑승승객수 증가
#         print("[o] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
#         cnt += 1
#     else:
#         print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))

# print("총 탑승 승객 : {0} 분".format(cnt))

# # 함수


# def open_account():
#     print("새 계좌 생성")


# open_account()

# # 입금함수


# def deposit(balance, money):
#     print("입금 완료! 작액은 {0} 입니다.".format(balance+money))
#     return balance+money

# # 출금함수


# def withdraw(balance, money):
#     if balance >= money:  # 잔액이 출금보다 많으면
#         print("출금완료 잔액은 {0}원입니다.".format(balance-money))
#         return balance-money
#     else:
#         print("출금 불가 잔액은 {0}입니다.".format(balance))
#         return balance

# # 수수료.. 저녁출금


# def withdraw_night(balance, money):
#     commission = 100  # 수수료 100원
#     return commission, balance-money-commission


# balance = 0  # 잔액
# balance = deposit(balance, 1000)
# balance = withdraw(balance, 2000)
# # balance = withdraw(balance,500)
# commission, balance = withdraw_night(balance, 500)
# print("수수료 {0}원, 잔액{1}원".format(commission, balance))
# print(balance)


# # 기본값
# # def profile(name, age, main_lang):
# #     print("이름 : {0}\t나이 : {1}\t주 언어 : {2}"\
# #         .format(name,age,main_lang))

# # profile("유재석","20","파이썬")
# # profile("김태호","30","자바")

# # 같은 학교 같은 학년 같은 반 같은 수업.
# def profile(name, age=17, main_lang="파이썬"):
#     print("이름 : {0}\t나이 : {1}\n주 언어 : {2}\n"
#           .format(name, age, main_lang))


# profile("유재석")
# profile("김태호")



# # 키워드 값 #
# def profile2(name, age, main_lang):
#     print(name,age,main_lang)

# profile2(age=20,name="강일원",main_lang="자바")# 아규먼트가 순서가 없어도, 파라미터 순서대로 출력됨(보내는 값 아규먼트, 받는 값 파라미터)



# # 가변인자# / 인자값이 늘어나거나 부족한경우
# '''
# def profile3(name,age,lang1,lang2,lang3,lang4,lang5):
#     print("name : {0}\tage{1}\t".format(name,age),end=" ")
#     print(lang1,lang2,lang3,lang4,lang5)

# profile3("유재석",20,"파이썬","자바","c","c++","c#")
# profile3("김태호",25,"kotlin","swift","","","")
# '''
# #위와 같은 기능이다
# def profile3(name,age,*language):
#     print("name : {0}\tage{1}\t".format(name,age),end=" ")
#     for lang in language:
#         print(lang,end=" ")
#     print()

# profile3("유재석",20,"스프링","파이썬","자바","c","c++","c#")
# profile3("김태호",25,"kotlin","swift")


# # 지역변수와 전역변수 #
# gun=10

# def checkpoint(soldiers):#경계근무자 수
#     global gun # 전역 공간에 있는 gun사용
#     gun = gun-soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))

# def checkpoint_ret(gun,soldiers):
#     gun=gun-soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
#     return gun

# print("전체 총 : {0}".format(gun))
# # checkpoint(2)#경계근무 2명 나감
# gun=checkpoint_ret(gun,2)
# print("남은 총 : {0}".format(gun))

# ##연습문제##
# print("연습문제")
# '''
# def std_weight(height,gender):
#     if gender=="남자":
#         print("키 {0}cm 남자의 표준 체중은 {1}kg 입니다.".format(height,round(((height/100)**2)*22,2)))
#     elif gender=="여자":
#         print("키 {0}cm 여자의 표준 체중은 {1}kg 입니다.".format(height,round(((height/100)**2)*21,2)))

# std_weight(175,"남자")
# '''

# def std_weight(height,gender):
#     if gender=="남자":
#         return height**2*22
#     else:
#         return height**2*21

# height=175
# gender="남자"
# weight=std_weight(height/100,gender)
# print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height,gender,round(weight,2)))

# # 표준 입출력#
# print("python","java",sep=",",end="?")#sep=","  // sep는 각 "문자"사이에 무엇으로 구분해줄지 / end="?"는 다음 print를 붙여서 한줄로 출력
# print("어떤 언어가 나와 더 잘 맞는가?")
# import sys
# print("python","java",file=sys.stdout)# 표준 출력
# print("python","java",file=sys.stderr)# 표준 에러

# #ex) 시험성적
# scores={"수학":0,"영어":50,"코딩":100}
# for subject,scores in scores.items():#사전에서 items는 키와 벨류를 같이 보내준다.
#     print(subject.ljust(8),str(scores).rjust(4),sep=":")#ljust(8) / 왼쪽 정렬을 하는데 8의 공간을 확보하고 해준다

# #ex) 은행 대기표
# for num in range(1,21):
#     print("대기번호 : " + str(num).zfill(3))#zfile(3) / 3의 공간을 확보하고 빈공간을 0으로 채워준다.

# # answer=input("아무값 입력! : ")
# # print("입력값은"+answer+"입니다.")#input을 이용한 입력값은 항상 String타입이다.

# #다양한 출력 포멧#

# #빈자리는 빈공간을 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
# print("{0: >10}".format(500))

# #빈자리는 -로 채우고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
# print("{0:->10}".format(500))

# #양수일 때 +표시,음수 - 표시
# print("{0: >+10}".format(-500))

# #왼쪽 정렬, 빈칸 _로 채움
# print("{0:_<10}".format(500))

# #3자리마다 , 찍어주기
# print("{0:,}".format(50000000000000))

# #3자리마다 , 찍어주기 +-표시까지
# print("{0:+,}".format(-50000000000000))

# #3자리마다 , 찍어주기 +-표시까지 /빈공간 확보 빈공간^로 채움
# print("{0:^<+30,}".format(-50000000000000))

# #소수점 출력
# print("{0:f}".format(5/3))

# #소수점 이하 자리수 제한
# print("{0:.2f}".format(5/3))#소수점 2째 자리까지 표기 3자리 이하는 반올림


# ##파일 입출력##
# # score_file=open("score.txt","w",encoding="utf8")# w/ 덮어 쓰기,
# # print("수학 : 0",file=score_file)
# # print("영어 : 50",file=score_file)
# # score_file.close()

# '''

# score_file=open("score.txt","a",encoding="utf8")# a/ 이어 쓰기,
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")#write는 자동 줄바꿈이 안됨
# score_file.close()

# score_file=open("score.txt","r",encoding="utf8")# r / 읽어오기
# print(score_file.read())#파일 전쳬읽기
# score_file.close()


# score_file=open("score.txt","r",encoding="utf8")# r / 읽어오기
# print(score_file.readline())#파일 한줄 읽고 커서는 다음줄 대기
# print(score_file.readline(),end="")#파일 한줄 읽고 커서는 다음줄 대기 / end=""줄바꿈안함
# print(score_file.readline())#파일 한줄 읽고 커서는 다음줄 대기
# score_file.close()

# #불러올 파일이 몇줄인지 모를때
# score_file=open("score.txt","r",encoding="utf8")# r / 읽어오기
# while True:
#     line=score_file.readline()
#     if not line:
#         break
#     print(line,end="")
# score_file.close

# score_file=open("score.txt","r",encoding="utf8")# r / 읽어오기
# lines=score_file.readlines()#모든 라인을 가져와서 list형태로 저장
# for line in lines:
#     print(line, end="")
# score_file.close()

# ##파일을 열고 나서는 항상 close를 해줘야함

# '''

# ##pickle##  / 프로그램 사용 데이터를 파일 형태로 저장

# 문잘열을 리스트로
# a=input() # 변수 a의 문자열을
# a=list(a) # 하나하나 문자로 나눠 리스트에 저장한다.

# 아스키코드 
# ord() # 문자를 아스키코드로
# chr() # 아스키코드를 문자로

###python 시간체크###
'''
import time
start_time = time.time() # 측정시작
#
# 프로그램 소스코드
# 작성
#
end_time = time.time() # 측정종료
print('프로그램 수행시간 : ',end_time-start_time) # 프로그램 수행시간을 출력한다.
'''

### 2차원 배열 ###
'''
n=4
m=3
array = [[0] * m for _ in range(n)]
print(array)
'''

### 특정 값 제외하고 리스트 다시 생성하기(remove) ##
'''
a=[1,2,3,4,5,5,5]
remove_set={3,5} # 집합자료형{3,5}를 제거하고 리스트를 만들어준다
result=[i for i in a if i not in remove_set]
print(remove_set)
'''

### 자료형, 사전 ###
'''
data = dict()           # 사전 자료형 선언 dict()
data['사과']='apple'
data['바나나']='banana'

print(data)
if '사과' in data: # '사과'가 data 안에 존재 하면
    print("키값 '사과'가 존재합니다.")
'''

### 문자열 빠르게 입력받기 ###
'''
import sys
data= sys.stdin.readline().rstrip() # rstrip() = 공백 기준으로 안쓰면 엔터 기준임
print(data)
'''

### 실전에서 주로 사용하는 표준 라이브러리 ###
'''
내장함수 : 기본 입출력 함수부터 정렬 함수까지 기본적인 함수제공,
    기본적 필수적 기능들
    ex) # eval()
            result=eval("(3+5)*7") # "" 안의 수식을 계산해서 반환해준다
            print(result)

        # sorted()
            result = sorted([9,1,8,5,4])
            reverse_result=sorted([9,1,8,5,4], reverse=True)
            print(result) # 오름차순 정렬 [1,4,5,8,9]
            print(reverse_result) # 내림차순 정렬 [9,8,5,4,1]

        # sorted() with Key
            array=[('홍길동',35),('이순신',75),('아무개',50)]
            result=sorted(array,Key=lambda x: x[1],reverse=True)
            print(result)

itertools: 반복되는 형태의 데이터 처리,
    순열과 조합 라이브러리를 자주 사용한다.
    순열: 서로 다른 n개에서 서로 다른 r개를 선택하여 일려로 나열하는 것
        {'a','b','c'}에서 3개를 선택하여 나열하는 경우 : 'abc', 'acb', 'bac', 'bca', 'cab', 'cba'로 나타낸다.
            form itertools import permutations

            data = ['A', 'B', 'C']

            result= list(permutations(data,3)) # data에서 3개로 조합가능한 모든 경우의 수
            print(result)   
    ##중복 순열(permutations 대신 product 사용) # 중복을 허용한다.

    조합: 서로 다른 n개에서 순서에 상관 없이 서로 다른 r개를 선택하는 것
        {'a','b','c'}에서 순서를 고려하지 않고 2개를 뽑는 경우 : 'ab', 'ac', 'bc'로 나타낸다.
             form itertools import combinations

            data = ['A', 'B', 'C']

            result= list(combinations(data,2)) # data에서 2개를 뽑는 모든 경우의 수
            print(result)
    ##중복 조합(combinations 대신 combinations_with_replacement 사용) # 중복을 허용한다.


heapq: 힙(Heap)자료구조 제공
    일반적으로 우선순위 큐 기능을 구현하기 위해 사용
bisect: 이진탐색(Binary Search)기능을 제공한다.
collections: 덱(deque), 카운터(Counter)등의 유용한 자료구조 포함
    # Counter : 등장횟수 세는 기능
        form collections import Counter

        Counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

        print(counter['blue']) # blue 등장 횟수
        print(counter['green']) # green 등장 횟수
        print(dict(counter)) # 사전 자료형으로 반환한다. 출력결과 : {'red':2, 'blue':3, 'green':1}

math: 필수적인 수학적 기능 제공
    펙토리얼, 제곱근, 최대공약수(gcd),삼각함수 관련 함수부터 파이(pi)와 같은 상수를 포함한다.
'''

### 그리디 알고리즘 (탐욕법) ###
'''
그리디 : 현재 상황에서 지금 당장 좋은 것만 고르는 방법

'''