from flask import Blueprint, render_template, request, redirect

from customer.service import CustomerService
from customer.vo import Customer

bp = Blueprint('customer', __name__, url_prefix='/customer')

cus_service = CustomerService()

# 회원가입 페이지
@bp.route('/join')
def joinForm():
    return render_template('customer/form.html')

# 회원가입 진행
@bp.route('/join', methods=['POST'])
def join():
    id = request.form['id']
    pwd = request.form['pwd']
    name = request.form['name']
    email = request.form['email']
    cus_service.join(Customer(id=id, pwd=pwd, name=name, email=email))
    msg='회원가입 완료! 로그인해주세요!'
    return render_template('customer/login.html', msg=msg)


# 로그인 페이지
@bp.route('/login')
def loginForm():
    return render_template('customer/login.html')

# 로그인 처리 진행
@bp.route('/login', methods=['POST'])
def login():
    id = request.form['id']
    pwd = request.form['pwd']
    flag = cus_service.login(id, pwd)
    return render_template('index.html')

# 내 정보 페이지
@bp.route('/myinfo')
def myinfo():
    c = cus_service.myinfo()
    return render_template('customer/myinfo.html', c=c)

# 내 정보 수정
@bp.route('/edit', methods=['POST'])
def editMyInfo():
    pwd = request.form['pwd']
    email = request.form['email']
    cus_service.editMyInfo(pwd, email)
    return render_template('index.html')

# 로그아웃
@bp.route('/logout')
def logout():
    cus_service.logout()
    return render_template('index.html')

# 탈퇴
@bp.route('/deleteMyInfo')
def deleteMyInfo():
    cus_service.deleteMyinfo()
    return render_template('index.html')
