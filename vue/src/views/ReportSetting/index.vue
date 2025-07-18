<template>
  <div class="report-setting">
    <ProjectBreadcrumb :main="'审计终结'" :sub="'入报设定'" @project-change="onProjectChange" />
    <el-card class="search-card" shadow="never">
      <el-form class="search-form" :model="searchForm" inline>
        <el-form-item label="问题等级">
          <el-select v-model="searchForm.level" placeholder="请选择问题等级" clearable style="width: 160px">
            <el-option label="高风险" value="高风险" />
            <el-option label="中风险" value="中风险" />
            <el-option label="低风险" value="低风险" />
          </el-select>
        </el-form-item>
        <el-form-item label="发现人">
          <el-input v-model="searchForm.finder" placeholder="请输入发现人" clearable style="width: 160px" />
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
          <span>问题列表</span>
          <div>
            <el-button type="primary" @click="setReport(true)" :disabled="!multipleSelection.length">设定入报告</el-button>
            <el-button type="warning" @click="setReport(false)" :disabled="!multipleSelection.length">设定不入报告</el-button>
          </div>
        </div>
      </template>
      <el-table
        :data="pagedData"
        style="width: 100%"
        v-loading="loading"
        @selection-change="handleSelectionChange"
      >
        <el-table-column type="selection" width="50" />
        <el-table-column prop="project_name" label="项目名称" min-width="160" />
        <el-table-column prop="issue_title" label="问题标题" min-width="180" />
        <el-table-column prop="level" label="问题等级" width="100" />
        <el-table-column prop="issue_desc" label="问题描述" min-width="200" />
        <el-table-column prop="finder" label="发现人" width="120" />
        <el-table-column prop="create_time" label="创建日期" width="160" />
        <el-table-column label="是否设定入报告" width="140">
          <template #default="scope">
            <el-switch v-model="scope.row.isReport" active-text="入报告" inactive-text="否" />
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
import { ElMessage } from 'element-plus'
import { draftList } from '../AuditDraft/mock.js'
import ProjectBreadcrumb from '@/components/ProjectBreadcrumb.vue'
const currentProject = ref({})
function onProjectChange(project) {
  currentProject.value = project
  filterTableData()
}

function filterTableData() {
  if (!currentProject.value.project_name) {
    tableData.value = []
    return
  }
  tableData.value = allIssues.filter(item => item.project_name === currentProject.value.project_name)
}

onMounted(() => {
  if (allIssues.length > 0) {
    currentProject.value = allIssues[0]
    filterTableData()
  }
})

// 扁平化所有底稿的customers为问题列表
const allIssues = []
draftList.forEach(draft => {
  (draft.customers || []).forEach((c, idx) => {
    allIssues.push({
      project_name: draft.project_name || '',
      issue_code: draft.draft_code + '-' + (idx + 1),
      issue_title: c.issue_title,
      level: c.level,
      issue_desc: c.issue_desc,
      finder: c.finder || '未知',
      create_time: draft.create_time,
      isReport: c.isReport || false
    })
  })
})

const loading = ref(false)
const tableData = ref([...allIssues])
const searchForm = ref({ level: '', finder: '' })
const currentPage = ref(1)
const pageSize = ref(10)
const multipleSelection = ref([])

const filteredData = computed(() => {
  let data = tableData.value
  if (searchForm.value.level) {
    data = data.filter(item => item.level === searchForm.value.level)
  }
  if (searchForm.value.finder) {
    data = data.filter(item => item.finder && item.finder.includes(searchForm.value.finder))
  }
  return data
})
const pagedData = computed(() => {
  const start = (currentPage.value - 1) * pageSize.value
  return filteredData.value.slice(start, start + pageSize.value)
})

function handleSelectionChange(val) {
  multipleSelection.value = val
}
function setReport(flag) {
  multipleSelection.value.forEach(row => {
    row.isReport = flag
  })
  ElMessage.success(flag ? '已设定为入报告' : '已设定为不入报告')
}
function handlePageChange(page) {
  currentPage.value = page
}
function handleSearch() {
  currentPage.value = 1
  filterTableData()
}
function handleReset() {
  searchForm.value.level = ''
  searchForm.value.finder = ''
  currentPage.value = 1
  filterTableData()
}
</script>

<style scoped>
.report-setting {
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