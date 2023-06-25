<template>
    <div class="container my-3 p-3 border rounded">
        <h3>Текущий заказ</h3>
        <div class="row mb-3">
            <div class="col-12 col-md-4 infocard mb-3 mb-md-0">
                <div class="card card-body h-100">
                    <div class="fw-bold fs-2">{{ orders[0].end_point }}</div>
                    <div class="text-muted">Адресс доставки</div>
                </div>
            </div>
            <div class="col-12 col-md-4 infocard mb-3 mb-md-0">
                <div class="card card-body h-100">
                    <div class="fw-bold fs-2">{{ new Date(orders[0].end_delivery_time).toTimeString().slice(0, 5) }}</div>
                    <div class="text-muted">Время к которому надо доставить</div>
                </div>
            </div>
            <div class="col-12 infocard col-md-4 mb-3 mb-md-0">
                <div class="card card-body h-100">
                    <div class="fw-bold fs-2"><a href="#" class="link-body-emphasis link-offset-2 link-underline-opacity-25 link-underline-opacity-75-hover">Открыть карту</a></div>
                </div>
            </div>
        </div>
        <div v-if="orders[0].comment">
            <h3>Коментарии клиента</h3>
            <p>{{ orders[0].comment }}</p>
        </div>
    </div>
    <div class="container my-3 p-3 border rounded" v-if="orders.slice(1).length > 0">
        <table class="table">
            <thead>
                <tr>
                    <th scope="col">#</th>
                    <th scope="col">Куда</th>
                    <th scope="col">Ожидаемое время</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="order in orders.slice(1)">
                    <th scope="row">{{ order.number_in_queue }}</th>
                    <td>{{ order.end_point }}</td>
                    <td>{{ order.end_delivery_time }}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>
<script setup lang="ts">
import axios from 'axios';
import { ref } from 'vue';

const GetUser = () => { // replace to real get user
    return {
        id: 1
    }
}
const user = GetUser()
const orders = ref()
axios.get("api/orders").then((res) => {
    orders.value = res.data.results.filter((el: any) => el.delivery_man_id === user.id).sort((el1: any, el2: any) => el1.number_in_queue - el2.number_in_queue) // Get all orders for deliver
})

</script>
<style scoped>
.infocard:nth-child(1)>.card {
    background-color: #01c29a !important;
}

.infocard:nth-child(2)>.card {
    background-color: #c89afe !important;
}

.infocard:nth-child(3)>.card {
    background-color: #f8fd99 !important;
}

.infocard>.card {
    --bs-card-color: rgba(0, 0, 0, 0.831) !important;
    --bs-secondary-color: rgba(0, 0, 0, 0.649) !important;
}
</style>