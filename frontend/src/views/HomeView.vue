<script setup lang="ts">
import LoginCard from '@/components/LoginCard.vue'
import ManagerPage from '@/components/ManagerPage.vue'
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
    <div v-else>
      <div v-if="authStore.user.account_type === 2">
        <ManagerPage />
      </div>
    </div>
  </main>
</template>
