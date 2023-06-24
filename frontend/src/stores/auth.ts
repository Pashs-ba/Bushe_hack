import { defineStore } from 'pinia'
import { LocalData, clearLocalData, getLocalData, setLocalData } from './local'
import { computed, ref } from 'vue'
import router from '@/router'
import {
  login,
  type TelegramUserData,
  logout,
  type APIUser,
  currentUser
} from '@/api/services/auth'

export const useAuthStore = defineStore('auth', () => {
  const access_token = ref<string | null>(getLocalData(LocalData.ACCESS_TOKEN))
  const refresh_token = ref<string | null>(getLocalData(LocalData.REFRESH_TOKEN))
  const user = ref<APIUser | null>(null)

  const loggedIn = computed(() => user.value !== null)

  function currentUserAction() {
    currentUser().then((r) => {
      user.value = r.data
    })
  }

  function loginAction(data: TelegramUserData) {
    login(data).then((response) => {
      setLocalData(LocalData.ACCESS_TOKEN, response.data.access)
      setLocalData(LocalData.REFRESH_TOKEN, response.data.refresh)
      access_token.value = response.data.access
      refresh_token.value = response.data.refresh
      currentUserAction()
    })
  }

  function logoutAction() {
    if (!refresh_token.value) return
    logout(refresh_token.value).then(() => {
      clearLocalData()
      user.value = null
      router.push('/')
    })
  }

  return {
    user,
    loggedIn,
    loginAction,
    logoutAction,
    access_token,
    refresh_token,
    currentUserAction
  }
})
