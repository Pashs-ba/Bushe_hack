<script setup lang="ts">
import CurrentRouteInfo from '@/components/CurrentRouteInfo.vue'
import YandexMapView, { type RouteInfo } from '@/components/YandexMapView.vue'
import { ref } from 'vue'

const orders = ['Санкт-Петербург, Площадь Льва Толстого 1-3', 'Большой проспект П.С., 44']

const currentRoute = ref<RouteInfo | null>(null)
</script>

<template>
  <div class="container mt-5">
    <h2 class="mb-3">Сбор доставки</h2>
    <YandexMapView :orders="orders" @update="(val) => (currentRoute = val)" />
    <CurrentRouteInfo :route="currentRoute" />
  </div>
</template>
