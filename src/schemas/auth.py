from datetime import datetime
from pydantic import BaseModel, EmailStr
from typing import Optional


class Token(BaseModel):
    """Схема для возврата JWT токена"""
    access_token: str
    token_type: str = "bearer"


class TokenData(BaseModel):
    """Схема для данных в JWT токене"""
    email: Optional[EmailStr] = None
    exp: Optional[datetime] = None


class UserLogin(BaseModel):
    """Схема для входа пользователя"""
    email: EmailStr
    password: str


class UserCreate(BaseModel):
    """Схема для создания пользователя"""
    email: EmailStr
    password: str
    is_active: Optional[bool] = True


class UserOut(BaseModel):
    """Схема для отображения пользователя"""
    id: int
    email: EmailStr
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True  # Для совместимости с SQLAlchemy моделями (бывшее orm_mode)
