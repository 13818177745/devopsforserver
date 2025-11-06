from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from backend.core.database import get_db
from backend.models.maintenance import MaintenanceOrder, MaintenanceTask
from backend.schemas.maintenance import (
    MaintenanceOrderCreate, MaintenanceOrderResponse,
    MaintenanceTaskCreate, MaintenanceTaskResponse
)

router = APIRouter()

@router.get("/orders", response_model=List[MaintenanceOrderResponse])
async def get_maintenance_orders(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """获取运维工单列表"""
    orders = db.query(MaintenanceOrder).offset(skip).limit(limit).all()
    return orders

@router.post("/orders", response_model=MaintenanceOrderResponse)
async def create_maintenance_order(
    order_data: MaintenanceOrderCreate,
    db: Session = Depends(get_db)
):
    """创建运维工单"""
    order = MaintenanceOrder(**order_data.dict())
    db.add(order)
    db.commit()
    db.refresh(order)
    return order

@router.get("/orders/{order_id}", response_model=MaintenanceOrderResponse)
async def get_maintenance_order(
    order_id: int,
    db: Session = Depends(get_db)
):
    """获取运维工单详情"""
    order = db.query(MaintenanceOrder).filter(MaintenanceOrder.id == order_id).first()
    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="运维工单不存在"
        )
    return order

@router.put("/orders/{order_id}", response_model=MaintenanceOrderResponse)
async def update_maintenance_order(
    order_id: int,
    order_data: MaintenanceOrderCreate,
    db: Session = Depends(get_db)
):
    """更新运维工单"""
    order = db.query(MaintenanceOrder).filter(MaintenanceOrder.id == order_id).first()
    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="运维工单不存在"
        )
    
    for field, value in order_data.dict(exclude_unset=True).items():
        setattr(order, field, value)
    
    db.commit()
    db.refresh(order)
    return order

@router.get("/orders/{order_id}/tasks", response_model=List[MaintenanceTaskResponse])
async def get_maintenance_tasks(
    order_id: int,
    db: Session = Depends(get_db)
):
    """获取运维任务列表"""
    tasks = db.query(MaintenanceTask).filter(
        MaintenanceTask.order_id == order_id
    ).all()
    return tasks

@router.post("/orders/{order_id}/tasks", response_model=MaintenanceTaskResponse)
async def create_maintenance_task(
    order_id: int,
    task_data: MaintenanceTaskCreate,
    db: Session = Depends(get_db)
):
    """创建运维任务"""
    order = db.query(MaintenanceOrder).filter(MaintenanceOrder.id == order_id).first()
    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="运维工单不存在"
        )
    
    task = MaintenanceTask(order_id=order_id, **task_data.dict())
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

@router.get("/dashboard/stats")
async def get_maintenance_stats(db: Session = Depends(get_db)):
    """获取运维统计信息"""
    # 统计各种状态的工单数量
    total_orders = db.query(MaintenanceOrder).count()
    pending_orders = db.query(MaintenanceOrder).filter(
        MaintenanceOrder.status == 'pending'
    ).count()
    in_progress_orders = db.query(MaintenanceOrder).filter(
        MaintenanceOrder.status == 'in_progress'
    ).count()
    completed_orders = db.query(MaintenanceOrder).filter(
        MaintenanceOrder.status == 'completed'
    ).count()
    
    return {
        "total_orders": total_orders,
        "pending_orders": pending_orders,
        "in_progress_orders": in_progress_orders,
        "completed_orders": completed_orders
    }