# 자바: 컴파일(.class/바이트코드) + 인터프리터
# 파이썬 : 인터프리터
# 파이썬에서의 변수
# 변수정의는 따러 하지 않음
# 변수이름=값
# 참조타입 : 기본타입 없이 모든 것이 참조타입이다!

a = 10
print(type(a), a)
a = 'asdf'
print(type(a), a)


b = [1,2,3]
for i in b:
    print(i)

print(len(b))

# b[3] = 1 -> b라는 리스트에 인덱스는 0,1,2 뿐임 -> 3번 인덱스는 존재하지 않기 때문에 index outof range 에러 발생
b.append(4)
print(b)

# mutable -> 변경 가능한 타입 ex) list
# immutable -> 변경 불가능한 타입 ex) int, float, str

c = (1,2,3)
print(type(c))

# 튜플을 정의할 경우 하나라면 뒤에 콤마(,) 를 붙인다
d= ( 1, )
print(type(d))

for i in c:
    print(i)

print(c[0])

# dictionary 형태 {}
# json : javascript object notation의 약자, 자바스크립트에서 객체를 정의하는 방법
# [] : 배열, {} : 객체
f = {'name' : 'aaa', 'age' : 12}
for key in f:
    print(key, f[key])
d = {}

# 함수정의
# def 함수명(파라미터 리스트):
#     실행문
#     실헹문

def mysum(data:list):
    s = 0
    for i in data:
        s += i

    return s

def test1(tel, name:str='', age=0):
    print(name, age, tel)
    age += 10

if __name__ == '__main__':
    d = [1,2,3,4,5]
    res = mysum(d)
    print(res)

    test1(age=12, name='sss', tel='1234')
    test1('4567')

# 리스트[1-10]를 하나 만들고, 파라미터로 받아서, 검색할 숫자

