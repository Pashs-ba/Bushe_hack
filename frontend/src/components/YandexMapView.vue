<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { loadYmap } from 'vue-yandex-maps'

const settings = {
  apiKey: '3b3ca92b-d69c-4721-baa1-32f8606be7e7',
  lang: 'ru_RU',
  coordorder: 'latlong',
  debug: true,
  version: '2.1'
}

const isLoading = ref<boolean>(true)

interface Props {
  orders?: string[]
  avoidTrafficJams?: boolean
}

export interface RouteInfo {
  duration: string
  durationInTraffic: string
  distance: string
}

const props = withDefaults(defineProps<Props>(), {
  orders: () => [],
  avoidTrafficJams: false
})

const emit = defineEmits<{
  (e: 'update', value: RouteInfo): void
}>()

onMounted(async () => {
  if (!props.orders.length) return

  await loadYmap(settings)

  let map_instance = new ymaps.Map('map', {
    center: [59.950347, 30.315766],
    zoom: 12,
    controls: ['fullscreenControl', 'zoomControl']
  })

  let multiRoute = new ymaps.multiRouter.MultiRoute(
    {
      referencePoints: props.orders,
      params: {
        avoidTrafficJams: props.avoidTrafficJams
      }
    },
    {
      boundsAutoApply: true
    }
  )

  multiRoute.events.once('update', () => {
    const curRouteData = multiRoute.getActiveRoute().properties.getAll()
    isLoading.value = false
    emit('update', {
      distance: curRouteData.distance.text,
      duration: curRouteData.duration.text,
      durationInTraffic: curRouteData.durationInTraffic.text
    })
  })

  map_instance.geoObjects.add(multiRoute)
})
</script>

<template>
  <div
    v-if="!props.orders.length"
    class="card card-body w-100 d-flex justify-content-center align-items-center"
    style="height: 450px"
  >
    Укажите точки, через которые должен идти маршрут
  </div>
  <div v-else class="position-relative">
    <div id="map" class="w-100" style="height: 450px"></div>
    <div v-if="isLoading" class="position-absolute top-0 w-100" style="height: 450px">
      <div class="d-flex justify-content-center align-items-center border rounded w-100 h-100 bg-dark">
        <div class="spinner-border text-light" role="status">
          <span class="visually-hidden">Loading...</span>
        </div>
      </div>
    </div>
  </div>
</template>

<style>
.yandex-container {
  height: 450px;
}
</style>
