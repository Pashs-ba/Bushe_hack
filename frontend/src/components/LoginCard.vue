<template>
  <div class="col-12 col-md-6 col-lg-4">
    <div class="card card-body d-flex align-items-center">
      <h5 class="card-title text-center mb-4">Войти</h5>
      <TelegramLoginWidget />
    </div>
  </div>
</template>

<script setup lang="ts">
import TelegramLoginWidget from './TelegramLoginWidget.vue'
</script>
