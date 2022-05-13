#pip3 install pymysql
import pymysql

# 1. db 커넥션 수립
conn = pymysql.connect(host='localhost', user='user2', password='4321', db='encore_db', charset='utf8')

# 2. 사용할 cursor객체 생성. db 작업 메서드가 이 클래스에 정의되어 있으므로 꼭 필요.
cursor = conn.cursor()

# 3. 실행할 sql문 정의
sql = 'insert into member values(%s, %s, %s, %s)'
#sql = 'insert into member values(:1, :2, :3, :4)'

# 4. sql 문에 %s를 사용했다면 각 자리에 들어갈 값을 튜플로 정의
d = ('abc4', '5555', 'nameabc', 'abc@email.com')

# 5. sql 실행(실행할 sql, %s매칭한 튜플)
cursor.execute(sql, d)

# 6. 쓰기동작(insert, update, delete) 에서 쓰기 완료
conn.commit()

#검색
sql = 'select * from member'
cursor.execute(sql) # execute()으로 검색하면 검색한 결과를 cursor에 담아 줌
for row in cursor:
    print(row[0], ' / ',row[1], ' / ',row[2], ' / ',row[3])

conn.close()

'''
create table member(
    id varchar(20) primary key,
    pwd varchar(20),
    name varchar(20),
    email varchar(50)
);
'''