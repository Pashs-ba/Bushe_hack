import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ManagerPage from "@/components/ManagerPage.vue";
import NewOrderPage from "@/components/NewOrderPage.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/manager',
      name: 'managers page',
      component: ManagerPage
    },
    {
      path: '/new-order',
      name: 'delivery club',
      component:NewOrderPage
    }
  ]
})

export default router
