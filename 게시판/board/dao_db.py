import pymysql

from 게시판.board.vo import Board


class BoardDao:
    def __init__(self):
        self.conn = None

    def connect(self):
        self.conn = pymysql.connect(host='localhost', user='user2', password='4321', db='encore_db', charset='utf8')

    def disconn(self):
        self.conn.close()

    # 글쓰기
    def insert(self, b:Board):
        self.connect()
        cursor = self.conn.cursor()
        sql = 'insert into board(writer, w_date, title, content) values(%s, now(), %s, %s)'
        w = (b.writer, b.title, b.content)
        cursor.execute(sql, w)
        self.conn.commit()
        self.disconn()

    # 검색 메서드
    def select(self, num: int):  # num(pk) 기준 검색, 1개 검색
        try:
            self.connect()  # db 연결
            cursor = self.conn.cursor()  # 사용할 커서 객체 생성
            sql = 'select * from board where num=%s'
            d = (num,)
            cursor.execute(sql, d)  # sql 실행
            row = cursor.fetchone()  # fetchone() : 현재 커서 위치의 한줄 추출하는 함수
            if row:
                return Board(row[0], row[1], row[2], row[3], row[4])
        except Exception as e:
            print(e)
        finally:
            self.disconn()

    # 글 번호로 검색
    def selectByNum(self, num:int):
        res = []
        try:
            self.connect()
            cursor = self.conn.cursor()
            sql = 'select * from board where num=%s'
            w = (num,)
            cursor.execute(sql, w)
            row = cursor.fetchone() # fetchone() : 현재 커서 위치의 한줄 추출하는 함수
            if row:
                return Board(row[0], row[1], row[2], row[3], row[4])
        except Exception as e:
            print(e)
        finally:
            self.disconn()

    # 글 작성자로 검색
    def selectByWriter(self, writer:str):
        res = []
        try:
            self.connect()
            cursor = self.conn.cursor()
            sql = 'select * from board where writer like %s'
            w = (writer,)
            cursor.execute(sql, w)  # sql 실행
            for row in cursor:
                res.append(Board(row[0], row[1], row[2], row[3], row[4]))
            return res
        except Exception as e:
            print(e)
        finally:
            self.disconn()

    # 타이틀로 검색
    def selectByTitle(self, title: str):  # name 기준 검색, 여러개 검색
        res = []
        try:
            self.connect()  # db 연결
            cursor = self.conn.cursor()  # 사용할 커서 객체 생성
            sql = 'select * from board where title like %s'
            w = (title,)
            cursor.execute(sql, w)  # sql 실행
            for row in cursor:
                res.append(Board(row[0], row[1], row[2], row[3], row[4]))
            return res
        except Exception as e:
            print(e)
        finally:
            self.disconn()

    # 수정
    def update(self, b:Board):
        try:
            self.connect()
            cursor = self.conn.cursor()
            sql = 'update board set title=%s, content=%s where num=%s'
            w = (b.title, b.content, b.num)
            cursor.execute(sql, w)  # sql 실행
            self.conn.commit()
        except Exception as e:
            print(e)
        finally:
            self.disconn()

    # 삭제(num)
    def delete(self, num:int):
        try:
            self.connect()
            cursor = self.conn.cursor()
            sql = 'delete from board where num=%s'
            w = (num,)
            cursor.execute(sql, w)  # sql 실행
            self.conn.commit()
        except Exception as e:
            print(e)
        finally:
            self.disconn()

    # 전체 목록
    def selectAll(self):
        res = []
        try:
            self.connect()  # db 연결
            cursor = self.conn.cursor()  # 사용할 커서 객체 생성
            sql = 'select * from board order by num'
            cursor.execute(sql)  # sql 실행
            for row in cursor:
                res.append(Board(row[0], row[1], row[2], row[3], row[4]))
            return res
        except Exception as e:
            print(e)
        finally:
            self.disconn()
