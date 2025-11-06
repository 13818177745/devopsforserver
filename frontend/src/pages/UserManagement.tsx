import React, { useState } from 'react'
import { Card, Table, Button, Space, Tag, Input, Select, Row, Col, Modal, Form, MessagePlugin } from 'tdesign-react'

const UserManagement: React.FC = () => {
  const [users, setUsers] = useState([
    {
      id: 1,
      username: 'admin',
      name: '系统管理员',
      role: '管理员',
      department: '信息技术部',
      status: '启用',
      lastLogin: '2024-01-15 09:00',
      createTime: '2024-01-01'
    },
    {
      id: 2,
      username: 'zhangsan',
      name: '张三',
      role: '运维工程师',
      department: '运维部',
      status: '启用',
      lastLogin: '2024-01-15 08:30',
      createTime: '2024-01-05'
    }
  ])

  const [isAddModalVisible, setIsAddModalVisible] = useState(false)

  const columns = [
    { title: '用户ID', colKey: 'id', width: 80 },
    { title: '用户名', colKey: 'username' },
    { title: '姓名', colKey: 'name' },
    { 
      title: '角色', 
      colKey: 'role',
      cell: (row: any) => (
        <Tag 
          theme={row.role === '管理员' ? 'danger' : 'primary'}
          variant="light"
        >
          {row.role}
        </Tag>
      )
    },
    { title: '部门', colKey: 'department' },
    { 
      title: '状态', 
      colKey: 'status',
      cell: (row: any) => (
        <Tag 
          theme={row.status === '启用' ? 'success' : 'default'}
          variant="light"
        >
          {row.status}
        </Tag>
      )
    },
    { title: '最后登录', colKey: 'lastLogin' },
    { title: '创建时间', colKey: 'createTime' },
    {
      title: '操作',
      colKey: 'operation',
      cell: (row: any) => (
        <Space>
          <Button theme="primary" variant="text" size="small">
            编辑
          </Button>
          <Button theme="danger" variant="text" size="small">
            禁用
          </Button>
        </Space>
      )
    }
  ]

  const handleAddUser = (formData: any) => {
    const newUser = {
      id: users.length + 1,
      ...formData,
      status: '启用',
      lastLogin: '从未登录',
      createTime: '2024-01-15'
    }
    setUsers([...users, newUser])
    setIsAddModalVisible(false)
    MessagePlugin.success('用户添加成功')
  }

  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-bold text-gray-900">用户管理</h1>
      
      {/* 搜索和操作栏 */}
      <Card>
        <Row gutter={16} align="middle">
          <Col span={6}>
            <Input placeholder="搜索用户名或姓名" />
          </Col>
          <Col span={4}>
            <Select
              options={[
                { label: '全部角色', value: '' },
                { label: '管理员', value: '管理员' },
                { label: '运维工程师', value: '运维工程师' },
                { label: '普通用户', value: '普通用户' }
              ]}
            />
          </Col>
          <Col flex="auto">
            <Space>
              <Button theme="primary" onClick={() => setIsAddModalVisible(true)}>
                添加用户
              </Button>
              <Button variant="outline">
                批量导入
              </Button>
            </Space>
          </Col>
        </Row>
      </Card>

      {/* 用户列表 */}
      <Card>
        <Table
          data={users}
          columns={columns}
          rowKey="id"
          size="medium"
          pagination={{
            defaultCurrent: 1,
            defaultPageSize: 10,
            total: users.length
          }}
        />
      </Card>

      {/* 添加用户模态框 */}
      <Modal
        header="添加用户"
        visible={isAddModalVisible}
        onClose={() => setIsAddModalVisible(false)}
        footer={null}
      >
        <Form onSubmit={handleAddUser} labelWidth={100}>
          <Form.FormItem label="用户名" name="username" required>
            <Input placeholder="请输入用户名" />
          </Form.FormItem>
          <Form.FormItem label="姓名" name="name" required>
            <Input placeholder="请输入真实姓名" />
          </Form.FormItem>
          <Form.FormItem label="角色" name="role" required>
            <Select
              options={[
                { label: '管理员', value: '管理员' },
                { label: '运维工程师', value: '运维工程师' },
                { label: '普通用户', value: '普通用户' }
              ]}
            />
          </Form.FormItem>
          <Form.FormItem label="部门" name="department">
            <Input placeholder="请输入部门" />
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

export default UserManagement