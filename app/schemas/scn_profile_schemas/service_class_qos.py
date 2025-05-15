from typing import Optional

from pydantic import BaseModel, Field, UUID4


"""
ex:
req = {
  "serviceClassQosName": "East",
  "refServiceClassName": "East",
  "refServiceClassId": "554aab05-dd7f-44ec-be0c-749eb083505c",
  "config": {
    "aqmCouplingFactor": 0,
    "asfDirection": "upstream",
    "asfPriority": 0,
    "classicSfScn": "",
    "dataRateUnitSetting": 0,
    "latencySfScn": "",
    "lowLatencyAsf": "",
    "maxAggregateTrafficRate": 0,
    "maxTrafficBurst": 0,
    "minReservedPacket": 0,
    "minReservedRate": 0,
    "peakTrafficRate": 0,
    "qpEnable": "",
    "qpDrainRateExponent": 0,
    "qpLatencyThreshold": 0,
    "qpQueuingScoreThreshold": 0,
    "schedulingWeight": 0
  }
}

res = {
  "serviceClassQosId": "554aab05-dd7f-44ec-be0c-749eb083505c",
  "serviceClassQosName": "East",
  "refServiceClassName": "East",
  "refServiceClassId": "554aab05-dd7f-44ec-be0c-749eb083505c",
  "config": {
    "aqmCouplingFactor": 0,
    "asfDirection": "upstream",
    "asfPriority": 0,
    "classicSfScn": "",
    "dataRateUnitSetting": 0,
    "latencySfScn": "",
    "lowLatencyAsf": "",
    "maxAggregateTrafficRate": 0,
    "maxTrafficBurst": 0,
    "minReservedPacket": 0,
    "minReservedRate": 0,
    "peakTrafficRate": 0,
    "qpEnable": "",
    "qpDrainRateExponent": 0,
    "qpLatencyThreshold": 0,
    "qpQueuingScoreThreshold": 0,
    "schedulingWeight": 0
  }
}
"""


class Config(BaseModel):
    aqmCouplingFactor: float
    asfDirection: str
    asfPriority: int
    classicSfScn: str
    dataRateUnitSetting: int
    latencySfScn: str
    lowLatencyAsf: str
    maxAggregateTrafficRate: float
    maxTrafficBurst: int
    minReservedPacket: int
    minReservedRate: float
    peakTrafficRate: float
    qpEnable: str
    qpDrainRateExponent: int
    qpLatencyThreshold: float
    qpQueuingScoreThreshold: float
    schedulingWeight: float


class ServiceClassQosBase(BaseModel):
    serviceClassQosName: str
    refServiceClassName: str
    refServiceClassId: UUID4 = Field(examples=["554aab05-dd7f-44ec-be0c-749eb083505c"])
    config: Optional[Config] = Field(None)


class ServiceClassQosCreate(ServiceClassQosBase):
    pass


class ServiceClassQosUpdate(ServiceClassQosBase):
    pass


class ServiceClassQosInDb(ServiceClassQosBase):
    serviceClassQosId: UUID4 | str = Field(
        examples=["554aab05-dd7f-44ec-be0c-749eb083505c"]
    )
