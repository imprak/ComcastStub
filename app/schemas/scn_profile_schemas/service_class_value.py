from typing import Optional

from pydantic import BaseModel, Field, UUID4

"""
ex:
req = {
  "serviceClassValueName": "East",
  "refServiceClassName": "East",
  "refServiceClassId": "554aab05-dd7f-44ec-be0c-749eb083505c",
  "config": {
    "applicationId": 0,
    "direction": "Upstream",
    "maxConcatenatedBurst": 0,
    "maxTrafficBurst": 0,
    "maxTrafficRate": 0,
    "maximumBuffer": 0,
    "minReservedPacket": 0,
    "multiplierBytesRequested": 0,
    "multiplierContentionRequestWindow": 0,
    "peakTrafficRate": 0,
    "priority": 0,
    "tosAndMask": "",
    "tosOrMask": "",
    "yangExt": {
      "ccapHarmonic": {
        "isDefaultMinReservedPacket": true
      }
    }
  }
}

res = {
  "serviceClassValueId": "554aab05-dd7f-44ec-be0c-749eb083505c",
  "serviceClassValueName": "East",
  "refServiceClassName": "East",
  "refServiceClassId": "554aab05-dd7f-44ec-be0c-749eb083505c",
  "config": {
    "applicationId": 0,
    "direction": "Upstream",
    "maxConcatenatedBurst": 0,
    "maxTrafficBurst": 0,
    "maxTrafficRate": 0,
    "maximumBuffer": 0,
    "minReservedPacket": 0,
    "multiplierBytesRequested": 0,
    "multiplierContentionRequestWindow": 0,
    "peakTrafficRate": 0,
    "priority": 0,
    "tosAndMask": "",
    "tosOrMask": "",
    "yangExt": {
      "ccapHarmonic": {
        "isDefaultMinReservedPacket": true
      }
    }
  }
}
"""


class CcapHarmonic(BaseModel):
    isDefaultMinReservedPacket: bool


class YangExt(BaseModel):
    ccapHarmonic: CcapHarmonic


class Config(BaseModel):
    applicationId: int
    direction: str
    maxConcatenatedBurst: int
    maxTrafficBurst: int
    maxTrafficRate: float
    maximumBuffer: int
    minReservedPacket: int
    multiplierBytesRequested: int
    multiplierContentionRequestWindow: int
    peakTrafficRate: float
    priority: int
    tosAndMask: str
    tosOrMask: str
    yangExt: YangExt


class ServiceClassValueBase(BaseModel):
    serviceClassValueName: str
    refServiceClassName: str
    refServiceClassId: UUID4 = Field(examples=["554aab05-dd7f-44ec-be0c-749eb083505c"])
    config: Optional[Config] = Field(None)


class ServiceClassValueCreate(ServiceClassValueBase):
    pass


class ServiceClassValueUpdate(ServiceClassValueBase):
    pass


class ServiceClassValueInDb(ServiceClassValueBase):
    serviceClassValueId: UUID4 | str = Field(
        examples=["554aab05-dd7f-44ec-be0c-749eb083505c"]
    )
