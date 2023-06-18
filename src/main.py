from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

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


@app.get("/basicInfo")
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
