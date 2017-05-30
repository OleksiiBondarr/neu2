import matplotlib.pyplot as plt
import numpy as np
import random
my_data = np.genfromtxt('data04.csv', delimiter=';')
full_len = 100
Learn_len = 80
j = 0
k = 0
learn = np.zeros((Learn_len, 3))
test = np.zeros((full_len - Learn_len, 3))
temp_mas = np.zeros((Learn_len, 3))
for i in range(0, full_len, 1):
    if i < Learn_len:
        learn[i] = my_data[i]
    else:
        test[i - Learn_len] = my_data[i]
w_num = 3
weight = np.zeros(w_num)
center = np.zeros(2)
center[0] = 0.8
center[1] = 0.7
n = 0.01
for i in range(0, w_num, 1):
    weight[i] = random.random()*0.1 + 0.1


def out(znach):
    res = 0.
    for i in range(0, w_num - 1, 1):
        res += weight[i] * znach[i]
    res -= weight[2]
    if res >= 0.:
        return 1.
    else:
        return 0.


def teach():
    iter = 0
    while True:
        iter += 1
        error = 0
        for i in range(0, Learn_len, 1):
            for j in range(0, w_num - 1, 1):
                temp_mas[i][j] = gaus(learn[i][0], learn[i][1], j)
            temp_mas[i][2] = learn[i][2]
            check = out(learn[i, :2])
            temp_error = learn[i, 2] - check
            error += abs(temp_error)
            for k in range(0, w_num - 1, 1):
                weight[k] = weight[k] + temp_mas[i][k]*n*(temp_mas[i][2] - check)
            weight[2] = weight[2] - n*(temp_mas[i][2] - check)
        print iter, error
        if not (error > 0.5):
            break


def gaus(x, y, i):
    return np.exp((-(x-center[i])*(x - center[i]) - (y - center[i])*(y - center[i]))/(2*0.01))

teach()
result = np.zeros(full_len - Learn_len)
for i in range(0, full_len - Learn_len, 1):
    result[i] = out(test[i, :2])

for i in range(0, full_len - Learn_len, 1):
    print result[i], ' ', test[i]


def gr():
    for i in range(0, Learn_len, 1):
        if learn[i, 2] == 1:
            plt.plot(learn[i, 0], learn[i, 1], 'bo', label='sampled', c='b')
        else:
            plt.plot(learn[i, 0], learn[i, 1], 'bo', label='sampled', c='r')
    for i in range(0,full_len - Learn_len, 1):
        if test[i, 2] == 1:
            plt.plot(test[i, 0], test[i, 1], 'bo', label='sampled', c='g')
        else:
            plt.plot(test[i, 0], test[i, 1], 'bo', label='sampled', c='k')
    plt.show()
print 'blue and red - patterns, green and black - test'
gr()
