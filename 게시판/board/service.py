from 게시판.board.dao_db import BoardDao
from 게시판.board.vo import Board
from 게시판.member.service import MemberService


class BoardService:
    def __init__(self):
        self.dao = BoardDao()

    # 글쓰기
    def addBoard(self):
        writer = MemberService.loginId
        title = input('title:')
        content = input('content:')

        self.dao.insert(Board(writer=writer, title=title, content=content))

    # 글번호로 검색
    def getByNum(self):
        print('=== 글 번호로 검색 ===')
        num = int(input('search num:'))
        b:Board = self.dao.selectByNum(num)
        if b == None:
            print('없는 글 번호')
        else:
            print(b)

    # 글작성자로 검색
    def getByWriter(self):
        print('=== 글 작성자로 검색 ===')
        writer = input('search writer:')
        res = self.dao.selectByWriter('%' + writer + '%')
        if res == None:
            print('exception')
        elif len(res) == 0:
            print('없는 글 작성자')
        else:
            for i in res:
                print(i)

    # 글타이틀로 검색
    def getByTitle(self):
        print('=== 글 번호로 검색 ===')
        title = input('search title:')
        res = self.dao.selectByTitle('%' + title + '%')
        if res == None:
            print('exception')
        elif len(res) == 0:
            print('없는 글 작성자')
        else:
            for i in res:
                print(i)

    # 수정
    def editBoard(self):
        print('=== 글 수정 ===')
        num = int(input('edit num:'))
        b:Board = self.dao.selectByNum(num)

        if b == None:  # 중복 안됨
            print('없는 글 번호. 수정 취소')
        else:
            data = []  # 빈리스트
            s = ['title', 'content']
            for i in range(0, len(s)):
                data.append(input('new ' + s[i] + ': '))

            for idx, i in enumerate(data):
                if i != '':  # 해당 항목에서 그냥 엔터치고 공백으로 넘어가면 해당 항목은 수정안하고 넘어가겠다/ 공백문자 아니면 수정된 값 대체하기
                    b.__setattr__(s[idx], i)  # 객체의 멤버변수 값을 수정하는 함수 / s[idx] = s의 이름 / i = 사용자가 입력한 값

            self.dao.update(b)

    #삭제
    def delBoard(self):
        print('=== 삭제 ===')
        num = input('del num:')
        self.dao.delete(num)

    #전체출력
    def printAll(self):
        print('=== 전체 출력 ===')
        data = self.dao.selectAll()
        for i in data:
            print(i)