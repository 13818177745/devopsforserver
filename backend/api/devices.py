from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional

from backend.core.database import get_db
from backend.models.device import Device, DeviceStatus, DeviceCategory
from backend.schemas.device import (
    DeviceCreate, DeviceResponse, DeviceUpdate,
    DeviceStatusCreate, DeviceStatusResponse,
    DeviceCategoryCreate, DeviceCategoryResponse
)

router = APIRouter()

@router.get("/", response_model=List[DeviceResponse])
async def get_devices(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """获取设备列表"""
    devices = db.query(Device).offset(skip).limit(limit).all()
    return devices

@router.post("/", response_model=DeviceResponse)
async def create_device(
    device_data: DeviceCreate,
    db: Session = Depends(get_db)
):
    """创建设备"""
    device = Device(**device_data.dict())
    db.add(device)
    db.commit()
    db.refresh(device)
    return device

@router.get("/{device_id}", response_model=DeviceResponse)
async def get_device(device_id: int, db: Session = Depends(get_db)):
    """获取设备详情"""
    device = db.query(Device).filter(Device.id == device_id).first()
    if not device:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="设备不存在"
        )
    return device

@router.put("/{device_id}", response_model=DeviceResponse)
async def update_device(
    device_id: int,
    device_data: DeviceUpdate,
    db: Session = Depends(get_db)
):
    """更新设备信息"""
    device = db.query(Device).filter(Device.id == device_id).first()
    if not device:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="设备不存在"
        )
    
    for field, value in device_data.dict(exclude_unset=True).items():
        setattr(device, field, value)
    
    db.commit()
    db.refresh(device)
    return device

@router.delete("/{device_id}")
async def delete_device(device_id: int, db: Session = Depends(get_db)):
    """删除设备"""
    device = db.query(Device).filter(Device.id == device_id).first()
    if not device:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="设备不存在"
        )
    
    db.delete(device)
    db.commit()
    return {"message": "设备删除成功"}

@router.get("/{device_id}/status", response_model=List[DeviceStatusResponse])
async def get_device_status_history(
    device_id: int,
    db: Session = Depends(get_db)
):
    """获取设备状态历史"""
    status_history = db.query(DeviceStatus).filter(
        DeviceStatus.device_id == device_id
    ).order_by(DeviceStatus.timestamp.desc()).all()
    return status_history

@router.post("/{device_id}/status", response_model=DeviceStatusResponse)
async def create_device_status(
    device_id: int,
    status_data: DeviceStatusCreate,
    db: Session = Depends(get_db)
):
    """创建设备状态记录"""
    device = db.query(Device).filter(Device.id == device_id).first()
    if not device:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="设备不存在"
        )
    
    status_record = DeviceStatus(
        device_id=device_id,
        **status_data.dict()
    )
    db.add(status_record)
    db.commit()
    db.refresh(status_record)
    return status_record