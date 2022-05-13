# http://ws.bus.go.kr/api/rest/busRouteInfo/getBusRouteList?ServiceKey=인증키&strSrch=3

import json

import requests
from bs4 import BeautifulSoup


class BusService:
    def __init__(self):
        self.key = 'BYgs6%2FjSL0du1z8yK4GxYdW1SepukkJ0gXtUP3tGUQpjThEU4JeQKRlspdSnxTWcjia6U6r5oPxW%2F7tK7HZ2sg%3D%3D'

    # 버스명으로 검색해서 노선정보(노선유형, 기점, 종점, 배차간격, ...) 출력
    def getBusInfo(self):
        num = input('검색할 버스명: ')
        url = 'http://ws.bus.go.kr/api/rest/busRouteInfo/getBusRouteList?'
        url += 'ServiceKey=' + self.key
        url += '&strSrch=' + num

        html = requests.get(url).text
        root = BeautifulSoup(html, 'lxml-xml')
        code = root.find('headerCd').get_text()
        if code == '0':
            name = root.find('busRouteNm').get_text()
            route = root.find('routeType').get_text()
            start = root.find('stStationNm').get_text()
            end = root.find('edStationNm').get_text()
            term = root.find('term').get_text()

            print('=== 정보 출력 ===')
            print('버스명: ' + str(name) + ' / 경로타입: ' + str(route) + ' / 기점: ' + str(start) + ' / 종점: ' + str(end) + ' / 배차간격(분): ' + str(term))
        else:
            print('예외발생')

    # 버스명으로 검색해서 이 버스가 경우하는 정거장 순번과 이름들을 출력
    def getBusRoute(self):
        num = input('검색할 버스명: ')
        url1 = 'http://ws.bus.go.kr/api/rest/busRouteInfo/getBusRouteList?'
        url1 += 'ServiceKey=' + self.key
        url1 += '&strSrch=' + num

        html = requests.get(url1).text
        root1 = BeautifulSoup(html, 'lxml-xml')
        code = root1.find('headerCd').get_text()
        if code == '0':
            id_org = root1.find('busRouteId').get_text()
            id = id_org
            url2 = 'http://ws.bus.go.kr/api/rest/busRouteInfo/getStaionByRoute?'
            url2 += 'ServiceKey=' + self.key
            url2 += '&busRouteId=' + id

            html = requests.get(url2).text
            root2 = BeautifulSoup(html, 'lxml-xml')
            code = root2.find('headerCd').get_text()
            if code == '0':
                seq_org = root2.find_all('seq')
                stationNm_org= root2.find_all('stationNm')

                for i in range(len(seq_org)):
                    print('순번 : ' + seq_org[i].get_text())
                    print('정류소이름 : ' + stationNm_org[i].get_text())
            else:
                print('예외발생')
