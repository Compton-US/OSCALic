from uuid import UUID
from pydantic import BaseModel,Field

class ByComponentAssembly(BaseModel):
    uuid: str | UUID
    component_uuid: str | UUID = Field(alias='component-uuid')
    description: str
