from pydantic import BaseModel
from typing import Optional

class Token(BaseModel):
    """Token响应模型"""
    access_token: str
    token_type: str
    user: dict

class TokenData(BaseModel):
    """Token数据模型"""
    username: Optional[str] = None

class UserBase(BaseModel):
    """用户基础模型"""
    username: str
    name: str
    role: str
    department: Optional[str] = None

class UserCreate(UserBase):
    """用户创建模型"""
    password: str

class UserResponse(UserBase):
    """用户响应模型"""
    id: int
    is_active: bool
    
    model_config = {"from_attributes": True}