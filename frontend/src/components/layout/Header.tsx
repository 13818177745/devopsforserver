import React from 'react'
import { useAuth } from '../../contexts/AuthContext'
import { Dropdown, Avatar, Space, Badge, Button } from 'tdesign-react'
import { BellIcon, UserIcon, LogoutIcon } from 'tdesign-icons-react'
import { useNavigate } from 'react-router-dom'

const Header: React.FC = () => {
  const { user, logout } = useAuth()
  const navigate = useNavigate()

  const handleLogout = () => {
    logout()
    navigate('/login')
  }

  const handleProfile = () => {
    // 跳转到个人资料页面
    console.log('Navigate to profile')
  }

  const dropdownOptions = [
    {
      content: '个人资料',
      value: 'profile',
      prefixIcon: <UserIcon />,
      onClick: handleProfile
    },
    {
      content: '退出登录',
      value: 'logout',
      prefixIcon: <LogoutIcon />,
      onClick: handleLogout
    }
  ]

  return (
    <header className="h-16 bg-white shadow-sm border-b border-gray-200 px-6 flex items-center justify-between">
      <div className="flex items-center">
        <h1 className="text-xl font-semibold text-gray-800">设备运维管理系统</h1>
      </div>
      
      <div className="flex items-center space-x-4">
        {/* 通知铃铛 */}
        <Badge count={3} dot={false}>
          <Button variant="text" shape="circle">
            <BellIcon />
          </Button>
        </Badge>
        
        {/* 用户信息 */}
        <Dropdown trigger="click" options={dropdownOptions}>
          <Space className="cursor-pointer px-3 py-2 rounded-lg hover:bg-gray-100 transition-colors">
            <Avatar size="medium" shape="circle">
              {user?.fullName?.charAt(0) || 'U'}
            </Avatar>
            <div className="flex flex-col items-start">
              <span className="text-sm font-medium text-gray-800">{user?.fullName || '用户'}</span>
              <span className="text-xs text-gray-500">{user?.role === 'admin' ? '管理员' : '操作员'}</span>
            </div>
          </Space>
        </Dropdown>
      </div>
    </header>
  )
}

export default Header