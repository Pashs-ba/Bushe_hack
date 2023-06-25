<template>
    <div class="container my-3 p-3 border rounded" v-if="orders.length > 0">
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
                    <div class="fw-bold fs-2">{{ new Date(orders[0].expected_time).toTimeString().slice(0, 5) }}</div>
                    <div class="text-muted">Время к которому надо доставить</div>
                </div>
            </div>
            <div class="col-12 infocard col-md-4 mb-3 mb-md-0">
                <div class="card card-body h-100">
                    <div class="fw-bold fs-2"><a href="#"
                            class="link-body-emphasis link-offset-2 link-underline-opacity-25 link-underline-opacity-75-hover"
                            @click="openMap(orders[0].end_point)">Открыть карту</a></div>
                </div>
            </div>
        </div>

        <div v-if="orders[0].comments">
            <h3>Коментарии клиента</h3>
            <p>{{ orders[0].comments }}</p>
        </div>
        <div class="text-center">

            <button class="btn btn-success me-5 mt-3 btn-lg" @click="sucsess_order(orders[0])">Заказ отдан</button>
            <button class="btn btn-danger btn-lg mt-3" @click="">Проблемы с заказом</button>
        </div>

    </div>
    <div v-else>
        <div class="container text-center mt-5">
            <h3>Заказов пока нет</h3>
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
                    <td>{{ new Date(order.expected_time).toTimeString().slice(0, 5) }}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>
<script setup lang="ts">
import router from '@/router';
import { useAuthStore } from '@/stores/auth';
import axios from 'axios';
import { ref } from 'vue';
import { routeLocationKey } from 'vue-router';

const authStore = useAuthStore()

const updateOrders = () => {
    axios.get("api/orders").then((res) => {
        console.log(res.data.results)
        orders.value = res.data.results.filter((el: any) => el.delivery_man_id === user.id && el.status === 4).sort((el1: any, el2: any) => el1.number_in_queue - el2.number_in_queue) // Get all orders for deliver
        if (orders.value.length === 0) {
            axios.get("api/delivery_mans").then((res) => {
                let deliver_id = res.data.results.filter((el: any) => el.user === user.id)[0].user
                axios.patch("api/delivery_mans/" + deliver_id).then((res) => {
                    status: 1
                })
            })

        }
    })

}

const sucsess_order = (order: any) => {
    axios.patch("api/orders/" + order.id, {
        status: 5
    })
    updateOrders()
}
const bad_order = (order: any) => {
    axios.patch("api/orders/" + order.id, {
        status: 5
    })
    updateOrders()
}


const openMap = (address: string) => {
    const settings = {
        apiKey: '3b3ca92b-d69c-4721-baa1-32f8606be7e7',
        lang: 'ru_RU',
        coordorder: 'latlong',
        debug: true,
        version: '2.1'
    }
    // console.log("http://geocode-maps.yandex.ru/1.x/?apikey="+settings.apiKey+"&format=json&geocode="+address)
    axios.get("http://geocode-maps.yandex.ru/1.x/?apikey=" + settings.apiKey + "&format=json&geocode=" + address).then((res) => {
        const coords = res.data.response.GeoObjectCollection.featureMember[0].GeoObject.Point.pos.split(" ");
        window.location.href = "https://yandex.ru/maps/?rtext=~" + coords[1] + "," + coords[0];
    })

}
const GetUser = () => { // replace to real get user
    const user = authStore.user //TODO fix
    return {
        id: 1
    }
}
const user = GetUser()
const orders = ref()
updateOrders()


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