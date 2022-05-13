import pymysql
from web_hello.bus_info.vo import MemBus

#Dao
class BusDao:
    def __init__(self):
        self.conn = None

    def connect(self):
        self.conn = pymysql.connect(host='localhost', user='user2', password='4321', db='encore_db', charset='utf8')

    def disconn(self):
        self.conn.close()

    # 추가 메서드
    def insert(self, b:MemBus):
        #1. db 커넥션 수립
        self.connect()

        # 2. 사용할 cursor객체 생성. db 작업 메서드가 이 클래스에 정의되어 있으므로 꼭 필요.
        cursor = self.conn.cursor()

        # 3. 실행할 sql문 정의
        sql = 'insert into membus(memid, busid, busnm, ststat, edstat, sttime, edtime, term)'
        sql += 'values(%s, %s, %s, %s, %s, %s, %s, %s)'

        # 4. sql 문에 %s를 사용했다면 각 자리에 들어갈 값을 튜플로 정의
        d = (b.memid, b.busid, b.busnm, b.ststat, b.edstat, b.sttime, b.edtime, b.term)

        # 5. sql 실행(실행할 sql, %s매칭한 튜플)
        cursor.execute(sql, d)

        # 6. 쓰기동작(insert, update, delete) 에서 쓰기 완료
        self.conn.commit()

        # db 커넥션 끊음
        self.disconn()

    # 삭제(name)
    def delete(self, busid:str):
        try:
            self.connect()  # db연결
            cursor = self.conn.cursor()  # 사용할 커서 객체 생성
            sql = 'delete from membus where busid = %s'
            d = (busid,)
            cursor.execute(sql, d)  # sql 실행
            self.conn.commit()

            return print('삭제가 완료되었습니다.')

        except Exception as e:
            print(e)
        finally:
            self.disconn()

    # memid 가 현재 가진 bus 정보 추출하기
    def selectAll(self, memid:str):
        res = []
        try:
            self.connect()  # db 연결
            cursor = self.conn.cursor()  # 사용할 커서 객체 생성
            sql = 'select * from membus where memid = %s'
            d = (memid, )
            cursor.execute(sql, d)  # sql 실행
            for row in cursor:
                res.append(MemBus(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]))
            return res
        except Exception as e:
            print(e)
        finally:
            self.disconn()
