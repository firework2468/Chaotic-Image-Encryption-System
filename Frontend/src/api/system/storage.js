import request from '@/utils/request'

// 查询本地存储列表
export function listStorage(query) {
  return request({
    url: '/system/storage/list',
    method: 'get',
    params: query
  })
}

// 查询本地存储详细
export function getStorage(storageId) {
  return request({
    url: '/system/storage/' + storageId,
    method: 'get'
  })
}

// 新增本地存储
export function addStorage(data) {
  return request({
    url: '/system/storage',
    method: 'post',
    data: data
  })
}

// 修改本地存储
export function updateStorage(data) {
  return request({
    url: '/system/storage',
    method: 'put',
    data: data
  })
}

// 删除本地存储
export function delStorage(storageId) {
  return request({
    url: '/system/storage/' + storageId,
    method: 'delete'
  })
}

// 导出本地存储
export function exportStorage(query) {
  return request({
    url: '/system/storage/export',
    method: 'get',
    params: query
  })
}


// 加密
export function imgEncrypt(data) {
  console.log(data)
  return request({
    url: '/system/storage/encrypted',
    method: 'post',
    data: data
  })
}

// 解密
export function imgDecrypt(data) {
  return request({
    url: '/system/storage/imgDecrypt',
    method: 'get',
    params: data
  })
}

// 加密结果
export function encryptRes(data) {
  return request({
    url: '/system/storage/encryptRes',
    method: 'get',
    params: data
  })
}

// 直方图分析
export function zanalysis(data) {
  return request({
    url: '/system/storage/zanalysis',
    method: 'get',
    params: data
  })
}

// 相邻相关性像素分析
export function xanalysis(data) {
  return request({
    url: '/system/storage/xanalysis',
    method: 'get',
    params: data
  })
}

// 信息熵分析
export function sanalysis(data) {
  return request({
    url: '/system/storage/sanalysis',
    method: 'get',
    params: data
  })
}

// 密钥敏感性
export function manalysis(data) {
  return request({
    url: '/system/storage/manalysis',
    method: 'get',
    params: data
  })
}

// 密钥敏感性
export function canalysis(data) {
  return request({
    url: '/system/storage/canalysis',
    method: 'get',
    params: data
  })
}
