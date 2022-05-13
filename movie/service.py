import movie.vo as vo
import requests
import json

class BoxOffService:
    def __init__(self):
        self.url='http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?'
        self.url2='http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?'
        self.key = 'ffeec26ea234c9b4c04cddb33bf824b0'


    def mkUrl(self, param, date): # param:[0, 2]
        self.url += 'key='+self.key
        self.url += '&targetDt='+date
        val = [('Y', 'N'), ('K', 'F')]
        params = ['&multiMovieYn=', '&repNationCd=']
        for idx, v in enumerate(param):# param:[0, 2]
            if v < 2:
                self.url += params[idx]+val[idx][v]
                print(self.url)


    def getBoxOfficeDaily(self):
        date = input('박스 오피스 기준일(yyyymmdd):')
        p1 = int(input('0.다양성영화 1.상업영화 2.전체(기본)'))
        if p1 < 0 or p1 > 2:
            p1 = 2

        p2 = int(input('0.한국영화 1.외국영화 2.전체(기본)'))
        if p2 < 0 or p2 > 2:
            p2 = 2

        self.mkUrl([p1, p2], date)

        html = requests.get(self.url).text
        res = json.loads(html)
        data = res['boxOfficeResult']
        type = data['boxofficeType']
        date = data['showRange']
        list = data['dailyBoxOfficeList']
        res = []

        for m in list:
            res.append(vo.BoxOff(type, date, m['rank'], m['rankInten'], m['movieNm'], m['openDt'], m['movieCd'], m['salesAmt'], m['audiCnt'], m['audiAcc'], m['scrnCnt']))

        return res

    def printBoxOfficeDaily(self, res):
        for m in res:
            print(m)

    # 영화코드를 파람으로 받아서 영화 상세 내용을 출력하기
    # 영화상세내용 : 영화코드/제목/감독/배우/개봉일

    def getMovieInfo(self, code):
        url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?'
        url += 'key=' + self.key
        url += '&movieCd=' + code
        html = requests.get(url).text
        res = json.loads(html)
        obj = res['movieInfoResult']
        mobj = obj['movieInfo']
        mcode = mobj['movieCd']
        ktitle = mobj['movieNm']
        etitle = mobj['movieNmEn']
        opendt = mobj['openDt']

        directors = mobj['directors']   # 리스트형태
        d_names = []    # 감독이름 저장 vo
        for d in directors:
            d_names.append(d['peopleNm'])

        actors = mobj['actors'] # 리스트형태
        a_names = []    # 배우이름 저장 vo
        for a in range(0, 3):   # 너무 많아서 3명만 출력
            aobj = actors[a]
            name = aobj['peopleNm']
            cast = aobj['cast']
            a_names.append('배우명: ' + name + ' / 배역: ' + cast)
        print('영화코드: ', mcode)
        print('영화명: ', ktitle)
        print('영화영문제목명: ', etitle)
        print('개봉일: ', opendt)
        print('감독명: ')
        for n in d_names:
            print(n)
        print('배우명: ')
        for n in a_names:
            print(n)
