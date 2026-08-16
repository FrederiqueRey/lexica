"""
Python module containing the data models of the data exchanged by the application.
"""

from typing import List
from pydantic import BaseModel, Field


class word(BaseModel):
    dic: str = Field(...)
    sort_key: int = Field(...)
    lang: str = Field(...)
    d: str = Field(...)
    m: List[str] = Field(...)
    b: List[str] = Field(...)
    l: List[str] = Field(...)
    


    class Config:
        schema_extra = {            
            "example": {
                "dic": "LSJ",
                "sort_key": 80329,
                "lang": "Greek",
                "m": ["παράδεισος"],
                "b": ["παραδεισος", "παραδεισοσ", "παραδειςος", "παραδειςοσ"],
                "l": ["paradeisos"],
                "d": "The Paradise"
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}