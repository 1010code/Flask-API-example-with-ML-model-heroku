from fastapi import FastAPI, Form
from pydantic import BaseModel
from typing import Optional
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
import requests

app = FastAPI()

# Global variables
flagForSymptoms: Optional[bool] = None
flagForBasicInfo: Optional[bool] = None
flagForRecords: Optional[bool] = None


class FlagModel(BaseModel):
    flagForSymptoms: bool
    flagForBasicInfo: bool
    flagForRecords: bool


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


class Result(BaseModel):
    id: str
    familyHistory: str
    weight: str
    age: str
    height: str

class Response(BaseModel):
    result: Result
    flagForBasicInfo: bool

@app.post("/get_basic_info", response_model=Response)
async def get_basic_info(userid: str = Form(...)):
    url = 'https://us-central1-fortesting-c54ba.cloudfunctions.net/post/accessbasic'
    data = {'userid': userid}
    response = requests.post(url, data=data)

    if response.status_code != 200:
        return {"detail": "Failed to fetch data from the database."}

    response_data = response.json()

    # Wrap the response data in a 'result' field and add the 'flagForBasicInfo' field.
    # Here we just set flagForBasicInfo to True for the example, you might want to replace this with actual logic.
    response_data = {"result": response_data, "flagForBasicInfo": True}

    return response_data

class SymptomsModel(BaseModel):
    userID: str


@app.post("/symptoms")
def post_for_symptoms(symptoms: SymptomsModel):
    return jsonable_encoder({
        "flag": "1",
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
        "flag": "1",
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
