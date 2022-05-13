import joblib
import pandas as pd
import re
from konlpy.tag import Twitter
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

class ModelService:
    def __init__(self):
        self.vec = None  # 벡터화 객체
        self.twitter = Twitter() # 한글 토큰화

    # train, test 파일 읽어서 데이터 프레임으로 변환 함수
    def read_dataFile(self, path):
        df = pd.read_csv(path, sep='\t')
        df = df.fillna(' ')
        X = df['document'].apply(lambda x: re.sub(r"\d+", " ", x))
        y = df['label']
        return X, y

    # 예측 데이터 읽어서 데이터 프레임으로 변환
    def read_predFile(self, path):
        df = pd.read_excel(path, sheet_name='sheet1')
        df = df.dropna()
        return df['review'].apply(lambda x: re.sub(r"\d+", " ", x))

    # 텍스트 토큰화함수
    def tw_tokenizer(self, text):
        # 입력 인자로 들어온 text 를 형태소 단어로 토큰화 하여 list 객체 반환
        tokens_ko = self.twitter.morphs(text)
        return tokens_ko

    # 벡터화 객체 생성 및 벡터화 객체에 학습 데이터 적용
    def tran_fit(self, fit_data):
        self.vec = TfidfVectorizer(tokenizer=self.tw_tokenizer, ngram_range=(1, 2), min_df=3, max_df=0.9)
        self.vec.fit(fit_data) # fit_data 기반으로 사전 생성

    # data를 사전을 참조해서 벡터화
    def data_vectorizer(self, data):
        data_vec = self.vec.transform(data)
        return data_vec

    # 학습 후 모델 반환
    def fit(self, X, y):
        lr = LogisticRegression(random_state=0)
        lr.fit(X, y)
        return lr

    # 테스팅할 모델, X, y 받아서 예측 및 평가
    def test(self, model, X, y):
        pred = model.predict(X)
        return accuracy_score(y, pred)

    def saveFile(self, model, fname):
        joblib.dump(model, fname+'.pkl')

    def loadFile(self, fname):
        return joblib.load(fname)

class ReviewService: # 학습, 평가, 예측
    def __init__(self):
        self.model = None # 파일에서 로드한 모델 저장할 변수
        self.modelservice = ModelService()

    def review_fit(self):
        # 학습 파일 로드 및 전처리
        X_train, y_train = self.modelservice.read_dataFile('static/ratings_train.txt')
        # 학습 데이터를 벡터 변환기에 설정=> 사전 생성
        self.modelservice.tran_fit(X_train)
        # 학습 데이터를 사전 기반으로 벡터화 작업
        X_vec = self.modelservice.data_vectorizer(X_train)
        # 학습
        self.model = self.modelservice.fit(X_vec, y_train)
        # 학습 모델을 파일로 저장
        self.modelservice.saveFile(self.model, 'static/review')

    # 모델 테스팅
    def review_test(self):
        # 테스팅 데이터 파일 로드 및 전처리
        X_test, y_test = self.modelservice.read_dataFile('static/ratings_test.txt')
        # 테스팅 데이터 벡터화
        X_vec = self.modelservice.data_vectorizer(X_test)
        # test()로 평가
        score = self.modelservice.test(self.model, X_vec, y_test)
        print('score:', score)
        return score

    # 실제 데이터 적용. 예측할 데이터와 모델로 테스팅
    def review_pred(self, path, sheet_name, model_path):
        # 멤버 변수 모델이 널이면 테스팅할 모델이 없으므로
        if self.model == None:
            # 이미 학습한 파일 모델을 로드
            self.model = joblib.load(model_path)
            # 학습 데이터를 로드해서 사전생성
            X_train, y_train = self.modelservice.read_dataFile('static/ratings_train.txt')
            self.modelservice.tran_fit(X_train)

        # 예측할 실제 데이터 로드 및 전처리
        df = pd.read_excel(path, sheet_name=sheet_name)
        df = df.dropna()
        X_data = df['review'].apply(lambda x: re.sub(r"\d+", " ", x))

        # 학습 때 생성한 사전으로 벡터화 작업
        X_vec = self.modelservice.data_vectorizer(X_data)
        print(X_vec[:10])
        # 벡터화된 데이터로 예측
        pred = self.model.predict(X_vec)
        print(pred)
        df['pred']=pred
        return df.values
