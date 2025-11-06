import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import { resolve } from 'path'

export default defineConfig({
  plugins: [react()],
  server: {
    host: '0.0.0.0',
    allowedHosts: true,
    port: 3000
  },
  build: {
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html')
      }
    }
  },
  resolve: {
    alias: {
      '@': resolve(__dirname, './src')
    }
  },
  css: {
    preprocessorOptions: {
      less: {
        modifyVars: {
          '@primary-color': '#0052d9',
          '@success-color': '#00a870',
          '@warning-color': '#ed7b2f',
          '@error-color': '#e34d59',
          '@btn-height-default': '40px',
          '@border-radius': '6px'
        },
        javascriptEnabled: true
      }
    }
  }
})