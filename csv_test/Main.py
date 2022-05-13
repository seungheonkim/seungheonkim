from csv_test.service import Service

if __name__ == '__main__':
    service = Service()
    # res = service.getByLoc1('부산')
    res = service.getMovieinfo(3)
    # for i in res:
    # i.printInfo()
    # print(res)

    res2 = service.getByHtml()
    print(res2)

    res3 = service.getFoodInfo('당진영덕고속도로')
    for i in res3:
        print(i)