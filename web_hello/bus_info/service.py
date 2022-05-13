import requests
from bs4 import BeautifulSoup
from web_hello.bus_info.vo import Bus, Station, MemBus
from web_hello.bus_info.dao import BusDao


class Service:
    def __init__(self):
        self.key = 'BYgs6%2FjSL0du1z8yK4GxYdW1SepukkJ0gXtUP3tGUQpjThEU4JeQKRlspdSnxTWcjia6U6r5oPxW%2F7tK7HZ2sg%3D%3D'

    def getBusinfoByNm(self, busnm):
        url = 'http://ws.bus.go.kr/api/rest/busRouteInfo/getBusRouteList?'
        url += 'ServiceKey='+self.key
        url += '&strSrch='+ busnm
        html = requests.get(url).text # url로 요청을 보내고 받은 응답 페이지 텍스트를 html에 저장
        root = BeautifulSoup(html, 'lxml-xml') # 파서 객체 생성
        headerCd = root.find('headerCd').text
        if headerCd != '0':
            msg = root.find('headerMsg').text
            print(msg)
            return

        routeList = root.find_all('itemList') #태그 이름이 'itemList'인 모든 태그 요소를 리스트에 담아서 반환
        res = []
        for route in routeList:
            busRouteId = route.find('busRouteId').text
            busRouteNm = route.find('busRouteNm').text
            stStationNm = route.find('stStationNm').text
            edStationNm =  route.find('edStationNm').text
            firstBusTm = route.find('firstBusTm').text
            lastBusTm = route.find('lastBusTm').text
            term = route.find('term').text
            res.append(Bus(busid=busRouteId, busnm=busRouteNm, ststat=stStationNm, edstat=edStationNm, sttime=firstBusTm, edtime=lastBusTm, term=term))

        return res

    # 버스명으로 검색된 애들 중 하나를 선택
    def getBusinfoByBusId(self, busid):
        url = 'http://ws.bus.go.kr/api/rest/busRouteInfo/getRouteInfo?'
        url += 'ServiceKey='+self.key
        url += '&busRouteId='+ busid
        html = requests.get(url).text # url로 요청을 보내고 받은 응답 페이지 텍스트를 html에 저장
        root = BeautifulSoup(html, 'lxml-xml') # 파서 객체 생성
        headerCd = root.find('headerCd').text
        if headerCd != '0':
            msg = root.find('headerMsg').text
            print(msg)
            return

        routeList = root.find_all('itemList') #태그 이름이 'itemList'인 모든 태그 요소를 리스트에 담아서 반환
        res = []
        for route in routeList:
            busRouteId = route.find('busRouteId').text
            busRouteNm = route.find('busRouteNm').text
            stStationNm = route.find('stStationNm').text
            edStationNm = route.find('edStationNm').text
            firstBusTm = route.find('firstBusTm').text
            lastBusTm = route.find('lastBusTm').text
            term = route.find('term').text
            res.append(Bus(busid=busRouteId, busnm=busRouteNm, ststat=stStationNm, edstat=edStationNm, sttime=firstBusTm, edtime=lastBusTm, term=term))

        return res

    # 버스 즐겨찾기 추가하기
    def addBus(self, b:MemBus):
        dao = BusDao()
        dao.insert(b)

    def findBus(self, memid):
        dao = BusDao()
        res = dao.selectAll(memid)
        return res

    # 버스명으로 검색해서 이 버스가 경유하는 정거장 순번과 이름들을 출력
    def getBusRoute(self, busid):
        url = 'http://ws.bus.go.kr/api/rest/busRouteInfo/getStaionByRoute?'
        url += 'ServiceKey=' + self.key
        url += '&busRouteId=' + busid

        html = requests.get(url).text
        root = BeautifulSoup(html, 'lxml-xml')
        headerCd = root.find('headerCd').get_text()

        if headerCd != '0':
            msg = root.find('headerMsg').text
            print(msg)
            return

        stationList = root.find_all('itemList')  # 태그 이름이 'itemList'인 모든 태그 요소를 리스트에 담아서 반환
        res = []
        for station in stationList:
            seq = station.find('seq').text
            stationNm = station.find('stationNm').text
            direction = station.find('direction').text
            gpsX = station.find('gpsX').text
            gpsY = station.find('gpsY').text
            res.append(Station(seq=seq, name=stationNm, direction=direction, x=gpsX, y=gpsY))

        return res




