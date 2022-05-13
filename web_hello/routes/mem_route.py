from flask import render_template, request, Blueprint, session, redirect

from web_hello.bus_info.vo import MemBus
from web_hello.member.service import MemberService
from web_hello.member.vo import Member
from  web_hello.bus_info.service import Service

bp = Blueprint('member', __name__, url_prefix='/member')
service = MemberService()
bus_service = Service()

@bp.route('/join_form', methods=['GET'])  # /member/join: get 방식 요청
def joinForm(): # 회원가입 양식 주는것
    return render_template('member/join_form.html')

@bp.route('/join_proc', methods=['POST'])  # /member/join: post 방식 요청
def join(): # 회원가입 양식에 작성하고 가입버튼 누른 요청. 가입완료 처리해주는 것
    id = request.form['id']
    pwd = request.form['pwd']
    name = request.form['name']
    email = request.form['email']
    m:Member = service.getById(id)
    if m == None:
        service.addMember(Member(id, pwd, name, email))
        msg = '회원가입이 정상적으로 되었습니다'
    else:
        msg = '이미 있는 아이디입니다'
    return render_template('/member/join_result.html', msg=msg)

@bp.route('/login_form')
def loginForm():
    return render_template('member/login_form.html')

@bp.route('/login_proc', methods=['POST'])
def login():
    id = request.form['id']
    pwd = request.form['pwd']
    msg = '로그인 정상 처리'
    m:Member = service.getById(id)
    if m == None:
        msg = '없는 아이디'
    else:
        if pwd == m.pwd:
            session['flag'] = True
            session['loginId'] = id
        else:
            msg = '패스워드 불일치'
    return render_template('member/login_result.html', msg=msg)

# 내정보 보기(로그인한 사람)
@bp.route('/mypage', methods = ['GET'])
def mypage():
    if session['flag'] == True:
        m:Member = service.getById(session['loginId'])
        session['name'] = m.name
        session['pwd'] = m.pwd
        session['email'] = m.email
        return render_template('member/mypage.html')

# 내 정보 수정하기
@bp.route('/edit_form', methods=['GET'])
def editForm():
    if session['flag'] != True:
        return redirect('member/login_form')
    m:Member = service.getById(session['loginId'])
    edit_email = m.email
    return render_template('member/edit_form.html', edit_email=edit_email)

@bp.route('/edit_proc', methods=['POST'])
def edit():
    new_pwd = request.form['pwd']
    new_email = request.form['email']
    name = request.form['name']
    id = request.form['id']
    m: Member = service.getById(id)
    if id == m.id:
        service.editMember(Member(id, new_pwd, name, new_email))
        msg = '수정이 완료되었습니다'
    else:
        msg = '수정할 id가 존재하지 않습니다'
    return render_template('member/edit_result.html', msg=msg)

# 로그아웃
@bp.route('/logout_proc')
def logout():
    session.clear()
    return redirect('/')

# 탈퇴
@bp.route('/delete_proc')
def delete():
    m:Member = service.getById(session.get('loginId'))
    service.delMember(m.id)
    session.clear()
    return redirect('/')

# 내 버스 목록
@bp.route('/mybus')
def mybus():
    id = session['loginId']
    b = bus_service.findBus(id)
    return render_template('member/mybus.html', res=b)