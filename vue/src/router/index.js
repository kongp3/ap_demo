import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  { path: '/', redirect: '/project-info' },
  { path: '/project-info', component: () => import('../views/ProjectInfo/index.vue') },
  { path: '/project-members', component: () => import('../views/ProjectMembers/index.vue') },
  { path: '/audit-plan', component: () => import('../views/AuditPlan/index.vue') },
  { path: '/audit-plan/detial', component: () => import('../views/AuditPlan/detial.vue') },
  { path: '/audit-draft', component: () => import('../views/AuditDraft/index.vue') },
  { path: '/report-setting', component: () => import('../views/ReportSetting/index.vue') },
  { path: '/document-archive', component: () => import('../views/DocumentArchive/index.vue') },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router 