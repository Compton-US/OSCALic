from uuid import UUID
from pydantic import BaseModel,Field

class ResponsibilitiesAssembly(BaseModel):
    uuid: str | UUID
    description: str | None
    provided_uuid: str | UUID = Field(default=None, alias='provided-uuid')
    action: str | None  
    
class ImplementationStatusAssembly(BaseModel):
    state: str | None
    remarks: str | None

class InheritanceAssembly(BaseModel):
    type: str | None
    remarks: str | None

class ProvidedAssembly(BaseModel):
    uuid: str | UUID
    description: str | None
    import_ref: UUID = Field(default=None, alias='import-ref')
    implementation_status: ImplementationStatusAssembly = Field(default=None, alias='implementation-status')
    inheritance: InheritanceAssembly = Field(default=None)

class ExportAssembly(BaseModel):
    provided: ProvidedAssembly = Field(default=None, alias='provided')
    responsibilities: ResponsibilitiesAssembly = Field(default=None, alias='responsibilities')

class ByComponentAssembly(BaseModel):
    uuid: str | UUID
    component_uuid: str | UUID = Field(alias='component-uuid')
    description: str | None
    export: ExportAssembly = Field(default=None, alias='export')




