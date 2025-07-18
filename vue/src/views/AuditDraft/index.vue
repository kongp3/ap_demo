<template>
  <div class="audit-draft">
    <ProjectBreadcrumb :main="'审计实施'" :sub="'审计底稿'" @project-change="onProjectChange" />
    <el-card class="search-card" shadow="never">
      <el-form :model="searchForm" inline>
        <el-form-item label="底稿名称">
          <el-input v-model="searchForm.draft_name" placeholder="请输入底稿名称" clearable style="width: 220px" />
        </el-form-item>
        <el-form-item label="被审计单位">
          <el-input v-model="searchForm.audit_unit" placeholder="请输入被审计单位" clearable style="width: 220px" />
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
          <span>底稿列表</span>
          <el-button type="primary" @click="handleAdd">新增底稿</el-button>
        </div>
      </template>
      <el-table :data="pagedData" style="width: 100%" v-loading="loading">
        <el-table-column type="index" label="序号" width="60" />
        <el-table-column prop="project_name" label="项目名称" min-width="180" />
        <el-table-column prop="draft_name" label="底稿名称" min-width="180" />
        <el-table-column prop="audit_unit" label="被审计单位" min-width="180" />
        <el-table-column prop="audit_items" label="审计事项" min-width="180">
          <template #default="scope">
            <el-tag v-for="item in scope.row.audit_items" :key="item" size="small" style="margin-right: 4px;">{{ item }}</el-tag>
          </template>
        </el-table-column>
        <!-- <el-table-column prop="collector" label="取证人" width="100" /> -->
        <!-- <el-table-column prop="issue_num" label="问题个数" width="100" /> -->
        <!-- <el-table-column prop="create_time" label="创建日期" width="160" /> -->
        <el-table-column prop="update_time" label="最后修改日期" width="160" />
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
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { ElMessage, ElMessageBox } from 'element-plus'
import { draftList } from './mock.js'
import ProjectBreadcrumb from '@/components/ProjectBreadcrumb.vue'

const loading = ref(false)
const tableData = ref([...draftList])
const searchForm = ref({ draft_name: '', audit_unit: '' })
const currentPage = ref(1)
const pageSize = ref(10)

const filteredData = computed(() => {
  let data = tableData.value
  if (searchForm.value.draft_name) {
    data = data.filter(item => item.draft_name && item.draft_name.includes(searchForm.value.draft_name))
  }
  if (searchForm.value.audit_unit) {
    data = data.filter(item => item.audit_unit && item.audit_unit.includes(searchForm.value.audit_unit))
  }
  return data
})
const pagedData = computed(() => {
  const start = (currentPage.value - 1) * pageSize.value
  return filteredData.value.slice(start, start + pageSize.value)
})
const router = useRouter()

function handleAdd() {
  router.push({ path: '/audit-draft/detail', query: { mode: 'add' } })
}
function handleEdit(row) {
  router.push({ path: '/audit-draft/detail', query: { mode: 'edit', draft_code: row.draft_code } })
}
function handleView(row) {
  router.push({ path: '/audit-draft/detail', query: { mode: 'view', draft_code: row.draft_code } })
}
function handleDelete(row) {
  ElMessageBox.confirm(`确定要删除底稿“${row.draft_name}”吗？`, '提示', {
    confirmButtonText: '确定',
    cancelButtonText: '取消',
    type: 'warning',
  }).then(() => {
    const index = tableData.value.findIndex(item => item.draft_code === row.draft_code)
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
}
function handleReset() {
  searchForm.value.draft_name = ''
  searchForm.value.audit_unit = ''
  currentPage.value = 1
  filterTableData()
}
</script>

<style scoped>
.audit-draft {
  padding: 0;
}
.search-card {
  margin-bottom: 16px;
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