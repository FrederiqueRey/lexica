"""
Python module containing the data models of the data exchanged by the application.
"""

from multiprocessing.sharedctypes import Array
from typing import Optional, List
from pydantic import BaseModel, EmailStr, Field
from bson.objectid import ObjectId




class word(BaseModel):
    d: str = Field(...)
    m: List[str] = Field(...)
    g: List[str] = Field(...)
    l: List[str] = Field(...)
    


    class Config:
        schema_extra = {            
            "example": {
                "d":"<b>ἀαδής</b>, <i>ές</i>, (for <i>ἀ-ϝαδής</i>) unpleasant, cj. for <i>ἀδαής</i> in Thgn.296.",
                "m":["ἀαδής"],
                "g":["ἀαδης","ἀαδησ","ααδης","ααδησ"],
                "l":["aades"]}
            }
        


# class UpdatewordModel(BaseModel):
#     title: Optional[str]
#     manuscript: Optional[str]
#     text: Optional[str]
   
#     class Config:
#         schema_extra = {
#             "example": {
#                 "title": "Ben Sira",
#                 "manuscript": "MS A",
#                 "text": "מכבד אמו ואביו",
#             }
#         }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}