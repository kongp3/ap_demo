// 审计底稿相关API
import axios from 'axios'

const BASE_URL = 'http://121.43.233.12:8080/api'

// 1.1 获取底稿基本信息
export function fetchDraftInfo() {
  return axios.get(`${BASE_URL}/draft/query`)
}

// 1.2 获取审计过程信息
export function fetchAuditProcess() {
  return axios.get(`${BASE_URL}/audit/query`)
}

// 1.3 根据 detail_id 获取审计问题详情
export function fetchAuditDetailById(detail_id: string | number) {
  return axios.get(`${BASE_URL}/audit/query/by_detail_id`, { params: { detail_id } })
} 