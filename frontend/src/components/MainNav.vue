<script setup lang="ts">
import TelegramLoginWidget from './TelegramLoginWidget.vue'
import UserIcon from './UserIcon.vue'

// const authStore = useAuthStore()
</script>

<template>
  <nav id="mainNavbar" class="navbar navbar-expand-lg bg-body-tertiary" data-bs-theme="dark">
    <div class="container-fluid">
      <RouterLink to="/" class="navbar-brand d-flex align-items-center">
        <div class="ms-3 text-gothic fs-3" id="brandName">буше</div>
      </RouterLink>


<!--      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"-->
<!--              aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">-->
<!--        <span class="navbar-toggler-icon"></span>-->
<!--      </button>-->
      <div class="collapse navbar-collapse" id="navbarNav">
        <RouterLink to="/" class="navbar-brand d-flex align-items-center">
          <div class="ms-3 text-gothic fs-5" id="new-order">Новый заказ</div>
        </RouterLink>
      </div>
    </div>
  </nav>
  <!--  <nav id="mainNavbar" class="navbar py-2" data-bs-theme="dark">-->
  <!--    <div class="container">-->
  <!--      <RouterLink to="/" class="navbar-brand d-flex align-items-center">-->
  <!--        Буше-->
  <!--        &lt;!&ndash; <div class="ms-3 text-gothic fs-3" id="brandName">u n i t y</div> &ndash;&gt;-->
  <!--      </RouterLink>-->

  <!--      <a herf = "https://yandex.ru/maps/2/saint-petersburg/chain/bushe/3270467278/filter/chain_id/3270467278/?ll=30.325709%2C59.962208&sll=30.313536%2C59.965572&sspn=0.180588%2C0.054049&z=12">map</a>-->

  <!--      <div class="d-flex" id="login-widget-wrapper">-->
  <!--        <TelegramLoginWidget/>-->
  <!--      </div>-->
  <!--&lt;!&ndash;            <div v-else class="d-flex align-items-center">&ndash;&gt;-->
  <!--&lt;!&ndash;              <div class="dropdown">&ndash;&gt;-->
  <!--&lt;!&ndash;                <div data-bs-toggle="dropdown" class="d-flex flex-row align-items-center">&ndash;&gt;-->
  <!--&lt;!&ndash;                  <div class="me-2 fw-bold">{{ authStore.user.username }}</div>&ndash;&gt;-->
  <!--&lt;!&ndash;                  <UserIcon :user="authStore.user" size="40px" />&ndash;&gt;-->
  <!--&lt;!&ndash;                </div>&ndash;&gt;-->

  <!--&lt;!&ndash;                <ul class="dropdown-menu">&ndash;&gt;-->
  <!--&lt;!&ndash;                  <li>&ndash;&gt;-->
  <!--&lt;!&ndash;                    <RouterLink class="dropdown-item" to="/profile">&ndash;&gt;-->
  <!--&lt;!&ndash;                      <i class="bi-person me-2"></i>&ndash;&gt;-->
  <!--&lt;!&ndash;                      <span>My profile</span>&ndash;&gt;-->
  <!--&lt;!&ndash;                    </RouterLink>&ndash;&gt;-->
  <!--&lt;!&ndash;                  </li>&ndash;&gt;-->
  <!--&lt;!&ndash;                  <li>&ndash;&gt;-->
  <!--&lt;!&ndash;                    <a class="dropdown-item" href="#" @click.prevent="authStore.logout">&ndash;&gt;-->
  <!--&lt;!&ndash;                      <i class="bi-box-arrow-right me-2"></i>&ndash;&gt;-->
  <!--&lt;!&ndash;                      <span>Log out</span>&ndash;&gt;-->
  <!--&lt;!&ndash;                    </a>&ndash;&gt;-->
  <!--&lt;!&ndash;                  </li>&ndash;&gt;-->
  <!--&lt;!&ndash;                </ul>&ndash;&gt;-->
  <!--&lt;!&ndash;              </div>&ndash;&gt;-->
  <!--&lt;!&ndash;            </div>&ndash;&gt;-->
  <!--    </div>-->
  <!--  </nav>-->
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
