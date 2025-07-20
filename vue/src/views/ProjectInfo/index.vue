<template>
    <div class="project-info">
      <ProjectBreadcrumb :main="'审计准备'" :sub="'项目信息'" projectless />
      <!-- 搜索区域 -->
      <el-card class="search-card" shadow="never">
        <el-form class="search-form" :model="searchForm" inline>
          <el-form-item label="项目编号">
            <el-input v-model="searchForm.project_code" placeholder="请输入项目编号" clearable />
          </el-form-item>
          <el-form-item label="项目名称">
            <el-input v-model="searchForm.project_name" placeholder="请输入项目名称" clearable style="width: 300px"/>
          </el-form-item>
          <el-form-item label="项目类型">
            <el-select v-model="searchForm.type" placeholder="请选择项目类型" clearable style="width: 120px">
                <el-option label="全部" value="" />
                <el-option
                    v-for="item in typeOptions"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value"
                    />
            </el-select>
          </el-form-item>
          <el-form-item label="项目状态">
            <el-select v-model="searchForm.state" placeholder="请选择项目状态" clearable style="width: 120px">
                <el-option label="全部" value="" />
                <el-option
                    v-for="item in stateOptions"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value"
                    />
            </el-select>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="handleSearch">搜索</el-button>
            <el-button @click="handleReset">重置</el-button>
          </el-form-item>
        </el-form>
      </el-card>
  
      <!-- 列表区域 -->
      <el-card class="list-card" shadow="never">
        <template #header>
          <div class="card-header">
            <span>项目信息列表</span>
            <el-button type="primary" @click="handleAdd">新增</el-button>
          </div>
        </template>
  
        <el-table :data="pagedData" style="width: 100%" v-loading="loading">
          <el-table-column type="index" label="序号" width="60" />
          <el-table-column prop="project_code" label="项目编号" min-width="140" />
          <el-table-column prop="year" label="项目年度" width="100" />
          <el-table-column prop="project_name" label="项目名称" min-width="300" />
          <el-table-column prop="type" label="项目类型" width="100" />
          <el-table-column prop="organization" label="审计机构" width="120" />
          <el-table-column prop="leader" label="项目负责人" width="120" />
          <el-table-column prop="state" label="项目状态" width="100">
            <template #default="{ row }">
              <el-tag :type="getStateType(row.state)">
                {{ row.state }}
              </el-tag>
            </template>
          </el-table-column>
          <el-table-column label="操作" width="150">
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
            :total="tableData.length"
            :page-size="pageSize"
            :current-page="currentPage"
            @current-change="handlePageChange"
          />
        </div>
      </el-card>
  
      <!-- 新增/编辑弹窗 -->
      <el-dialog
        v-model="dialogVisible"
        :title="dialogTitle"
        width="60%"
        :close-on-click-modal="false"
      >
        <el-form
          ref="formRef"
          :model="form"
          :rules="rules"
          label-width="120px"
          class="dialog-form"
        >
          <el-row :gutter="20">
            <el-col :span="12">
              <el-form-item label="项目编号" prop="project_code">
                <el-input v-model="form.project_code" placeholder="请输入项目编号" />
              </el-form-item>
            </el-col>
            <el-col :span="12">
              <el-form-item label="项目状态" prop="state">
                <el-select v-model="form.state" placeholder="请选择项目状态">
                  <el-option v-for="item in stateOptions" :key="item.value" :label="item.label" :value="item.value" />
                </el-select>
              </el-form-item>
            </el-col>
          </el-row>
          <el-row :gutter="20">
            <el-col :span="24">
              <el-form-item label="项目名称" prop="project_name">
                <el-input v-model="form.project_name" placeholder="请输入项目名称" />
              </el-form-item>
            </el-col>
          </el-row>
          <el-row :gutter="20">
            <el-col :span="12">
              <el-form-item label="项目类型" prop="type">
                <el-select v-model="form.type" placeholder="请选择项目类型">
                  <el-option v-for="item in typeOptions" :key="item.value" :label="item.label" :value="item.value" />
                </el-select>
              </el-form-item>
            </el-col>
            <el-col :span="12">
              <el-form-item label="项目年度" prop="year">
                <el-date-picker v-model="form.year" type="year" placeholder="请选择项目年度" style="width: 100%" value-format="YYYY" />
              </el-form-item>
            </el-col>
          </el-row>
          <el-row :gutter="20">
            <el-col :span="12">
              <el-form-item label="审计机构" prop="organization">
                <el-select v-model="form.organization" placeholder="请选择审计机构" style="width: 100%">
                  <el-option
                    v-for="org in organizationOptions"
                    :key="org.value"
                    :label="org.label"
                    :value="org.value"
                  />
                </el-select>
              </el-form-item>
            </el-col>
            <el-col :span="12">
              <el-form-item label="项目负责人" prop="leader">
                <el-select v-model="form.leader" placeholder="请选择项目负责人" style="width: 100%">
                  <el-option
                    v-for="member in memberOptions"
                    :key="member.code"
                    :label="member.username"
                    :value="member.username"
                  />
                </el-select>
              </el-form-item>
            </el-col>
          </el-row>
          <el-row :gutter="20">
            <el-col :span="12">
              <el-form-item label="审计开始日期" prop="start_date">
                <el-date-picker v-model="form.start_date" type="date" placeholder="请选择审计开始日期" style="width: 100%" value-format="YYYY-MM-DD" />
              </el-form-item>
            </el-col>
            <el-col :span="12">
              <el-form-item label="审计结束日期" prop="end_date">
                <el-date-picker v-model="form.end_date" type="date" placeholder="请选择审计结束日期" style="width: 100%" value-format="YYYY-MM-DD" />
              </el-form-item>
            </el-col>
          </el-row>
          <el-row :gutter="20">
            <el-col :span="12">
              <el-form-item label="被审计单位" prop="audit_unit">
                <el-input v-model="form.audit_unit" placeholder="请输入被审计单位" />
              </el-form-item>
            </el-col>
            <el-col :span="12">
              <!-- 占位，保持备注独占一行 -->
            </el-col>
          </el-row>
          <el-row :gutter="20">
            <el-col :span="24">
              <el-form-item label="备注" prop="remark">
                <el-input type="textarea" v-model="form.remark" placeholder="请输入备注" :rows="4" />
              </el-form-item>
            </el-col>
          </el-row>
        </el-form>
        <template #footer>
          <span class="dialog-footer">
            <el-button @click="dialogVisible = false">取消</el-button>
            <el-button type="primary" @click="handleSubmit">确定</el-button>
          </span>
        </template>
      </el-dialog>
  
      <!-- 查看弹窗 -->
      <el-dialog v-model="viewDialogVisible" title="项目信息查看" width="60%" :close-on-click-modal="false">
        <el-form :model="viewData" label-width="120px" class="dialog-form" disabled>
          <el-row :gutter="20">
            <el-col :span="12">
              <el-form-item label="项目编号" prop="project_code">
                <el-input v-model="viewData.project_code" disabled />
              </el-form-item>
            </el-col>
            <el-col :span="12">
              <el-form-item label="项目状态" prop="state">
                <el-select v-model="viewData.state" disabled style="width: 100%">
                  <el-option v-for="item in stateOptions" :key="item.value" :label="item.label" :value="item.value" />
                </el-select>
              </el-form-item>
            </el-col>
          </el-row>
          <el-row :gutter="20">
            <el-col :span="24">
              <el-form-item label="项目名称" prop="project_name">
                <el-input v-model="viewData.project_name" disabled />
              </el-form-item>
            </el-col>
          </el-row>
          <el-row :gutter="20">
            <el-col :span="12">
              <el-form-item label="项目类型" prop="type">
                <el-input v-model="viewData.type" disabled />
              </el-form-item>
            </el-col>
            <el-col :span="12">
              <el-form-item label="审计机构" prop="organization">
                <el-select v-model="viewData.organization" disabled style="width: 100%">
                  <el-option
                    v-for="org in organizationOptions"
                    :key="org.value"
                    :label="org.label"
                    :value="org.value"
                  />
                </el-select>
              </el-form-item>
            </el-col>
          </el-row>
          <el-row :gutter="20">
            <el-col :span="12">
              <el-form-item label="项目负责人" prop="leader">
                <el-select v-model="viewData.leader" disabled style="width: 100%">
                  <el-option
                    v-for="member in memberOptions"
                    :key="member.code"
                    :label="member.username"
                    :value="member.username"
                  />
                </el-select>
              </el-form-item>
            </el-col>
            <el-col :span="12">
              <el-form-item label="项目年度" prop="year">
                <el-input v-model="viewData.year" disabled />
              </el-form-item>
            </el-col>
          </el-row>
          <el-row :gutter="20">
            <el-col :span="12">
              <el-form-item label="被审计单位" prop="audit_unit">
                <el-input v-model="viewData.audit_unit" disabled />
              </el-form-item>
            </el-col>
            <el-col :span="12">
              <el-form-item label="备注" prop="remark">
                <el-input v-model="viewData.remark" disabled />
              </el-form-item>
            </el-col>
          </el-row>
          <el-row :gutter="20">
            <el-col :span="12">
              <el-form-item label="开始日期" prop="start_date">
                <el-input v-model="viewData.start_date" disabled />
              </el-form-item>
            </el-col>
            <el-col :span="12">
              <el-form-item label="结束日期" prop="end_date">
                <el-input v-model="viewData.end_date" disabled />
              </el-form-item>
            </el-col>
          </el-row>
        </el-form>
        <template #footer>
          <el-button @click="viewDialogVisible = false">关闭</el-button>
        </template>
      </el-dialog>
    </div>
  </template>
  
  <script setup>
  import { ref, reactive, computed, onMounted } from 'vue'
import { ElMessage, ElMessageBox } from 'element-plus'
import { projectList, organizationOptions } from './mock.js'
import { memberList } from '../ProjectMembers/mock.js'
import ProjectBreadcrumb from '@/components/ProjectBreadcrumb.vue'
  
  // Mock数据
  const mockData = projectList

  const typeOptions = [
    {
        value: '专项审计',
        label: '专项审计',
    },
    {
        value: '建设项目审计',
        label: '建设项目审计',
    },
    {
        value: '内部控制审计',
        label: '内部控制审计',
    }
  ]

  const stateOptions = [
    {
        value: '已完成',
        label: '已完成',
    },
    {
        value: '进行中',
        label: '进行中',
    },
    {
        value: '已取消',
        label: '已取消',
    }
  ]

  // 项目成员选项
  const memberOptions = memberList
  
  // 响应式数据
  const loading = ref(false)
  const tableData = ref([])
  const dialogVisible = ref(false)
  const dialogTitle = ref('新增项目')
  const isEdit = ref(false)
  const currentId = ref('')
  const viewDialogVisible = ref(false)
  const viewData = ref({})
  
  const searchForm = reactive({
    project_code: '',
    project_name: '',
    type: '',
    state: ''
  })
  
  const form = reactive({
    project_code: '',
    year: '',
    project_name: '',
    type: '',
    organization: '',
    leader: '',
    start_date: '',
    end_date: '',
    audit_unit: '',
    remark: '',
    state: '' // 默认空值
  })
  
  const rules = {
    project_code: [
      { required: true, message: '请输入项目编号', trigger: 'blur' }
    ],
    year: [
      { required: true, message: '请输入项目年度', trigger: 'blur' }
    ],
    project_name: [
      { required: true, message: '请输入项目名称', trigger: 'blur' }
    ],
    type: [
      { required: true, message: '请选择项目类型', trigger: 'change' }
    ],
    organization: [
      { required: true, message: '请输入审计机构', trigger: 'blur' }
    ],
    leader: [
      { required: true, message: '请输入项目负责人', trigger: 'blur' }
    ],
    start_date: [
      { required: true, message: '请选择审计开始日期', trigger: 'change' }
    ],
    end_date: [],
    audit_unit: [
      { required: true, message: '请输入被审计单位', trigger: 'blur' }
    ],
    remark: [],
    state: [ // Added state validation rule
      { required: true, message: '请选择项目状态', trigger: 'change' }
    ]
  }
  
  const formRef = ref()
  
  const currentPage = ref(1)
  const pageSize = ref(10)
  const pagedData = computed(() => {
    const start = (currentPage.value - 1) * pageSize.value
    return tableData.value.slice(start, start + pageSize.value)
  })
  function handlePageChange(page) {
    currentPage.value = page
  }
  
  // 方法
  const getStateType = (state) => {
    const stateMap = {
      '已完成': 'success',
      '进行中': 'warning',
      '已取消': 'info'
    }
    return stateMap[state] || 'info'
  }
  
  const loadData = () => {
    loading.value = true
    setTimeout(() => {
      tableData.value = [...mockData]
      loading.value = false
    }, 500)
  }
  
  const handleSearch = () => {
    loading.value = true
    setTimeout(() => {
      let filteredData = [...mockData]
      if (searchForm.project_code) {
        filteredData = filteredData.filter(item => item.project_code.includes(searchForm.project_code))
      }
      if (searchForm.project_name) {
        filteredData = filteredData.filter(item => item.project_name.includes(searchForm.project_name))
      }
      if (searchForm.type) {
        filteredData = filteredData.filter(item => item.type === searchForm.type)
      }
      if (searchForm.state) {
        filteredData = filteredData.filter(item => item.state === searchForm.state)
      }
      tableData.value = filteredData
      loading.value = false
    }, 300)
  }
  
  const handleReset = () => {
    searchForm.project_code = ''
    searchForm.project_name = ''
    searchForm.type = ''
    searchForm.state = ''
    loadData()
  }
  
  const handleAdd = () => {
    dialogTitle.value = '新增项目'
    isEdit.value = false
    resetForm()
    dialogVisible.value = true
  }
  
  const handleEdit = (row) => {
    dialogTitle.value = '编辑项目'
    isEdit.value = true
    currentId.value = row.project_code
    Object.assign(form, row)
    dialogVisible.value = true
  }

  function handleView(row) {
    viewData.value = { ...row }
    viewDialogVisible.value = true
  }
  
  const handleDelete = (row) => {
    ElMessageBox.confirm(
      `确定要删除项目"${row.project_name}"吗？`,
      '提示',
      {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning',
      }
    ).then(() => {
      const index = tableData.value.findIndex(item => item.project_code === row.project_code)
      if (index > -1) {
        tableData.value.splice(index, 1)
        ElMessage.success('删除成功')
      }
    }).catch(() => {})
  }
  
  const resetForm = () => {
    form.project_code = ''
    form.year = ''
    form.project_name = ''
    form.type = ''
    form.organization = ''
    form.leader = ''
    form.start_date = ''
    form.end_date = ''
    form.audit_unit = ''
    form.remark = ''
    form.state = '' // Reset state field
    if (formRef.value) {
      formRef.value.clearValidate()
    }
  }
  
  const handleSubmit = async () => {
    if (!formRef.value) return
    try {
      await formRef.value.validate()
      if (isEdit.value) {
        const index = tableData.value.findIndex(item => item.project_code === currentId.value)
        if (index > -1) {
          tableData.value[index] = { ...tableData.value[index], ...form }
          ElMessage.success('编辑成功')
        }
      } else {
        tableData.value.push({ ...form })
        ElMessage.success('新增成功')
      }
      dialogVisible.value = false
    } catch (error) {
      console.log('表单验证失败', error)
    }
  }
  
  onMounted(() => {
    loadData()
  })
  </script>
  
  <style scoped>
  .project-info {
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
  .dialog-form .el-form-item {
    margin-bottom: 22px;
  }
  </style>