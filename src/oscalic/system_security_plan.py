from uuid import UUID
from typing import List
from pydantic import BaseModel
from .control import ControlAssembly

class SystemSecurityPlan(BaseModel):
    uuid: str | UUID
    controls: List[ControlAssembly] | None