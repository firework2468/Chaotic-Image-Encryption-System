import request from '@/utils/request'

// 查询vip会员购买记录列表
export function listRecord(query) {
  return request({
    url: '/system/record/list',
    method: 'get',
    params: query
  })
}

// 查询vip会员购买记录详细
export function getRecord(recordId) {
  return request({
    url: '/system/record/' + recordId,
    method: 'get'
  })
}

// 新增vip会员购买记录
export function addRecord(data) {
  return request({
    url: '/system/record',
    method: 'post',
    data: data
  })
}

// 修改vip会员购买记录
export function updateRecord(data) {
  return request({
    url: '/system/record',
    method: 'put',
    data: data
  })
}

// 删除vip会员购买记录
export function delRecord(recordId) {
  return request({
    url: '/system/record/' + recordId,
    method: 'delete'
  })
}

// 导出vip会员购买记录
export function exportRecord(query) {
  return request({
    url: '/system/record/export',
    method: 'get',
    params: query
  })
}
