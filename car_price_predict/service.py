# import joblib
# import numpy as np
# import json
# from sklearn.pipeline import make_pipeline
#
# from sklearn.preprocessing import StandardScaler
#
#
# class Service:
#     def __init__(self):
#         self.br_size = 0
#         self.mo_size = 0
#         self.tr_size = 0
#         self.fuel_size = 0
#
#     def read_data(self):
#         f = open('static/car_info.json', 'r')
#         json_data = json.load(f)
#         br = json_data['brand']
#         mo = json_data['models']
#         en = json_data['engine_size']
#         tr = json_data['transmission']
#         fuel = json_data['fuelType']
#
#         self.br_size = len(br)
#         self.mo_size = len(mo)
#         self.tr_size = len(tr)
#         self.fuel_size = len(fuel)
#
#         f.close()
#         return br, mo, en, tr, fuel
#
#     def predict(self, data:list):
#         pred_data = np.zeros((113,))
#         for i in range(0, 5):
#             pred_data[i]=data[i]
#
#         # 브랜드 설정
#         pred_data[5+data[5]]=1
#
#         # 모델 설정
#         pred_data[5+self.br_size + data[6]] = 1
#
#         # 기어 설정
#         pred_data[5 + self.br_size + self.mo_size + data[7]] = 1
#
#         # 연료 설정
#         pred_data[5 + self.br_size + self.mo_size + self.tr_size + data[8]] = 1
#
#         print(pred_data)
#
#         model = joblib.load('static/car_price_pred_inverse-2.pkl')
#         data_input = np.array([pred_data])
#         price = model.predict(data_input)
#         print('price :', price)
#         return price
#
