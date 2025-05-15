from typing import List, Optional

from pydantic import BaseModel, Field, UUID4

"""
ex:
req = {
  "siteIntentName": "9 digit ISP name",
  "refHubName": "GAL1",
  "refHubId": "554aab05-dd7f-44ec-be0c-749eb083505c",
  "csvIpOob": "10.10.10.10",
  "ipAllocation": {
    "comcastRoutable": {
      "ipv4": [
        "10.10.10.10"
      ],
      "ipv6": [
        "10.10.10.10.10.10"
      ]
    },
    "partnerInternal": {
      "ipv4": [
        "10.10.10.10"
      ],
      "ipv6": [
        "10.10.10.10.10.10"
      ]
    },
    "internetRouted": {
      "ipv4": [
        "10.10.10.10"
      ],
      "ipv6": [
        "10.10.10.10.10.10"
      ]
    }
  }
}

res = {
  "siteIntentId": "554aab05-dd7f-44ec-be0c-749eb083505c",
  "siteIntentName": "9 digit ISP name",
  "refHubName": "GAL1",
  "refHubId": "554aab05-dd7f-44ec-be0c-749eb083505c",
  "csvIpOob": "10.10.10.10",
  "ipAllocation": {
    "comcastRoutable": {
      "ipv4": [
        "10.10.10.10"
      ],
      "ipv6": [
        "10.10.10.10.10.10"
      ]
    },
    "partnerInternal": {
      "ipv4": [
        "10.10.10.10"
      ],
      "ipv6": [
        "10.10.10.10.10.10"
      ]
    },
    "internetRouted": {
      "ipv4": [
        "10.10.10.10"
      ],
      "ipv6": [
        "10.10.10.10.10.10"
      ]
    }
  }
}
"""


class Ip(BaseModel):
    ipv4: List[str]
    ipv6: List[str]


class IpAllocation(BaseModel):
    comcastRoutable: Ip
    partnerInternal: Ip
    internetRouted: Ip


class SiteIntentBase(BaseModel):
    siteIntentName: str
    refHubName: str
    refCpodIntentNames: UUID4 = Field(examples=["554aab05-dd7f-44ec-be0c-749eb083505c"])
    csvIpOob: Optional[str] = Field(None)
    ipAllocation: Optional[IpAllocation] = Field(None)


class SiteIntentCreate(SiteIntentBase):
    pass


class SiteIntentUpdate(SiteIntentBase):
    pass


class SiteIntentInDb(SiteIntentBase):
    siteIntentId: UUID4 | str = Field(examples=["554aab05-dd7f-44ec-be0c-749eb083505c"])
