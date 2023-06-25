<script setup lang="ts">
import CurrentRouteInfo from '@/components/CurrentRouteInfo.vue'
import LoginCard from '@/components/LoginCard.vue'
import YandexMapView, { type RouteInfo } from '@/components/YandexMapView.vue'
import { useAuthStore } from '@/stores/auth'
import { ref } from 'vue'

const authStore = useAuthStore()

const orders = ['Большой проспект П.С., 44', 'Большой проспект В.О., 20']

const currentRoute = ref<RouteInfo | null>(null)
</script>

<template>
  <main class="container mt-5">
    <div v-if="authStore.user === null">
      <div class="row justify-content-center">
        <LoginCard />
      </div>
    </div>
    <div v-else>
      <YandexMapView :orders="orders" @update="(val) => (currentRoute = val)" />
      <CurrentRouteInfo :route="currentRoute" />
    </div>
  </main>
</template>
