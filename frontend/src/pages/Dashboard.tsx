import React, { useState, useEffect } from 'react'
import { Card, Space, Statistic, Table, Row, Col } from 'tdesign-react'
import { Icon } from 'tdesign-react'

const Dashboard: React.FC = () => {
  const [stats, setStats] = useState({
    totalDevices: 0,
    onlineDevices: 0,
    maintenanceOrders: 0,
    criticalAlerts: 0
  })

  const [recentOrders, setRecentOrders] = useState([])

  useEffect(() => {
    // 模拟数据获取
    setStats({
      totalDevices: 156,
      onlineDevices: 142,
      maintenanceOrders: 8,
      criticalAlerts: 3
    })

    setRecentOrders([
      {
        id: 1,
        deviceName: '生产设备A',
        type: '日常维护',
        status: '进行中',
        assignee: '张三',
        createTime: '2024-01-15 09:00'
      },
      {
        id: 2,
        deviceName: '检测设备B',
        type: '紧急维修',
        status: '待处理',
        assignee: '李四',
        createTime: '2024-01-15 08:30'
      }
    ])
  }, [])

  const columns = [
    { title: '工单ID', colKey: 'id' },
    { title: '设备名称', colKey: 'deviceName' },
    { title: '工单类型', colKey: 'type' },
    { title: '状态', colKey: 'status' },
    { title: '负责人', colKey: 'assignee' },
    { title: '创建时间', colKey: 'createTime' }
  ]

  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-bold text-gray-900">设备运维监控看板</h1>
      
      {/* 统计卡片 */}
      <Row gutter={16}>
        <Col span={6}>
          <Card>
            <Statistic
              title="总设备数"
              value={stats.totalDevices}
              prefix={<Icon name="app" />}
              valueStyle={{ color: '#3b82f6' }}
            />
          </Card>
        </Col>
        <Col span={6}>
          <Card>
            <Statistic
              title="在线设备"
              value={stats.onlineDevices}
              prefix={<Icon name="check-circle" />}
              valueStyle={{ color: '#10b981' }}
            />
          </Card>
        </Col>
        <Col span={6}>
          <Card>
            <Statistic
              title="运维工单"
              value={stats.maintenanceOrders}
              prefix={<Icon name="file" />}
              valueStyle={{ color: '#f59e0b' }}
            />
          </Card>
        </Col>
        <Col span={6}>
          <Card>
            <Statistic
              title="紧急告警"
              value={stats.criticalAlerts}
              prefix={<Icon name="error-circle" />}
              valueStyle={{ color: '#ef4444' }}
            />
          </Card>
        </Col>
      </Row>

      {/* 最近工单 */}
      <Card title="最近运维工单">
        <Table
          data={recentOrders}
          columns={columns}
          rowKey="id"
          size="medium"
        />
      </Card>
    </div>
  )
}

export default Dashboard