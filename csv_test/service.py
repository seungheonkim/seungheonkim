import json

import pandas as pd
import requests as requests
import json
from csv_test.vo import TraffInfo, Food


class Service:
    # param 으로 시 이름을 받아서 그 시의 교통사고 현황 결과를 반환
    def getByLoc1(self,loc1):
        data = pd.read_csv('files/노인교통사고.csv', index_col='시도', encoding='euc-kr')
        d1 = data.loc[loc1] # param으로 받은 도시이름으로 검색 / loc : index 기준으로 줄로 추출
        size = len(d1)  # 검색된 줄 수
        res = []    # vo 담을 그릇 만들기
        for i in range(0, size):
            row = d1.iloc[i] # 한 줄만 추출하기 /인덱스 번호로 접근 : iloc[]
            t = TraffInfo(loc1, row['시군구'], row['발생건수'], row['사망자수'],
                          row['부상자수'], row['중상'], row['경상'],
                          row['부상신고'])
            res.append(t)

        return res

    def getMovieinfo(self, num):
        movie = pd.read_excel('files/영화순위.xlsx', index_col='순위', engine='openpyxl') #openpyxl pip install openpyxl 다운
        m1 = movie.loc[num]
        print(m1)

    def getByHtml(self):
        url = 'https://www.kobis.or.kr/kobis/business/stat/boxs/findWeeklyBoxOfficeList.do'
        html = requests.get(url, headers={'User-agent' : 'Mozilla/5.0'}).text
        mv = pd.read_html(html, index_col='순위', encoding='utf-8')[0]
        mv = mv.dropna()    # Nan 결측치 제거하기
        print(mv)

    # 고속도로별로 음식이 무엇이 있는지 제공해주는 함수
    def getFoodInfo(self, routeName):
        f = open('files/serviceAreaFoods.json', 'r', encoding='utf-8')
        json_data = json.load(f)
        res = []
        for key in json_data:
            f = json_data[key]
            if routeName in f['http://data.ex.co.kr:80/link/def/routeName'][0]['value']:
                foodvo = Food()
                for j in f: # 음식정보를 하나씩 추출
                    ss = j.split('/')
                    title = ss[len(ss) - 1]  # 전체 길이 -1 -> 마지막 항목인 routeName 같은것들
                    if title.startswith('rdf'): # rdf-schema 항목은 메뉴이름과 중복이기 때문에 제외
                        continue
                    data = f[j][0]['value']
                    foodvo.__setattr__(title, data)
                    print(title, data)
                res.append(foodvo)
        return res
