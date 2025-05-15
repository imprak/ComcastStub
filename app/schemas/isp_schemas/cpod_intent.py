from typing import List, Optional

from pydantic import BaseModel, Field, UUID4

"""
ex:
req = {
    "cpodIntentName": "9 digit ISP name",
    "refSiteIntentName": "9 digit ISP Name",
    "refSiteIntentId": "554aab05-dd7f-44ec-be0c-749eb083505c",
    "leafUplink": {
        "leafA": {
            "lag": {
                "ipv4": {
                    "local": "10.10.10.10",
                    "remote": "10.10.10.10",
                    "subnet": "10.10.10.10",
                },
                "ipv6": {
                    "local": "10.10.10.10.10.10",
                    "remote": "10.10.10.10.10.10",
                    "subnet": "10.10.10.10.10.10",
                },
            },
            "ethernetInterfaces": [
                {"localInterface": "string", "remoteInterface": "string"}
            ],
            "remoteHost": "",
        },
        "leafB": {
            "lag": {
                "ipv4": {
                    "local": "10.10.10.10",
                    "remote": "10.10.10.10",
                    "subnet": "10.10.10.10",
                },
                "ipv6": {
                    "local": "10.10.10.10.10.10",
                    "remote": "10.10.10.10.10.10",
                    "subnet": "10.10.10.10.10.10",
                },
            },
            "ethernetInterfaces": [
                {"localInterface": "string", "remoteInterface": "string"}
            ],
            "remoteHost": "",
        },
    },
}

res = {
    "cpodIntentId": "554aab05-dd7f-44ec-be0c-749eb083505c",
    "cpodIntentName": "9 digit ISP name",
    "refSiteIntentName": "9 digit ISP Name",
    "refSiteIntentId": "554aab05-dd7f-44ec-be0c-749eb083505c",
    "leafUplink": {
        "leafA": {
            "lag": {
                "ipv4": {
                    "local": "10.10.10.10",
                    "remote": "10.10.10.10",
                    "subnet": "10.10.10.10",
                },
                "ipv6": {
                    "local": "10.10.10.10.10.10",
                    "remote": "10.10.10.10.10.10",
                    "subnet": "10.10.10.10.10.10",
                },
            },
            "ethernetInterfaces": [
                {"localInterface": "string", "remoteInterface": "string"}
            ],
            "remoteHost": "",
        },
        "leafB": {
            "lag": {
                "ipv4": {
                    "local": "10.10.10.10",
                    "remote": "10.10.10.10",
                    "subnet": "10.10.10.10",
                },
                "ipv6": {
                    "local": "10.10.10.10.10.10",
                    "remote": "10.10.10.10.10.10",
                    "subnet": "10.10.10.10.10.10",
                },
            },
            "ethernetInterfaces": [
                {"localInterface": "string", "remoteInterface": "string"}
            ],
            "remoteHost": "",
        },
    },
}
"""


class EthernetInterfaces(BaseModel):
    localInterface: str
    remoteInterface: str


class IpvInfo(BaseModel):
    local: str
    remote: str
    subnet: str


class Lag(BaseModel):
    ipv4: IpvInfo
    ipv6: IpvInfo


class Leaf(BaseModel):
    lag: Lag
    ethernetInterfaces: List[EthernetInterfaces]
    remoteHost: str


class LeafUplink(BaseModel):
    leafA: Leaf
    leafB: Leaf


class CpodIntentBase(BaseModel):
    cpodIntentName: str
    refSiteIntentName: str
    siteIntentId: UUID4 = Field(examples=["554aab05-dd7f-44ec-be0c-749eb083505c"])
    leafUplink: Optional[LeafUplink] = Field(None)


class CpodIntentCreate(CpodIntentBase):
    pass


class CpodIntentUpdate(CpodIntentBase):
    pass


class CpodIntentInDb(CpodIntentBase):
    cpodIntentId: UUID4 | str = Field(examples=["554aab05-dd7f-44ec-be0c-749eb083505c"])
