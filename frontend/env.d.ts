/// <reference types="vite/client" />
interface ImportMetaEnv {
  VITE_APP_TELEGRAM_BOT_TOKEN: string
  VITE_APP_TELEGRAM_BOT_NAME: string
  VITE_APP_TELEGRAM_AUTH_CALLBACK_URL: string
}

declare const __APP_VERSION__: string
