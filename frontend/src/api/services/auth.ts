import type { AxiosResponse } from 'axios'
import API from '..'

export interface TelegramUserData {
  auth_date: number
  first_name: string
  hash: string
  id: number
  last_name?: string
  username: string
  photo_url?: string
}

export enum AuthAPIURLS {
  CURRENT_USER = 'auth/users/me',
  LOGIN = 'auth/login',
  LOGOUT = 'auth/logout',
  REFRESH_TOKEN = 'auth/refresh'
}

export interface APIUser {
  photo_url: string | null
  username: string
  id: number
  telegram_id: number
  account_type: number
}

export interface APITokens {
  access: string
  refresh: string
}

export const login = (data: TelegramUserData): Promise<AxiosResponse<APITokens>> => {
  return API.noAuthAxios.post(AuthAPIURLS.LOGIN, data)
}

export const logout = (refresh_token: string): Promise<AxiosResponse> => {
  return API.axios.post(AuthAPIURLS.LOGOUT, { refresh: refresh_token })
}

export const currentUser = (): Promise<AxiosResponse<APIUser>> => {
  return API.axios.get(AuthAPIURLS.CURRENT_USER)
}
