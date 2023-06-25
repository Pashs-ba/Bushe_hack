<script setup lang="ts">
import {onMounted, ref} from 'vue';
import {useOrdersStore} from "@/stores/orders";
import {setErrors} from "@formkit/vue";


const orders = useOrdersStore();

const curOrder = ref({
  orderId: '',
  restaurantId: '',
  deliveryAddress: '',
  status: 'в обработке'
})

onMounted(() => {
  setErrors('order-form', ['  '], {
    order_address_input: 'адрес не может быть пустым.',
  })
})

function submit(formData, node) {

  node.clearErrors()

  orders.addOrder(curOrder.value);
}

</script>p

<template>
  <div>
    <FormKit
        type="checkbox"
        label="меню"
        :options="[
    {
      value: '1',
      label: 'продукт 1',
    },
    {
      value: '2',
      label: 'продукт 2',
    },
    {
      value: '3',
      label: 'продукт 3',
    },
    {
      value: '4',
      label: 'продукт 4',
    }
  ]"
        help=""
    />
    <form-kit
        name="order_address_input"
        label="адрес доставки"
        v-model="curOrder.deliveryAddress"
    />
    <form-kit
        id="order-form"
        type="form"
        @submit="submit"
    />
  </div>
</template>

<style scoped>

</style>