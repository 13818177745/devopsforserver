from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text, Float, ForeignKey, JSON, Enum
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from backend.core.database import Base
import enum

class MaintenanceType(enum.Enum):
    PREVENTIVE = "preventive"  # 预防性维护
    CORRECTIVE = "corrective"  # 纠正性维护
    PREDICTIVE = "predictive"  # 预测性维护
    EMERGENCY = "emergency"    # 紧急维护

class MaintenancePriority(enum.Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    URGENT = "urgent"

class MaintenanceStatus(enum.Enum):
    PENDING = "pending"        # 待处理
    ASSIGNED = "assigned"      # 已分配
    IN_PROGRESS = "in_progress" # 进行中
    COMPLETED = "completed"    # 已完成
    CANCELLED = "cancelled"    # 已取消

class MaintenanceOrder(Base):
    __tablename__ = "maintenance_orders"
    
    id = Column(Integer, primary_key=True, index=True)
    order_number = Column(String(50), unique=True, index=True, nullable=False)  # 工单编号
    title = Column(String(200), nullable=False)  # 工单标题
    description = Column(Text)  # 工单描述
    
    # 工单类型和优先级
    maintenance_type = Column(Enum(MaintenanceType), nullable=False)
    priority = Column(Enum(MaintenancePriority), nullable=False)
    status = Column(Enum(MaintenanceStatus), default=MaintenanceStatus.PENDING, nullable=False)
    
    # 设备信息
    device_id = Column(Integer, ForeignKey("devices.id"), nullable=False)
    
    # 负责人信息
    assignee_id = Column(Integer, ForeignKey("users.id"))
    reporter_id = Column(Integer, ForeignKey("users.id"), nullable=False)  # 报告人
    
    # 时间信息
    scheduled_date = Column(DateTime)  # 计划开始时间
    due_date = Column(DateTime)        # 截止时间
    actual_start_date = Column(DateTime)  # 实际开始时间
    actual_end_date = Column(DateTime)    # 实际结束时间
    
    # 预计时长和实际时长
    estimated_duration = Column(Float)  # 预计时长（小时）
    actual_duration = Column(Float)    # 实际时长（小时）
    
    # 费用信息
    estimated_cost = Column(Float)  # 预计费用
    actual_cost = Column(Float)     # 实际费用
    
    # 工作内容和结果
    work_content = Column(Text)  # 工作内容
    result = Column(Text)        # 处理结果
    notes = Column(Text)         # 备注
    
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    
    # 关联关系
    device = relationship("Device", back_populates="maintenance_orders")
    assignee = relationship("User", foreign_keys=[assignee_id], back_populates="maintenance_orders")
    reporter = relationship("User", foreign_keys=[reporter_id])
    tasks = relationship("MaintenanceTask", back_populates="order")

class MaintenanceTask(Base):
    __tablename__ = "maintenance_tasks"
    
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("maintenance_orders.id"), nullable=False)
    task_name = Column(String(200), nullable=False)  # 任务名称
    description = Column(Text)  # 任务描述
    
    # 任务状态
    status = Column(String(20), default="pending")  # pending, in_progress, completed, failed
    
    # 执行信息
    assigned_to = Column(Integer, ForeignKey("users.id"))  # 执行人
    estimated_time = Column(Float)  # 预计时间（小时）
    actual_time = Column(Float)     # 实际时间（小时）
    
    # 执行结果
    result = Column(Text)        # 执行结果
    notes = Column(Text)         # 备注
    
    # 顺序和依赖
    sequence = Column(Integer, default=0)  # 执行顺序
    depends_on = Column(Integer, ForeignKey("maintenance_tasks.id"))  # 依赖任务
    
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    
    # 关联关系
    order = relationship("MaintenanceOrder", back_populates="tasks")
    assigned_user = relationship("User", foreign_keys=[assigned_to])

class MaintenanceTemplate(Base):
    __tablename__ = "maintenance_templates"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)  # 模板名称
    description = Column(Text)  # 模板描述
    
    # 模板类型
    template_type = Column(String(50), nullable=False)  # 模板类型
    device_type = Column(String(50), nullable=False)      # 设备类型
    
    # 维护周期
    interval_type = Column(String(20))  # daily, weekly, monthly, quarterly, yearly
    interval_value = Column(Integer)   # 间隔值
    
    # 预计信息
    estimated_duration = Column(Float)  # 预计时长
    estimated_cost = Column(Float)       # 预计费用
    
    # 任务列表
    tasks_config = Column(JSON)  # 任务配置
    
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

class MaintenanceHistory(Base):
    __tablename__ = "maintenance_history"
    
    id = Column(Integer, primary_key=True, index=True)
    device_id = Column(Integer, ForeignKey("devices.id"), nullable=False)
    order_id = Column(Integer, ForeignKey("maintenance_orders.id"), nullable=False)
    
    # 维护信息
    maintenance_type = Column(String(50), nullable=False)
    work_content = Column(Text)
    result = Column(Text)
    
    # 执行信息
    performed_by = Column(Integer, ForeignKey("users.id"))
    performed_at = Column(DateTime, default=func.now())
    
    # 费用信息
    cost = Column(Float)
    duration = Column(Float)
    
    created_at = Column(DateTime, default=func.now())
    
    # 关联关系
    device = relationship("Device")
    order = relationship("MaintenanceOrder")
    performer = relationship("User", foreign_keys=[performed_by])