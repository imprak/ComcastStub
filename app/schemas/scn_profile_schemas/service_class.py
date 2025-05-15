from pydantic import BaseModel, Field, UUID4


"""
ex:
req = {
  "serviceClassName": "East"
}

res = {
  "serviceClassId": "554aab05-dd7f-44ec-be0c-749eb083505c",
  "serviceClassName": "East"
}
"""


class ServiceClassBase(BaseModel):
    serviceClassName: str


class ServiceClassCreate(ServiceClassBase):
    pass


class ServiceClassUpdate(ServiceClassBase):
    pass


class ServiceClassInDb(ServiceClassBase):
    serviceClassId: UUID4 | str = Field(
        examples=["554aab05-dd7f-44ec-be0c-749eb083505c"]
    )
