#!/usr/bin/env python3
"""数据库初始化脚本"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.core.database import engine, Base
from backend.models.user import User
from backend.models.device import Device, DeviceCategory
from backend.core.security import get_password_hash

from sqlalchemy.orm import sessionmaker

# 创建数据库表
Base.metadata.create_all(bind=engine)

# 创建会话
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_data():
    """初始化数据"""
    db = SessionLocal()
    
    try:
        # 检查是否已有管理员用户
        admin_user = db.query(User).filter(User.username == "admin").first()
        if not admin_user:
            # 创建管理员用户
            admin_user = User(
                username="admin",
                name="系统管理员",
                hashed_password=get_password_hash("admin123"),
                role="admin",
                department="信息技术部",
                is_active=True
            )
            db.add(admin_user)
            
            # 创建普通用户
            user1 = User(
                username="zhangsan",
                name="张三",
                hashed_password=get_password_hash("user123"),
                role="engineer",
                department="运维部",
                is_active=True
            )
            db.add(user1)
            
            # 创建设备分类
            categories = [
                DeviceCategory(name="生产设备", description="生产线主要设备"),
                DeviceCategory(name="检测设备", description="质量检测设备"),
                DeviceCategory(name="辅助设备", description="辅助生产设备"),
                DeviceCategory(name="办公设备", description="办公用设备")
            ]
            
            for category in categories:
                db.add(category)
            
            db.commit()
            
            # 获取分类ID
            production_category = db.query(DeviceCategory).filter(
                DeviceCategory.name == "生产设备"
            ).first()
            
            # 创建设备数据
            devices = [
                Device(
                    name="生产设备A",
                    type="注塑机",
                    model="HD-1000",
                    serial_number="SN001",
                    location="车间A",
                    status="online",
                    category_id=production_category.id
                ),
                Device(
                    name="检测设备B",
                    type="光谱仪",
                    model="SP-2000",
                    serial_number="SN002",
                    location="实验室",
                    status="offline",
                    category_id=production_category.id
                )
            ]
            
            for device in devices:
                db.add(device)
            
            db.commit()
            print("数据库初始化完成！")
            print("管理员账号: admin / admin123")
            print("普通用户账号: zhangsan / user123")
        else:
            print("数据库已初始化，无需重复操作")
            
    except Exception as e:
        print(f"数据库初始化失败: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    init_data()