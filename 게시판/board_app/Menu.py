from 게시판.board.menu import Board_Menu
from 게시판.member.menu import Mem_Menu


class SMenu:
    def __init__(self):
        self.b_menu = Board_Menu()
        self.m_menu = Mem_Menu()

    def run(self):
        while True:
            m = input('1.회원관리 2.게시판 3.종료')
            if m == '1':
                self.m_menu.run()
            elif m == '2':
                self.b_menu.run()
            elif m == '3':
                break