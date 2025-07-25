<template>
  <div class="project-members">
    <ProjectBreadcrumb :main="'审计准备'" :sub="'项目成员'" @project-change="onProjectChange" />
    <el-card class="list-card" shadow="never">
      <template #header>
        <div class="card-header">
          <span>成员列表</span>
          <el-button type="primary" @click="handleAdd">新增成员</el-button>
        </div>
      </template>
      <el-table :data="pagedData" style="width: 100%" v-loading="loading">
        <el-table-column type="index" label="序号" width="60" />
        <el-table-column prop="project_name" label="项目名称" min-width="180" />
        <el-table-column prop="username" label="成员姓名" min-width="120" />
        <el-table-column prop="role" label="项目角色" min-width="120" />
        <el-table-column prop="organization" label="所属审计机构" min-width="120" />
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

    <!-- 新增/查看/修改弹窗 -->
    <el-dialog
      v-model="dialogVisible"
      :title="dialogTitle"
      width="600px"
      :close-on-click-modal="false"
    >
      <el-form
        ref="formRef"
        :model="form"
        :rules="rules"
        label-width="120px"
        class="dialog-form"
      >
        <el-form-item label="项目名称" prop="project_name">
          <el-select v-model="form.project_name" placeholder="请选择项目名称" :disabled="dialogMode==='view'||dialogMode==='add'">
            <el-option v-for="item in projectNameList" :key="item.project_code" :label="item.project_name" :value="item.project_name" />
          </el-select>
        </el-form-item>
        <el-form-item label="成员姓名" prop="username">
          <el-select v-model="form.username" placeholder="请选择成员姓名" :disabled="dialogMode==='view'">
            <el-option v-for="item in userOptions" :key="item" :label="item" :value="item" />
          </el-select>
        </el-form-item>
        <el-form-item label="项目角色" prop="role">
          <el-select v-model="form.role" placeholder="请选择项目角色" :disabled="dialogMode==='view'">
            <el-option v-for="item in roleOptions" :key="item" :label="item" :value="item" />
          </el-select>
        </el-form-item>
        <el-form-item label="被审计单位" prop="audit_unit">
          <el-select v-model="form.audit_unit" placeholder="请选择被审计单位" :disabled="dialogMode==='view'" allow-create filterable>
            <el-option v-for="item in unitList" :key="item.code" :label="item.organization" :value="item.organization" />
          </el-select>
        </el-form-item>
      </el-form>
      <template #footer>
        <span class="dialog-footer">
          <el-button @click="dialogVisible = false">取消</el-button>
          <el-button v-if="dialogMode!=='view'" type="primary" @click="handleSubmit">确定</el-button>
        </span>
      </template>
    </el-dialog>
  </div>
</template>

<script setup>
import { ref, reactive, computed, onMounted } from 'vue'
import { ElMessage, ElMessageBox } from 'element-plus'
import ProjectBreadcrumb from '@/components/ProjectBreadcrumb.vue'
import {memberList} from './mock.js'
import { projectNameList } from '../ProjectInfo/mock.js'
import { unitList } from './mock.js'

const mockData = memberList

const userOptions = ['张三', '李四', '王五', '赵六']
const roleOptions = ['项目组长', '项目主审', '项目组员']

const loading = ref(false)
const tableData = ref([]) // 初始化为空数组，等待项目选择后再加载数据
const dialogVisible = ref(false)
const dialogTitle = ref('')
const dialogMode = ref('add') // add/edit/view
const currentCode = ref('')
const formRef = ref()
const form = reactive({
  username: '',
  role: '',
  organization: '',
  project_name: '',
  audit_unit: ''
})
const rules = {
  username: [ { required: true, message: '请选择成员姓名', trigger: 'change' } ],
  role: [ { required: true, message: '请选择项目角色', trigger: 'change' } ],
  organization: [ { required: true, message: '请输入所属审计机构', trigger: 'blur' } ],
  project_name: [ { required: true, message: '请输入项目名称', trigger: 'blur' } ],
  audit_unit: [ { required: true, message: '请选择被审计单位', trigger: 'change' } ]
}

const searchForm = ref({ project_name: '' })

const filteredData = computed(() => {
  let data = tableData.value
  if (searchForm.value.project_name) {
    data = data.filter(item => item.project_name.includes(searchForm.value.project_name))
  }
  return data
})
const pagedData = computed(() => {
  const start = (currentPage.value - 1) * pageSize.value
  return filteredData.value.slice(start, start + pageSize.value)
})
function handleSearch() {
  currentPage.value = 1
  filterTableData()
}
function handleReset() {
  currentPage.value = 1
  filterTableData()
}

// 分页
const currentPage = ref(1)
const pageSize = ref(10)
function handlePageChange(page) {
  currentPage.value = page
}

function handleAdd() {
  dialogTitle.value = '新增成员'
  dialogMode.value = 'add'
  resetForm()
  // 新增时，项目名称默认取面包屑选中项目
  const savedCode = localStorage.getItem('global_project_code')
  if (savedCode) {
    const project = projectNameList.find(p => p.project_code === savedCode)
    if (project) {
      form.project_name = project.project_name
    }
  }
  dialogVisible.value = true
}
function handleEdit(row) {
  dialogTitle.value = '修改成员信息'
  dialogMode.value = 'edit'
  Object.assign(form, row)
  currentCode.value = row.code
  dialogVisible.value = true
}
function handleView(row) {
  dialogTitle.value = '成员信息'
  dialogMode.value = 'view'
  Object.assign(form, row)
  currentCode.value = row.code
  dialogVisible.value = true
}
function handleDelete(row) {
  ElMessageBox.confirm(`确定要删除成员“${row.username}”吗？`, '提示', {
    confirmButtonText: '确定',
    cancelButtonText: '取消',
    type: 'warning',
  }).then(() => {
    const index = tableData.value.findIndex(item => item.code === row.code)
    if (index > -1) {
      tableData.value.splice(index, 1)
      ElMessage.success('删除成功')
    }
  }).catch(() => {})
}
function resetForm() {
  form.username = ''
  form.role = ''
  form.organization = ''
  form.project_name = ''
  form.audit_unit = ''
  if (formRef.value) formRef.value.clearValidate()
}
async function handleSubmit() {
  if (!formRef.value) return
  try {
    await formRef.value.validate()
    if (dialogMode.value === 'add') {
      tableData.value.push({
        code: (tableData.value.length + 1).toString(),
        username: form.username,
        role: form.role,
        organization: form.organization,
        project_name: form.project_name,
        audit_unit: form.audit_unit
      })
      ElMessage.success('新增成功')
    } else if (dialogMode.value === 'edit') {
      const index = tableData.value.findIndex(item => item.code === currentCode.value)
      if (index > -1) {
        tableData.value[index] = { ...tableData.value[index], ...form }
        ElMessage.success('修改成功')
      }
    }
    dialogVisible.value = false
  } catch (error) {
    // 表单校验失败
  }
}

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
  tableData.value = mockData.filter(item => item.project_name === currentProject.value.project_name)
}

onMounted(() => {
  // 页面刷新时，从localStorage读取项目选择并立即过滤数据
  const savedCode = localStorage.getItem('global_project_code')
  if (savedCode) {
    const project = projectNameList.find(p => p.project_code === savedCode)
    if (project) {
      currentProject.value = project
      filterTableData()
    }
  }
})
</script>

<style scoped>
.project-members {
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
.dialog-footer {
  display: flex;
  justify-content: flex-end;
  gap: 12px;
}
.dialog-form {
  margin-top: 10px;
}
</style> 