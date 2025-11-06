from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class MaintenanceOrderBase(BaseModel):
    """运维工单基础模型"""
    title: str
    description: Optional[str] = None
    priority: str = "medium"
    status: str = "pending"
    device_id: int
    assignee_id: Optional[int] = None
    deadline: Optional[datetime] = None

class MaintenanceOrderCreate(MaintenanceOrderBase):
    """运维工单创建模型"""
    pass

class MaintenanceOrderResponse(MaintenanceOrderBase):
    """运维工单响应模型"""
    id: int
    created_at: datetime
    updated_at: datetime
    
    model_config = {"from_attributes": True}

class MaintenanceTaskBase(BaseModel):
    """运维任务基础模型"""
    title: str
    description: Optional[str] = None
    status: str = "pending"
    estimated_hours: Optional[float] = None
    actual_hours: Optional[float] = None

class MaintenanceTaskCreate(MaintenanceTaskBase):
    """运维任务创建模型"""
    pass

class MaintenanceTaskResponse(MaintenanceTaskBase):
    """运维任务响应模型"""
    id: int
    order_id: int
    created_at: datetime
    updated_at: datetime
    
    model_config = {"from_attributes": True}