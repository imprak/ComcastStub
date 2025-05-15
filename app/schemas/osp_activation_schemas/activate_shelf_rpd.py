from typing import Optional

from pydantic import BaseModel, UUID4, Field

"""
ex:
req = {
  "activateShelfRpdName": "10 digit OSP name",
  "refRemotePhyIntentId": "554aab05-dd7f-44ec-be0c-749eb083505c",
  "refRemotePhyIntentName": "10 digit OSP name",
  "identification": {
    "macAddress": "foo",
    "make": "foo",
    "model": "foo",
    "serialNumber": "foo"
  },
  "rfsShelf": {
    "rfsName": "MDCHD00100",
    "row": "0",
    "rack": "0",
    "rackUnit": "0",
    "floor": "0"
  },
  "location": {
    "gpsLatitude": "foo",
    "gpsLongitude": "foo"
  }
}

res = {
  "activateShelfRpdId": "554aab05-dd7f-44ec-be0c-749eb083505c",
  "activateShelfRpdName": "10 digit OSP name",
  "refRemotePhyIntentId": "554aab05-dd7f-44ec-be0c-749eb083505c",
  "refRemotePhyIntentName": "10 digit OSP name",
  "identification": {
    "macAddress": "foo",
    "make": "foo",
    "model": "foo",
    "serialNumber": "foo"
  },
  "rfsShelf": {
    "rfsName": "MDCHD00100",
    "row": "0",
    "rack": "0",
    "rackUnit": "0",
    "floor": "0"
  },
  "location": {
    "gpsLatitude": "foo",
    "gpsLongitude": "foo"
  }
}

doubts:
    in swagger in request payload all fields are optional &
    in response payload identification, location fields are optional 
    which does not make sense to me
    for now making identification, location fields optional for both
"""


class Identification(BaseModel):
    macAddress: str
    make: str
    model: str
    serialNumber: str


class RfsShelf(BaseModel):
    rfsName: str
    row: str
    rack: str
    rackUnit: str
    floor: str


class Location(BaseModel):
    gpsLatitude: str
    gpsLongitude: str


class ActivateShelfRpdBase(BaseModel):
    activateShelfRpdName: str
    refRemotePhyIntentId: UUID4 = Field(
        examples=["554aab05-dd7f-44ec-be0c-749eb083505c"]
    )
    refRemotePhyIntentName: str
    identification: Optional[Identification] = Field(None)
    rfsShelf: RfsShelf = Field(None)
    location: Location = Field(None)


class ActivateShelfRpdCreate(ActivateShelfRpdBase):
    pass


class ActivateShelfRpdUpdate(ActivateShelfRpdBase):
    pass


class ActivateShelfRpdInDb(ActivateShelfRpdBase):
    activateShelfRpdId: UUID4 | str = Field(
        examples=["554aab05-dd7f-44ec-be0c-749eb083505c"]
    )
