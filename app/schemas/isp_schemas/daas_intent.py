from typing import List, Optional

from pydantic import BaseModel, Field, UUID4

"""
ex:
req = {
  "daasIntentName": "9 digit ISP name",
  "refPpodIntentName": "9 digit ISP name",
  "refPpodIntentId": "554aab05-dd7f-44ec-be0c-749eb083505c",
  "haggConnections": {
    "ethernetInterfaces": [
      {
        "localInterface": "string",
        "remoteInterface": "string"
      }
    ]
  }
}

res = {
  "daasIntentId": "554aab05-dd7f-44ec-be0c-749eb083505c",
  "daasIntentName": "9 digit ISP name",
  "refPpodIntentName": "9 digit ISP name",
  "refPpodIntentId": "554aab05-dd7f-44ec-be0c-749eb083505c",
  "haggConnections": {
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


class HaggConnections(BaseModel):
    ethernetInterfaces: List[EthernetInterfaces]


class DaasIntentBase(BaseModel):
    daasIntentName: str
    refPpodIntentName: str
    refPpodIntentId: UUID4 = Field(examples=["554aab05-dd7f-44ec-be0c-749eb083505c"])
    haggConnections: Optional[HaggConnections] = Field(None)


class DaasIntentCreate(DaasIntentBase):
    pass


class DaasIntentUpdate(DaasIntentBase):
    pass


class DaasIntentInDb(DaasIntentBase):
    daasIntentId: UUID4 | str = Field(examples=["554aab05-dd7f-44ec-be0c-749eb083505c"])
