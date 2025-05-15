from typing import List, Optional

from pydantic import BaseModel, Field, UUID4

"""
ex:
res = {
  "ppodIntentName": "9 digit ISP Name",
  "refCpodIntentName": "9 digit ISP Name",
  "refCpodIntentId": "554aab05-dd7f-44ec-be0c-749eb083505c",
  "leafUplink": {
    "leafA": {
      "lag": {
        "ipv4": {
          "local": "10.10.10.10",
          "remote": "10.10.10.10",
          "subnet": "10.10.10.10"
        },
        "ipv6": {
          "local": "10.10.10.10.10.10",
          "remote": "10.10.10.10.10.10",
          "subnet": "10.10.10.10.10.10"
        }
      },
      "ethernetInterfaces": [
        {
          "localInterface": "string",
          "remoteInterface": "string"
        }
      ],
      "remoteHost": ""
    },
    "leafB": {
      "lag": {
        "ipv4": {
          "local": "10.10.10.10",
          "remote": "10.10.10.10",
          "subnet": "10.10.10.10"
        },
        "ipv6": {
          "local": "10.10.10.10.10.10",
          "remote": "10.10.10.10.10.10",
          "subnet": "10.10.10.10.10.10"
        }
      },
      "ethernetInterfaces": [
        {
          "localInterface": "string",
          "remoteInterface": "string"
        }
      ],
      "remoteHost": ""
    }
  },
  "dhcpServers": {
    "ipv4": [
      "10.10.10.10"
    ],
    "ipv6": [
      "10.10.10.10.10.10"
    ]
  },
  "vault": {
    "cmSharedSecret": {
      "path": "string",
      "lastUpdated": "string"
    },
    "ripKey": {
      "path": "string",
      "lastUpdated": "string"
    }
  },
  "maggConnections": {
    "ethernetInterfaces": [
      {
        "localInterface": "string",
        "remoteInterface": "string"
      }
    ]
  },
  "custIpScopeConfiguration": {
    "vrfIPScopes": {
      "vrf": [
        {
          "vrfType": "",
          "cm_v4_net": [
            "100.75.170.0/26"
          ],
          "cm_v6_net": [
            "2001:558:40a1::/64"
          ]
        },
        {
          "vrfType": "",
          "cpe_v4_net": [
            "68.35.2.0/23",
            "68.35.30.0/23",
            "21.60.9.0/24",
            "21.60.21.0/24"
          ],
          "cpe_v6_net": [
            "2001:558:6032::/64",
            "2603:27c0:8800::/40"
          ]
        }
      ],
      "anIpscopes": {
        "cm_scope_v4_net": [
          "100.75.170.0/26"
        ],
        "cm_scope_v6_net": [
          "2001:558:40a1:e::/64"
        ],
        "cpe_scope_v4_net": [
          "68.35.2.0/23",
          "68.35.30.0/23"
        ],
        "cpe_scope_v6_net": [
          "2001:558:6032:e::/64"
        ],
        "mta_scope_v4_net": [
          "21.60.9.0/24",
          "21.60.21.0/24",
          "21.60.139.0/24"
        ],
        "mta_scope_v6_net": [
          "2001:558:800a:e::/64"
        ],
        "stb_scope_v6_net": [
          "2603:27c0:8800::/40"
        ],
        "resi_pd_scope_v6_net": [
          "2601:7c0:c800::/40"
        ]
      }
    }
  },
  "refScnProfileId": "554aab05-dd7f-44ec-be0c-749eb083505c",
  "refScnProfileName": "Partner East"
}

res = {
  "ppodIntentId": "554aab05-dd7f-44ec-be0c-749eb083505c",
  "ppodIntentName": "9 digit ISP Name",
  "refCpodIntentName": "9 digit ISP Name",
  "cpodIntentId": "554aab05-dd7f-44ec-be0c-749eb083505c",
  "leafUplink": {
    "leafA": {
      "lag": {
        "ipv4": {
          "local": "10.10.10.10",
          "remote": "10.10.10.10",
          "subnet": "10.10.10.10"
        },
        "ipv6": {
          "local": "10.10.10.10.10.10",
          "remote": "10.10.10.10.10.10",
          "subnet": "10.10.10.10.10.10"
        }
      },
      "ethernetInterfaces": [
        {
          "localInterface": "string",
          "remoteInterface": "string"
        }
      ],
      "remoteHost": ""
    },
    "leafB": {
      "lag": {
        "ipv4": {
          "local": "10.10.10.10",
          "remote": "10.10.10.10",
          "subnet": "10.10.10.10"
        },
        "ipv6": {
          "local": "10.10.10.10.10.10",
          "remote": "10.10.10.10.10.10",
          "subnet": "10.10.10.10.10.10"
        }
      },
      "ethernetInterfaces": [
        {
          "localInterface": "string",
          "remoteInterface": "string"
        }
      ],
      "remoteHost": ""
    }
  },
  "dhcpServers": {
    "ipv4": [
      "10.10.10.10"
    ],
    "ipv6": [
      "10.10.10.10.10.10"
    ]
  },
  "vault": {
    "cmSharedSecret": {
      "path": "string",
      "lastUpdated": "string"
    },
    "ripKey": {
      "path": "string",
      "lastUpdated": "string"
    }
  },
  "maggConnections": {
    "ethernetInterfaces": [
      {
        "localInterface": "string",
        "remoteInterface": "string"
      }
    ]
  },
  "custIpScopeConfiguration": {
    "vrfIPScopes": {
      "vrf": [
        {
          "vrfType": "",
          "cm_v4_net": [
            "100.75.170.0/26"
          ],
          "cm_v6_net": [
            "2001:558:40a1::/64"
          ]
        },
        {
          "vrfType": "",
          "cpe_v4_net": [
            "68.35.2.0/23",
            "68.35.30.0/23",
            "21.60.9.0/24",
            "21.60.21.0/24"
          ],
          "cpe_v6_net": [
            "2001:558:6032::/64",
            "2603:27c0:8800::/40"
          ]
        }
      ],
      "anIpscopes": {
        "cm_scope_v4_net": [
          "100.75.170.0/26"
        ],
        "cm_scope_v6_net": [
          "2001:558:40a1:e::/64"
        ],
        "cpe_scope_v4_net": [
          "68.35.2.0/23",
          "68.35.30.0/23"
        ],
        "cpe_scope_v6_net": [
          "2001:558:6032:e::/64"
        ],
        "mta_scope_v4_net": [
          "21.60.9.0/24",
          "21.60.21.0/24",
          "21.60.139.0/24"
        ],
        "mta_scope_v6_net": [
          "2001:558:800a:e::/64"
        ],
        "stb_scope_v6_net": [
          "2603:27c0:8800::/40"
        ],
        "resi_pd_scope_v6_net": [
          "2601:7c0:c800::/40"
        ]
      }
    }
  },
  "refScnProfileName": "Partner East",
  "refScnProfileId": "554aab05-dd7f-44ec-be0c-749eb083505c"
}
"""


class Ip(BaseModel):
    local: str
    remote: str
    subnet: str


class Lag(BaseModel):
    ipv4: Ip
    ipv6: Ip


class EthernetInterfaces(BaseModel):
    localInterface: str
    remoteInterface: str


class Leaf(BaseModel):
    lag: Lag
    ethernetInterfaces: List[EthernetInterfaces]
    remoteHost: str


class LeafUplink(BaseModel):
    leafA: Leaf
    leafB: Leaf


class DhcpServers(BaseModel):
    ipv4: List[str]
    ipv6: List[str]


class CmSharedSecret(BaseModel):
    path: str
    lastUpdated: str


class RipKey(BaseModel):
    path: str
    lastUpdated: str


class Vault(BaseModel):
    cmSharedSecret: CmSharedSecret
    ripKey: RipKey


class MaggConnections(BaseModel):
    ethernetInterfaces: List[EthernetInterfaces]


class AnIpscopes(BaseModel):
    cm_scope_v4_net: List[str]
    cm_scope_v6_net: List[str]
    cpe_scope_v4_net: List[str]
    cpe_scope_v6_net: List[str]
    mta_scope_v4_net: List[str]
    mta_scope_v6_net: List[str]
    stb_scope_v6_net: List[str]
    resi_pd_scope_v6_net: List[str]


class Vrf(BaseModel):
    vrfType: str = Field(None)
    cpe_v4_net: List[str] = Field(None)
    cpe_v6_net: List[str] = Field(None)
    cm_v4_net: List[str] = Field(None)
    cm_v6_net: List[str] = Field(None)


class VrfIPScopes(BaseModel):
    vrf: List[Vrf]
    anIpscopes: AnIpscopes


class CustIpScopeConfiguration(BaseModel):
    vrfIPScopes: VrfIPScopes


class PpodIntentBase(BaseModel):
    ppodIntentName: str
    refCpodIntentName: str
    leafUplink: Optional[LeafUplink] = Field(None)
    dhcpServers: Optional[DhcpServers] = Field(None)
    vault: Optional[Vault] = Field(None)
    maggConnections: Optional[MaggConnections] = Field(None)
    custIpScopeConfiguration: Optional[CustIpScopeConfiguration] = Field(None)
    refScnProfileId: Optional[UUID4] = Field(
        None, examples=["554aab05-dd7f-44ec-be0c-749eb083505c"]
    )
    refScnProfileName: Optional[str] = Field(None)


class PpodIntentCreate(PpodIntentBase):
    refCpodIntentId: UUID4 = Field(examples=["554aab05-dd7f-44ec-be0c-749eb083505c"])


class PpodIntentUpdate(PpodIntentBase):
    refCpodIntentId: UUID4 = Field(examples=["554aab05-dd7f-44ec-be0c-749eb083505c"])


class PpodIntentInDb(PpodIntentBase):
    cpodIntentId: Optional[UUID4 | str] = Field(
        None, examples=["554aab05-dd7f-44ec-be0c-749eb083505c"]
    )
    ppodIntentId: UUID4 | str = Field(examples=["554aab05-dd7f-44ec-be0c-749eb083505c"])
