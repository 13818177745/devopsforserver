import React, { useState } from 'react'
import { 
  Card, 
  Table, 
  Button, 
  Space, 
  Input, 
  Select, 
  Tag,
  Row,
  Col,
  Modal,
  Form,
  MessagePlugin
} from 'tdesign-react'

const DeviceManagement: React.FC = () => {
  const [devices, setDevices] = useState([
    {
      id: 1,
      name: '生产设备A',
      type: '生产设备',
      status: '在线',
      location: '车间A',
      lastMaintenance: '2024-01-10',
      nextMaintenance: '2024-02-10'
    },
    {
      id: 2,
      name: '检测设备B',
      type: '检测设备',
      status: '离线',
      location: '实验室',
      lastMaintenance: '2024-01-05',
      nextMaintenance: '2024-02-05'
    }
  ])

  const [searchValue, setSearchValue] = useState('')
  const [statusFilter, setStatusFilter] = useState('')
  const [isAddModalVisible, setIsAddModalVisible] = useState(false)

  const columns = [
    { title: '设备ID', colKey: 'id', width: 80 },
    { title: '设备名称', colKey: 'name' },
    { title: '设备类型', colKey: 'type' },
    { 
      title: '状态', 
      colKey: 'status',
      cell: (row: any) => (
        <Tag 
          theme={row.status === '在线' ? 'success' : 'danger'}
          variant="light"
        >
          {row.status}
        </Tag>
      )
    },
    { title: '位置', colKey: 'location' },
    { title: '上次维护', colKey: 'lastMaintenance' },
    { title: '下次维护', colKey: 'nextMaintenance' },
    {
      title: '操作',
      colKey: 'operation',
      cell: (row: any) => (
        <Space>
          <Button theme="primary" variant="text" size="small">
            编辑
          </Button>
          <Button theme="danger" variant="text" size="small">
            删除
          </Button>
        </Space>
      )
    }
  ]

  const handleAddDevice = (formData: any) => {
    const newDevice = {
      id: devices.length + 1,
      ...formData,
      lastMaintenance: '2024-01-15',
      nextMaintenance: '2024-02-15'
    }
    setDevices([...devices, newDevice])
    setIsAddModalVisible(false)
    MessagePlugin.success('设备添加成功')
  }

  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-bold text-gray-900">设备管理</h1>
      
      {/* 搜索和操作栏 */}
      <Card>
        <Row gutter={16} align="middle">
          <Col span={6}>
            <Input
              placeholder="搜索设备名称"
              value={searchValue}
              onChange={(value) => setSearchValue(value)}
            />
          </Col>
          <Col span={4}>
            <Select
              value={statusFilter}
              onChange={(value) => setStatusFilter(value)}
              options={[
                { label: '全部状态', value: '' },
                { label: '在线', value: '在线' },
                { label: '离线', value: '离线' }
              ]}
            />
          </Col>
          <Col flex="auto">
            <Space>
              <Button theme="primary" onClick={() => setIsAddModalVisible(true)}>
                添加设备
              </Button>
              <Button variant="outline">
                批量导入
              </Button>
            </Space>
          </Col>
        </Row>
      </Card>

      {/* 设备列表 */}
      <Card>
        <Table
          data={devices}
          columns={columns}
          rowKey="id"
          size="medium"
          pagination={{
            defaultCurrent: 1,
            defaultPageSize: 10,
            total: devices.length
          }}
        />
      </Card>

      {/* 添加设备模态框 */}
      <Modal
        header="添加设备"
        visible={isAddModalVisible}
        onClose={() => setIsAddModalVisible(false)}
        footer={null}
      >
        <Form onSubmit={handleAddDevice} labelWidth={100}>
          <Form.FormItem label="设备名称" name="name">
            <Input placeholder="请输入设备名称" />
          </Form.FormItem>
          <Form.FormItem label="设备类型" name="type">
            <Select
              options={[
                { label: '生产设备', value: '生产设备' },
                { label: '检测设备', value: '检测设备' },
                { label: '辅助设备', value: '辅助设备' }
              ]}
            />
          </Form.FormItem>
          <Form.FormItem label="位置" name="location">
            <Input placeholder="请输入设备位置" />
          </Form.FormItem>
          <Form.FormItem>
            <Space>
              <Button theme="primary" type="submit">确认</Button>
              <Button variant="outline" onClick={() => setIsAddModalVisible(false)}>取消</Button>
            </Space>
          </Form.FormItem>
        </Form>
      </Modal>
    </div>
  )
}

export default DeviceManagement