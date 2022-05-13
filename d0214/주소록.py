# 1.추가 / 2.검색 / 3.수정 / 4.삭제 / 5.전체출력 / 6.종료
# 이름, 전화, 주소

# vo 만들기
#vo
class Addr:  #주소 1개
    def __init__(self, name:str=None, tel:str=None, addr:str=None):
        self.name = name
        self.tel = tel
        self.addr = addr

    def __str__(self): # toString(). 객체 설명 메서드
        return 'name:'+self.name+' / tel:'+self.tel+' / addr:'+self.addr

#Dao
class AddrDao:
    def __init__(self):
        self.data = []

    # 추가 메서드
    def insert(self, a:Addr):
        self.data.append(a)

    # 검색 메서드
    def select(self, name:str):
        for i in self.data:
            if name == i.name:
                return i

    # 삭제(name)
    def delete(self, name:str):
        a = self.select(name)
        if a==None:
            print('없는 이름')
        else:
            self.data.remove(a)

# service
class AddrService:
    def __init__(self):
        self.dao = AddrDao()

    #추가. name 중복 허용 안됨
    def addAddr(self):
        print('=== 추가 ===')
        while True:
            name = input('name:')
            a = self.dao.select(name)
            if a==None: #중복 안됨
                break #while문 빠져나옴
            else:
                print('중복된 이름. 다시입력하시오')
        tel = input('tel:')
        addr = input('addr:')
        self.dao.insert(Addr(name=name, tel=tel, addr=addr))

    #검색: 검색할 이름을 입력받아서 dao로 검색한 결과 출력
    def printAddr(self):
        print('=== 검색 ===')
        name = input('search name:')
        a = self.dao.select(name)
        if a==None: #중복 안됨
            print('없는 이름')
        else:
            print(a)

    #수정
    def editAddr(self):
        print('=== 수정 ===')
        name = input('edit name:')
        a = self.dao.select(name)
        if a == None:  # 중복 안됨
            print('없는 이름. 수정 취소')
        else:
            a.tel = input('new tel:')
            a.addr = input('new addr:')

    #삭제
    def delArrd(self):
        print('=== 삭제 ===')
        name = input('del name:')
        self.dao.delete(name)

    #전체출력
    def printAll(self):
        for i in self.dao.data:
            print(i)

#menu
class Menu:
    def __init__(self):
        self.service = AddrService()

    def run(self):
        while True:
            m = input('1.추가 2.검색 3.수정 4.삭제 5.전체출력 6.종료')
            if m == '1':
                self.service.addAddr()
            elif m == '2':
                self.service.printAddr()
            elif m == '3':
                self.service.editAddr()
            elif m == '4':
                self.service.delArrd()
            elif m == '5':
                self.service.printAll()
            elif m == '6':
                break  # while문 종료

if __name__=='__main__':
    m = Menu()
    m.run()