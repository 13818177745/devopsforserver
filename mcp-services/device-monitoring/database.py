"""数据库管理模块"""

import logging
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text

logger = logging.getLogger(__name__)

class DatabaseManager:
    """数据库管理器"""
    
    def __init__(self):
        self.engine = None
        self.async_session = None
    
    async def connect(self):
        """连接数据库"""
        try:
            # 从环境变量获取数据库连接信息
            database_url = "postgresql+asyncpg://admin:admin123@postgres:5432/device_management"
            
            self.engine = create_async_engine(
                database_url,
                echo=True,
                pool_size=10,
                max_overflow=20
            )
            
            self.async_session = sessionmaker(
                self.engine,
                class_=AsyncSession,
                expire_on_commit=False
            )
            
            # 测试连接
            async with self.engine.connect() as conn:
                await conn.execute(text("SELECT 1"))
            
            logger.info("数据库连接成功")
            
        except Exception as e:
            logger.error(f"数据库连接失败: {e}")
            raise
    
    async def disconnect(self):
        """断开数据库连接"""
        if self.engine:
            await self.engine.dispose()
            logger.info("数据库连接已关闭")
    
    async def get_session(self):
        """获取数据库会话"""
        if not self.async_session:
            raise Exception("数据库未连接")
        
        async with self.async_session() as session:
            yield session