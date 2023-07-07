from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
import requests
import re
import json

app = FastAPI()
def deque(userid):
    sendData = {'userid': "multiUser"}
    response = requests.post('https://us-central1-fortesting-c54ba.cloudfunctions.net/post/accessflag', data=sendData)
    getData = response.json()
    userQueue = eval(getData['result']['flagforuser'])

    userQueue.remove(userid)
    postData = {"userid": "multiUser",
                "flagforuser": json.dumps(userQueue),
                "flagforsymptom":getData['result']['flagforsymptom'],
                "flagfordaily":getData['result']['flagfordaily']}
    response = requests.post('https://us-central1-fortesting-c54ba.cloudfunctions.net/post/flag', data=postData)
    print(response)

class multiUserModel(BaseModel):
    userID: str
@app.post("/testMultiUser")
def postForMultiUser(multiUser: multiUserModel):
    userid = multiUser.userID
    sendData = {'userid': "multiUser"}
    response = requests.post('https://us-central1-fortesting-c54ba.cloudfunctions.net/post/accessflag', data=sendData)
    getData = response.json()
    userQueue = eval(getData['result']['flagforuser'])

    userQueue.append(userid)
    postData = {"userid": "multiUser",
                "flagforuser": json.dumps(userQueue),
                "flagforsymptom":getData['result']['flagforsymptom'],
                "flagfordaily":getData['result']['flagfordaily']}
    response = requests.post('https://us-central1-fortesting-c54ba.cloudfunctions.net/post/flag', data=postData)
    if response.status_code == 200:
        return "OK"
    else:
        return "fail"


@app.get("/basicInfo")
def get_for_basic_info():
    
    sendData = {'userid': "multiUser"}
    response = requests.post('https://us-central1-fortesting-c54ba.cloudfunctions.net/post/accessflag', data=sendData)
    getData = response.json()
    userQueue = eval(getData['result']['flagforuser'])
    userid = userQueue[0]

    # Prepare the data
    data = {'userid': userid}
    print("user",userid)
    # Send a POST request
    response = requests.post('https://us-central1-fortesting-c54ba.cloudfunctions.net/post/accessbasic', data=data)
    # Extract data from the response
    if response.status_code == 200:
        user_data = response.json()
    else:
        user_data = {}

    # Prepare the final result
    result = {
        "userID":userid,
        "result": user_data['result']
    }

    deque(userid)
        ################ dequeue

    # sendData = {'userid': "multiUser"}
    # response = requests.post('https://us-central1-fortesting-c54ba.cloudfunctions.net/post/accessflag', data=sendData)
    # getData = response.json()
    # userQueue = eval(getData['result']['flagforuser'])

    # userQueue.pop(0)
    # postData = {"userid": "multiUser",
    #             "flagforuser": json.dumps(userQueue),
    #             "flagforsymptom":getData['result']['flagforsymptom'],
    #             "flagfordaily":getData['result']['flagfordaily']}
    # response = requests.post('https://us-central1-fortesting-c54ba.cloudfunctions.net/post/flag', data=postData)
    # print(response)
            
    return jsonable_encoder(result)


class SymptomsModel(BaseModel):
    userID: str
@app.post("/symptoms")
def post_for_symptoms(symptoms: SymptomsModel):

    userid = symptoms.userID
    # Prepare the data
    data = {'userid': userid}
    # Send a POST request
    response = requests.post('https://us-central1-fortesting-c54ba.cloudfunctions.net/post/accesssymptoms', data=data)
    # Extract data from the response
    if response.status_code == 200:
        user_data = response.json()
    else:
        user_data = {}
    # Prepare the final result
    result = user_data['result']
    
        # Prepare the data
    data1 = {'userid': userid,
                'returns': "",
            'diagnosis': ""}
    # Send a POST request
    response = requests.post('https://us-central1-fortesting-c54ba.cloudfunctions.net/post/diagnosis', data=data1)
    if response.status_code == 200:
         data1  = {}
    else:
        return "post_diagnoss_error"
    
    # Prepare the data
    data2 = {
    'userid': userid,
    "urineprotein": "- ",
    "urineob": "-",
    "urineglucose": "-",
    "bloodhb": "15 g/dL",
    "bloodht": "45 %",
    "bloodplt": "120 x 10^3/µL",
    "bloodpressure": "舒張壓:89 mmHg, 收縮壓:132 mmHg",
    "bloodrbc": "500 x 10^6/µL",
    "bloodwbc": "12.3 x 10^3/µL",
    "cholesterol": "150 mg/dL",
    "hbeag": "-",
    "hbsab": "-",
    "hbsag": "-",
    "kidneybun": "15 mg/dL",
    "liversgot": "25 U/L",
    "liversgpt": "30 U/L",
    "kidneycre": "0.7 mg/dL"
    }
    # Send a POST request
    response = requests.post('https://us-central1-fortesting-c54ba.cloudfunctions.net/post/testinfo', data=data2)
    if response.status_code == 200:
         data2  = {}
    else:
        return "post_testinfo_error"
  

        
    return jsonable_encoder(result)



class ClinicModel(BaseModel):
    userID: str
@app.post("/forClinic")
def post_for_clinic(clinic: ClinicModel):
    userid = clinic.userID
    # Prepare the data
    data = {'userid': userid}
    # Send a POST request
    response = requests.post('https://us-central1-fortesting-c54ba.cloudfunctions.net/post/accessdiagnosis', data=data)
    # Extract data from the response
    if response.status_code == 200:
        user_data = response.json()
        user_data["result"]["userID"]=userid
        result = {
            "result":user_data["result"]
        }
    
        return jsonable_encoder(result)
    else:
        user_data = {}
        return "R"
    # Prepare the final result
 


class RecordsModel(BaseModel):
    userID: str
@app.post("/records")
def post_for_records(records: RecordsModel):
    userid = records.userID

    # Prepare the data
    data = {'userid': userid}

    # Send a POST request
    response = requests.post('https://us-central1-fortesting-c54ba.cloudfunctions.net/post/accesstestinfo', data=data)
    # Extract data from the response
    if response.status_code == 200:
        user_data = response.json()
    else:
        user_data = {}

    # Prepare the final result
    user_data['result']['userID']=userid

    result = {
        "result":user_data['result']
    }
   
    
    return jsonable_encoder(result)


class NextStepModel(BaseModel):
    nextStep: str
@app.post("/nextStep")
def post_next_step(next_step: NextStepModel):
    return "OK"

class waitModel(BaseModel):
    userID : str
    
@app.post("/wait")
def wait(wait: waitModel):



    return jsonable_encoder({
        "result": {
            "userID": wait.userID
        }
    })

class updateDataModel(BaseModel):
    clinicData: str
    userID: str

@app.post("/updateClinic")
def post_for_update_clinic(updateData: updateDataModel):
    
    data = {'userid': updateData.userID}
    # Send a POST request
    response = requests.post('https://us-central1-fortesting-c54ba.cloudfunctions.net/post/accessbasic', data=data)
    # Extract data from the response
    if response.status_code == 200:
        user_data = response.json()
    else:
        user_data = {}
        return updateData.userID
    info_key_mapping = {"姓名":"name", "性別":"gender", "年齡": "age", "身高": "height", "體重": "weight", "家族病史": "family", "個人病史": "record"}
    
    send_user_data = {}

    for i in user_data['result']:
        send_user_data[info_key_mapping[i]] = user_data['result'][i]
    send_user_data['userid'] = updateData.userID
    send_user_data['record'] = updateData.clinicData

    response2 = requests.post('https://us-central1-fortesting-c54ba.cloudfunctions.net/post/basic', data=send_user_data)
    # Extract data from the response
    if response.status_code == 200:
        return send_user_data
    else:
        user_data = {}
        return "update fail"

class isReturnModel(BaseModel):
    message: str
    userID: str

@app.post("/isReturn")
def post_for_isReturn(isReturn: isReturnModel):
    data = isReturn.message
    userid = isReturn.userID

    score = [int(i) for i in re.findall(r'\d+', data)]
    # deque(userid)

    if score[0] > 7: 
        result = {'message':'請您立即回診',
                  'userID': userid}
        requests.post('https://i-care-te-st-21770a966fd0.herokuapp.com/external_api', json=result)

        postData = {"userid": userid,
                    "flagforuser": "",
                    "flagforsymptom":"2",
                    "flagfordaily":"0"}
        response = requests.post('https://us-central1-fortesting-c54ba.cloudfunctions.net/post/flag', data=postData)
        print(response)
        return "1"
    else:
        result = {'message':'您的狀況良好!請繼續保持!OvO',
                  'userID': userid}
        requests.post('https://i-care-te-st-21770a966fd0.herokuapp.com/external_api', json=result)
        postData = {"userid": userid,
                    "flagforuser": "",
                    "flagforsymptom":"2",
                    "flagfordaily":"0"}
        response = requests.post('https://us-central1-fortesting-c54ba.cloudfunctions.net/post/flag', data=postData)
        print(response)
        return "0"
    

class messageModel(BaseModel):
    userID: str
@app.post("/messages")
def post_for_records(data_messages: messageModel):
    userid = data_messages.userID
    # Prepare the data
    data = {'userid': userid}

    # Send a POST request
    response = requests.post('https://us-central1-fortesting-c54ba.cloudfunctions.net/post/accessmessage', data=data)
    # Extract data from the response
    if response.status_code == 200:
        user_data = response.json()
    else:
        user_data = {}

    # Prepare the final result
    user_data['result']['userID']=userid

    result = {
        "result":user_data['result']
    }
   
    
    return jsonable_encoder(result)





# class changeFlagModel(BaseModel):
#     userid: str
#     flagforuser: str
#     flagforsymptom: str
#     flagfordaily: str

# @app.post("/changeFlag")
# def changeFlag(flagForChange: changeFlagModel):
#     userid = flagForChange.userid
#     flagforuser=flagForChange.flagforuser
#     flagforsymptom=flagForChange.flagforsymptom
#     flagfordaily=flagForChange.flagfordaily

#     postData = {"userid": userid,
#                 "flagforuser": flagforuser,
#                 "flagforsymptom":flagforsymptom,
#                 "flagfordaily":flagfordaily}
#     response = requests.post('https://us-central1-fortesting-c54ba.cloudfunctions.net/post/flag', data=postData)
#     print(response)