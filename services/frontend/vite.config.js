import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// Vite configuration for the frontend app
export default defineConfig({
  plugins: [react()],
  server: {
    host: '0.0.0.0', // Allow external access
    port: 3000,
    watch: {
      usePolling: true, // Necessary for Docker environments
    },
  },
})
