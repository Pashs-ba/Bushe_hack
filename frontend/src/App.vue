<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import MainNav from '@/components/MainNav.vue'
</script>

<template>
  <MainNav />
  <div class="view-wrapper">
    <RouterView />
  </div>
</template>

<style scoped>
.logo {
  display: block;
  margin: 0 auto 2rem;
}
</style>
