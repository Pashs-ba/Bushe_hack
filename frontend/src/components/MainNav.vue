<script setup lang="ts">
import TelegramLoginWidget from '@/components/TelegramLoginWidget.vue'
import { useAuthStore } from '@/stores/auth'
import UserIcon from './UserIcon.vue'

const authStore = useAuthStore()
</script>

<template>
  <nav id="mainNavbar" class="navbar py-2" data-bs-theme="dark">
    <div class="container">
      <RouterLink to="/" class="navbar-brand d-flex align-items-center">
        <img src="@/assets/images/logo/logo.png" height="30" />
        <!-- <div class="ms-3 text-gothic fs-3" id="brandName">u n i t y</div> -->
      </RouterLink>

      <div v-if="authStore.user === null" class="d-flex" id="login-widget-wrapper">
        <TelegramLoginWidget />
      </div>
      <div v-else class="d-flex align-items-center">
        <div class="dropdown">
          <div data-bs-toggle="dropdown" class="d-flex flex-row align-items-center">
            <div class="me-2 fw-bold">{{ authStore.user.username }}</div>
            <UserIcon :user="authStore.user" size="40px" />
          </div>

          <ul class="dropdown-menu">
            <li>
              <RouterLink class="dropdown-item" to="/profile">
                <i class="bi-person me-2"></i>
                <span>My profile</span>
              </RouterLink>
            </li>
            <li>
              <a class="dropdown-item" href="#" @click.prevent="authStore.logout">
                <i class="bi-box-arrow-right me-2"></i>
                <span>Log out</span>
              </a>
            </li>
          </ul>
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
