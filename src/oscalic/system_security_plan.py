from uuid import UUID
from typing import List
from pydantic import BaseModel
from assemblies import ControlAssembly

class SystemSecurityPlanModel(BaseModel):
    uuid: str | UUID
    controls: List[ControlAssembly] | None