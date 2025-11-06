from pydantic_settings import BaseSettings
from typing import List
import os

class Settings(BaseSettings):
    # 数据库配置
    database_url: str = "postgresql://postgres:password@localhost:5432/equipment_ops"
    redis_url: str = "redis://localhost:6379/0"
    
    # JWT配置
    secret_key: str = "your-secret-key-change-this-in-production"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    
    # 应用配置
    debug: bool = True
    cors_origins: List[str] = ["http://localhost:3000", "http://127.0.0.1:3000"]
    
    # MCP服务配置
    mcp_services_path: str = "./mcp-services"
    
    class Config:
        env_file = ".env"

settings = Settings()