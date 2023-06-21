from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
import requests
import time

app = FastAPI()

# Global variables
flagForSymptoms: Optional[int] = 0
flagForBasicInfo: Optional[int] = 0
flagForRecords: Optional[int] = 1
flagForClinic: Optional[int] = 1

urlForChange= "https://for-api-32f276cf322d.herokuapp.com/changeFlag"

class FlagModel(BaseModel):
    target: str
    val: int
   


@app.post("/changeFlag")
def post_for_change_flag(flag: FlagModel):
    global flagForSymptoms
    global flagForBasicInfo
    global flagForRecords
    global flagForClinic

    if flag.target == "flagForSymptoms":
        flagForSymptoms = flag.val
        return "OK"
    
    elif flag.target == "flagForBasicInfo":
        flagForBasicInfo = flag.val
        return "OK"
    
    elif flag.target == "flagForRecords":
        flagForRecords = flag.val
        return "OK"
    
    elif flag.target == "flagForClinic":
        flagForClinic = flag.val
        return "OK"
    

    return "fail"



class AllFlagModel(BaseModel):
    flagForSymptoms: int
    flagForBasicInfo: int
    flagForRecords: int
    flagForClinic: int


@app.post("/changeAllFlag")
def post_for_change_All_flag(flag: AllFlagModel):
    global flagForSymptoms
    global flagForBasicInfo
    global flagForRecords
    global flagForClinic

    flagForSymptoms = flag.flagForSymptoms
    flagForBasicInfo = flag.flagForBasicInfo
    flagForRecords = flag.flagForRecords
    flagForClinic = flag.flagForClinic

    return "OK"


@app.get("/getFlag")
def get_for_flag():
    return jsonable_encoder({
        "flagForSymptoms": flagForSymptoms,
        "flagForBasicInfo": flagForBasicInfo,
        "flagForRecords": flagForRecords,
        "flagForClinic": flagForClinic,

    })


@app.get("/basicInfo")
def get_for_basic_info():
    userid = "Ue1350bef1851afd418a9aa81e444eaa7"
    flag = flagForBasicInfo

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
        "flag": flag,
        "userID":userid,
        "result": user_data['result']
    }
    # changeFlag = {
    #     "target": "flagForBasicInfo",
    #     "val": 0 
    # }
    # for i in range(5):
    # # Send a POST request
    #     response = requests.post(urlForChange, json=changeFlag)
    #     # Extract data from the response
    #     if response.status_code == 200:
    #         user_data = response.json()
    #     else:
    #         user_data = {}
    #     time.sleep(0.2)
            
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
    
    result = {
        user_data['result']
    }
        # Prepare the data
    data1 = {'userid': userid,
                'returns': "",
            'diagnosis': ""}
    # Send a POST request
    response = requests.post('https://us-central1-fortesting-c54ba.cloudfunctions.net/post/diagnosis', data=data1)
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
        
  

        
    return jsonable_encoder(result)



class ClinicModel(BaseModel):
    userID: str
@app.post("/forClinic")
def post_for_clinic(clinic: ClinicModel):
    userid = clinic.userID
    flag = flagForClinic
    # Prepare the data
    data = {'userid': userid}
    # Send a POST request
    response = requests.post('https://us-central1-fortesting-c54ba.cloudfunctions.net/post/accessdiagnosis', data=data)
    # Extract data from the response
    if response.status_code == 200:
        user_data = response.json()
        result = {
            "result":{
            "userID":userid,
            "clinic":user_data["result"]
            }
        
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
    flag = flagForRecords

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

    
