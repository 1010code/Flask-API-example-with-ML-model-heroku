import pickle
import gzip

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
# PROJECT_DIR = os.path.join(PROJECT_ROOT,'../../')
PROJECT_DIR=''

# 載入Model
with gzip.open(PROJECT_DIR+'model/xgboost-iris.pgz', 'rb') as f:
    xgboostModel = pickle.load(f)

def test():
    return "This is model.py"

def predict(input):
    predicted=xgboostModel.predict(input)[0]
    print(predicted)
    return predicted