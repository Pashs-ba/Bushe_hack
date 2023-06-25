  <script setup lang="ts">
import type { User } from '@/utils/auth'
import { toSvg } from 'jdenticon'
import { computed } from 'vue'

const props = defineProps<{ size: string; user: User }>()

const jdenticon = computed(() => {
  if (props.user.photo_url) return null
  return toSvg(props.user.id, parseInt(props.size))
})
</script>

<template>
  <img
    v-if="user.photo_url"
    :src="user.photo_url"
    alt=""
    class="userAvatar"
    :style="{ width: `${size}`, height: `${size}` }"
  />
  <div v-else v-html="jdenticon" class="userAvatar jdenticon-wrapper"></div>
</template>

<style scoped>
.jdenticon-wrapper {
  background-color: rgb(47, 47, 47);
}
</style>
