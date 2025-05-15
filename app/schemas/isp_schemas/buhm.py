from pydantic import BaseModel, Field, UUID4


"""
ex:
req = {
  "buhmType": "Hub-Market",
  "buhmName": "Philadelphia",
  "refParentBuhmId": "554aab05-dd7f-44ec-be0c-749eb083505c",
  "refParentBuhmName": "NED"
}

res={
  "buhmId": "554aab05-dd7f-44ec-be0c-749eb083506c",
  "buhmType": "Market, Region, Division",
  "buhmName": "Philadelphia",
  "refParentBuhmId": "554aab05-dd7f-44ec-be0c-749eb083505c",
  "refParentBuhmName": "NED"
}
"""


class BuhmBase(BaseModel):
    buhmType: str
    buhmName: str
    refParentBuhmId: UUID4 = Field(examples=["554aab05-dd7f-44ec-be0c-749eb083505c"])
    refParentBuhmName: str


class BuhmCreate(BuhmBase):
    pass


class BuhmUpdate(BuhmBase):
    pass


class BuhmInDb(BuhmBase):
    buhmId: UUID4 | str = Field(examples=["554aab05-dd7f-44ec-be0c-749eb083505c"])
