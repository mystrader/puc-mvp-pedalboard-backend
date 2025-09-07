from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class PedalboardBase(BaseModel):
    """Schema base para pedalboard"""
    name: str = Field(..., min_length=1, max_length=100, description="Nome do pedalboard")
    description: Optional[str] = Field(None, description="Descrição do pedalboard")
    user_id: int = Field(..., description="ID do usuário proprietário")

class PedalboardCreateSchema(PedalboardBase):
    """Schema para criação de pedalboard"""
    pass

class PedalboardSchema(PedalboardBase):
    """Schema para resposta de pedalboard"""
    id: int
    created_at: datetime
    updated_at: datetime
    pedals: List['PedalSchema'] = []
    
    class Config:
        from_attributes = True

class PedalBase(BaseModel):
    """Schema base para pedal"""
    name: str = Field(..., min_length=1, max_length=100, description="Nome do pedal")
    brand: str = Field(..., min_length=1, max_length=50, description="Marca do pedal")
    category: str = Field(..., min_length=1, max_length=50, description="Categoria do pedal (ex: distortion, delay, reverb)")
    description: Optional[str] = Field(None, description="Descrição do pedal")
    pedalboard_id: int = Field(..., description="ID do pedalboard ao qual pertence")

class PedalCreateSchema(PedalBase):
    """Schema para criação de pedal"""
    pass

class PedalSchema(PedalBase):
    """Schema para resposta de pedal"""
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

# Schemas para parâmetros de path
class PedalboardPathSchema(BaseModel):
    """Schema para parâmetros de path do pedalboard"""
    pedalboard_id: int = Field(..., description="ID do pedalboard")

class PedalPathSchema(BaseModel):
    """Schema para parâmetros de path do pedal"""
    pedal_id: int = Field(..., description="ID do pedal")

# Atualizar referências para evitar problemas de forward reference
PedalboardSchema.model_rebuild()