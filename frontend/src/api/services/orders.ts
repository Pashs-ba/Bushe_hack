import type { AxiosResponse } from 'axios'
import API, { type Paginator } from '..'

export enum OrdersAPIURLS {
  LIST_ORDERS = 'orders'
}

export enum KitchenAPIURLS {
  LIST_KITCHENS = 'kitchens'
}

export enum OrderStatus {
  opened = 1,
  cooking,
  witing_delivery,
  on_the_way,
  closed
}

export interface Order {
  id: number

  status: OrderStatus
  order_list: string
  comments?: string
  expected_time: string
  end_point: string

  delivery_comments?: string
  kitchen_id?: number
  delivery_man_id?: number
  number_in_queue?: number

  created_at: string
  start_cook_time?: string
  end_cook_time?: string
  start_delivery_time?: string
  end_delivery_time?: string
}

export interface Kitchen {
  geotag: string
}

export const listOrders = (): Promise<AxiosResponse<Paginator<Order>>> => {
  return API.axios.get(OrdersAPIURLS.LIST_ORDERS)
}

export const listKitchens = (): Promise<AxiosResponse<Paginator<Kitchen>>> => {
  return API.axios.get(KitchenAPIURLS.LIST_KITCHENS)
}
