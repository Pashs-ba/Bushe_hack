<script setup lang="ts">
import type { RouteInfo } from './YandexMapView.vue'

defineProps<{ route: RouteInfo | null }>()
</script>

<template>
  <div class="mt-4">
    <h5 class="mb-3">Информация о маршруте</h5>

    <div v-if="route !== null">
      <div class="row">
        <div class="col-12 col-md-4 infocard mb-3 mb-md-0">
          <div class="card card-body h-100">
            <div class="fw-bold fs-2">{{ route.distance }}</div>
            <div class="text-muted">Длина пути</div>
          </div>
        </div>

        <div class="col-12 col-md-4 infocard mb-3 mb-md-0">
          <div class="card card-body h-100">
            <div class="fw-bold fs-2">{{ route.duration }}</div>
            <div class="text-muted">Время в пути</div>
          </div>
        </div>

        <div class="col-12 col-md-4 infocard mb-3 mb-md-0">
          <div class="card card-body h-100">
            <div class="fw-bold fs-2">{{ route.durationInTraffic }}</div>
            <div class="text-muted">Учитывая пробки</div>
          </div>
        </div>
      </div>
    </div>
    <div v-else class="w-100 d-flex justify-content-center align-items-center">
      <div class="spinner-border" role="status">
        <span class="visually-hidden">Loading...</span>
      </div>
    </div>
  </div>
</template>

<style scoped>
.infocard:nth-child(1) > .card {
  background-color: #01c29a !important;
}

.infocard:nth-child(2) > .card {
  background-color: #c89afe !important;
}

.infocard:nth-child(3) > .card {
  background-color: #f8fd99 !important;
}

.infocard > .card {
  --bs-card-color: rgba(0, 0, 0, 0.831) !important;
  --bs-secondary-color: rgba(0, 0, 0, 0.649) !important;
}
</style>
