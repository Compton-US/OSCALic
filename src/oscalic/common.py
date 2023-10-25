from pydantic import BaseModel, Field, List
from .control import ControlAssembly
from uuid import UUID

class RoleAssembly(BaseModel):
    id: str | None
    title: str | None

class PartyAssembly(BaseModel):
    uuid: str | None
    type: str | None

class MetadataAssembly(BaseModel):
    title: str
    last_modified: str = Field(default=None, alias='last-modified')
    version: str
    oscal_version: str = Field(default=None, alias='oscal-version')
    roles: List[RoleAssembly] | None
    parties: List[PartyAssembly] | None

class ImportProfileAssembly(BaseModel):
    href: str | None

class IdAssembly(BaseModel):
    id: str | None

class StatusAssembly(BaseModel):
    state: str

class ControlImplementationAssembly(BaseModel):
    description: str
    implemented_requirements: List[ControlAssembly] = Field(default=None, alias='implemented-requirements')

class PropsAssembly(BaseModel):
    name: str
    value: str

class ComponentAssembly(BaseModel):
    uuid: str | UUID
    type: str
    title: str
    description: str
    props: List[PropsAssembly]
    status: StatusAssembly