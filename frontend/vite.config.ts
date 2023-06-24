import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  server: {
    host: true,
    port: 80,
    proxy: {
      '/api': {
        target: 'http://localhost:8000'
      },
      '/media': {
        target: 'http://localhost:8000'
      },
      '/admin-extended': {
        target: 'http://localhost:8000'
      },
      '/static': {
        target: 'http://localhost:8000'
      }
    }
  },
  define: {
    __APP_VERSION__: JSON.stringify(process.env.npm_package_version)
  }
})
