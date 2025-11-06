import React from 'react'
import { Menu, MenuItem } from 'tdesign-react'
import { 
  DashboardIcon, 
  DeviceIcon, 
  MaintenanceIcon, 
  UserIcon,
  SettingsIcon 
} from 'tdesign-icons-react'
import { useNavigate, useLocation } from 'react-router-dom'

const Sidebar: React.FC = () => {
  const navigate = useNavigate()
  const location = useLocation()

  const menuItems = [
    {
      value: '/dashboard',
      label: '仪表板',
      icon: <DashboardIcon />
    },
    {
      value: '/devices',
      label: '设备管理',
      icon: <DeviceIcon />
    },
    {
      value: '/maintenance',
      label: '运维工单',
      icon: <MaintenanceIcon />
    },
    {
      value: '/users',
      label: '用户管理',
      icon: <UserIcon />
    },
    {
      value: '/settings',
      label: '系统设置',
      icon: <SettingsIcon />
    }
  ]

  const handleMenuClick = (value: string) => {
    navigate(value)
  }

  return (
    <aside className="w-64 bg-white shadow-lg h-full">
      <div className="p-4 border-b border-gray-200">
        <div className="flex items-center space-x-3">
          <div className="w-10 h-10 bg-gradient-to-r from-blue-500 to-blue-600 rounded-lg flex items-center justify-center">
            <span className="text-white font-bold text-lg">E</span>
          </div>
          <div>
            <h2 className="text-lg font-semibold text-gray-800">运维系统</h2>
            <p className="text-xs text-gray-500">Equipment Ops</p>
          </div>
        </div>
      </div>
      
      <nav className="p-4">
        <Menu
          value={location.pathname}
          onChange={handleMenuClick}
          theme="light"
          width="100%"
        >
          {menuItems.map((item) => (
            <MenuItem 
              key={item.value} 
              value={item.value}
              icon={item.icon}
            >
              {item.label}
            </MenuItem>
          ))}
        </Menu>
      </nav>
      
      <div className="absolute bottom-0 left-0 right-0 p-4 border-t border-gray-200">
        <div className="flex items-center space-x-3 p-3 bg-gray-50 rounded-lg">
          <div className="w-8 h-8 bg-blue-100 rounded-full flex items-center justify-center">
            <span className="text-blue-600 text-sm font-medium">A</span>
          </div>
          <div className="flex-1 min-w-0">
            <p className="text-sm font-medium text-gray-800 truncate">系统管理员</p>
            <p className="text-xs text-gray-500 truncate">管理员</p>
          </div>
        </div>
      </div>
    </aside>
  )
}

export default Sidebar