# # 1. 숫자를 두번 물어보게 하고 별을 출력해서 사각형을 만드세요
# x = int(input('가로의 숫자를 입력하세요 :'))
# y = int(input('세로의 숫자를 입력하세요 :'))
# for i in range(1, y+1):
#     print(x * '* ')
#
# # 2. 삼각형의 가로와 높이를 받아서 넓이를 출력하는 함수를 작성하시오
# def triangle(가로, 높이):
#     return 가로 * 높이 / 2
#
# 가로 = int(input('삼각형 가로 길이를 입력하세요:'))
# 높이 = int(input('삼각형 높이를 입력하세요:'))
#
# print('삼각형의 넓이: ', triangle(가로, 높이))
#
# # 3. 아래와 같이 별이 찍히게 출력하시오.
# x=int(input('숫자를 입력하세요: '))
#
# for i in range(1, x, 1):
#     print(" " *(x-i),'*'*(i))
# for i in range(x,0,-1):
#     print(" "*(x-i),'*'*(i))
#
# # 4.1부터 100까지의 수의 합을 계산하던 중에 합이 1000 이상일때, 최초로 1000을 넘게하는 수가
# # 무엇인지 코드를 만들고 답을 구하시오
# sum=0
# for i in range(1,101,1):
#     sum += i
#     if sum > 1000:
#         print(i)
#         break
#
# # 5. 정수를 입력했을때 짝수인지 홀수인지 판별하는 코드를 작성하시오.
# x=int(input('짝홀 판별할 정수 입력해주세요: '))
# if x % 2 == 0:
#     print('짝수입니다.')
# else:
#     print('홀수입니다.')
#
# # 6. 리스트 method 중 하나를 이용하여 아래의 리스트를 알파벳 순서대로 정렬하세요.
# namelist=['Mary','Sams','Aimy','Tom','Michale','Bob','Kelly']
# namelist.sort()
# print(namelist)
#
# # 7. 주민등록번호를 입력하면 남자인지 여자인지 알려주는 프로그램을 작성하시오.
# x=input('주민번호를 입력하세요 : ')
# x.split('-')
# gender = int(x.split('-')[1][0])
#
# if gender == 1 & 3:
#     print('M')
# else:
#     print('F')
#
# # 8. 확장자가 포함된 파일이름이 담긴 리스트에서 확장자를 제거하고 파일 이름만 추가 리스트에 저장하시오.
# file=['exit.py','hi.py','playdata.hwp','intro.jpg']
# newfile=[]
# for filename in file:
#     filename = filename.split('.')[0]
#     newfile.append(filename)
# print(newfile)
#
# # 9. 다음 리스트에서 알파벳의 갯수가 7개인 단어를 출력하시오
# a = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india']
# a_7=[]
# for i in a:
#     if len(i) == 7:
#         a_7.append(i)
# print(a_7)
#
# # 10. 리스트 메서드 중 하나를 이용하여 아래의 리스트에 '화성' 이라는 요소를 삽입하시오.
# planet =['태양','수성','금성','목성','토성','천왕성','해왕성']
# planet.insert(3,'화성')
# print(planet)
#
# # 11. 점수 구간에 해당하는 학점이 아래와 같이 정의되어 있다. 점수를 입력했을때 해당 학점이 출력하시오
# (A: 100 ~ 81, B: 80 ~ 61, C: 60 ~ 41, D: 40 ~ 21, F: 20 ~ 0)
# score=int(input('점수를 입력하세요 : '))
# if score > 80 and score <= 100:
#     print('A')
# elif score <= 80 and score > 60:
#     print('B')
# elif score <= 60 and score > 40:
#     print('C')
# elif score <= 40 and score > 20:
#     print('D')
# elif score <= 20 and score >= 0:
#     print('F')
#
# # 12. 최대공약수 및 최소공배수를 구하는 함수를 구현하시오.
# x=int(input('숫자를 입력하세요 : '))
# y=int(input('숫자를 입력하세요 : '))
#
# def maxi(x,y):
#     for i in range(min(x,y),0,-1):
#         if x%i==0 and y%i==0:
#             print(i)
#             break
# def mini(x,y):
#     for i in range(max(x,y), (x*y)+1):
#         if i%x==0 and i%y==0:
#             print(i)
#             break
# maxi(x, y)
# mini(x, y)
#
# # 13. card 클래스를 생성해 카드에 충전기능, 소비기능, 잔약을 알려주는 기능을 넣으세요.
# class Card:
#     def __init__(self, money):
#         self.money = money
#
#     def charge(self, cash):
#         print('얼마를 충전하시겠습니까?')
#         print('{}원 충전을 진행합니다.'.format(cash))
#         self.money += cash
#
#     def consume(self, cash):
#         if self.money < cash:
#             print('잔액이 부족합니다')
#         else:
#             print('삐빅')
#             self.money -= cash
#
#     def check(self):
#         print('# 잔액이 {}원 입니다'.format(self.money))
#
# buscard=Card(1000)
# buscard.check()
# buscard.consume(800)
# buscard.check()
# buscard.charge(5000)
# buscard.check()
#
#
#
# # 14. 년, 월, 일 입력하여 그날이 무슨 요일인지 출력하기
# from datetime import date
#
# myyear=int(input('연도를 입력하세요: '))
# mymonth=int(input('월을 입력하세요: '))
# myday=int(input('일을 입력하세요: '))
#
# def printDay(year, month, day):
#     dayoftheweek=['월요일','화요일','수요일','목요일','금요일','토요일','일요일']
#     return dayoftheweek[date(year, month, day).weekday()]
# print('%d년 %d월 %d일은 %s 입니다!' % (myyear, mymonth, myday, printDay(myyear, mymonth, myday)))
#
# # 15. 계산기 기능을 하는 calculator 클래스 만들기
# class Calculator:
#     def __init__(self):
#         self.plus = 0
#         self.minus = 0
#         self.multiple = 0
#         self.divide = 0
#
#     def Plus(self, num1:int, num2:int):
#         self.plus = self.plus + 1
#         return num1 + num2
#
#     def Minus(self,num1, num2):
#         self.minus = self.minus + 1
#         return num1 - num2
#
#     def Multiple(self,num1, num2):
#         self.multiple = self.multiple + 1
#         return num1 * num2
#
#     def Divide(self, num1, num2):
#         self.divide = self.divide + 1
#         return num1 / num2
#
# cal = Calculator()
# print(cal.Plus(10,20))
# print(cal.Minus(10,20))
# print(cal.Multiple(10,20))
# print(cal.Divide(10,20))
#
# # 16. Gorilla 라는 클래스를 생성하시오.
# class Gorilla:
#     def __init__(self, banana):
#         self.banana = banana
#
#     def shout(self, num):
#         for i in range(num):
#             if self.banana == 0:
#                 print('배가 고파서 소리를 못지릅니다')
#                 break
#             else:
#                 print('바나나 내놔!!')
#                 self.banana -= 1
#
#     def walk(self, num):
#         for i in range(num):
#             if self.banana == 0:
#                 print('배가 고파서 걸을 수 없습니다')
#                 break
#             else:
#                 print('뚜벅뚜벅')
#                 self.banana -= 1
#
#     def eat(self, num):
#         print('냠냠')
#         self.banana -= 1
#
#     def check(self):
#         print('{}개의 바나나 남음'.format(self.banana))
#
# ksh_gorilla = Gorilla(10)
# ksh_gorilla.shout(1)
# ksh_gorilla.eat(1)
# ksh_gorilla.walk(1)
# ksh_gorilla.check()
#
# # 17. Gun 이라는 클래스를 생성하시오
# class Gun:
#     def __init__(self, bullet):
#         self.bullet = bullet
#
#     def charge(self, num):
#         print('총알을 {}개 충전합니다.'.format(num))
#         self.bullet += num
#
#     def shoot(self, num):
#         for i in range(num):
#             if self.bullet == 0:
#                 print('발사할 총알이 없습니다')
#                 break
#             else:
#                 print('빵야!!')
#                 self.bullet -= 1
#
#     def check(self):
#         print('{}개의 총알 남음'.format(self.bullet))
#
# ksh_gun = Gun(1)
# ksh_gun.shoot(1)
# ksh_gun.check()
# ksh_gun.charge(5)
# ksh_gun.check()
#
# # 18. 아직 정렬되지 않은 값을 이미 정렬된 배열 사이에 끼워 넣는 과정을 반복하여 정렬하는 것 을 삽입정렬이라고 합니다. 주어진 리스트를 삽입정렬함수(insert_sort)를 생성하여 오름차순으로 정렬하시오.
# list=[6,2,3,7,8,10,21,1]
# def insert_sort(list):
#     for end in range(1, len(list)):
#         i = end
#         while i > 0 and list[i-1] > list[i]:
#             list[i-1], list[i] = list[i], list[i-1]
#             i -= 1
#     return list
#
# print(insert_sort(list))
#
# # 19 .앞뒤로 이웃한 숫자를 비교하여 크기가 큰 숫자가 작은숫자보다 앞에 있을 경우 서로 위치를 바꿔 가며 정렬하는 것을 버블정렬이라고 합니다. 주어진 리스트를 버블정렬함수(bubble_sort)를 생성하여 오름차순으로 정렬하시오.
# list=[4,3,2,1,8,7,5,10,11,16,21,6]
#
# def bubble_sort(list):
#     # 배열의 크기만큼 반복
#     for i in range(len(list)):
#         # 배열의 총 크기에서 i의 값과 1을 뺀 만큼 반복
#         for j in range(0, len(list) - i - 1):
#             # 만약 현재 인덱스의 값이 다음 인덱스의 값보다 클경우 실행
#             if list[j] > list[j + 1]:
#                 list[j], list[j + 1] = list[j + 1], list[j]  # 서로 위치를 변환
#     return list
#
# print(bubble_sort(list))
#
# # 20. 팩토리얼은 1부터 n까지 연속한 숫자의 곱이라 합니다. 팩토리얼을 함수(factorial)로 구현하 는데 재귀함수를 이용하여 구현하시오.
# def factorial(n):
#     if n > 1:
#         return n * factorial(n-1)
#     else:
#         return 1
#
# print(factorial(4))