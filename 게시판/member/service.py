from 게시판.member.dao_db import MemberDao
from 게시판.member.vo import Member


class MemberService:

    loginId = '' # '': 로그아웃상태. 공백문자아니면 로그인상태

    def __init__(self):
        self.dao = MemberDao()

    # 회원가입
    def addMember(self):
        id = input('id:')
        pwd = input('pwd:')
        name = input('name:')
        email = input('email:')

        self.dao.insert(Member(id=id, pwd=pwd, name=name, email=email))

    # 로그인 하기
    def login(self):
        if MemberService.loginId != '':
            print('이미 로그인중')
            return

        id = input('로그인 id:')
        m = self.dao.select(id)

        if m == None:
            print('없는 회원Id')
            return
        else:
            pwd = input('password:')
            if pwd == m.pwd:
                MemberService.loginId = id # 로그인 처리
                print('로그인 성공')
            else:
                print('패스워드 불일치')

    # 내 정보 보기
    def printMyInfo(self):  # 로그인 상태에서만 사용해야함
        print('=== 내 정보 보기 ===')
        if MemberService.loginId == '':
            print('로그인을 먼저 하세요')
            return

        m = self.dao.select(MemberService.loginId)
        print(m)

    # 내 정보 수정
    def editMem(self):
        print('=== 수정 ===')
        id = input('edit id:')
        m:Member = self.dao.select(id) # 수정전 데이터 검색

        if m == None:  # 중복 안됨
            print('없는 id. 수정 취소')
        else:
            data = [] # 빈리스트
            s = ['pwd', 'name', 'email']
            for i in range(0, len(s)):
                data.append(input('new ' + s[i] + ': '))

            for idx,i in enumerate(data):
                if i != '': # 해당 항목에서 그냥 엔터치고 공백으로 넘어가면 해당 항목은 수정안하고 넘어가겠다/ 공백문자 아니면 수정된 값 대체하기
                    m.__setattr__(s[idx], i) # 객체의 멤버변수 값을 수정하는 함수 / s[idx] = s의 이름 / i = 사용자가 입력한 값

            self.dao.update(m)

    # 로그아웃
    def logout(self):
        if MemberService.loginId == '':
            print('로그인을 먼저 하세요')
            return
        print('로그아웃 완료!')
        MemberService.loginId = ''

    # 탈퇴
    def delMem(self):
        print('=== 삭제 ===')
        id = input('del id:')
        self.dao.delete(id)