from uuid import UUID
from typing import List
from pydantic import BaseModel,Field

class SetParameterAssembly(BaseModel):
    param_id: str = Field(alias='param-id')
    values: List[str] = []

class ByComponenAssembly(BaseModel):
    uuid: str | UUID
    component_uuid: str | UUID = Field(alias='component-uuid')
    description: str

class StatementAssembly(BaseModel):
    uuid: str | UUID
    statement_id: str = Field(alias='statement-id')
    by_components: List[ByComponenAssembly] = Field(default=None, alias='by-components')

class ControlAssembly(BaseModel):
    uuid: str | UUID
    control_id: str = Field(alias='control-id')
    set_parameters: List[SetParameterAssembly] = Field(default=None, alias='set-parameters')
    statements: List[StatementAssembly] | None
    by_components: List[ByComponenAssembly] = Field(default=None, alias='by-components')