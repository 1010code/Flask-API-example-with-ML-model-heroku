# -*- coding: UTF-8 -*-
import numpy as np
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/test', methods=['GET'])
def getResult():
    result = {"id": "Ace","family history": "心臟病, 高血壓, 糖尿病","weight": "60","age": "22","height": "170"}

    return jsonify(result)

@app.route('/predict', methods=['POST'])
def postInput():
    # 取得前端傳過來的數值
    insertValues = request.get_json()
    x1=insertValues['userID']
    # 進行預測
    result = '我起床的時候頭暈'
    return jsonify({'result': str(result)})
