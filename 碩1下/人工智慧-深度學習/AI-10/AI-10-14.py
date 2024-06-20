import pandas as pd

stockdf = pd.read_csv("dataset.csv", index_col=0)
stockdf.dropna(how='any', inplace=True)

# print(stockdf)

from sklearn import preprocessing
from keras.utils import to_categorical
min_max_scaler = preprocessing.MinMaxScaler()

newdf = stockdf.copy()
flagdf = stockdf.copy()

newdf['open'] = min_max_scaler.fit_transform(stockdf.open.values.reshape(-1,1))
newdf['low'] = min_max_scaler.fit_transform(stockdf.low.values.reshape(-1,1))
newdf['high'] = min_max_scaler.fit_transform(stockdf.high.values.reshape(-1,1))
newdf['close'] = min_max_scaler.fit_transform(stockdf.close.values.reshape(-1,1))
newdf['volume'] = min_max_scaler.fit_transform(stockdf.volume.values.reshape(-1,1))

# print(stockdf)
# print(newdf)

import numpy as np
datavalue = newdf.values
result = []

# print(datavalue)

time_frame = 10
for index in range(len(datavalue) - (time_frame+1)):
    result.append(datavalue[index: index+(time_frame+1)])

# print(result)
result = np.array(result)
# print(result.shape[0])
# print(result[0])
# print(result[1])

number_train = round(0.9 * result.shape[0])
X_train = result[:int(number_train), : -1, 0:5]
# print(X_train)
Y_train = result[:int(number_train),-1][:,-1]
# print(Y_train)
Y_train_onehot = to_categorical(Y_train)
# print(Y_train_onehot)

X_test = result[int(number_train):, : -1, 0:5]
Y_test = result[int(number_train):,-1][:,-1]
Y_test_onehot = to_categorical(Y_test)
# print(X_test)
# print(Y_test)
# print(Y_test_onehot)

from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, LSTM


from keras.models import load_model
model = load_model('D:\\lstm.h5')
predictions = model.predict(X_test)
predicted_classes = np.argmax(predictions, axis=1)
print(predicted_classes)
print(Y_test)

print(predictions[0, 0])
print(predicted_classes[0])
print(predictions)
print(predicted_classes)
tp_count = 0
print(Y_test.shape[0])
for i in range(Y_test.shape[0]):
    if(predicted_classes[i] == 2 and Y_train[i] == 2):
        tp_count = tp_count+1
print(tp_count)