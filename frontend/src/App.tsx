import React from 'react'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import { ConfigProvider } from 'tdesign-react'
import { Layout } from 'tdesign-react'
import { Space } from 'tdesign-react'
import zhCN from 'tdesign-react/es/locale/zh_CN'

// 导入组件
import Header from './components/layout/Header'
import Sidebar from './components/layout/Sidebar'
import Dashboard from './pages/Dashboard'
import DeviceManagement from './pages/DeviceManagement'
import MaintenanceOrders from './pages/MaintenanceOrders'
import UserManagement from './pages/UserManagement'
import Login from './pages/Login'

// 导入状态管理
import { AuthProvider } from './contexts/AuthContext'

const { Content } = Layout

function App() {
  return (
    <ConfigProvider locale={zhCN}>
      <AuthProvider>
        <Router>
          <div className="flex h-screen bg-gray-50">
            <Routes>
              <Route path="/login" element={<Login />} />
              <Route path="*" element={
                <div className="flex w-full">
                  <Sidebar />
                  <div className="flex-1 flex flex-col min-w-0">
                    <Header />
                    <Content className="flex-1 overflow-auto p-6">
                      <Routes>
                        <Route path="/" element={<Dashboard />} />
                        <Route path="/dashboard" element={<Dashboard />} />
                        <Route path="/devices" element={<DeviceManagement />} />
                        <Route path="/maintenance" element={<MaintenanceOrders />} />
                        <Route path="/users" element={<UserManagement />} />
                      </Routes>
                    </Content>
                  </div>
                </div>
              } />
            </Routes>
          </div>
        </Router>
      </AuthProvider>
    </ConfigProvider>
  )
}

export default App