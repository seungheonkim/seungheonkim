from flask import Flask, render_template
from service import ReviewService
import pandas as pd

service = ReviewService()
model_path = 'static/senti.pkl'

app = Flask(__name__)  #웹 어플리케이션

@app.route('/')  # 요청 url 등록
def root():
    return render_template('index.html')

@app.route('/fit')  # 요청 url 등록
def fit():
    service.review_fit()
    score = service.review_test()
    return render_template('index.html', score=score)

@app.route('/senti')  # 요청 url 등록
def senti():
    df = pd.read_excel('static/movie_review.xls', sheet_name='sheet2')
    title = df['title']
    avg_score = df['avg_score']
    res_df = service.review_pred('static/movie_review.xls', 'sheet1', model_path)
    return render_template('senti_res.html', title=title, avg_score=avg_score, res_df=res_df)

if __name__=='__main__':
    app.run()
