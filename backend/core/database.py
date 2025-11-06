from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings
from .compatibility import TypeSafeConfig, check_compatibility

# 检查兼容性
compatibility_report = check_compatibility()
if not compatibility_report["compatible"]:
    print("警告: 检测到兼容性问题:")
    for issue in compatibility_report["issues"]:
        print(f"  - {issue}")

# 创建数据库引擎，使用类型安全配置
engine = create_engine(
    settings.database_url, 
    **TypeSafeConfig.SQLALCHEMY_ENGINE_OPTIONS
)

# 创建会话工厂
SessionLocal = sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=engine,
    expire_on_commit=False  # 避免对象过期问题
)

# 声明基类
Base = declarative_base()

def get_db():
    """获取数据库会话"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()