<template>
  <div class="breadcrumb-wrapper">
    <el-breadcrumb separator="/">
      <el-breadcrumb-item>{{ main }}</el-breadcrumb-item>
      <el-breadcrumb-item>{{ sub }}</el-breadcrumb-item>
      <el-breadcrumb-item v-if="!projectless">
        <el-dropdown @command="handleProjectChange">
          <span class="el-dropdown-link">
            {{ currentProject.project_name || '请选择项目' }}
            <el-icon><arrow-down /></el-icon>
          </span>
          <template #dropdown>
            <el-dropdown-menu>
              <el-dropdown-item
                v-for="item in projectList"
                :key="item.project_code"
                :command="item.project_code"
              >
                {{ item.project_name }}
              </el-dropdown-item>
            </el-dropdown-menu>
          </template>
        </el-dropdown>
      </el-breadcrumb-item>
    </el-breadcrumb>
  </div>
</template>

<script setup>
import { ref, watch, defineProps, defineEmits, onMounted } from 'vue'
import { ArrowDown } from '@element-plus/icons-vue'
import { projectList } from '../views/ProjectInfo/mock.js'

const props = defineProps({
  main: String,
  sub: String,
  projectCode: String,
  projectless: Boolean
})
const emit = defineEmits(['project-change'])

const currentProjectCode = ref('')
const currentProject = ref({})

onMounted(() => {
  // 优先从localStorage读取全局选中项目
  const savedCode = localStorage.getItem('global_project_code')
  if (savedCode && projectList.find(p => p.project_code === savedCode)) {
    currentProjectCode.value = savedCode
    currentProject.value = projectList.find(p => p.project_code === savedCode)
  } else {
    currentProjectCode.value = projectList[0]?.project_code || ''
    currentProject.value = projectList.find(p => p.project_code === currentProjectCode.value) || {}
  }
})

function handleProjectChange(code) {
  currentProjectCode.value = code
  currentProject.value = projectList.find(p => p.project_code === code) || {}
  localStorage.setItem('global_project_code', code)
  emit('project-change', currentProject.value)
}

watch(() => props.projectCode, (val) => {
  if (val) {
    currentProjectCode.value = val
    currentProject.value = projectList.find(p => p.project_code === val) || {}
    localStorage.setItem('global_project_code', val)
  }
})
</script>

<style scoped>
.breadcrumb-wrapper {
  background: #f8f9fb;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.04);
  padding: 12px 24px 12px 20px;
  margin-bottom: 18px;
  border: 1px solid #ebeef5;
}
.el-dropdown-link {
  cursor: pointer;
  color: #409EFF;
  font-weight: 500;
  display: flex;
  align-items: center;
  outline: none;
  border: none;
  background: transparent;
}
.el-dropdown-link:focus,
.el-dropdown-link:active {
  outline: none !important;
  border: none !important;
  box-shadow: none !important;
  background: transparent !important;
}
</style> 