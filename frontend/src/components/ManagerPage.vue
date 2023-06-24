<script setup lang="ts">
import {ref} from 'vue'
import {useOrdersStore} from "@/stores/orders";

const statusOptions = ref([
  'в обработке',
  'собирается',
  'едет',
  'доставлен',
])

const ordersStore = useOrdersStore()

ordersStore.addOrder({
  orderId: '1',
  restaurantId: '12312',
  deliveryAddress: 'Ясная поляна',
  status: 'доставлен'
})
ordersStore.addOrder({
  orderId: '1',
  restaurantId: '12312',
  deliveryAddress: 'Приморский проспект',
  status: 'в обработке'
})
const items = ref([{
  orderId: '1',
  restaurantId: '12312',
  deliveryAddress: 'Ясная поляна',
  status: 'доставлен'
},
  {
    orderId: '1',
    restaurantId: '12312',
    deliveryAddress: 'Приморский проспект',
    status: 'в обработке'
  },
  {
    orderId: '1',
    restaurantId: '12312',
    deliveryAddress: 'Приморский проспект',
    status: 'в обработке'
  },
  {
    orderId: '1',
    restaurantId: '12312',
    deliveryAddress: 'Приморский проспект',
    status: 'в обработке'
  },
  {
    orderId: '1',
    restaurantId: '12312',
    deliveryAddress: 'Приморский проспект',
    status: 'в обработке'
  },
  {
    orderId: '1',
    restaurantId: '12312',
    deliveryAddress: 'Приморский проспект',
    status: 'в обработке'
  }])
</script>

<template>
  <div class="list-group">
    <h>
      Заказы
    </h>
    <li v-for="item in ordersStore.ordersList" class="list-group-item list-group-item-action">
      {{ item.deliveryAddress}}
      <FormKit
          style="max-width:250px;"
          v-model="item.status"
          type="select"
          name="orderStatus"
      >
        <option selected disabled hidden="true">{{item.status}}</option>
        <option>в обработке</option>
        <option>собирается</option>
        <option>едет</option>
        <option>доставлен</option>
      </FormKit>
      <!--      <select class="custom-select" size="1"  v-model="item.status">-->
      <!--      <option selected>{{item.status}}</option>-->
<!--            <option>в обработке</option>-->
<!--            <option>собирается</option>-->
<!--            <option>едет</option>-->
<!--            <option>доставлен</option>-->
      <!--      <option></option>-->
      <!--    </select>-->
      <!--      {{item.status}}-->
    </li>
  </div>
</template>

<style scoped>

</style>