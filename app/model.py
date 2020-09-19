import pickle
import gzip

import pickle 
print(pickle.format_version)
# 載入Model
with gzip.open('app/model/xgboost-iris.pgz', 'rb') as f:
    xgboostModel = pickle.load(f)
    print(xgboostModel)

def test():
    return "This is model.py"

def predict(input):
    predicted=xgboostModel.predict(input)[0]
    print(predicted)
    return predicted