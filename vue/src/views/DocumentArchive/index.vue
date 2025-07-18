<template>
  <div class="document-archive">
    <ProjectBreadcrumb :main="'审计终结'" :sub="'文书归档'" @project-change="onProjectChange" />
    <el-card class="list-card" shadow="never">
      <template #header>
        <div class="card-header">
          <span>文档列表</span>
          <div>
            <el-button type="success" @click="handleInit">初始化归档模版</el-button>
            <el-button type="primary" @click="setArchive('已归档')" :disabled="!multipleSelection.length">归档确认</el-button>
            <el-button type="warning" @click="setArchive('未归档')" :disabled="!multipleSelection.length">撤销归档</el-button>
          </div>
        </div>
      </template>
      <el-table
        :data="currentProjectDocs"
        style="width: 100%"
        v-loading="loading"
        @selection-change="handleSelectionChange"
        :span-method="tableSpanMethod"
      >
        <el-table-column type="selection" width="50" />
        <el-table-column prop="stage" label="项目阶段" min-width="100" />
        <el-table-column prop="type" label="工作项" min-width="80" />
        <el-table-column prop="model" label="对应模版" min-width="80" />
        <el-table-column prop="attach" label="已传文书" min-width="160">
          <template #default="scope">
            <template v-if="scope.row.attach">
              <el-link type="primary" :underline="false" @click="handleDownload(scope.row)">{{ scope.row.attach }}</el-link>
            </template>
            <template v-else>--</template>
          </template>
        </el-table-column>
        <el-table-column prop="state" label="状态" width="100">
          <template #default="scope">
            <template v-if="scope.row.state">
              <el-tag :type="scope.row.state === '已归档' ? 'success' : 'info'">{{ scope.row.state }}</el-tag>
            </template>
            <template v-else>
              <!-- 空状态不显示tag -->
            </template>
          </template>
        </el-table-column>
        <el-table-column label="操作" width="180">
          <template #default="scope">
            <div style="display: flex; gap: 8px; align-items: center;">
              <template v-if="scope.row.state === '已归档'">
                <el-button type="warning" link @click="handleUnarchive(scope.row)">撤销归档</el-button>
              </template>
              <template v-else-if="scope.row.attach">
                <el-button type="success" link @click="handleArchive(scope.row)">确认归档</el-button>
                <el-button type="danger" link @click="handleClear(scope.row)">清空文书</el-button>
              </template>
              <template v-else>
                <el-upload
                  :show-file-list="false"
                  :before-upload="file => handleUpload(scope.row, file)"
                >
                  <el-button type="primary" link>上传文书</el-button>
                </el-upload>
              </template>
            </div>
          </template>
        </el-table-column>
      </el-table>
    </el-card>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { ElMessage } from 'element-plus'
import { archiveList } from './mock.js'
import { modelList } from './model.js'
import { projectList } from '../ProjectInfo/mock.js'
import ProjectBreadcrumb from '@/components/ProjectBreadcrumb.vue'

const loading = ref(false)
const allArchiveData = ref([...archiveList])
const searchForm = ref({ project_name: '' })
const multipleSelection = ref([])
const currentProject = ref({})

function onProjectChange(project) {
  currentProject.value = project
  filterTableData()
}

function filterTableData() {
  if (!currentProject.value.project_name) {
    allArchiveData.value = []
    return
  }
  allArchiveData.value = archiveList.filter(item => item.project_name === currentProject.value.project_name)
}

onMounted(() => {
  if (archiveList.length > 0) {
    currentProject.value = archiveList[0]
    filterTableData()
  }
})

const projectNames = computed(() => {
  return Array.from(new Set((projectList || []).map(item => item.project_name).filter(Boolean)))
})

// 当前选中项目的文档列表
const currentProjectDocs = computed(() => {
  const item = allArchiveData.value.find(i => i.project_name === currentProject.value.project_name)
  if (item) {
    // 给每个文档加上 project_name 字段，方便后续操作
    return item.documents.map(doc => ({ ...doc, project_name: item.project_name }))
  }
  return []
})

function handleSelectionChange(val) {
  multipleSelection.value = val
}
function setArchive(status) {
  const item = allArchiveData.value.find(i => i.project_name === currentProject.value.project_name)
  if (item) {
    multipleSelection.value.forEach(row => {
      const doc = item.documents.find(d => d.stage === row.stage && d.type === row.type)
      if (doc) doc.state = status
    })
    ElMessage.success(status === '已归档' ? '已归档' : '已撤销归档')
  }
}
function handleUpload(row, file) {
  const item = allArchiveData.value.find(i => i.project_name === currentProject.value.project_name)
  if (item) {
    const doc = item.documents.find(d => d.stage === row.stage && d.type === row.type)
    if (doc) doc.attach = file.name
    ElMessage.success('上传成功')
  }
  return false // 阻止自动上传
}
function handleDelete(row) {
  const item = allArchiveData.value.find(i => i.project_name === currentProject.value.project_name)
  if (item) {
    const idx = item.documents.findIndex(d => d.stage === row.stage && d.type === row.type)
    if (idx > -1) item.documents.splice(idx, 1)
    ElMessage.success('删除成功')
  }
}
// 新增清空操作
function handleClear(row) {
  const item = allArchiveData.value.find(i => i.project_name === currentProject.value.project_name)
  if (item) {
    const doc = item.documents.find(d => d.stage === row.stage && d.type === row.type)
    if (doc) doc.attach = ''
    ElMessage.success('已清空')
  }
}
// 新增下载/查看操作
function handleDownload(row) {
  if (row.attach) {
    // 这里假设attach为文件名，实际项目可替换为真实url
    // 这里只做下载模拟
    const link = document.createElement('a')
    link.href = `/download/${encodeURIComponent(row.attach)}`
    link.download = row.attach
    document.body.appendChild(link)
    link.click()
    document.body.removeChild(link)
  }
}
function handleSearch() {
  multipleSelection.value = []
  filterTableData()
}
function handleReset() {
  multipleSelection.value = []
  filterTableData()
}
function handleInit() {
  if (!currentProject.value.project_name) {
    ElMessage.warning('请先选择项目名称')
    return
  }
  const newDocs = modelList.map(item => ({ ...item, state: '未归档' }))
  const idx = allArchiveData.value.findIndex(item => item.project_name === currentProject.value.project_name)
  if (idx > -1) {
    allArchiveData.value[idx].documents = newDocs
  } else {
    allArchiveData.value.push({
      project_name: currentProject.value.project_name,
      documents: newDocs
    })
  }
  ElMessage.success('归档模版已初始化')
}
function tableSpanMethod({ row, column, rowIndex }) {
  if (column.property === 'stage') {
    const data = currentProjectDocs.value
    let prev = null, count = 0, start = 0
    for (let i = 0; i < data.length; i++) {
      if (i === 0 || data[i].stage !== prev) {
        if (count > 0) {
          if (rowIndex === start) return { rowspan: count, colspan: 1 }
          if (rowIndex > start && rowIndex < start + count) return { rowspan: 0, colspan: 0 }
        }
        prev = data[i].stage
        count = 1
        start = i
      } else {
        count++
        if (i === data.length - 1) {
          if (rowIndex === start) return { rowspan: count, colspan: 1 }
          if (rowIndex > start && rowIndex < start + count) return { rowspan: 0, colspan: 0 }
        }
      }
    }
  }
}
// 新增归档/撤销归档操作
function handleArchive(row) {
  const item = allArchiveData.value.find(i => i.project_name === currentProject.value.project_name)
  if (item) {
    const doc = item.documents.find(d => d.stage === row.stage && d.type === row.type)
    if (doc) doc.state = '已归档'
    ElMessage.success('已归档')
  }
}
function handleUnarchive(row) {
  const item = allArchiveData.value.find(i => i.project_name === currentProject.value.project_name)
  if (item) {
    const doc = item.documents.find(d => d.stage === row.stage && d.type === row.type)
    if (doc) doc.state = '未归档'
    ElMessage.success('已撤销归档')
  }
}
</script>

<style scoped>
.document-archive {
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