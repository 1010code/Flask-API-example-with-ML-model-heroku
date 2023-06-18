from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
import requests
app = FastAPI()

# Global variables
flagForSymptoms: Optional[int] = 0
flagForBasicInfo: Optional[int] = 0
flagForRecords: Optional[int] = 0


class FlagModel(BaseModel):
    flagForSymptoms: int
    flagForBasicInfo: int
    flagForRecords: int


@app.post("/changeFlag")
def post_for_change_flag(flag: FlagModel):
    global flagForSymptoms
    global flagForBasicInfo
    global flagForRecords

    flagForSymptoms = flag.flagForSymptoms
    flagForBasicInfo = flag.flagForBasicInfo
    flagForRecords = flag.flagForRecords

    return "OK"


@app.get("/getFlag")
def get_for_flag():
    return jsonable_encoder({
        "flagForSymptoms": flagForSymptoms,
        "flagForBasicInfo": flagForBasicInfo,
        "flagForRecords": flagForRecords,
    })


@app.get("/basicInfo")
def get_for_basic_info():
    userid = "Ace"

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
        "flag": flagForBasicInfo,
        "userID":userid,
        "result": user_data['result']
    }
    return jsonable_encoder(result)

class SymptomsModel(BaseModel):
    userID: str


@app.post("/symptoms")
def post_for_symptoms(symptoms: SymptomsModel):
    return jsonable_encoder({
        "flag": flagForSymptoms,
        "result": {

            "symptom": "我今天頭很痛"
        }
    })


class ClinicModel(BaseModel):
    forClinic: str


@app.post("/forClinic")
def post_for_clinic(clinic: ClinicModel):
    return "OK"


class RecordsModel(BaseModel):
    userID: str


@app.post("/records")
def post_for_records(records: RecordsModel):
    return jsonable_encoder({
        "flag": flagForRecords,
        "result": {
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
    })


class NextStepModel(BaseModel):
    nextStep: str


@app.post("/nextStep")
def post_next_step(next_step: NextStepModel):
    return "OK"


@app.get("/FakeBasicInfo")
def get_for_basic_info():
    return jsonable_encoder({
        "flag": flagForBasicInfo,
        "result": {
            "id": "Ace",
            "familyHistory": "心臟病, 高血壓, 糖尿病",
            "weight": "60",
            "age": "18",
            "height": "180"
        }
    })
