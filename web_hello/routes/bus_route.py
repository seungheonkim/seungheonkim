from flask import Flask, render_template, request, Blueprint, session
from web_hello.bus_info.service import Service
from web_hello.bus_info.vo import MemBus, Bus

# 버스와 관련된 기능 제공 클래스
bus_service = Service()

# 블루프린트 객체 생성 : 라우트 등록 객체
# (부를이름, 실행되는 값, 기본 url 설정값)
bp = Blueprint('bus', __name__, url_prefix='/bus')

@bp.route('/businfo', methods=['POST'])
def businfo():
    # form 양식의 이름이 'busnm' 인 요소의 값을 읽음
    busnm = request.form['busnm']

    # busnm 으로 검색해서 res 리스트에 담음
    res = bus_service.getBusinfoByNm(busnm)

    # bus 디렉토리 밑의 busList 페이지를 보여주는데, 이때 res라는 데이터 전송
    # 앞이 view 페이지에서 부를 이름, 뒤에서 받아올 값
    return render_template('bus/busList.html', res=res)

@bp.route('/stationinfo/<string:id>')  # string 인 id 값을 받아올것이다 {{b.busid}}
def stationinfo(id):
    res = bus_service.getBusRoute(id)
    return render_template('bus/stationinfo.html', res=res)

# 1. 자주 사용하는 버스 등록: 등록폼에 버스이름을 입력 이걸로 검색해서 있으면 등록후 결과 페이지 정보 추출해서 db에 저장,
# 없는 버스면 없다는 결과 출력하기
@bp.route('/bus_regist_form', methods=['GET'])
def registBus():
    return render_template('bus/bus_regist_form')

@bp.route('/addbus/<string:busid>', methods=['GET','POST'])
def addbus(busid):
    res:Bus = bus_service.getBusinfoByBusId(busid)
    id = session['loginId']
    bus = ''
    check = True
    for i in res:
        bus = i
    b:MemBus = bus_service.findBus(id)

    for j in b:
        if bus.busid == j.busid:
            check = False

    if check == False:
        msg = '이미 등록되어있는 버스입니다'
    else:
        bus_service.addBus(MemBus(memid=id, busid=bus.busid, busnm=bus.busnm, ststat=bus.ststat, edstat=bus.edstat, sttime=bus.sttime, edtime=bus.edtime, term=bus.term))
        msg = '즐겨찾기 등록이 완료되었습니다'
    return render_template('bus/add_result.html', msg=msg)

# 2. 등록한 버스 목록
# 등록한 모든 버스 db에서 읽어서 정보 출력