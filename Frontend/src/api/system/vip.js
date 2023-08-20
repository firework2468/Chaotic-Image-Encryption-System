import request from '@/utils/request'

// 查询vip会员等级列表
export function listVip(query) {
  return request({
    url: '/system/vip/list',
    method: 'get',
    params: query
  })
}

// 查询vip会员等级详细
export function getVip(vipId) {
  return request({
    url: '/system/vip/' + vipId,
    method: 'get'
  })
}

// 新增vip会员等级
export function addVip(data) {
  return request({
    url: '/system/vip',
    method: 'post',
    data: data
  })
}

// 修改vip会员等级
export function updateVip(data) {
  return request({
    url: '/system/vip',
    method: 'put',
    data: data
  })
}

// 删除vip会员等级
export function delVip(vipId) {
  return request({
    url: '/system/vip/' + vipId,
    method: 'delete'
  })
}

// 导出vip会员等级
export function exportVip(query) {
  return request({
    url: '/system/vip/export',
    method: 'get',
    params: query
  })
}