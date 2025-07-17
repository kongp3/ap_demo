<template>
    <el-container style="height: 100vh; width: 100%;">
      <!-- 顶部导航栏 -->
      <el-header style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; display: flex; align-items: center; justify-content: space-between; padding: 0 24px; box-shadow: 0 2px 8px rgba(0,0,0,0.04);">
        <h2 style="margin: 0; font-weight: 600; font-size: 20px;">智能审计系统</h2>
        <el-dropdown>
          <el-avatar :size="32" src="https://cube.elemecdn.com/0/88/03b0d395834826768a7534e55.png" />
          <template #dropdown>
            <el-dropdown-menu>
              <el-dropdown-item>个人中心</el-dropdown-item>
              <el-dropdown-item>退出登录</el-dropdown-item>
            </el-dropdown-menu>
          </template>
        </el-dropdown>
      </el-header>
  
      <el-container style="height: calc(100vh - 60px);">
        <!-- 左侧菜单 -->
        <el-aside width="220px" style="background: #304156; color: #bfcbd9; height: 100%;">
          <el-menu
            :default-active="activeMenu"
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
  
        <!-- 主内容区 -->
        <el-main style="padding: 24px; background: #f5f7fa; width: 100%; height: 100%; overflow: auto;">
          <el-card shadow="never" style="min-height: calc(100vh - 108px); border-radius: 8px; border: none; width: 100%;">
            <router-view />
          </el-card>
        </el-main>
      </el-container>
    </el-container>
  </template>
  
  <script setup>
  import { ref, watch } from 'vue'
  import { useRouter, useRoute } from 'vue-router'
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
  
  // 监听路由变化，更新激活菜单
  watch(() => route.path, (newPath) => {
    activeMenu.value = newPath
  })
  
  function handleSelect(index) {
    router.push(index)
    activeMenu.value = index
  }
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