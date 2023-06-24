<template>
  <div ref="telegramRef" class="d-flex"></div>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { createUser } from '@/api/services/auth'

export interface TelegramUserData {
  auth_date: number
  first_name: string
  hash: string
  id: number
  last_name?: string
  username: string
  photo_url?: string
}

const telegramRef = ref<null | HTMLElement>(null)

declare global {
  interface Window {
    onTelegramAuth: (data: TelegramUserData) => void
  }
}

const telegramBotName = import.meta.env.VITE_APP_TELEGRAM_BOT_NAME
const apiCallbackURL = import.meta.env.VITE_APP_TELEGRAM_AUTH_CALLBACK_URL

onMounted(() => {
  const script = document.createElement('script')
  window.onTelegramAuth = onTelegramAuth
  script.async = true
  script.src = 'https://telegram.org/js/telegram-widget.js?3'
  script.setAttribute('data-size', 'medium')
  script.setAttribute('data-userpic', 'false')
  script.setAttribute('data-telegram-login', telegramBotName)
  script.setAttribute('data-request-access', 'read')
  script.setAttribute('data-onauth', 'onTelegramAuth(user)')
  script.setAttribute('data-radius', '6px')
  telegramRef.value?.appendChild(script)
})

const onTelegramAuth = (data: TelegramUserData) => {
  createUser(data)
}
</script>
