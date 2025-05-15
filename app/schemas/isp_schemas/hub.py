from pydantic import BaseModel, UUID4, Field
from typing import Optional

"""
ex:
req = {
  "hubName": "GAL1",
  "hubType": "Primary",
  "refParentHubName": "GAL2",
  "refParentHubId": "554aab05-dd7f-44ec-be0c-749eb083505c",
  "refBuhmId": "554aab05-dd7f-44ec-be0c-749eb083505c",
  "refBuhmName": "Philadelphia",
  "postalAddress": {
    "addr1": "375 Rockbridge Rd NW",
    "addr2": "Unit 2",
    "administrativeArea": "PA",
    "country": "US",
    "postalCode": ""
  },
  "timezone": "GMT"
}

res = {
  "hubId": "554aab05-dd7f-44ec-be0c-749eb083505c",
  "hubName": "GAL1",
  "hubType": "Primary",
  "parentHubName": "GAL2",
  "refBuhmId": "554aab05-dd7f-44ec-be0c-749eb083505c",
  "refBuhmName": "Philadelphia",
  "postalAddress": {
    "addr1": "375 Rockbridge Rd NW",
    "addr2": "Unit 2",
    "administrativeArea": "PA",
    "country": "US",
    "postalCode": ""
  },
  "timezone": "GMT"
}

doubts:
    in swagger PUT endpoint request & response schema 
    seems to be incorrect & duplicated from buhm api.
    implementing POST endpoint schema for both POST & PUT endpoint.
"""


class PostalAddress(BaseModel):
    addr1: str
    addr2: str
    administrativeArea: str
    country: str
    postalCode: str


class HubBase(BaseModel):
    hubName: str
    hubType: str
    refBuhmId: UUID4 = Field(examples=["554aab05-dd7f-44ec-be0c-749eb083505c"])
    refBuhmName: str
    postalAddress: Optional[PostalAddress] = Field(None)
    timezone: Optional[str] = Field(None)


class HubCreate(HubBase):
    refParentHubName: str
    refParentHubId: str


class HubUpdate(HubBase):
    refParentHubName: str
    refParentHubId: str


class HubInDb(HubBase):
    hubId: UUID4 | str = Field(examples=["554aab05-dd7f-44ec-be0c-749eb083505c"])
    parentHubName: str
