from flask import Flask, request, render_template, redirect, Blueprint, session
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
bp = Blueprint('upload', __name__, url_prefix='/upload')

app = Flask(__name__)   # 웹 어플리케이션

@app.route('/') # 요청 url 등록
def root():
    return render_template('index.html')


@app.route('/graph')
def graph():
    img_path = 'static/my_plot.png'
    x = [1, 2, 3, 4]
    y = [3, 8, 5, 6]
    fig, ax = plt.subplots()
    plt.plot(x, y)
    fig.savefig(img_path)
    img_path = '/' + img_path
    return render_template('graph.html', img_path=img_path)



@app.route('/form')
def upload_form():
    return render_template('upload/form.html')

@app.route('/upload', methods=['POST'])
def upload():
    upload_path = 'static/img/'
    f = request.files['file']
    fname = upload_path + f.filename  # f.filename:업로드된 파일명
    f.save(fname)
    fname = '/' + fname
    return render_template('upload/img_list.html', img_path=fname)

if __name__ == '__main__':
    app.run(debug=True)

