from 게시판.board.service import BoardService

#menu
class Board_Menu:
    def __init__(self):
        self.service = BoardService()

    def run(self):
        while True:
            m = input('1.글쓰기 2.글번호로 검색 3.글작성자로 검색 4.글제목으로 검색 5.수정 6.삭제 7.전체목록 8.종료')
            if m == '1':
                self.service.addBoard()
            elif m == '2':
                self.service.getByNum()
            elif m == '3':
                self.service.getByWriter()
            elif m == '4':
                self.service.getByTitle()
            elif m == '5':
                self.service.editBoard()
            elif m == '6':
                self.service.delBoard()
            elif m == '7':
                self.service.printAll()
            elif m == '8':
                break