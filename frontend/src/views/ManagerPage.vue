<script setup lang="ts">
import {ref} from 'vue'
import {useOrdersStore} from "@/stores/orders";
import ManagersOrederList from "@/components/ManagersOrederList.vue";

const statusOptions = ref([
  'в обработке',
  'собирается',
  'едет',
  'доставлен',
])

const ordersStore = useOrdersStore()

// ordersStore.addOrder({
//   orderId: '1',
//   restaurantId: '12312',
//   deliveryAddress: 'Ясная поляна',
//   status: 'доставлен'
// })
// ordersStore.addOrder({
//   orderId: '1',
//   restaurantId: '12312',
//   deliveryAddress: 'Приморский проспект',
//   status: 'в обработке'
// })

</script>

<template>
  <ManagersOrederList />
</template>

<style scoped>

</style>