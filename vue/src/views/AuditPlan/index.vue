<template>
  <div class="audit-plan">
    <ProjectBreadcrumb :main="'审计准备'" :sub="'审计方案'" @project-change="onProjectChange" />
    <el-card class="search-card" shadow="never">
      <el-form class="search-form" :model="searchForm" inline>
        <el-form-item label="方案名称">
          <el-input v-model="searchForm.plan_name" placeholder="请输入方案名称" clearable style="width: 220px" />
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="handleSearch">搜索</el-button>
          <el-button @click="handleReset">重置</el-button>
        </el-form-item>
      </el-form>
    </el-card>
    <el-card class="list-card" shadow="never">
      <template #header>
        <div class="card-header">
          <span>方案列表</span>
          <el-button type="primary" @click="handleAdd">新增方案</el-button>
        </div>
      </template>
      <el-table :data="pagedData" style="width: 100%" v-loading="loading">
        <el-table-column type="index" label="序号" width="60" />
        <el-table-column prop="project_name" label="项目名称" min-width="180" />
        <el-table-column prop="plan_name" label="方案名称" min-width="200" />
        <el-table-column prop="date" label="编制日期" width="120" />
        <el-table-column label="审计事项清单" min-width="300">
          <template #default="scope">
            <span>
              <el-tag
                v-for="leaf in getAllLeafNodes(scope.row.items)"
                :key="leaf.item_code"
                style="margin-right: 4px; margin-bottom: 4px;"
                size="small"
              >
                {{ leaf.item_name }}
              </el-tag>
            </span>
          </template>
        </el-table-column>
        <el-table-column label="操作" width="220">
          <template #default="scope">
            <el-button type="info" link @click="handleView(scope.row)">查看</el-button>
            <el-button type="primary" link @click="handleEdit(scope.row)">编辑</el-button>
            <el-button type="danger" link @click="handleDelete(scope.row)">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
      <div style="margin-top: 16px; text-align: right; display: flex; justify-content: flex-end;">
        <el-pagination
          background
          layout="prev, pager, next"
          :total="filteredData.length"
          :page-size="pageSize"
          :current-page="currentPage"
          @current-change="handlePageChange"
        />
      </div>
    </el-card>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { ElMessage, ElMessageBox } from 'element-plus'
import { auditPlanList } from './mock.js'
import ProjectBreadcrumb from '@/components/ProjectBreadcrumb.vue'

const loading = ref(false)
const tableData = ref([...auditPlanList])
const searchForm = ref({ project_name: '', plan_name: '' })
const currentPage = ref(1)
const pageSize = ref(10)
const currentProject = ref({})

const filteredData = computed(() => {
  let data = tableData.value
  if (searchForm.value.plan_name) {
    data = data.filter(item => item.plan_name && item.plan_name.includes(searchForm.value.plan_name))
  }
  return data
})
const pagedData = computed(() => {
  const start = (currentPage.value - 1) * pageSize.value
  return filteredData.value.slice(start, start + pageSize.value)
})
const router = useRouter()

function onProjectChange(project) {
  currentProject.value = project
  filterTableData()
}

function filterTableData() {
  if (!currentProject.value.project_name) {
    tableData.value = []
    return
  }
  tableData.value = auditPlanList.filter(item => item.project_name === currentProject.value.project_name)
}

onMounted(() => {
  if (auditPlanList.length > 0) {
    currentProject.value = auditPlanList[0]
    filterTableData()
  }
})

function handleAdd() {
  router.push({ path: '/audit-plan/detial', query: { mode: 'add' } })
}
function handleEdit(row) {
  router.push({ path: '/audit-plan/detial', query: { mode: 'edit', plan_code: row.plan_code } })
}
function handleView(row) {
  router.push({ path: '/audit-plan/detial', query: { mode: 'view', plan_code: row.plan_code } })
}
function handleDelete(row) {
  ElMessageBox.confirm(`确定要删除方案“${row.plan_name}”吗？`, '提示', {
    confirmButtonText: '确定',
    cancelButtonText: '取消',
    type: 'warning',
  }).then(() => {
    const index = tableData.value.findIndex(item => item.plan_code === row.plan_code)
    if (index > -1) {
      tableData.value.splice(index, 1)
      ElMessage.success('删除成功')
    }
  }).catch(() => {})
}
function handlePageChange(page) {
  currentPage.value = page
}
function handleSearch() {
  currentPage.value = 1
  filterTableData()
}
function handleReset() {
  searchForm.value.plan_name = ''
  currentPage.value = 1
  filterTableData()
}
function getAllLeafNodes(items) {
  const result = []
  function dfs(nodes) {
    if (!nodes) return
    for (const node of nodes) {
      if (node.childs && node.childs.length > 0) {
        dfs(node.childs)
      } else if (node.item_name) {
        result.push(node)
      }
    }
  }
  dfs(items)
  return result
}
</script>

<style scoped>
.audit-plan {
  padding: 0;
}
.search-card {
  margin-bottom: 16px;
}
.search-form .el-form-item{
  margin-bottom: 0;
}
.list-card {
  margin-bottom: 16px;
}
.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
</style> 