import torch

# 1. 1차원 텐서
t = torch.FloatTensor([0., 1., 2., 3., 4., 5., 6.])
print(t)

# 배열 차원
print(t.dim())

# shape
print(t.shape)

# shape와 동일
print(t.size())

# 인덱스로 접근
print(t[0], t[1], t[-1])

# 슬라이싱
print(t[2:5], t[4:-1])
# 슬라이싱
print(t[:2], t[3:])

#2. 2차원 텐서
t = torch.FloatTensor([[1., 2., 3.],
                       [4., 5., 6.],
                       [7., 8., 9.],
                       [10., 11., 12.]])
print(t)

print(t.dim())  # rank. 즉, 차원
print(t.shape)
print(t.size()) # shape

print(t[:, 1]) # 첫번째 차원을 전체 선택한 상황에서 두번째 차원의 첫번째 것만 가져온다.
print(t[:, 1].size()) # ↑ 위의 경우의 크기

print(t[:, :-1]) # 첫번째 차원을 전체 선택한 상황에서 두번째 차원에서는 맨 마지막에서 첫번째를 제외하고 다 가져온다.

#3. 브로드캐스팅
m1 = torch.FloatTensor([[3, 3]])
m2 = torch.FloatTensor([[2, 2]])
print(m1 + m2)

# Vector + scalar
m1 = torch.FloatTensor([[1, 2]])
m2 = torch.FloatTensor([3]) # [3] -> [3, 3]
print(m1 + m2)

print(m1+5)

# 2 x 1 Vector + 1 x 2 Vector
m1 = torch.FloatTensor([[1, 2]])
m2 = torch.FloatTensor([[3], [4]])
print(m1 + m2)

#4. 행렬곱셈
m1 = torch.FloatTensor([[1, 2], [3, 4]])
m2 = torch.FloatTensor([[1], [2]])
print('Shape of Matrix 1: ', m1.shape) # 2 x 2
print('Shape of Matrix 2: ', m2.shape) # 2 x 1
print(m1.matmul(m2)) # [[1*1 + 2*2], [3*1 + 4*2]]

m1 = torch.FloatTensor([[1, 2], [3, 4]])
m2 = torch.FloatTensor([[1], [2]])
print('Shape of Matrix 1: ', m1.shape) # 2 x 2
print('Shape of Matrix 2: ', m2.shape) # 2 x 1
print(m1 * m2) # [[1*1 , 2*1], [3*2 , 4*2]]
print(m1.mul(m2))

#5. 평균
t = torch.FloatTensor([1, 2])
print(t.mean())

t = torch.FloatTensor([[1, 2], [3, 4]])
print(t.mean())

# dim은 차원 축소 속성으로 dim=0은 행을 제거, dim=1은 열을 제거함

print(t.mean(dim=0)) #dim=0: 열끼리 계산.
'''
 [[1, 2],
  [3, 4]]
  [1과3의 평균, 2와4의 평균]
'''

print(t.mean(dim=1)) #dim=1: 행끼리 계산
'''
 [[1, 2],
  [3, 4]]
  [1과2의 평균, 3와4의 평균]
'''

print(t.mean(dim=-1)) #dim=1과 동일. 행끼리 계산

#6. 덧셈

t = torch.FloatTensor([[1, 2], [3, 4]])
print(t.sum()) # 단순히 원소 전체의 덧셈을 수행
print(t.sum(dim=0)) # 행을 제거
print(t.sum(dim=1)) # 열을 제거
print(t.sum(dim=-1)) # 열을 제거

#7. 최대(Max, ArgMax)
t = torch.FloatTensor([[1, 2], [3, 4]])
print(t.max()) # Returns one value: max

print(t.max(dim=0)) # Returns two values: max and argmax

# [1, 1]도 함께 리턴. max에 dim 인자를 주면 argmax도 함께 리턴.
# argmax는 최대값 요소의 위치(인덱스)

print('Max: ', t.max(dim=0)[0])
print('Argmax: ', t.max(dim=0)[1])

print(t.max(dim=1))
print(t.max(dim=-1))

#8. 뷰(view) -> 텐서의 shape 변경
import numpy as np

t = np.array([[[0, 1, 2],
               [3, 4, 5]],
              [[6, 7, 8],
               [9, 10, 11]]])
ft = torch.FloatTensor(t)

print(ft.shape)

#3차원 텐서에서 2차원 텐서로 변경

print(ft.view([-1, 3])) # ft라는 텐서를 (?, 3)의 크기로 변경
print(ft.view([-1, 3]).shape)

print(ft.view([-1, 1, 3]))
print(ft.view([-1, 1, 3]).shape)

# 9. 스퀴즈(Squeeze) - 차원이 1인것 제거
ft = torch.FloatTensor([[0], [1], [2]])
print(ft)
print(ft.shape)

print(ft.squeeze())
print(ft.squeeze().shape)

# 9. 언스퀴즈(UnSqueeze) - 특정위치에 1인 차원을 추가함
ft = torch.Tensor([0, 1, 2])
print(ft.shape)

print(ft.unsqueeze(0)) # 인덱스가 0부터 시작하므로 0은 첫번째 차원을 의미한다.
print(ft.unsqueeze(0).shape)

#view로도 표현가능
print(ft.view(1, -1))
print(ft.view(1, -1).shape)

print(ft.unsqueeze(1))#1번째 차원 추가
print(ft.unsqueeze(1).shape)

#10. 타입캐스팅
lt = torch.LongTensor([1, 2, 3, 4])
print(lt)

print(lt.float())

bt = torch.ByteTensor([True, False, False, True])
print(bt)

print(bt.long())
print(bt.float())

#11. 연결하기(concatenate)
x = torch.FloatTensor([[1, 2], [3, 4]])
y = torch.FloatTensor([[5, 6], [7, 8]])

print(torch.cat([x, y], dim=0))
print(torch.cat([x, y], dim=1))

#12. 스택킹(Stacking)
x = torch.FloatTensor([1, 4])
y = torch.FloatTensor([2, 5])
z = torch.FloatTensor([3, 6])

print(torch.stack([x, y, z]))

print(torch.cat([x.unsqueeze(0), y.unsqueeze(0), z.unsqueeze(0)], dim=0))

print(torch.stack([x, y, z], dim=1))

# 13) ones_like와 zeros_like - 0으로 채워진 텐서와 1로 채워진 텐서
x = torch.FloatTensor([[0, 1, 2], [2, 1, 0]])
print(x)

# 입력 텐서와 크기를 동일하게 하면서 값을 1로 채우기
print(torch.ones_like(x))

# 입력 텐서와 크기를 동일하게 하면서 값을 0으로 채우기
print(torch.zeros_like(x))

# 14) In-place Operation (덮어쓰기 연산)
x = torch.FloatTensor([[1, 2], [3, 4]])

print(x.mul(2.)) # 곱하기 2를 수행한 결과를 출력
print(x) # 기존의 값 출력

#연산 뒤에 _를 붙이면 기존의 값을 덮어씀
print(x.mul_(2.))  # 곱하기 2를 수행한 결과를 변수 x에 값을 저장하면서 결과를 출력
print(x) # 기존의 값 출력


