import torch
# 뉴런 네트워크
import torch.nn as nn
# 딥러닝과 관련된 함수 제공해주는 패키지
import torch.nn.functional as F
# 최적화 작업 수행 패키지
import torch.optim as optim

#랜덤 시드(random seed)
torch.manual_seed(1)

#학습 데이터와 레이블 변수에 저장
x_train = torch.FloatTensor([[1], [2], [3]]) #학습 데이터
y_train = torch.FloatTensor([[2], [4], [6]]) #학습 레이블(정답)

print(x_train)
print(y_train)

#가중치w와 편향 b 0으로 초기화하여 정의

#requires_grad=True:  이 변수는 학습을 통해 계속 값이 변경되는 변수임을 의미
W = torch.zeros(1, requires_grad=True)
b = torch.zeros(1, requires_grad=True)

print(W)
print(b)

#가설 수식 만들기
hypothesis = x_train * W + b

#비용함수 정의
#cost = 1/n((예측값1-실제값1)제곱 + (예측값2-실제값2)제곱 ...)
cost = torch.mean((hypothesis - y_train) ** 2)

#경사 하강 알고리즘 정의. lr은 학습률
optimizer = optim.SGD([W, b], lr=0.01)

# gradient를 0으로 초기화
optimizer.zero_grad()
# 비용 함수를 미분하여 gradient 계산
cost.backward()
# W와 b를 업데이트
optimizer.step()

print(cost)
print(W)
print(b)

# <전체 코드>
# 에포크(Epoch)는 전체 훈련 데이터가 학습에 한 번 사용된 주기
# 데이터
x_train = torch.FloatTensor([[1], [2], [3]])
y_train = torch.FloatTensor([[2], [4], [6]])
# 모델 초기화
W = torch.zeros(1, requires_grad=True)
b = torch.zeros(1, requires_grad=True)
# optimizer 설정
optimizer = optim.SGD([W, b], lr=0.01)

nb_epochs = 1999 # 원하는만큼 경사 하강법을 반복
for epoch in range(nb_epochs + 1):

    # H(x) 계산
    hypothesis = x_train * W + b

    # cost 계산
    cost = torch.mean((hypothesis - y_train) ** 2)

    # cost로 H(x) 개선
    optimizer.zero_grad()
    cost.backward()
    optimizer.step()

    # 100번마다 로그 출력
    if epoch % 100 == 0:
        print('Epoch {:4d}/{} W: {:.3f}, b: {:.3f} Cost: {:.6f}'.format(
            epoch, nb_epochs, W.item(), b.item(), cost.item()
        ))

# 파이토치는 미분을 통해 얻은 기울기를 이전에 계산된 기울기 값에 누적시킴. 그래서 미분을 초기화해주는 optimizer.zero_grad() 함수를 사용해야함
w = torch.tensor(2.0, requires_grad=True)

nb_epochs = 20
for epoch in range(nb_epochs + 1):
    z = 2*w
    z.backward()
    print('수식을 w로 미분한 값 : {}'.format(w.grad))

# 다중선형회귀
torch.manual_seed(1)

# 훈련 데이터
#퀴즈1 5명의점수
x1_train = torch.FloatTensor([[73], [93], [89], [96], [73]])

#퀴즈2 5명의점수
x2_train = torch.FloatTensor([[80], [88], [91], [98], [66]])

#퀴즈3 5명의점수
x3_train = torch.FloatTensor([[75], [93], [90], [100], [70]])

#기말 5명의점수
y_train = torch.FloatTensor([[152], [185], [180], [196], [142]])

# 가중치 w와 편향 b 초기화
w1 = torch.zeros(1, requires_grad=True)
w2 = torch.zeros(1, requires_grad=True)
w3 = torch.zeros(1, requires_grad=True)
b = torch.zeros(1, requires_grad=True)

# optimizer 설정
optimizer = optim.SGD([w1, w2, w3, b], lr=1e-5)

nb_epochs = 1000
for epoch in range(nb_epochs + 1):

    # H(x) 계산
    hypothesis = x1_train * w1 + x2_train * w2 + x3_train * w3 + b

    # cost 계산
    cost = torch.mean((hypothesis - y_train) ** 2)

    # cost로 H(x) 개선
    optimizer.zero_grad()
    cost.backward()
    optimizer.step()

    # 100번마다 로그 출력
    if epoch % 100 == 0:
        print('Epoch {:4d}/{} w1: {:.3f} w2: {:.3f} w3: {:.3f} b: {:.3f} Cost: {:.6f}'.format(
            epoch, nb_epochs, w1.item(), w2.item(), w3.item(), b.item(), cost.item()
        ))

# 벡터와 행렬 연산으로 바꾸기
# x의 개수가 3개였으니까 x1_train, x2_train, x3_train와 w1, w2, w3를 일일히 선언했지만 x의 개수가 1,000개라고 하면 일일이 선언하기는 힘들다. 이를 행렬로 변환하여 처리하면 훨씬 간단해 진다.
#전체 코드
x_train = torch.FloatTensor([[73, 80, 75],
                             [93, 88, 93],
                             [89, 91, 80],
                             [96, 98, 100],
                             [73, 66, 70]])
y_train  =  torch.FloatTensor([[152],  [185],  [180],  [196],  [142]])

# 모델 초기화
W = torch.zeros((3, 1), requires_grad=True)
b = torch.zeros(1, requires_grad=True)
# optimizer 설정
optimizer = optim.SGD([W, b], lr=1e-5)

nb_epochs = 20
for epoch in range(nb_epochs + 1):

    # H(x) 계산
    # 편향 b는 브로드 캐스팅되어 각 샘플에 더해집니다.
    hypothesis = x_train.matmul(W) + b

    # cost 계산
    cost = torch.mean((hypothesis - y_train) ** 2)

    # cost로 H(x) 개선
    optimizer.zero_grad()
    cost.backward()
    optimizer.step()

    print('Epoch {:4d}/{} hypothesis: {} Cost: {:.6f}'.format(
        epoch, nb_epochs, hypothesis.squeeze().detach(), cost.item()
    ))

