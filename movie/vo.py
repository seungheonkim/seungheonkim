#box office vo
class BoxOff:
    def __init__(self, type, date, rank, rankinter, title, open_date, movieco, salesAmt, audiCnt, audiAcc, screenCnt):
        self.type = type
        self.date = date
        self.rank = rank
        self.rankinter = rankinter
        self.title = title
        self.open_date = open_date
        self.movieco = movieco
        self.salesAmt = salesAmt
        self.audiCnt = audiCnt
        self.audiAcc = audiAcc
        self.screenCnt = screenCnt

    def __str__(self) -> str:
        data = ''
        data += '타입: ' + self.type + '\n'
        data += '기준일: ' + self.date + '\n'
        data += '순위: '+self.rank+'\n'
        data += '제목: ' + self.title + '\n'
        data += '새진입여부: ' + self.rankinter + '\n'
        data += '개봉일: ' + self.open_date + '\n'
        data += '영화코드: ' + self.movieco + '\n'
        data += '매출액: ' + self.salesAmt + '\n'
        data += '관객수: ' + self.audiCnt + '\n'
        data += '누적관객수: ' + self.audiAcc + '\n'
        data += '스크린수: ' + self.screenCnt + '\n'
        return data


