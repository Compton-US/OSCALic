from uuid import UUID
from typing import List,Field
from pydantic import BaseModel
from .assemblies import ByComponentAssembly

class StatementAssembly(BaseModel):
    uuid: str | UUID
    statement_id: str = Field(alias='statement-id')
    by_components: List[ByComponentAssembly] = Field(default=None, alias='by-components')
