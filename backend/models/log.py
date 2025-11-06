from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text, ForeignKey, JSON
from sqlalchemy.sql import func
from backend.core.database import Base

class SystemLog(Base):
    __tablename__ = "system_logs"
    
    id = Column(Integer, primary_key=True, index=True)
    
    # 日志基本信息
    level = Column(String(20), nullable=False)  # info, warning, error, critical
    module = Column(String(100), nullable=False)  # 模块名称
    action = Column(String(200), nullable=False)  # 操作行为
    
    # 用户信息
    user_id = Column(Integer, ForeignKey("users.id"))
    ip_address = Column(String(50))  # IP地址
    user_agent = Column(Text)       # 用户代理
    
    # 请求信息
    request_method = Column(String(10))  # GET, POST, PUT, DELETE
    request_path = Column(String(500))   # 请求路径
    request_params = Column(JSON)       # 请求参数
    
    # 响应信息
    response_status = Column(Integer)  # 响应状态码
    response_time = Column(Float)       # 响应时间（毫秒）
    
    # 详细信息
    message = Column(Text)             # 日志消息
    details = Column(JSON)             # 详细数据
    
    created_at = Column(DateTime, default=func.now())

class OperationLog(Base):
    __tablename__ = "operation_logs"
    
    id = Column(Integer, primary_key=True, index=True)
    
    # 操作信息
    operation_type = Column(String(50), nullable=False)  # 操作类型
    resource_type = Column(String(100), nullable=False)  # 资源类型
    resource_id = Column(Integer)                          # 资源ID
    
    # 用户信息
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    # 操作内容
    action = Column(String(200), nullable=False)  # 操作行为
    description = Column(Text)                   # 操作描述
    
    # 变更信息
    before_change = Column(JSON)  # 变更前数据
    after_change = Column(JSON)  # 变更后数据
    
    # 位置信息
    ip_address = Column(String(50))  # IP地址
    
    created_at = Column(DateTime, default=func.now())