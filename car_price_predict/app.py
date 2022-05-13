from flask import Flask, render_template, request
from service import Service
serv = Service()

app = Flask(__name__)  #웹 어플리케이션

@app.route('/')  # 요청 url 등록
def root():
    br, mo, en, tr, fuel = serv.read_data()
    return render_template('index.html', enumerate=enumerate, br=br, mo=mo, en=en, tr=tr, fuel=fuel)

@app.route('/test',methods=['POST'])  # 요청 url 등록
def test():
    year=float(request.form['year'])
    mileage=float(request.form['mileage'])
    tax=float(request.form['tax'])
    mpg=float(request.form['mpg'])
    brand=int(request.form['brand'])
    models=int(request.form['models'])
    engine=float(request.form['engine'])
    tr=int(request.form['tr'])
    fuel=int(request.form['fuel'])

    price = serv.predict([year, mileage, tax, mpg, engine, brand, models, tr, fuel])
    return render_template('result.html', price=price)

if __name__=='__main__':
    app.run()