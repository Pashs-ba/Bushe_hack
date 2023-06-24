import {defineStore} from "pinia";
import {ref} from "vue";

export const useOrdersStore = defineStore('orders', () => {
    const ordersList = ref<Array<any>>([])

    function addOrder(order: any) {
        ordersList.value.push(order)
    }

    return {ordersList, addOrder}
})