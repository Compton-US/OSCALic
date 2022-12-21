from uuid import UUID
from typing import List
from pydantic import BaseModel,Field

from yaml import safe_load,YAMLError,dump

from .validation import Validation
from .by_component import ByComponentAssembly
from .set_parameter import SetParameterAssembly
from .statement import StatementAssembly

class ControlAssembly(BaseModel):
    uuid: str | UUID
    control_id: str = Field(alias='control-id')
    set_parameters: List[SetParameterAssembly] = Field(default=None, alias='set-parameters')
    statements: List[StatementAssembly] | None
    by_components: List[ByComponentAssembly] = Field(default=None, alias='by-components')
