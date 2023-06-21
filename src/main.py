from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
import requests
import re

app = FastAPI()

@app.get("/basicInfo")
def get_for_basic_info():
    userid = "Ue1350bef1851afd418a9aa81e444eaa7"

    # Prepare the data
    data = {'userid': userid}

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
        "urineprotein": "-",
        "urineob": "-",
        "urineglucose": "-",
        "bloodhb": "15",
        "bloodht": "45",
        "bloodplt": "30",
        "bloodpressure": "73-124",
        "bloodrbc": "500",
        "bloodwbc": "5500 %",
        "cholesterol": "150",
        "hbeag": "-",
        "hbsab": "-",
        "hbsag": "-",
        "kidneybun": "15",
        "liversgot": "25",
        "liversgpt": "30",
        "kidneycre": "0.7"
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
    if score[0] > 7: 
        result = {'message':'請您立即回診',
                  'userID': userid}
        requests.post('https://i-care-te-st-21770a966fd0.herokuapp.com/external_api', json=result)
        return "1"
    else:
        result = {'message':'您的狀況良好!請繼續保持!OvO',
                  'userID': userid}
        requests.post('https://i-care-te-st-21770a966fd0.herokuapp.com/external_api', json=result)
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
