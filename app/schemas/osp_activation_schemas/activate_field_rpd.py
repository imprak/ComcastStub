from typing import Optional

from pydantic import BaseModel, UUID4, Field

"""
ex:
req = {
  "activateFieldRpdName": "10 digit OSP name",
  "refRemotePhyIntentId": "554aab05-dd7f-44ec-be0c-749eb083505c",
  "refRemotePhyIntentName": "10 digit OSP name",
  "refDaasIntentId": "554aab05-dd7f-44ec-be0c-749eb083505c",
  "refDaasIntentName": "9 digit ISP name",
  "identification": {
    "make": "",
    "model": "",
    "macAddress": "foo",
    "serialNumber": ""
  },
  "location": {
    "gpsLatitude": "",
    "gpsLongitude": ""
  }
}

res = {
  "activateFieldRpdId": "554aab05-dd7f-44ec-be0c-749eb083505c",
  "activateFieldRpdName": "10 digit OSP name",
  "refRemotePhyIntentId": "554aab05-dd7f-44ec-be0c-749eb083505c",
  "refRemotePhyIntentName": "10 digit OSP name",
  "refDaasIntentId": "554aab05-dd7f-44ec-be0c-749eb083505c",
  "refDaasIntentName": "9 digit ISP name",
  "identification": {
    "make": "",
    "model": "",
    "macAddress": "foo",
    "serialNumber": ""
  },
  "location": {
    "gpsLatitude": "",
    "gpsLongitude": ""
  }
}

doubts:
    in swagger in request payload all fields are optional &
    in response payload identification, location fields are optional 
    which does not make sense to me
    for now making identification, location fields optional for both
"""


class Identification(BaseModel):
    make: str
    model: str
    macAddress: str
    serialNumber: str


class Location(BaseModel):
    gpsLatitude: str
    gpsLongitude: str


class ActivateFieldRpdBase(BaseModel):
    activateFieldRpdName: str
    refRemotePhyIntentId: UUID4 = Field(
        examples=["554aab05-dd7f-44ec-be0c-749eb083505c"]
    )
    refRemotePhyIntentName: str
    refDaasIntentId: UUID4 = Field(examples=["554aab05-dd7f-44ec-be0c-749eb083505c"])
    refDaasIntentName: str
    identification: Optional[Identification] = Field(None)
    location: Optional[Location] = Field(None)


class ActivateFieldRpdCreate(ActivateFieldRpdBase):
    pass


class ActivateFieldRpdUpdate(ActivateFieldRpdBase):
    pass


class ActivateFieldRpdInDb(ActivateFieldRpdBase):
    activateFieldRpdId: UUID4 | str = Field(
        examples=["554aab05-dd7f-44ec-be0c-749eb083505c"]
    )
