import React, { useState } from 'react'
import { Card, Table, Button, Space, Tag, Input, Select, Row, Col } from 'tdesign-react'

const MaintenanceOrders: React.FC = () => {
  const [orders, setOrders] = useState([
    {
      id: 1,
      orderNo: 'MO20240115001',
      deviceName: '生产设备A',
      type: '日常维护',
      priority: '高',
      status: '进行中',
      assignee: '张三',
      createTime: '2024-01-15 09:00',
      deadline: '2024-01-16 18:00'
    },
    {
      id: 2,
      orderNo: 'MO20240115002',
      deviceName: '检测设备B',
      type: '紧急维修',
      priority: '紧急',
      status: '待处理',
      assignee: '李四',
      createTime: '2024-01-15 08:30',
      deadline: '2024-01-15 12:00'
    }
  ])

  const columns = [
    { title: '工单号', colKey: 'orderNo' },
    { title: '设备名称', colKey: 'deviceName' },
    { title: '工单类型', colKey: 'type' },
    { 
      title: '优先级', 
      colKey: 'priority',
      cell: (row: any) => (
        <Tag 
          theme={row.priority === '紧急' ? 'danger' : row.priority === '高' ? 'warning' : 'primary'}
          variant="light"
        >
          {row.priority}
        </Tag>
      )
    },
    { 
      title: '状态', 
      colKey: 'status',
      cell: (row: any) => (
        <Tag 
          theme={row.status === '进行中' ? 'primary' : row.status === '已完成' ? 'success' : 'default'}
          variant="light"
        >
          {row.status}
        </Tag>
      )
    },
    { title: '负责人', colKey: 'assignee' },
    { title: '创建时间', colKey: 'createTime' },
    { title: '截止时间', colKey: 'deadline' },
    {
      title: '操作',
      colKey: 'operation',
      cell: (row: any) => (
        <Space>
          <Button theme="primary" variant="text" size="small">
            详情
          </Button>
          <Button theme="success" variant="text" size="small">
            处理
          </Button>
        </Space>
      )
    }
  ]

  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-bold text-gray-900">运维工单管理</h1>
      
      {/* 统计和操作栏 */}
      <Row gutter={16}>
        <Col span={6}>
          <Card>
            <div className="text-center">
              <div className="text-2xl font-bold text-blue-600">8</div>
              <div className="text-gray-600">进行中工单</div>
            </div>
          </Card>
        </Col>
        <Col span={6}>
          <Card>
            <div className="text-center">
              <div className="text-2xl font-bold text-red-600">3</div>
              <div className="text-gray-600">紧急工单</div>
            </div>
          </Card>
        </Col>
        <Col span={6}>
          <Card>
            <div className="text-center">
              <div className="text-2xl font-bold text-green-600">12</div>
              <div className="text-gray-600">已完成工单</div>
            </div>
          </Card>
        </Col>
        <Col span={6}>
          <Card>
            <div className="text-center">
              <div className="text-2xl font-bold text-orange-600">5</div>
              <div className="text-gray-600">待处理工单</div>
            </div>
          </Card>
        </Col>
      </Row>

      {/* 搜索和过滤 */}
      <Card>
        <Row gutter={16} align="middle">
          <Col span={6}>
            <Input placeholder="搜索工单号或设备名称" />
          </Col>
          <Col span={4}>
            <Select
              options={[
                { label: '全部状态', value: '' },
                { label: '待处理', value: '待处理' },
                { label: '进行中', value: '进行中' },
                { label: '已完成', value: '已完成' }
              ]}
            />
          </Col>
          <Col span={4}>
            <Select
              options={[
                { label: '全部优先级', value: '' },
                { label: '紧急', value: '紧急' },
                { label: '高', value: '高' },
                { label: '普通', value: '普通' }
              ]}
            />
          </Col>
          <Col flex="auto">
            <Space>
              <Button theme="primary">新建工单</Button>
              <Button variant="outline">导出报表</Button>
            </Space>
          </Col>
        </Row>
      </Card>

      {/* 工单列表 */}
      <Card>
        <Table
          data={orders}
          columns={columns}
          rowKey="id"
          size="medium"
          pagination={{
            defaultCurrent: 1,
            defaultPageSize: 10,
            total: orders.length
          }}
        />
      </Card>
    </div>
  )
}

export default MaintenanceOrders