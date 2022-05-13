from addr.service import AddrService

#menu
class Menu:
    def __init__(self):
        self.service = AddrService()

    def run(self):
        while True:
            m = input('1.추가 2.번호로검색 3.이름으로검색 4.수정 5.삭제 6.전체출력 7.종료')
            if m == '1':
                self.service.addAddr()
            elif m == '2':
                self.service.getByNum()
            elif m == '3':
                self.service.printAddr()
            elif m == '4':
                self.service.editAddr()
            elif m == '5':
                self.service.delArrd()
            elif m == '6':
                self.service.printAll()
            elif m == '7':
                break  # while문 종료