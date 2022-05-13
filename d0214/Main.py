from addr.menu import Menu

if __name__=='__main__':
    print(__name__) # 모듈명 내장 속성
    print('asdf', __file__) # 소스 파일의 경로 내장 속성

    m = Menu()
    m.run()