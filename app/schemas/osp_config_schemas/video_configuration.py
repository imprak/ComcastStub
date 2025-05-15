from typing import List

from pydantic import BaseModel, Field, UUID4

"""
ex:
req = {
  "videoConfigHash": "",
  "serviceAffecting": false,
  "comment": "Why was the video config publish",
  "userId": "Video config was published by",
  "oob552": {
    "auxCore552": ""
  },
  "broadcast": [
    {
      "channel": 1,
      "channelType": "",
      "groupIP": "",
      "powerAdjust": 0,
      "sessionId": ""
    }
  ],
  "dsgTunnels": {
    "ca": {
      "group": "",
      "SourceIP": ""
    },
    "eas": {
      "group": "",
      "SourceIP": ""
    },
    "si": {
      "group": "",
      "SourceIP": ""
    }
  },
  "deploymentType": "",
  "multiUsPortConfigured": 0,
  "om": {
    "frequency": [
      0
    ],
    "groupAddress": "",
    "sessionId": ""
  },
  "rpd": {
    "cfType": "",
    "oob": 0
  },
  "tone": [
    {
      "description": "",
      "frequency": 0,
      "highAccuracy": false,
      "power": 1.23
    }
  ],
  "varpd": {
    "frequency": [
      0
    ],
    "sessionId": "",
    "slot": 0,
    "vardip": ""
  }
}

res = {
  "videoConfigurationId": "554aab05-dd7f-44ec-be0c-749eb083505c",
  "videoConfigHash": "",
  "serviceAffecting": false,
  "comment": "Why was the video config publish",
  "userId": "Video config was published by",
  "oob552": {
    "auxCore552": ""
  },
  "broadcast": [
    {
      "channel": 1,
      "channelType": "",
      "groupIP": "",
      "powerAdjust": 0,
      "sessionId": ""
    }
  ],
  "dsgTunnels": {
    "ca": {
      "group": "",
      "SourceIP": ""
    },
    "eas": {
      "group": "",
      "SourceIP": ""
    },
    "si": {
      "group": "",
      "SourceIP": ""
    }
  },
  "deploymentType": "",
  "multiUsPortConfigured": 0,
  "om": {
    "frequency": [
      0
    ],
    "groupAddress": "",
    "sessionId": ""
  },
  "rpd": {
    "cfType": "",
    "oob": 0
  },
  "tone": [
    {
      "description": "",
      "frequency": 0,
      "highAccuracy": false,
      "power": 1.23
    }
  ],
  "varpd": {
    "frequency": [
      0
    ],
    "sessionId": "",
    "slot": 0,
    "vardip": ""
  }
}

doubts:
    in swagger, all fields are optional in request payload &
    in response payload all fields are optional except 
    videoConfigurationId field, which not make sense to me.
    for now implementing all mandatory in both request & response.
"""


class Oob552(BaseModel):
    auxCore552: str


class Broadcast(BaseModel):
    channel: int
    channelType: str
    groupIP: str
    powerAdjust: int
    sessionId: str


class SimilarForCaEasSi(BaseModel):
    group: str
    SourceIP: str


class DsgTunnels(BaseModel):
    ca: SimilarForCaEasSi
    eas: SimilarForCaEasSi
    si: SimilarForCaEasSi


class Om(BaseModel):
    frequency: List[float]
    groupAddress: str
    sessionId: str


class Rpd(BaseModel):
    cfType: str
    oob: int


class Tone(BaseModel):
    description: str
    frequency: float
    highAccuracy: bool
    power: float


class Varpd(BaseModel):
    frequency: List[float]
    sessionId: str
    slot: int
    vardip: str


class VideoConfigurationBase(BaseModel):
    videoConfigHash: str
    serviceAffecting: bool
    comment: str
    userId: str
    oob552: Oob552
    broadcast: List[Broadcast]
    dsgTunnels: DsgTunnels
    deploymentType: str
    multiUsPortConfigured: int
    om: Om
    rpd: Rpd
    tone: List[Tone]
    varpd: Varpd


class VideoConfigurationCreate(VideoConfigurationBase):
    pass


class VideoConfigurationUpdate(VideoConfigurationBase):
    pass


class VideoConfigurationInDb(VideoConfigurationBase):
    videoConfigurationId: UUID4 | str = Field(
        examples=["554aab05-dd7f-44ec-be0c-749eb083505c"]
    )
