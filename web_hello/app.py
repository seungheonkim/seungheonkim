from flask import Flask, render_template, session
# bus_route 의 bp 객체를 불러와서 bus_bp 라고 불러오겠다
from web_hello.routes.bus_route import bp as bus_bp
from web_hello.routes.mem_route import bp as mem_bp

app = Flask(__name__)   # 웹 어플리케이션
app.secret_key = '1111' # secret_key 를 지정해줘야 session이 사용가능하다
app.register_blueprint(bus_bp)
app.register_blueprint(mem_bp)

@app.route('/') # 요청 url 등록
def root(): # root 함수를 통해
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
    session['flag'] = False # 현재 첫 실행시에는 로그인이 되어있지 않은 상태

