# 리스트[1-10]를 하나 만들고, 파라미터로 받아서, 검색할 숫자
def search(data:list, val:int):
    if val in data:
        return data.index(val)

def myinput():
    name = input('name:')
    tel = input('tel:')
    address = input('address:')
    # 파이선은 값 여러개 반환 가능. 튜플 형태로 반환
    return name, tel, address

if __name__ == '__main__':
    d = [1,2,3,4,5,6,7,8,9,10]
    val = 5
    res = search(d, 5)
    if res != None:
        print(res, '방에 있음')
    else:
        print('not found')

    res = search(d, 15)
    if res != None:
        print(res, '방에 있음')
    else:
        print('not found')

    res = myinput()
    print(type(res))
    for i in res:
        print(i)
    name, tel, address = myinput()
    print(name, tel, address)