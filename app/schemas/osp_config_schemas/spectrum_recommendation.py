from typing import List

from pydantic import BaseModel, Field, UUID4

"""
ex:
req = {
  "recommendationHash": "",
  "config": {
    "video": [
      {
        "startFreq": 0,
        "endFreq": 0
      }
    ],
    "docsis": {
      "scqamUs": [
        {
          "startFreq": 0,
          "endFreq": 0
        }
      ],
      "scqamDs": [
        {
          "startFreq": 0,
          "endFreq": 0
        }
      ],
      "ofdma": {
        "startFreq": 0,
        "endFreq": 0,
        "exclusionZones": [
          {
            "startFreq": 0,
            "endFreq": 0
          }
        ],
        "initialRangingFreq": 0,
        "fineRangingFreq": 0
      },
      "ofdm": {
        "startFreq": "",
        "endFreq": 0,
        "exclusionZones": [
          {
            "startFreq": 0,
            "endFreq": 0
          }
        ],
        "exclusionNotes": [
          {
            "startFreq": 0,
            "type": ""
          }
        ],
        "plc": 0
      },
      "fdxResource": {
        "allocatedSpectrum": 0,
        "fdxOfdma": {
          "startFreq": 0,
          "endFreq": 0,
          "exclusionZones": [
            {
              "startFreq": 0,
              "endFreq": 0
            }
          ],
          "initialRangingFreq": 0,
          "fineRangingFreq": 0
        },
        "fdxOfdm": {
          "startFreq": 0,
          "endFreq": 0,
          "exclusionZones": [
            {
              "startFreq": 0,
              "endFreq": 0
            }
          ],
          "exclusionNotes": [
            {
              "startFreq": 0,
              "type": ""
            }
          ],
          "plc": 0
        }
      }
    },
    "rfModulated": [
      {
        "startFreq": 0,
        "endFreq": 0
      }
    ],
    "capability": {
      "speed": [
        {
          "docsisVersion": "",
          "fdxBondingCapability": "",
          "maxSpeedUS": 0,
          "maxSpeedDS": 0
        }
      ]
    }
  }
}

res = {
  "spectrumRecommendationId": "554aab05-dd7f-44ec-be0c-749eb083505c",
  "recommendationHash": "",
  "config": {
    "video": [
      {
        "startFreq": 0,
        "endFreq": 0
      }
    ],
    "docsis": {
      "scqamUs": [
        {
          "startFreq": 0,
          "endFreq": 0
        }
      ],
      "scqamDs": [
        {
          "startFreq": 0,
          "endFreq": 0
        }
      ],
      "ofdma": {
        "startFreq": 0,
        "endFreq": 0,
        "exclusionZones": [
          {
            "startFreq": 0,
            "endFreq": 0
          }
        ],
        "initialRangingFreq": 0,
        "fineRangingFreq": 0
      },
      "ofdm": {
        "startFreq": "",
        "endFreq": 0,
        "exclusionZones": [
          {
            "startFreq": 0,
            "endFreq": 0
          }
        ],
        "exclusionNotes": [
          {
            "startFreq": 0,
            "type": ""
          }
        ],
        "plc": 0
      },
      "fdxResource": {
        "allocatedSpectrum": 0,
        "fdxOfdma": {
          "startFreq": 0,
          "endFreq": 0,
          "exclusionZones": [
            {
              "startFreq": 0,
              "endFreq": 0
            }
          ],
          "initialRangingFreq": 0,
          "fineRangingFreq": 0
        },
        "fdxOfdm": {
          "startFreq": 0,
          "endFreq": 0,
          "exclusionZones": [
            {
              "startFreq": 0,
              "endFreq": 0
            }
          ],
          "exclusionNotes": [
            {
              "startFreq": 0,
              "type": ""
            }
          ],
          "plc": 0
        }
      }
    },
    "rfModulated": [
      {
        "startFreq": 0,
        "endFreq": 0
      }
    ],
    "capability": {
      "speed": [
        {
          "docsisVersion": "",
          "fdxBondingCapability": "",
          "maxSpeedUS": 0,
          "maxSpeedDS": 0
        }
      ]
    }
  }
}

doubts:
    in swagger, all fields are optional, which does not make sense
    for now implementing all mandatory.
    in swagger, type of startFreq field under config-docsis-ofdm 
    is string, whereas int at other places, so considering int
"""


class ExclusionNotes(BaseModel):
    startFreq: float
    type: str


class FrequencyRange(BaseModel):
    startFreq: float
    endFreq: float


class Ofdma(FrequencyRange):
    exclusionZones: List[FrequencyRange]
    initialRangingFreq: float
    fineRangingFreq: float


class Ofdm(FrequencyRange):
    exclusionZones: List[FrequencyRange]
    exclusionNotes: List[ExclusionNotes]
    plc: int


class FdxResource(BaseModel):
    allocatedSpectrum: int
    fdxOfdma: Ofdma
    fdxOfdm: Ofdm


class Docsis(BaseModel):
    scqamUs: List[FrequencyRange]
    scqamDs: List[FrequencyRange]
    ofdma: Ofdma
    ofdm: Ofdm
    fdxResource: FdxResource


class Speed(BaseModel):
    docsisVersion: str
    fdxBondingCapability: str
    maxSpeedUS: int
    maxSpeedDS: int


class Capability(BaseModel):
    speed: List[Speed]


class Config(BaseModel):
    video: List[FrequencyRange]
    docsis: Docsis
    rfModulated: List[FrequencyRange]
    capability: Capability


class SpectrumRecommendationBase(BaseModel):
    recommendationHash: str
    config: Config


class SpectrumRecommendationCreate(SpectrumRecommendationBase):
    pass


class SpectrumRecommendationUpdate(SpectrumRecommendationBase):
    pass


class SpectrumRecommendationInDb(SpectrumRecommendationBase):
    spectrumRecommendationId: UUID4 | str = Field(
        examples=["554aab05-dd7f-44ec-be0c-749eb083505c"]
    )
