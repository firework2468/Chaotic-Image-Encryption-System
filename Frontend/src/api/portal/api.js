import request from '@/utils/request'
import { getToken } from "@/utils/auth";

// 查询菜单列表
export function listMenu(query) {
  let url = "";
  if (getToken() !== undefined){
    url = '/system/news/list'
  } else {
    url = '/portal/api/news'
  }

  return request({
    url: url,
    method: 'get',
    params: query
  })
}

// 查询菜单列表
export function listVip() {

  let url = "";
  if (getToken() !== undefined){
    url = '/system/vip/vip'
  } else {
    url = '/portal/api/vip'
  }
  return request({
    url: url,
    method: 'get'
  })
}
