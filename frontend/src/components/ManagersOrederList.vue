<script setup lang="ts">
import {useOrdersStore} from "@/stores/orders";

const ordersStore = useOrdersStore()
</script>

<template>
  <div class="container align-self-center">
    <div style="width: 500px" class="list-group">
      <h1 class="align-self-center">
        Заказы
      </h1>
      <li v-for="item in ordersStore.ordersList" class="list-group-item list-group-item-action">
        {{ item.deliveryAddress }}
        <FormKit
            style="max-width:250px"
            v-model="item.status"
            type="select"
            name="orderStatus"
        >
          <option selected disabled hidden="true">{{ item.status }}</option>
          <option>в обработке</option>
          <option>собирается</option>
          <option>едет</option>
          <option>доставлен</option>
        </FormKit>
      </li>
    </div>
  </div>

</template>

<style scoped>

</style>