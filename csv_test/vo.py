import numpy as np


class TraffInfo:
    def __init__(self, loc1=None, loc2=None, acc=0, dnum=0, wnum=0, hnum=0, lnum=0, callnum=0):
        self.loc1 = loc1    # 시도
        self.loc2 = loc2    # 시군구
        self.acc = acc  # 발생건수
        self.dnum = dnum    # 사망자수
        self.wnum = wnum    # 부상자수
        self.hnum = hnum    # 중상
        self.lnum = lnum    # 경상
        self.callnum = callnum  # 부상신고

    # def printInfo(self):
    #     print('시도:', self.loc1)
    #     print('시군구:', self.loc2)
    #     print('발생건수:', self.acc)
    #     print('사망자수:', self.dnum)
    #     print('부상자수:', self.wnum)
    #     print('중상:', self.hnum)
    #     print('경상:', self.lnum)
    #     print('부상신고:', self.callnum)

    def __str__(self):  # toString
        return '시도:' + self.loc1 + ' / 시군구:' + self.loc2 + ' / 발생건수:' + \
               self.acc.astype('str') + ' / 사망자수:' + self.dnum.astype('str') + \
               ' / 부상자수:' + self.wnum.astype('str') + ' / 중상:' + self.hnum.astype('str') + \
               ' / 경상:' + self.lnum.astype('str') + ' / 부상신고:' + self.callnum.astype('str')

class Food:
    def __init__(self, salePrice=None, batchMenu=None, serviceAreaName=None,
                 routeName=None, direction=None):
        self.batchMenu = batchMenu
        self.salePrice = salePrice
        self.serviceAreaName = serviceAreaName
        self.routeName = routeName
        self.direction = direction

    def __str__(self):
        return 'batchMenu:' + self.batchMenu + ' / salePrice:' + self.salePrice + ' / serviceAreaName:' + \
               self.serviceAreaName + ' / routeName:' + self.routeName + \
               ' / direction:' + self.direction