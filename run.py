
from app import app

import pickle
import gzip

with gzip.open('xgboost-iris.pgz', 'r') as f:
    xgboostModel = pickle.load(f)
    print(xgboostModel)


@app.route('/')
def index():
    return 'hello  !'


if __name__ == '__main__':
    app.run(debug=True)