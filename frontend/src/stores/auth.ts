export interface TelegramUserData {
  auth_date: number
  first_name: string
  hash: string
  id: number
  last_name?: string
  username: string
  photo_url?: string
}

const readLocalUserData = (): TelegramUserData | null => {
  const userDataJSON = localStorage.getItem('tg-user')
  if (!userDataJSON) return null
  const userData = JSON.parse(userDataJSON) as TelegramUserData
  const isValid = checkAuthValidity(userData)
  if (!isValid) return null
  return userData
}

export const useAuthStore = defineStore('auth', () => {
  const user = ref<TelegramUserData | null>(readLocalUserData())

  const loggedIn = computed(() => user.value !== null)

  function login(data: TelegramUserData) {
    user.value = data
    localStorage.setItem('tg-user', JSON.stringify(user.value))
    addMember(data)
  }

  function logout() {
    localStorage.removeItem('tg-user')
    user.value = null
    router.push('/')
  }

  return { user, loggedIn, login, logout }
})
