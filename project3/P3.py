import pandas as pd
import numpy as np
import random 
import matplotlib.pyplot as plt

my_data = pd.read_csv('covid_cases.csv')
train_data = my_data.sample(frac = 0.9)
test_data = my_data.drop(train_data.index)

def train_set(train_data , R_order):

    x_train = train_data['World'].index
    y_train = train_data['World'] 
    A = np.ones((len(train_data), R_order))
    A[:, 1] = x_train.to_numpy()
    if R_order == 3:
        A[:, 2] = x_train * x_train

    y = y_train.to_numpy()
    X = np.linalg.inv((np.transpose(A).dot(A))).dot(np.transpose(A)).dot(y)
    return X

def test_set(test_data , X , R_order):
    x_test = test_data['World'].index
    y_real = test_data['World'].to_numpy() 

    A = np.ones((len(test_data), R_order))
    A[:, 1] = x_test.to_numpy()
    if R_order == 3:
        A[:, 2] = x_test * x_test

    y = A.dot(X) 
    random_result = random.sample(range(0, len(test_data)), 5)
    for i in random_result:
        print(f'Real value: {y_real[i]}')
        print(f'Estimated value: {y[i]}')
        print(f'Error: {abs(y[i] - y_real[i])}') 
        print('-' * 50)

def data_plot(X , R_order):
    x = my_data.index.to_numpy()
    A = np.ones((len(my_data), R_order))
    A[:, 1] = x
    if R_order == 3:
        A[:, 2] = x * x

    y_estimate = A.dot(X)
    y_real = my_data['World'].to_numpy()
        
    plt.plot(x, y_estimate)
    plt.plot(x, y_real)
    plt.show(block=True)


X = train_set(train_data , 2)
test_set(test_data , X , 2)
data_plot(X , 2)


X = train_set(train_data , 3)
test_set(test_data , X , 3)
data_plot(X , 3)

















