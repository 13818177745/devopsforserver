from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text, Float, ForeignKey, JSON
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from backend.core.database import Base

class Device(Base):
    __tablename__ = "devices"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    device_code = Column(String(50), unique=True, index=True, nullable=False)
    device_type = Column(String(50), nullable=False)  # 设备类型
    model = Column(String(100))  # 设备型号
    manufacturer = Column(String(100))  # 生产厂家
    serial_number = Column(String(100), unique=True)  # 序列号
    
    # 设备位置信息
    location = Column(String(200))
    department = Column(String(100))
    
    # 技术参数
    technical_specs = Column(JSON)  # 技术规格
    installation_date = Column(DateTime)
    warranty_period = Column(Integer)  # 保修期（月）
    
    # 状态信息
    status = Column(String(20), default="normal")  # normal, warning, fault, maintenance
    is_online = Column(Boolean, default=False)  # 是否在线
    last_heartbeat = Column(DateTime)  # 最后心跳时间
    
    # 负责人信息
    owner_id = Column(Integer, ForeignKey("users.id"))
    
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    
    # 关联关系
    owner = relationship("User", back_populates="devices")
    status_history = relationship("DeviceStatus", back_populates="device")
    maintenance_orders = relationship("MaintenanceOrder", back_populates="device")

class DeviceStatus(Base):
    __tablename__ = "device_status"
    
    id = Column(Integer, primary_key=True, index=True)
    device_id = Column(Integer, ForeignKey("devices.id"), nullable=False)
    status = Column(String(20), nullable=False)  # 状态
    temperature = Column(Float)  # 温度
    pressure = Column(Float)  # 压力
    vibration = Column(Float)  # 振动
    power_consumption = Column(Float)  # 功耗
    
    # 运行参数
    running_hours = Column(Float)  # 运行小时数
    production_count = Column(Integer)  # 生产数量
    
    # 其他监测数据
    monitoring_data = Column(JSON)  # 其他监测数据
    
    created_at = Column(DateTime, default=func.now())
    
    # 关联关系
    device = relationship("Device", back_populates="status_history")

class DeviceCategory(Base):
    __tablename__ = "device_categories"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, nullable=False)
    description = Column(Text)
    parent_id = Column(Integer, ForeignKey("device_categories.id"))  # 父级分类
    created_at = Column(DateTime, default=func.now())
    
    # 自关联关系
    parent = relationship("DeviceCategory", remote_side=[id])
    
class DeviceParameter(Base):
    __tablename__ = "device_parameters"
    
    id = Column(Integer, primary_key=True, index=True)
    device_type = Column(String(50), nullable=False)
    parameter_name = Column(String(100), nullable=False)
    parameter_type = Column(String(20), nullable=False)  # number, string, boolean
    min_value = Column(Float)
    max_value = Column(Float)
    unit = Column(String(20))
    description = Column(Text)
    created_at = Column(DateTime, default=func.now())