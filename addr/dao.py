from addr.vo import Addr

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