import pymysql

from addr.vo import Addr
# 번호(id)/ 이름(pwd)

class AddrDaoDB:
    def __init__(self):
        self.conn = None

    def connect(self):
        self.conn = pymysql.connect(host='localhost', user='user2', password='4321', db='encore_db', charset='utf8')

    def disconn(self):
        self.conn.close()

    # 추가 메서드
    def insert(self, a:Addr):
        # 1. connection 수립
        self.connect()

        # 2. 사용할 cursor객체 생성. db 작업 메서드가 이 클래스에 정의되어 있으므로 꼭 필요.
        cursor = self.conn.cursor()

        # 3. 실행할 sql문 정의
        sql = 'insert into address(name, tel, addr) values(%s, %s, %s)'

        # 4. sql 문에 %s를 사용했다면 각 자리에 들어갈 값을 튜플로 정의
        d = (a.name, a.tel, a.addr)

        # 5. sql 실행(실행할 sql, %s매칭한 튜플)
        cursor.execute(sql, d)

        # 6. 쓰기동작(insert, update, delete) 에서 쓰기 완료
        self.conn.commit()

        # db 커넥션 끊기
        self.disconn()

    # 검색 메서드
    def select(self, num:int): # num(pk) 기준 검색, 1개 검색
        try:
            self.connect() # db 연결
            cursor = self.conn.cursor() # 사용할 커서 객체 생성
            sql = 'select * from address where num=%s'
            d = (num,)
            cursor.execute(sql, d) # sql 실행
            row = cursor.fetchone() # fetchone() : 현재 커서 위치의 한줄 추출하는 함수
            if row:
                return Addr(row[0], row[1], row[2], row[3])
        except Exception as e:
            print(e)
        finally:
            self.disconn()


    # 검색 메서드
    def selectByName(self, name:str): # name 기준 검색, 여러개 검색
        res = []
        try:
            self.connect()  # db 연결
            cursor = self.conn.cursor()  # 사용할 커서 객체 생성
            sql = 'select * from address where name like %s'
            d = (name,)
            cursor.execute(sql, d)  # sql 실행
            for row in cursor:
                res.append(Addr(row[0], row[1], row[2], row[3]))
            return res
        except Exception as e:
            print(e)
        finally:
            self.disconn()

    # 삭제(num)
    def delete(self, num:int):
        try:
            self.connect()  # db 연결
            cursor = self.conn.cursor()  # 사용할 커서 객체 생성
            sql = 'delete from address where num=%s'
            d = (num,)
            cursor.execute(sql, d)  # sql 실행
            self.conn.commit()
        except Exception as e:
            print(e)
        finally:
            self.disconn()

    def update(self, a:Addr):
        try:
            self.connect()  # db 연결
            cursor = self.conn.cursor()  # 사용할 커서 객체 생성
            sql = 'update address set name=%s, tel=%s, addr=%s where num=%s'
            d = (a.name, a.tel, a.addr, a.num)
            cursor.execute(sql, d)  # sql 실행
            self.conn.commit()
        except Exception as e:
            print(e)
        finally:
            self.disconn()

    def selectAll(self):
        res = []
        try:
            self.connect()  # db 연결
            cursor = self.conn.cursor()  # 사용할 커서 객체 생성
            sql = 'select * from address order by num'
            cursor.execute(sql)  # sql 실행
            for row in cursor:
                res.append(Addr(row[0], row[1], row[2], row[3]))
            return res
        except Exception as e:
            print(e)
        finally:
            self.disconn()
