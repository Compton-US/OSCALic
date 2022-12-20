from typing import List,Field
from pydantic import BaseModel

class SetParameterAssembly(BaseModel):
    param_id: str = Field(alias='param-id')
    values: List[str] = []
