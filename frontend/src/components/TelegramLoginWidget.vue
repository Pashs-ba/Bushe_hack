<template>
  <div ref="telegramRef" class="d-flex"></div>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue'

const telegramRef = ref<null | HTMLElement>(null)

const telegramBotName = import.meta.env.VITE_APP_TELEGRAM_BOT_NAME
const apiCallbackURL = import.meta.env.VITE_APP_TELEGRAM_AUTH_CALLBACK

onMounted(() => {
  const script = document.createElement('script')
  //   window.onTelegramAuth = onTelegramAuth
  script.async = true
  script.src = 'https://telegram.org/js/telegram-widget.js?3'
  script.setAttribute('data-size', 'medium')
  script.setAttribute('data-userpic', 'false')
  script.setAttribute('data-telegram-login', telegramBotName)
  script.setAttribute('data-request-access', 'read')
  script.setAttribute('data-auth-url', apiCallbackURL)
  script.setAttribute('data-radius', '6px')
  telegramRef.value?.appendChild(script)
})
</script>
