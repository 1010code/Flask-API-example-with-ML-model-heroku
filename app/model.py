import pickle
import gzip
import xgboost as xgb

PROJECT_DIR=''
# 載入Model
with gzip.open(PROJECT_DIR+'app/model/xgboost-iris.pgz', 'rb') as f:
    print(xgb.__version__)
    xgboostModel = pickle.load(f)
    print(xgboostModel)
    

def test():
    return "This is model.py"

def predict(input):
    predicted=xgboostModel.predict(input)[0]
    print(predicted)
    return predicted