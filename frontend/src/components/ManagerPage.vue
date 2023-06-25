<script setup lang="ts">
import { type Order, listOrders } from '@/api/services/orders'
import { ref } from 'vue'
import { onMounted } from 'vue'
import { type Paginator } from '@/api'

const orders = ref<Paginator<Order> | null>(null)

const selectedOrders = ref<Order[]>([])

onMounted(() => {
  listOrders().then((d) => (orders.value = d.data))
})

const alterSelected = (order: Order) => {
  const ind = selectedOrders.value.findIndex((val) => val.id === order.id)
  if (ind !== -1) selectedOrders.value.splice(ind, 1)
  else selectedOrders.value.push(order)
}
</script>

<template>
  <div class="container mt-4">
    <div class="mb-3">
      <RouterLink to="/compose" class="btn btn-outline-success">Собрать заказ</RouterLink>
    </div>
    <table class="table table-bordered table-dark">
      <thead>
        <tr>
          <th></th>
          <th>ID заказа</th>
          <th>Адрес</th>
          <th>Ожидаемое время</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="order in orders?.results" :key="order.id">
          <td>
            <div class="d-flex justify-content-center align-items-center w-100 h-100">
              <input
                type="checkbox"
                class="form-check-input"
                :checked="selectedOrders.findIndex((val) => val.id === order.id) !== -1"
                @click="alterSelected(order)"
              />
            </div>
          </td>
          <td>{{ order.id }}</td>
          <td>{{ order.end_point }}</td>
          <td>
            {{
              new Date(order.expected_time).toLocaleString(undefined, {
                day: '2-digit',
                month: 'short',
                hour: 'numeric',
                minute: '2-digit'
              })
            }}
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<style scoped></style>
