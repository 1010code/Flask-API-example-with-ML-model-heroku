# -*- coding: UTF-8 -*-
import numpy as np
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
flagForSymptoms = 0
flagForBasicInfo = 0
flagForRecords = 0

@app.route('/changeFlag', methods=['POST'])
def postForChangeFlag():
    global flagForSymptoms
    global flagForBasicInfo
    global flagForRecords

    insertValues = request.get_json()
    flagForSymptoms=insertValues['flagForSymptoms']
    flagForBasicInfo=insertValues['flagForBasicInfo']
    flagForRecords=insertValues['flagForRecords']

    return "OK"


@app.route('/basicInfo', methods=['GET'])
def getForBasicInfo():
    result = {
    "flag":flagForBasicInfo,
    "result":
    {
        
        "id": "Ace",
        "familyHistory": "心臟病, 高血壓, 糖尿病",
        "weight": "60",
        "age": "18",
        "height": "180"
    }

}     # LINE API 
    return jsonify(result)

@app.route('/symptoms', methods=['POST'])
def postForSymptoms():
    # 取得前端傳過來的數值
    insertValues = request.get_json()
    x1=insertValues['userID']
    flag = 1
    result = {
    "flag":"1",
    "result":
    {
        
        "symptom":"我今天頭很痛"
        
    }

}     # LINE API 
    return jsonify(result)

@app.route('/forClinic', methods=['POST']) # test 從雅典娜回傳 json 檔
def postForClinic():
    insertValues = request.get_json()
    message=insertValues['forClinic']
    return "OK"

@app.route('/records', methods=['POST']) # 缺看診紀錄
def postForRecords():
    # 取得前端傳過來的數值
    insertValues = request.get_json()
    x1=insertValues['userID']
    flag = 1
    result = {
        "flag":"1",
        "result":
        {
            "id": "Ace",
            "xray": "-",
            "urineob": "-",
            "bloodhb": "15",
            "bloodrbc": "500",
            "liversgot": "25",
            "liversgpt": "30",
            "hbeag": "-",
            "bloodwbc": "5500",
            "bloodplt": "30",
            "bloodht": "45",
            "hbsag": "-",
            "urineglucose": "-",
            "cholesterol": "150",
            "bloodpressure": "73-124",
            "urineprotein": "-",
            "kidneycre": "0.7",
            "hbsab": "-",
            "kidneybun": "15",
            "familyHistory": "心臟病, 高血壓, 糖尿病",
           
        }

    }     # LINE API 
    return jsonify(result)

@app.route('/nextStep', methods=['POST']) # test 從雅典娜回傳 json 檔
def postNextStep():
    insertValues = request.get_json()
    nextstep=insertValues['nextStep'] # 兩個方向的判斷
    return "OK"






####################### for early testing ###############################################

@app.route('/test', methods=['GET'])
def test():
    
    #['Ace': {"id": "Ace","family history": "心臟病, 高血壓, 糖尿病","weight": "60","age": "22","height": "170"}]
    result = {"id": "Ace","family history": "心臟病, 高血壓, 糖尿病","weight": "60","age": "22","height": "170"}
    return jsonify(result)

@app.route('/right', methods=['POST'])
def postInput():
    insertValues = request.get_json()
    x1=insertValues['userID']
    result = 1
    text = "我今天頭很痛" # LINE API 症狀
    return jsonify({'result': str(result), 'text': str(text)})

@app.route('/test2', methods=['GET'])
def getResult2():
    
    #['Ace': {"id": "Ace","family history": "心臟病, 高血壓, 糖尿病","weight": "60","age": "22","height": "170"}]
    result = 1
    return jsonify({'result': str(result)})

@app.route('/test3', methods=['GET'])
def getResult3():
    
    #['Ace': {"id": "Ace","family history": "心臟病, 高血壓, 糖尿病","weight": "60","age": "22","height": "170"}]
    result = {
    "flag":"1",    
    "result":[
        {
            "id": "Ace",
            "familyHistory": "心臟病, 高血壓, 糖尿病",
            "weight": "60",
            "age": "22",
            "height": "170"
        }
    ]
}
    return jsonify(result)