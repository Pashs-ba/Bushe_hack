<script setup lang="ts">
import LoginCard from '@/components/LoginCard.vue'
import { useAuthStore } from '@/stores/auth'

const authStore = useAuthStore()
</script>

<template>
  <main class="container mt-5">
    <div v-if="authStore.user === null">
      <div class="row justify-content-center">
        <LoginCard />
      </div>
    </div>
  </main>
</template>
