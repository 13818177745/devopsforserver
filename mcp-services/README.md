# MCP 服务层

设备运维系统的智能服务层，基于 MCP (Model Context Protocol) 提供设备监控、运维任务调度和数据分析服务。

## 服务架构

```
MCP 服务层
├── 设备监控服务 (Device Monitoring Service)
├── 运维任务服务 (Maintenance Task Service)
└── 数据分析服务 (Data Analysis Service)
```

## 服务功能

### 1. 设备监控服务
- 实时数据采集和分析
- 设备状态监控和预警
- 性能指标计算
- 异常检测和故障预测

### 2. 运维任务服务
- 智能工单分配
- 任务调度优化
- 资源调配建议
- 工作流自动化

### 3. 数据分析服务
- 运维数据统计分析
- 趋势预测和优化建议
- 成本效益分析
- 报表生成和可视化

## 部署方式

使用 Docker Compose 部署：

```bash
cd mcp-services
# 构建镜像
docker-compose build

# 启动服务
docker-compose up -d

# 查看服务状态
docker-compose logs -f
```

## API 集成

MCP 服务通过 HTTP API 与后端系统集成：

- 监控数据推送：`POST /api/mcp/monitoring/data`
- 任务调度请求：`POST /api/mcp/tasks/schedule`
- 分析报告生成：`POST /api/mcp/analysis/report`

## 配置说明

服务配置通过环境变量管理：

```bash
# 数据库配置
DATABASE_URL=postgresql://admin:admin123@postgres:5432/device_management

# Redis 配置
REDIS_URL=redis://redis:6379/0

# 服务端口
MCP_SERVICE_PORT=8080

# 日志级别
LOG_LEVEL=INFO
```