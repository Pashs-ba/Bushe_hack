import type { AxiosResponse } from 'axios'
import API from '..'

export enum AuthAPIURLS {
  CURRENT_USER = 'auth/users/me',
  GET_TOKEN = 'auth/jwt/create/',
  REMOVE_TOKEN = 'auth/jwt/blacklist/',
  REFRESH_TOKEN = 'auth/jwt/refresh/'
}

export interface APITokens {
  access: string
  refresh: string
}

export const createUser = async (data: any): Promise<AxiosResponse> => {
  return await API.noAuthAxios.post('auth/users/create', data)
}

export const login = (credentials: any): Promise<AxiosResponse<APITokens>> => {
  return API.noAuthAxios.post(AuthAPIURLS.GET_TOKEN, {
    email: credentials.email,
    password: credentials.password
  })
}
