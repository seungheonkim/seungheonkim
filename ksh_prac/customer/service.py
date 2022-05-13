from customer.vo import Customer, db
from flask import session

class CustomerService:

    # 회원가입
    def join(self, c:Customer):
        db.session.add(c)
        db.session.commit()

    # 로그인
    def login(self, id:str, pwd:str):
        cus = Customer.query.get(id)
        if cus != None:
            if pwd == cus.pwd:
                session['login_id'] = id
                session['flag'] = True
                return True
        return False

    # 내 정보 보기
    def myinfo(self):
        id = session['login_id']
        return Customer.query.get(id)

    # 내 정보 수정
    def editMyInfo(self, pwd:str, email:str):
        cus = self.myinfo()
        cus.pwd = pwd
        cus.email = email
        db.session.commit()

    # 로그아웃
    def logout(self):
        session.clear()
        session['flag'] = False

    # 탈퇴
    def deleteMyinfo(self):
        cus = self.myinfo()
        db.session.delete(cus)
        db.session.commit()
        self.logout()