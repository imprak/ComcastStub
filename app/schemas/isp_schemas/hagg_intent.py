from typing import List, Optional

from pydantic import BaseModel, Field, UUID4

"""
ex:
req = {
  "haggIntentName": "9 digit ISP name",
  "refSiteIntentName": "9 digit ISP Name",
  "refSiteIntentId": "554aab05-dd7f-44ec-be0c-749eb083505c",
  "maggConnections": {
    "ethernetInterfaces": [
      {
        "localInterface": "string",
        "remoteInterface": "string"
      }
    ]
  }
}

res = {
  "haggIntentId": "554aab05-dd7f-44ec-be0c-749eb083505c",
  "haggIntentName": "9 digit ISP name",
  "refSiteIntentName": "9 digit ISP Name",
  "refSiteIntentId": "554aab05-dd7f-44ec-be0c-749eb083505c",
  "maggConnections": {
    "ethernetInterfaces": [
      {
        "localInterface": "string",
        "remoteInterface": "string"
      }
    ]
  }
}
"""


class EthernetInterfaces(BaseModel):
    localInterface: str
    remoteInterface: str


class MaggConnections(BaseModel):
    ethernetInterfaces: List[EthernetInterfaces]


class HaggIntentBase(BaseModel):
    haggIntentName: str
    refSiteIntentName: str
    refSiteIntentId: UUID4 = Field(examples=["554aab05-dd7f-44ec-be0c-749eb083505c"])
    maggConnections: Optional[MaggConnections] = Field(None)


class HaggIntentCreate(HaggIntentBase):
    pass


class HaggIntentUpdate(HaggIntentBase):
    pass


class HaggIntentinDb(HaggIntentBase):
    haggIntentId: UUID4 | str = Field(examples=["554aab05-dd7f-44ec-be0c-749eb083505c"])
