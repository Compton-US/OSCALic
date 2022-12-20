from uuid import UUID
from typing import List
from pydantic import BaseModel,Field

from yaml import safe_load,YAMLError,dump

from .validation import OSCALValidationError
from .by_component import ByComponentAssembly
from .set_parameter import SetParameterAssembly
from .statement import StatementAssembly

class ControlAssembly(BaseModel):
    uuid: str | UUID
    control_id: str = Field(alias='control-id')
    set_parameters: List[SetParameterAssembly] = Field(default=None, alias='set-parameters')
    statements: List[StatementAssembly] | None
    by_components: List[ByComponentAssembly] = Field(default=None, alias='by-components')

    def from_yaml(yaml_content, template):
        control = None

        try:
            loaded_yaml = safe_load(yaml_content)
        except YAMLError as e:
            print(f"YAML ERROR: Could not interpret ({e.problem}).\n")
            raise

        try:
            control = ControlAssembly(**loaded_yaml)
        except OSCALValidationError as e:
            print(f"VALIDATION ERROR: {e.json()}\n")
            raise

        return control


    def to_yaml(model):
        dump(model.dict(by_alias=True,exclude_unset=True), sort_keys=False)