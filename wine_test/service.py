import joblib
import numpy as np
import sklearn

class Service:
    def wine_test(self, data:list):
        model = joblib.load('static/winequality_model.pkl')
        input = np.array([data])
        pred = model.predict(input)
        print('pred : ', pred)
        return pred