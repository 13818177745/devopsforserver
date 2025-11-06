# 设备运维管理系统

一个基于现代Web技术的企业级设备运维管理平台，提供设备监控、运维工单管理、数据分析等功能。

## 系统架构

```
┌─────────────────────────────────────────┐
│             前端展示层 (Frontend)         │
│  React + TDesign + TypeScript           │
└─────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────┐
│             API网关层 (Gateway)         │
│        Nginx + 负载均衡                 │
└─────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────┐
│           业务逻辑层 (Backend)          │
│      FastAPI + PostgreSQL + Redis       │
└─────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────┐
│           MCP服务层 (MCP Services)     │
│   设备监控 + 运维任务 + 数据分析        │
└─────────────────────────────────────────┘
```

## 功能特性

### 核心功能
- **设备管理**: 设备信息管理、状态监控、维护记录
- **运维工单**: 工单创建、任务分配、进度跟踪
- **用户管理**: 用户认证、权限管理、角色控制
- **数据统计**: 设备运行统计、运维分析、报表生成

### 技术特色
- **现代化前端**: 使用React + TDesign构建响应式界面
- **高性能后端**: FastAPI提供RESTful API接口
- **实时监控**: MCP服务层实现设备实时监控和告警
- **容器化部署**: Docker Compose一键部署

## 快速开始

### 环境要求
- Docker 20.10+
- Docker Compose 2.0+

### 部署步骤

1. **克隆项目**
```bash
git clone <repository-url>
cd device-management-system
```

2. **启动服务**
```bash
# 使用Docker Compose启动所有服务
docker-compose up -d

# 查看服务状态
docker-compose ps
```

3. **初始化数据库**
```bash
# 执行数据库初始化脚本
docker-compose exec backend python scripts/init_db.py
```

4. **访问应用**
- 前端应用: http://localhost:3000
- 后端API: http://localhost:8000
- API文档: http://localhost:8000/docs

### 默认账号
- 管理员: admin / admin123
- 运维工程师: zhangsan / user123

## 项目结构

```
├── backend/                 # 后端服务
│   ├── api/                # API接口
│   ├── core/               # 核心模块
│   ├── models/             # 数据模型
│   ├── schemas/            # 数据模式
│   ├── scripts/            # 脚本文件
│   └── main.py             # 应用入口
├── frontend/               # 前端应用
│   ├── src/
│   │   ├── components/     # 组件
│   │   ├── pages/          # 页面
│   │   └── contexts/       # 上下文
│   └── package.json
├── mcp-services/           # MCP智能服务
│   ├── device-monitoring/  # 设备监控服务
│   ├── maintenance-task/   # 运维任务服务
│   └── data-analysis/      # 数据分析服务
├── docker-compose.yml      # Docker编排文件
└── README.md              # 项目说明
```

## 开发指南

### 后端开发
```bash
cd backend

# 安装依赖
pip install -r requirements.txt

# 启动开发服务器
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### 前端开发
```bash
cd frontend

# 安装依赖
npm install

# 启动开发服务器
npm run dev
```

### 数据库迁移
```bash
# 生成迁移文件
alembic revision --autogenerate -m "description"

# 执行迁移
alembic upgrade head
```

## API文档

启动后端服务后，访问以下地址查看API文档：
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 配置说明

### 环境变量

主要环境变量配置：

```bash
# 数据库配置
DATABASE_URL=postgresql://admin:admin123@postgres:5432/device_management

# Redis配置
REDIS_URL=redis://redis:6379/0

# JWT密钥
SECRET_KEY=your-secret-key

# 前端API地址
REACT_APP_API_URL=http://localhost:8000/api
```

### 日志配置

系统使用标准Python日志模块，日志级别可通过环境变量配置：

```bash
LOG_LEVEL=INFO  # DEBUG, INFO, WARNING, ERROR
```

## 故障排除

### 常见问题

1. **端口冲突**
   - 检查80、3000、8000端口是否被占用
   - 修改docker-compose.yml中的端口映射

2. **数据库连接失败**
   - 检查PostgreSQL容器是否正常启动
   - 验证数据库连接字符串

3. **前端无法访问后端**
   - 检查CORS配置
   - 验证API地址配置

### 日志查看

```bash
# 查看所有服务日志
docker-compose logs

# 查看特定服务日志
docker-compose logs backend
docker-compose logs frontend
```

## 许可证

本项目采用MIT许可证，详见LICENSE文件。

## 贡献指南

欢迎提交Issue和Pull Request来改进本项目。

## 联系方式

如有问题请联系项目维护团队。