from flask import Flask, render_template, request
from service import Service
serv = Service()

#플라스크 객체 생성
app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/wine_form')
def form():
    return render_template('form.html')

@app.route('/wine_test', methods=['POST'])
def test1():
    data=[]
    data.append(float(request.form['fixed acidity']))
    data.append(float(request.form['volatile acidity']))
    data.append(float(request.form['citric acid']))
    data.append(float(request.form['residual sugar']))
    data.append(float(request.form['chlorides']))
    data.append(float(request.form['free sulfur dioxide']))
    data.append(float(request.form['total sulfur dioxide']))
    data.append(float(request.form['density']))
    data.append(float(request.form['pH']))
    data.append(float(request.form['sulphates']))
    data.append(float(request.form['alcohol']))
    level = serv.wine_test(data)
    print(level)
    return render_template('index.html', level=level)


if __name__ == '__main__':
    app.run(debug=True)#flask 서버 실행