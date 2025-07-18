<template>
    <el-container style="height: 100vh; width: 100%;">
      <!-- 顶部导航栏 -->
      <el-header style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; display: flex; align-items: center; justify-content: space-between; padding: 0 24px; box-shadow: 0 2px 8px rgba(0,0,0,0.04);">
        <h2 style="margin: 0; font-weight: 600; font-size: 20px; display: flex; align-items: center; gap: 10px;">
          <img :src="shenjilogo" alt="logo" style="height:32px;vertical-align:middle;" />
          智能审计系统
        </h2>
        <div style="display: flex; align-items: center; gap: 16px;">
          <!-- Dify 聊天机器人入口 -->
          <el-popover
            placement="bottom-end"
            width="1000"
            trigger="click"
            :show-arrow="false"
            popper-style="margin-top: -2px; padding:0;box-shadow:0 2px 12px rgba(0,0,0,0.12);border-radius:12px;overflow:hidden; inset: 62px 0px auto auto;"
            v-model:visible="aiPopoverVisible"
          >
            <template #reference>
              <el-button circle size="large" style="background:rgba(255,255,255,0.15);border:none;font-size:22px;">
                🤖
              </el-button>
            </template>
            <iframe
              src="http://121.43.233.12/chatbot/mpqT0yUa43BmDT3M"
              style="width: 1000px; height: calc(100vh - 90px); min-height: 400px; border: none; border-radius: 12px; margin: -8px 0;"
              frameborder="0"
              allow="microphone"
            ></iframe>
          </el-popover>
          <el-dropdown>
            <el-avatar :size="32" :src="avatarUrl" />
            <template #dropdown>
              <el-dropdown-menu>
                <el-dropdown-item>个人中心</el-dropdown-item>
                <el-dropdown-item>退出登录</el-dropdown-item>
              </el-dropdown-menu>
            </template>
          </el-dropdown>
        </div>
      </el-header>
  
      <el-container style="height: calc(100vh - 60px);">
        <!-- 左侧菜单 -->
        <el-aside width="220px" style="background: #304156; color: #bfcbd9; height: 100%;">
          <el-menu
            :default-active="activeMenu"
            :default-openeds="openMenus"
            background-color="#304156"
            text-color="#bfcbd9"
            active-text-color="#409EFF"
            @select="handleSelect"
            style="border-right: none; height: 100%;"
          >
            <el-sub-menu index="1">
              <template #title>
                <el-icon><Document /></el-icon>
                <span>审计准备</span>
              </template>
              <el-menu-item index="/project-info">
                <el-icon><InfoFilled /></el-icon>
                <span>项目信息</span>
              </el-menu-item>
              <el-menu-item index="/project-members">
                <el-icon><User /></el-icon>
                <span>项目成员</span>
              </el-menu-item>
              <el-menu-item index="/audit-plan">
                <el-icon><Files /></el-icon>
                <span>审计方案</span>
              </el-menu-item>
            </el-sub-menu>
            <el-sub-menu index="2">
              <template #title>
                <el-icon><Edit /></el-icon>
                <span>审计实施</span>
              </template>
              <el-menu-item index="/audit-draft">
                <el-icon><Document /></el-icon>
                <span>审计底稿</span>
              </el-menu-item>
            </el-sub-menu>
            <el-sub-menu index="3">
              <template #title>
                <el-icon><Check /></el-icon>
                <span>审计终结</span>
              </template>
              <el-menu-item index="/report-setting">
                <el-icon><Setting /></el-icon>
                <span>入报设定</span>
              </el-menu-item>
              <el-menu-item index="/document-archive">
                <el-icon><Folder /></el-icon>
                <span>文书归档</span>
              </el-menu-item>
            </el-sub-menu>
          </el-menu>
        </el-aside>
  
        <el-container>
          <!-- 主内容区 -->
          <el-main style="background: #f5f7fa; width: 100%; height: 100%; overflow: auto;">
            <el-card shadow="never" style="min-height: calc(100vh - 146px); border-radius: 8px; border: none; width: 100%;">
              <router-view />
            </el-card>
          </el-main>
          <!-- 版权信息 -->
          <el-footer style="height: 40px; background: #f5f7fa; border-top: 1px solid #e4e7ed; display: flex; align-items: center; justify-content: center; padding: 0;">
            <div style="color: #909399; font-size: 12px;">
              © {{ new Date().getFullYear() }} 北京航空航天大学. 版权所有.
            </div>
          </el-footer>
        </el-container>
      </el-container>
    </el-container>
  </template>
  
  <script setup>
  import { ref, watch, onMounted } from 'vue'
  import { useRouter, useRoute } from 'vue-router'
  import shenjilogo from './assets/shenjilogo.png'
  import {
    Document,
    InfoFilled,
    User,
    Files,
    Edit,
    Check,
    Setting,
    Folder
  } from '@element-plus/icons-vue'
  
  const router = useRouter()
  const route = useRoute()
  const activeMenu = ref(route.path || '/project-info')
  
  // 展开的二级菜单index
  const openMenus = ref(['1', '2', '3'])

  // Dify 聊天机器人弹窗显示状态
  const aiPopoverVisible = ref(false)
  
  // 随机头像生成（使用 https://api.dicebear.com/）
  const avatarUrl = `https://api.dicebear.com/7.x/identicon/svg?seed=wxshj9e8k6`
  
  // 监听路由变化，更新激活菜单
  watch(() => route.path, (newPath) => {
    activeMenu.value = newPath
  })
  
  function handleSelect(index) {
    router.push(index)
    activeMenu.value = index
  }
  
  onMounted(() => {
    openMenus.value = ['1', '2', '3']
  })

  watch(aiPopoverVisible, (val) => {
    if (!val) {
      window.dispatchEvent(new Event('ai-popover-close'))
    }
  })
  </script>
  
  <style>
  body, html, #app {
    height: 100%;
    width: 100%;
    margin: 0;
    padding: 0;
    overflow: hidden;
  }
  
  * {
    box-sizing: border-box;
  }
  </style>

<style>
.el-popover__content {
  padding: 0 !important;
  min-width: 0 !important;
  min-height: 0 !important;
  background: transparent !important;
  box-shadow: none !important;
}
</style>