# -*- coding: utf-8 -*-
# Author: kaizhang01
# Date: 2020/12/20
# Desc:

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader as web
import datetime as dt
import pickle
import copy

from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, LSTM

# Load Data

company = 'XPEV'

start = dt.datetime(2000, 1, 1)
end = dt.datetime(2020, 12, 20)
data = web.DataReader(company, 'yahoo', start, end)

print(data)
# Prepare Data
scaler = MinMaxScaler(feature_range=(0, 1))
scaler_data = scaler.fit_transform(data['Close'].values.reshape(-1, 1))

prediction_days = 60

x_train = []
y_train = []
for x in range(prediction_days, len(scaler_data)):
    x_train.append(scaler_data[x - prediction_days:x, 0])
    y_train.append(scaler_data[x, 0])

x_train, y_train = np.array(x_train), np.array(y_train)
x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

# Build The Model

model = copy.deepcopy(Sequential())

model.add(LSTM(units=50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
model.add(Dropout(0.2))
model.add(LSTM(units=50, return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(units=50))
model.add(Dropout(0.2))

model.add(Dense(units=1))

model.compile(optimizer='adam', loss='mean_squared_error')

model.fit(x_train, y_train, epochs=25, batch_size=32)

'''' Test The Model Accurcy o Existing Data '''

test_start = dt.datetime(2021, 1, 1)

test_end = dt.datetime.now()

test_data = web.DataReader(company, 'yahoo', test_start, test_end)

actual_prices = test_data['Close'].values

total_dataset = pd.concat((data['Close'], test_data['Close']), axis=0)

model_inputs = total_dataset[len(total_dataset) - len(test_data) - prediction_days:].values

model_inputs = model_inputs.reshape(-1, 1)

model_inputs = scaler.transform(model_inputs)

# Make Proedictions on Test Data

x_test = []

for x in range(prediction_days, len(model_inputs)):
    x_test.append(model_inputs[x - prediction_days:x, 0])

x_test = np.array(x_test)

x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

# model就是个python对象，写入本地，变成二进制的文件，相当于java的ObjectOutputStream
file = '/Users/zhangkai/tmp/mm1'
s = pickle.dumps(model)
with open(file, 'wb+') as f:
    f.write(s)

# load 模型，就又变成python的对象，，就可以直接用对象的方法了
mm = pickle.loads(open(file, 'rb').read())

prediction_prices = mm.predict(x_test)
print("本地模型预测结果：", prediction_prices)

prediction_prices = scaler.inverse_transform(prediction_prices)

print(actual_prices)
print(prediction_prices)
# Plot The Test Predictions
plt.plot(actual_prices, color='black', label='真实股价')
plt.plot(prediction_prices, color='green', label="预测股价")
plt.title(f"{company} Share Price")
plt.xlabel('Time')
plt.ylabel(f"{company} Share Price")
plt.legend()
plt.show()

# Prediction Next Day
real_data = [model_inputs[len(model_inputs) + 1 - prediction_days: len(model_inputs + 1)], 1]

real_data = np.array(real_data)

real_data = np.reshape(real_data, (real_data.shape[0], real_data.shape[1], 1))

# print(scaler.inverse_transform(real_data[-1]))

predction = model.predict(real_data)

predction = scaler.inverse_transform(predction)

print(f"Prediction: {predction}")
