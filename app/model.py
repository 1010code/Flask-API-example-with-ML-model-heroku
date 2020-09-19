import pickle
import gzip
import xgboost as xgb

import pickle 
print(pickle.format_version)
# 載入Model
# with gzip.open(PROJECT_DIR+'app/model/xgb(classfication)-42-12000-scale-all.pgz', 'rb') as f:
#     print(xgb.__version__)
#     xgboostModel = pickle.load(f)
#     print(xgboostModel)

def test():
    return "This is model.py"

def predict(input):
    predicted=xgboostModel.predict(input)[0]
    print(predicted)
    return predicted