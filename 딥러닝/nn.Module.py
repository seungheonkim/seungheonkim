# 파이토치에는 선형 회귀모델이 구현되어 함수로 제공되고 있다.
#
# 선형 회귀 모델: nn.Linear(input_dim, output_dim)
# 평균 제곱오차: nn.functional.mse_loss(prediction, y_train)
import torch
import torch.nn as nn
import torch.nn.functional as F

torch.manual_seed(1)

# 데이터
x_train = torch.FloatTensor([[1], [2], [3]])
y_train = torch.FloatTensor([[2], [4], [6]])

# 모델을 선언 및 초기화.
model = nn.Linear(1, 1)

# 2개의 값이 출력되는데 첫번째 값이 W고, 두번째 값이 b
# 두 값 모두 현재는 랜덤 초기화가 되어져 있다
print(list(model.parameters()))

# optimizer 정의. 경사 하강법 SGD를 사용하고 learning rate를 의미하는 lr은 0.01
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

# 전체 훈련 데이터에 대해 경사 하강법을 2,000회 반복
nb_epochs = 2000
for epoch in range(nb_epochs + 1):

    # H(x) 계산
    prediction = model(x_train)

    # cost 계산
    cost = F.mse_loss(prediction, y_train)  # <== 파이토치에서 제공하는 평균 제곱 오차 함수

    # cost로 H(x) 개선하는 부분
    # gradient를 0으로 초기화
    optimizer.zero_grad()
    # 비용 함수를 미분하여 gradient 계산
    cost.backward()  # backward 연산
    # W와 b를 업데이트
    optimizer.step()

    if epoch % 100 == 0:
        # 100번마다 로그 출력
        print('Epoch {:4d}/{} Cost: {:.6f}'.format(
            epoch, nb_epochs, cost.item()
        ))

# 임의의 입력 4를 선언
new_var = torch.FloatTensor([[4.0]])
# 입력한 값 4에 대해서 예측값 y를 리턴받아서 pred_y에 저장
pred_y = model(new_var)  # forward 연산
# y = 2x 이므로 입력이 4라면 y가 8에 가까운 값이 나와야 제대로 학습이 된 것
print("훈련 후 입력이 4일 때의 예측값 :", pred_y)

print(list(model.parameters()))

# H(x)식에 x입력 로부터 예측된 y를 얻는 것을 forward 연산한다.
# 학습 전, prediction = model(x_train)은 x_train으로부터 예측값을 리턴하므로 forward 연산이다.
# 학습 후, pred_y = model(new_var)는 임의의 값 new_var로부터 예측값을 리턴하므로 forward 연산이다.
# 학습 과정에서 비용 함수를 미분하여 기울기를 구하는 것을 backward 연산이라고 한다.
# cost.backward()는 비용 함수로부터 기울기를 구하라는 의미이며 backward 연산이다.
# <다중 선형 회귀 라이브러리 함수로 구현>
# 가설: H(x) = w1x1 + w2x2 + w3x3 + b

torch.manual_seed(1)

# 데이터
x_train = torch.FloatTensor([[73, 80, 75],
                             [93, 88, 93],
                             [89, 91, 90],
                             [96, 98, 100],
                             [73, 66, 70]])
y_train = torch.FloatTensor([[152], [185], [180], [196], [142]])

# 모델을 선언 및 초기화. 다중 선형 회귀이므로 input_dim=3, output_dim=1.
model = nn.Linear(3, 1)

print(list(model.parameters()))

# optimizer 정의 . 학습률 lr=0.00001
optimizer = torch.optim.SGD(model.parameters(), lr=1e-5)

nb_epochs = 2000
for epoch in range(nb_epochs + 1):

    # H(x) 계산
    prediction = model(x_train)
    # model(x_train)은 model.forward(x_train)와 동일함.

    # cost 계산
    cost = F.mse_loss(prediction, y_train)  # <== 파이토치에서 제공하는 평균 제곱 오차 함수

    # cost로 H(x) 개선하는 부분
    # gradient를 0으로 초기화
    optimizer.zero_grad()
    # 비용 함수를 미분하여 gradient 계산
    cost.backward()
    # W와 b를 업데이트
    optimizer.step()

    if epoch % 100 == 0:
        # 100번마다 로그 출력
        print('Epoch {:4d}/{} Cost: {:.6f}'.format(
            epoch, nb_epochs, cost.item()
        ))

# 임의의 입력 [73, 80, 75]를 선언
new_var =  torch.FloatTensor([[73, 80, 75]])
# 입력한 값 [73, 80, 75]에 대해서 예측값 y를 리턴받아서 pred_y에 저장
pred_y = model(new_var)
print("훈련 후 입력이 73, 80, 75일 때의 예측값 :", pred_y)

print(list(model.parameters()))