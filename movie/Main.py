import movie.service as service

if __name__ == '__main__':
    serv = service.BoxOffService()
    # res = serv.getBoxOfficeDaily()
    # serv.printBoxOfficeDaily(res)

    # 영화코드를 파람으로 받아서 영화 상세 내용을 출력하기
    # 영화상세내용 : 영화코드/제목/감독/배우/개봉일
    serv.getMovieInfo('20124079')


