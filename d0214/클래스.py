# class classname:
#     내용

class Point:
    cnt = 0 # static 변수(정적변수/ 클래식 변수). 객체 생성 상관없이 존재
    def __init__(self, x = 0, y = 0): # 생성자 self : java 의 this와 동일 / 현재 객체를 의미
        # 객체를 생성해야 변수가 생성됨
        # 멤버변수는 생성자를 호출할 시에 생성하는 것이 좋다
        self.x = x
        self.y = y

    def printXY(self): # 일반 메서드
        print('x:', self.x)
        print('y:', self.y)

    def method1(): # 클래스 이름으로 접근 / 클래스 변수나 메서드만 사용이 가능함
        print('정적 메서드')
        print('cnt:', Point.cnt)

if __name__ == '__main__':
    print('cnt:', Point.cnt)
    p1 = Point()
    p1.printXY()
    Point.method1()

    Point.cnt = 2
    p2 = Point(4, 5)
    p2.printXY()
    Point.method1()


