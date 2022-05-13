#from addr.dao import AddrDao
from addr.dao_db import AddrDaoDB
from addr.vo import Addr

# service
class AddrService:

    loginNum = 0 # 로그인한 사람 num. loginNum이 0이면 로그아웃. 0이 아니면 로그인 상태
    # loginId = '' # '': 로그아웃상태. 공백문자아니면 로그인상태

    def __init__(self):
        self.dao = AddrDaoDB()

    #추가. name 중복 허용 안됨
    def addAddr(self):
        print('=== 추가 ===')
        name = input('name:')
        tel = input('tel:')
        addr = input('addr:')
        self.dao.insert(Addr(name=name, tel=tel, addr=addr))


    #검색: 검색할 이름을 입력받아서 dao로 검색한 결과 출력
    def printAddr(self):
        print('=== 이름으로 검색 ===')
        name = input('search name:')
        res = self.dao.selectByName('%' + name + '%')
        if res == None: #중복 안됨
            print('예외 발생')
        elif len(res) == 0:
            print('검색결과 없음')
        else:
            for i in res:
                print(i)

    #수정
    def editAddr(self):
        print('=== 수정 ===')
        num = int(input('edit num:'))
        a:Addr = self.dao.select(num) # 수정전 데이터 검색

        if a == None:  # 중복 안됨
            print('없는 번호. 수정 취소')
        else:
            data = [] # 빈리스트
            s = ['name', 'tel', 'addr']
            for i in range(0, len(s)):
                data.append(input('new ' + s[i] + ': '))

            for idx,i in enumerate(data):
                if i != '': # 해당 항목에서 그냥 엔터치고 공백으로 넘어가면 해당 항목은 수정안하고 넘어가겠다/ 공백문자 아니면 수정된 값 대체하기
                    a.__setattr__(s[idx], i) # 객체의 멤버변수 값을 수정하는 함수 / s[idx] = s의 이름 / i = 사용자가 입력한 값

            self.dao.update(a)


    #삭제
    def delArrd(self):
        print('=== 삭제 ===')
        num = input('del num:')
        self.dao.delete(num)

    #전체출력
    def printAll(self):
        print('=== 전체 출력 ===')
        data = self.dao.selectAll()
        for i in data:
            print(i)

    # 로그인 하기
    def login(self):
        if AddrService.loginNum != 0:
            print('이미 로그인중')
            return

        num = int(input('로그인 번호:'))
        a = self.dao.select(num)

        if a == None:
            print('없는 회원번호')
            return
        else:
            name = input('로그인 이름:')
            if name == a.name:
                AddrService.loginNum = num # 로그인 처리
                print('로그인 성공')
            else:
                print('패스워드 불일치')

    # 내 정보보기
    def printMyInfo(self): # 로그인 상태에서만 사용해야함
        if AddrService.loginNum == 0:
            print('로그인을 먼저 하세요')
            return

        a = self.dao.select(AddrService.loginNum)
        print(a)

    # 로그아웃
    def logout(self):
        if AddrService.loginNum == 0:
            print('로그인을 먼저 하세요')
            return
        AddrService.loginNum = 0 # AddrService.loginId = ''