from typing import List, Optional

from pydantic import BaseModel, Field, UUID4

"""
ex:
req = {
  "scnProfileName": "Partner East",
  "version": "",
  "serviceClassValues": [
    {
      "refServiceClassValueId": "East",
      "refServiceClassValueName": "Partner East"
    }
  ],
  "serviceClassQosValues": [
    {
      "refServiceClassQosId": "East",
      "refServiceClassQosName": "Partner East"
    }
  ]
}

res = {
  "scnProfileId": "554aab05-dd7f-44ec-be0c-749eb083505c",
  "scnProfileName": "Partner East",
  "version": "",
  "serviceClassValues": [
    {
      "refServiceClassValueId": "East",
      "refServiceClassValueName": "Partner East"
    }
  ],
  "serviceClassQosValues": [
    {
      "refServiceClassQosId": "East",
      "refServiceClassQosName": "Partner East"
    }
  ]
}
"""


class ServiceClassValues(BaseModel):
    refServiceClassValueId: str
    refServiceClassValueName: str


class ServiceClassQosValues(BaseModel):
    refServiceClassQosId: str
    refServiceClassQosName: str


class ScnProfileBase(BaseModel):
    scnProfileName: str
    version: Optional[str] = Field(None)
    serviceClassValues: List[ServiceClassValues]
    serviceClassQosValues: Optional[List[ServiceClassQosValues]] = Field(None)


class ScnProfileCreate(ScnProfileBase):
    pass


class ScnProfileUpdate(ScnProfileBase):
    pass


class ScnProfileInDb(ScnProfileBase):
    scnProfileId: UUID4 | str = Field(examples=["554aab05-dd7f-44ec-be0c-749eb083505c"])
