#!/usr/bin/env python3
"""
SQLAlchemy和Pydantic兼容性测试脚本
验证修复后的系统兼容性
"""

import sys
import os

# 添加项目根目录到Python路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_imports():
    """测试基本导入功能"""
    print("=== 测试基本导入功能 ===")
    
    try:
        # 测试SQLAlchemy导入
        import sqlalchemy
        print(f"✓ SQLAlchemy版本: {sqlalchemy.__version__}")
        
        # 测试Pydantic导入
        import pydantic
        print(f"✓ Pydantic版本: {pydantic.__version__}")
        
        # 测试FastAPI导入
        import fastapi
        print(f"✓ FastAPI版本: {fastapi.__version__}")
        
        return True
    except Exception as e:
        print(f"✗ 导入失败: {e}")
        return False

def test_database_config():
    """测试数据库配置"""
    print("\n=== 测试数据库配置 ===")
    
    try:
        from backend.core.config import settings
        print("✓ 配置设置加载成功")
        
        from backend.core.database import engine, SessionLocal, Base
        print("✓ 数据库模块导入成功")
        
        # 测试兼容性检查
        from backend.core.compatibility import check_compatibility
        report = check_compatibility()
        print(f"✓ 兼容性检查完成: {report['compatible']}")
        
        if not report['compatible']:
            print("警告: 检测到兼容性问题:")
            for issue in report['issues']:
                print(f"  - {issue}")
        
        return True
    except Exception as e:
        print(f"✗ 数据库配置测试失败: {e}")
        return False

def test_schemas():
    """测试Schema定义"""
    print("\n=== 测试Schema定义 ===")
    
    try:
        # 测试设备schema
        from backend.schemas.device import DeviceCreate, DeviceResponse
        print("✓ 设备Schema导入成功")
        
        # 测试认证schema
        from backend.schemas.auth import UserCreate, UserResponse
        print("✓ 认证Schema导入成功")
        
        # 测试运维schema
        from backend.schemas.maintenance import MaintenanceOrderCreate
        print("✓ 运维Schema导入成功")
        
        # 测试模型实例化
        device_data = {
            "name": "测试设备",
            "type": "测试类型",
            "model": "测试型号",
            "serial_number": "12345",
            "location": "测试位置"
        }
        device = DeviceCreate(**device_data)
        print("✓ 设备模型实例化成功")
        
        user_data = {
            "username": "testuser",
            "name": "测试用户",
            "role": "operator",
            "password": "testpass"
        }
        user = UserCreate(**user_data)
        print("✓ 用户模型实例化成功")
        
        return True
    except Exception as e:
        print(f"✗ Schema测试失败: {e}")
        return False

def test_models():
    """测试数据库模型"""
    print("\n=== 测试数据库模型 ===")
    
    try:
        from backend.models.device import Device, DeviceStatus
        print("✓ 设备模型导入成功")
        
        from backend.models.user import User
        print("✓ 用户模型导入成功")
        
        # 检查模型属性
        device_columns = [col.name for col in Device.__table__.columns]
        print(f"✓ 设备模型列: {device_columns}")
        
        user_columns = [col.name for col in User.__table__.columns]
        print(f"✓ 用户模型列: {user_columns}")
        
        return True
    except Exception as e:
        print(f"✗ 模型测试失败: {e}")
        return False

def test_compatibility_functions():
    """测试兼容性函数"""
    print("\n=== 测试兼容性函数 ===")
    
    try:
        from backend.core.compatibility import (
            SQLAlchemyPydanticCompat,
            check_compatibility,
            compatibility_aware
        )
        print("✓ 兼容性模块导入成功")
        
        # 测试兼容性检查
        report = check_compatibility()
        print(f"✓ 兼容性报告生成成功")
        
        # 测试装饰器
        @compatibility_aware
def test_function():
            return "测试成功"
        
        result = test_function()
        print(f"✓ 装饰器测试: {result}")
        
        return True
    except Exception as e:
        print(f"✗ 兼容性函数测试失败: {e}")
        return False

def main():
    """主测试函数"""
    print("开始测试SQLAlchemy和Pydantic兼容性修复...")
    
    tests = [
        test_imports,
        test_database_config,
        test_schemas,
        test_models,
        test_compatibility_functions
    ]
    
    results = []
    for test_func in tests:
        try:
            result = test_func()
            results.append(result)
        except Exception as e:
            print(f"测试异常: {e}")
            results.append(False)
    
    print("\n" + "="*50)
    print("测试结果汇总:")
    
    passed = sum(results)
    total = len(results)
    
    for i, result in enumerate(results):
        status = "✓ 通过" if result else "✗ 失败"
        print(f"测试 {i+1}: {status}")
    
    print(f"\n总体结果: {passed}/{total} 测试通过")
    
    if passed == total:
        print("🎉 所有兼容性修复验证通过！")
        return 0
    else:
        print("⚠️ 部分测试未通过，请检查相关错误")
        return 1

if __name__ == "__main__":
    sys.exit(main())