<script setup lang="ts">
import {useAuthStore} from '@/stores/auth'
import TelegramLoginWidget from './TelegramLoginWidget.vue'
import UserIcon from './UserIcon.vue'
import ButtonToContactManager from "@/components/ButtonToContactManager.vue";

const authStore = useAuthStore()
</script>

<template>
  <nav id="mainNavbar" class="navbar navbar-expand-md" data-bs-theme="dark">
    <div class="container">
      <RouterLink to="/" class="navbar-brand bushe-font d-flex align-items-center">
        <span class="ms-3 fs-3" id="brandName">буше</span>
      </RouterLink>

      <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarContent"
      >
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse justify-content-end" id="navbarContent">
        <div v-if="authStore.user" class="d-flex align-items-center">
          <div class="dropdown">
            <div data-bs-toggle="dropdown" class="d-flex flex-row align-items-center">
              <div class="me-2 fw-bold">{{ authStore.user.username }}</div>
              <UserIcon :user="authStore.user" size="40px"/>
            </div>

            <ul class="dropdown-menu">
              <li>
                <RouterLink class="dropdown-item" to="/profile">
                  <i class="bi-person me-2"></i>
                  <span>Мой аккаунт</span>
                </RouterLink>
              </li>
              <li>
                <a class="dropdown-item" href="#" @click.prevent="authStore.logoutAction">
                  <i class="bi-box-arrow-right me-2"></i>
                  <span>Выход</span>
                </a>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </nav>
</template>

<style scoped>
#mainNavbar {
  background-color: #161c23;
}

#brandName {
  line-height: 30px !important;
  text-align: center;
}

.userAvatar {
  border-radius: 20%;
}
</style>
