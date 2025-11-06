import React, { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { useAuth } from '../contexts/AuthContext'
import { Card, Form, Input, Button, Message, Space } from 'tdesign-react'
import { UserIcon, LockIcon } from 'tdesign-icons-react'

const Login: React.FC = () => {
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')
  const [loading, setLoading] = useState(false)
  const { login } = useAuth()
  const navigate = useNavigate()

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    
    if (!username || !password) {
      Message.error('请输入用户名和密码')
      return
    }

    setLoading(true)
    try {
      const success = await login(username, password)
      if (success) {
        Message.success('登录成功')
        navigate('/dashboard')
      } else {
        Message.error('用户名或密码错误')
      }
    } catch (error) {
      Message.error('登录失败，请稍后重试')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-blue-50 to-indigo-100">
      <Card className="w-full max-w-md shadow-xl" bordered={false}>
        <div className="text-center mb-8">
          <div className="w-20 h-20 bg-gradient-to-r from-blue-500 to-blue-600 rounded-full flex items-center justify-center mx-auto mb-4">
            <span className="text-white text-2xl font-bold">E</span>
          </div>
          <h1 className="text-2xl font-bold text-gray-800">设备运维管理系统</h1>
          <p className="text-gray-600 mt-2">请输入您的账号信息</p>
        </div>

        <Form onSubmit={handleSubmit}>
          <Space direction="vertical" size="large" className="w-full">
            <Form.Item 
              name="username" 
              label="用户名"
              rules={[{ required: true, message: '请输入用户名' }]}
            >
              <Input
                prefixIcon={<UserIcon />}
                placeholder="请输入用户名"
                value={username}
                onChange={(value) => setUsername(value)}
                size="large"
              />
            </Form.Item>

            <Form.Item 
              name="password" 
              label="密码"
              rules={[{ required: true, message: '请输入密码' }]}
            >
              <Input
                type="password"
                prefixIcon={<LockIcon />}
                placeholder="请输入密码"
                value={password}
                onChange={(value) => setPassword(value)}
                size="large"
              />
            </Form.Item>

            <Button
              type="submit"
              theme="primary"
              size="large"
              loading={loading}
              block
            >
              登录
            </Button>
          </Space>
        </Form>

        <div className="mt-6 text-center text-sm text-gray-500">
          <p>默认账号：admin / admin123</p>
        </div>
      </Card>
    </div>
  )
}

export default Login