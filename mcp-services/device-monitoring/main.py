#!/usr/bin/env python3
"""设备监控服务 - 实时监控设备状态和数据"""

import asyncio
import logging
from datetime import datetime
from typing import Dict, Any

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from database import DatabaseManager
from monitor import DeviceMonitor

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="设备监控服务", version="1.0.0")

db_manager = DatabaseManager()
device_monitor = DeviceMonitor(db_manager)

class DeviceStatusUpdate(BaseModel):
    """设备状态更新模型"""
    device_id: int
    status: str
    metrics: Dict[str, Any]
    timestamp: datetime

class MonitoringAlert(BaseModel):
    """监控告警模型"""
    device_id: int
    alert_type: str
    severity: str
    message: str
    timestamp: datetime

@app.on_event("startup")
async def startup_event():
    """启动时初始化"""
    await db_manager.connect()
    await device_monitor.start_monitoring()
    logger.info("设备监控服务启动完成")

@app.on_event("shutdown")
async def shutdown_event():
    """关闭时清理"""
    await device_monitor.stop_monitoring()
    await db_manager.disconnect()
    logger.info("设备监控服务已关闭")

@app.post("/monitoring/status")
async def update_device_status(status_update: DeviceStatusUpdate):
    """更新设备状态"""
    try:
        await device_monitor.update_device_status(status_update)
        return {"message": "设备状态更新成功"}
    except Exception as e:
        logger.error(f"设备状态更新失败: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/monitoring/alerts")
async def create_monitoring_alert(alert: MonitoringAlert):
    """创建监控告警"""
    try:
        await device_monitor.create_alert(alert)
        return {"message": "告警创建成功"}
    except Exception as e:
        logger.error(f"告警创建失败: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/monitoring/devices/{device_id}/metrics")
async def get_device_metrics(device_id: int):
    """获取设备监控指标"""
    try:
        metrics = await device_monitor.get_device_metrics(device_id)
        return metrics
    except Exception as e:
        logger.error(f"获取设备指标失败: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/monitoring/alerts")
async def get_recent_alerts(limit: int = 10):
    """获取最近告警"""
    try:
        alerts = await device_monitor.get_recent_alerts(limit)
        return alerts
    except Exception as e:
        logger.error(f"获取告警失败: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    """健康检查"""
    return {
        "status": "healthy",
        "service": "device-monitoring",
        "timestamp": datetime.now().isoformat()
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)