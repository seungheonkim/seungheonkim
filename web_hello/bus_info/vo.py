class Bus:
    def __init__(self, busid=None, busnm=None, ststat=None,
                 edstat=None, sttime=None, edtime=None, term=None, seq=None, stationNm=None):
        self.busid = busid
        self.busnm = busnm
        self.ststat = ststat
        self.edstat = edstat
        self.sttime = sttime
        self.edtime = edtime
        self.term = term
        self.seq = seq
        self.stationNm = stationNm

    def __str__(self):
        s = ''
        s += '버스id: ' + self.busid + '\n'
        s += '버스명: ' + self.busnm + '\n'
        s += '기점: ' + self.ststat + '\n'
        s += '종점: ' + self.edstat + '\n'
        s += '첫차시간: ' + self.sttime + '\n'
        s += '막차시간: ' + self.edtime + '\n'
        s += '배차간격(분): ' + self.term + '\n'

        return s

class Station:
    def __init__(self, seq=None, name=None, direction=None, x=None, y=None):
        self.seq = seq
        self.name = name
        self.direction = direction
        self.x = x
        self.y = y

class MemBus:
    def __init__(self, num:int = 0,memid=None, busid=None, busnm=None, ststat=None, edstat=None,
                 sttime=None, edtime=None, term=None):
        self.num = num
        self.memid = memid
        self.busid = busid
        self.busnm = busnm
        self.ststat = ststat
        self.edstat = edstat
        self.sttime = sttime
        self.edtime = edtime
        self.term = term

