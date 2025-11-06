from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class DeviceBase(BaseModel):
    """设备基础模型"""
    name: str
    type: str
    model: str
    serial_number: str
    location: str
    status: str = "offline"
    category_id: Optional[int] = None

class DeviceCreate(DeviceBase):
    """设备创建模型"""
    pass

class DeviceUpdate(BaseModel):
    """设备更新模型"""
    name: Optional[str] = None
    type: Optional[str] = None
    location: Optional[str] = None
    status: Optional[str] = None

class DeviceResponse(DeviceBase):
    """设备响应模型"""
    id: int
    created_at: datetime
    updated_at: datetime
    
    model_config = {"from_attributes": True}

class DeviceStatusBase(BaseModel):
    """设备状态基础模型"""
    status: str
    description: Optional[str] = None

class DeviceStatusCreate(DeviceStatusBase):
    """设备状态创建模型"""
    pass

class DeviceStatusResponse(DeviceStatusBase):
    """设备状态响应模型"""
    id: int
    device_id: int
    timestamp: datetime
    
    model_config = {"from_attributes": True}

class DeviceCategoryBase(BaseModel):
    """设备分类基础模型"""
    name: str
    description: Optional[str] = None

class DeviceCategoryCreate(DeviceCategoryBase):
    """设备分类创建模型"""
    pass

class DeviceCategoryResponse(DeviceCategoryBase):
    """设备分类响应模型"""
    id: int
    created_at: datetime
    
    model_config = {"from_attributes": True}