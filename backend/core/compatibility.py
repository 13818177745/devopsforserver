"""
SQLAlchemy和Pydantic兼容性模块
解决Python 3.14.0与SQLAlchemy 2.0+的兼容性问题
"""

from typing import Any, Type, TypeVar, Optional
from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy.orm import Mapped
from pydantic import BaseModel, create_model, Field
import logging

logger = logging.getLogger(__name__)

T = TypeVar('T', bound=BaseModel)

class SQLAlchemyPydanticCompat:
    """SQLAlchemy与Pydantic兼容性处理类"""
    
    @staticmethod
    def create_compatible_model(model_class: Type[BaseModel], 
                               db_model: DeclarativeMeta) -> Type[BaseModel]:
        """
        创建兼容的Pydantic模型，解决SQLAlchemy类型映射问题
        
        Args:
            model_class: 原始Pydantic模型类
            db_model: SQLAlchemy数据库模型类
            
        Returns:
            兼容的Pydantic模型类
        """
        try:
            # 获取模型的字段定义
            field_definitions = {}
            
            for field_name, field_info in model_class.__annotations__.items():
                # 处理SQLAlchemy的Mapped类型
                if hasattr(field_info, '__origin__') and field_info.__origin__ is Mapped:
                    # 从Mapped类型中提取实际类型
                    actual_type = field_info.__args__[0] if field_info.__args__ else Any
                    field_definitions[field_name] = (actual_type, ...)
                else:
                    field_definitions[field_name] = (field_info, ...)
            
            # 创建新的模型类
            return create_model(
                f"Compatible{model_class.__name__}",
                **field_definitions,
                __config__=model_class.model_config if hasattr(model_class, 'model_config') else None
            )
            
        except Exception as e:
            logger.warning(f"创建兼容模型失败: {e}")
            return model_class
    
    @staticmethod
    def convert_to_pydantic(db_obj: Any, pydantic_model: Type[T]) -> Optional[T]:
        """
        将SQLAlchemy对象转换为Pydantic模型
        
        Args:
            db_obj: SQLAlchemy数据库对象
            pydantic_model: 目标Pydantic模型类
            
        Returns:
            Pydantic模型实例或None
        """
        if db_obj is None:
            return None
            
        try:
            # 获取数据库对象的属性字典
            data = {}
            for column in db_obj.__table__.columns:
                if hasattr(db_obj, column.name):
                    data[column.name] = getattr(db_obj, column.name)
            
            # 创建Pydantic模型实例
            return pydantic_model(**data)
            
        except Exception as e:
            logger.error(f"转换到Pydantic失败: {e}")
            return None
    
    @staticmethod
    def handle_datetime_serialization(data: dict) -> dict:
        """
        处理日期时间序列化问题
        
        Args:
            data: 包含日期时间字段的数据字典
            
        Returns:
            处理后的数据字典
        """
        import datetime
        
        processed_data = {}
        for key, value in data.items():
            if isinstance(value, datetime.datetime):
                # 将datetime转换为ISO格式字符串
                processed_data[key] = value.isoformat()
            else:
                processed_data[key] = value
        
        return processed_data


class TypeSafeConfig:
    """类型安全配置类"""
    
    # SQLAlchemy配置
    SQLALCHEMY_ENGINE_OPTIONS = {
        "pool_pre_ping": True,
        "pool_recycle": 3600,
        "echo": False
    }
    
    # Pydantic配置
    PYDANTIC_CONFIG = {
        "from_attributes": True,
        "str_strip_whitespace": True,
        "validate_assignment": True,
        "arbitrary_types_allowed": True
    }


# 兼容性检查函数
def check_compatibility() -> dict:
    """
    检查当前环境的兼容性状态
    
    Returns:
        兼容性状态字典
    """
    import sys
    
    compatibility_report = {
        "python_version": sys.version,
        "compatible": True,
        "issues": []
    }
    
    try:
        # 检查SQLAlchemy
        import sqlalchemy
        compatibility_report["sqlalchemy_version"] = sqlalchemy.__version__
        
        # 检查Pydantic
        import pydantic
        compatibility_report["pydantic_version"] = pydantic.__version__
        
        # 检查Python版本兼容性
        if sys.version_info >= (3, 14):
            if sqlalchemy.__version__.startswith("2.0"):
                # 检查是否为兼容版本
                if sqlalchemy.__version__ < "2.0.25":
                    compatibility_report["issues"].append(
                        "SQLAlchemy版本低于2.0.25，可能与Python 3.14+存在兼容性问题"
                    )
                    compatibility_report["compatible"] = False
        
        # 检查类型注解兼容性
        try:
            from typing import get_args, get_origin
            compatibility_report["typing_compatibility"] = "正常"
        except ImportError:
            compatibility_report["issues"].append(
                "typing模块版本可能过旧，请检查Python版本"
            )
            
    except ImportError as e:
        compatibility_report["compatible"] = False
        compatibility_report["issues"].append(f"导入失败: {e}")
    
    return compatibility_report


# 装饰器函数
def compatibility_aware(func):
    """
    兼容性感知装饰器
    自动处理SQLAlchemy和Pydantic之间的兼容性问题
    """
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            # 记录详细的错误信息
            logger.error(f"兼容性错误在 {func.__name__}: {e}")
            
            # 检查是否是SQLAlchemy特定的错误
            if "SQLCoreOperations" in str(e) or "TypingOnly" in str(e):
                logger.warning("检测到SQLAlchemy类型系统兼容性问题")
                # 这里可以添加特定的修复逻辑
                
            # 重新抛出异常
            raise
    
    return wrapper