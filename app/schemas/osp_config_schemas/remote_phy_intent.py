from typing import Optional, List

from pydantic import BaseModel, UUID4, Field

"""
ex:
req = {
  "remotePhyIntentName": "10 digit OSP name",
  "refDaasIntentId": "554aab05-dd7f-44ec-be0c-749eb083505c",
  "refDaasIntentName": "9 digit ISP name",
  "metaData": {
    "planId": "foo",
    "preferredExecutionDate": "0",
    "deploymentType": "foo",
    "rpdSegmentationType": "foo"
  },
  "rfsShelf": {
    "rfsName": "MDCHD00100",
    "port": 0
  },
  "location": {
    "gpsLatitude": "",
    "gpsLongitude": ""
  },
  "nodeSegmentList": [
    {
      "nodesegName": "10 digit OSP name",
      "usPort": 0
    }
  ],
  "refSpectrumRecommendationId": "554aab05-dd7f-44ec-be0c-749eb083505c",
  "refVideoConfigId": "554aab05-dd7f-44ec-be0c-749eb083505c"
}

res = {
  "remotePhyIntentId": "554aab05-dd7f-44ec-be0c-749eb083505c",
  "remotePhyIntentName": "10 digit OSP name",
  "refDaasIntentId": "554aab05-dd7f-44ec-be0c-749eb083505c",
  "refDaasIntentName": "10 digit OSP name",
  "metaData": {
    "planId": "foo",
    "preferredExecutionDate": "0",
    "deploymentType": "foo",
    "rpdSegmentationType": "foo"
  },
  "rfsShelf": {
    "rfsName": "MDCHD00100",
    "port": 0
  },
  "location": {
    "gpsLatitude": "",
    "gpsLongitude": ""
  },
  "nodeSegmentList": [
    {
      "nodesegName": "10 digit OSP name",
      "usPort": 0
    }
  ],
  "refSpectrumRecommendationId": "554aab05-dd7f-44ec-be0c-749eb083505c",
  "refVideoConfigId": "554aab05-dd7f-44ec-be0c-749eb083505c"
}

doubts: 
    in swagger, refDaasIntentName is 9 digit in req & 10 digit 
    in res, how so?
"""


class Metadata(BaseModel):
    planId: str
    preferredExecutionDate: str
    deploymentType: str
    rpdSegmentationType: str


class RfsShelf(BaseModel):
    rfsName: str
    port: int


class Location(BaseModel):
    gpsLatitude: str
    gpsLongitude: str


class NodeSegmentList(BaseModel):
    nodesegName: str
    usPort: int


class RemotePhyIntentBase(BaseModel):
    remotePhyIntentName: str
    refDaasIntentId: UUID4 = Field(examples=["554aab05-dd7f-44ec-be0c-749eb083505c"])
    refDaasIntentName: str
    metaData: Optional[Metadata] = Field(None)
    rfsShelf: Optional[RfsShelf] = Field(None)
    location: Optional[Location] = Field(None)
    nodeSegmentList: Optional[List[NodeSegmentList]] = Field(None)
    refSpectrumRecommendationId: Optional[UUID4] = Field(
        None, examples=["554aab05-dd7f-44ec-be0c-749eb083505c"]
    )
    refVideoConfigId: Optional[UUID4] = Field(
        None, examples=["554aab05-dd7f-44ec-be0c-749eb083505c"]
    )


class RemotePhyIntentCreate(RemotePhyIntentBase):
    pass


class RemotePhyIntentUpdate(RemotePhyIntentBase):
    pass


class RemotePhyIntentInDb(RemotePhyIntentBase):
    remotePhyIntentId: UUID4 | str = Field(
        examples=["554aab05-dd7f-44ec-be0c-749eb083505c"]
    )
