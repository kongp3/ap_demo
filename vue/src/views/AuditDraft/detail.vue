<template>
  <div class="draft-detail">
    <!-- 基本信息 -->
    <el-card class="section-card" shadow="never">
      <div class="section-title">底稿基本信息</div>
      <el-form :model="draftForm" label-width="120px" :disabled="isView" :rules="rules" ref="formRef">
        <el-row :gutter="20">
          <el-col :span="12">
            <el-form-item label="项目名称" prop="project_name">
              <el-select
                v-model="draftForm.project_name"
                filterable
                remote
                reserve-keyword
                placeholder="请输入项目名称"
                :remote-method="remoteProjectSearch"
                :loading="projectLoading"
                style="width: 100%"
                :disabled="true"
              >
                <el-option
                  v-for="item in projectOptions"
                  :key="item.project_code"
                  :label="item.project_name"
                  :value="item.project_name"
                />
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="底稿名称" prop="draft_name">
              <el-input v-model="draftForm.draft_name" placeholder="请输入底稿名称" />
            </el-form-item>
          </el-col>
        </el-row>
        <el-row :gutter="20">
          <el-col :span="12">
            <el-form-item label="底稿编号" prop="draft_code">
              <el-input v-model="draftForm.draft_code" placeholder="请输入底稿编号" />
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="被审计单位" prop="audit_unit">
              <el-select v-model="draftForm.audit_unit" placeholder="请选择被审计单位" allow-create filterable>
                <el-option v-for="item in unitList" :key="item.code" :label="item.organization" :value="item.organization" />
              </el-select>
            </el-form-item>
          </el-col>
        </el-row>
        <el-row :gutter="20">
          <el-col :span="12">
            <el-form-item label="取证人" prop="collector">
              <el-input v-model="draftForm.collector" placeholder="请输入取证人" />
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="审计事项" prop="audit_items">
              <el-select v-model="draftForm.audit_items" multiple placeholder="请选择审计事项">
                <el-option v-for="item in allAuditItems" :key="item" :label="item" :value="item" />
              </el-select>
            </el-form-item>
          </el-col>
        </el-row>
        <el-row :gutter="20">
          <el-col :span="12">
            <el-form-item label="创建日期" prop="create_time">
              <el-date-picker v-model="draftForm.create_time" type="datetime" placeholder="请选择创建日期" style="width: 100%" value-format="YYYY-MM-DD HH:mm:ss" />
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="最后修改日期" prop="update_time">
              <el-date-picker v-model="draftForm.update_time" type="datetime" placeholder="请选择最后修改日期" style="width: 100%" value-format="YYYY-MM-DD HH:mm:ss" />
            </el-form-item>
          </el-col>
        </el-row>
        <el-row :gutter="20">
          <el-col :span="12">
            <el-form-item label="问题个数" prop="issue_num">
              <el-input v-model="draftForm.issue_num" placeholder="请输入问题个数" />
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="风险模版" prop="risk_tpl">
              <el-select v-model="draftForm.risk_tpl" placeholder="请选择风险模版">
                <el-option v-for="item in riskTplOptions" :key="item" :label="item" :value="item" />
              </el-select>
            </el-form-item>
          </el-col>
        </el-row>
      </el-form>
    </el-card>
    <!-- 审计过程信息 -->
    <el-card class="section-card" shadow="never" style="margin-top: 20px;">
      <div class="section-title">审计过程信息</div>
      <el-form :model="draftForm" label-width="120px" :disabled="isView">
        <el-row :gutter="20">
          <el-col :span="24">
            <el-form-item label="审计过程" prop="process">
              <el-input type="textarea" v-model="draftForm.process" :rows="8" placeholder="请输入审计过程" />
            </el-form-item>
          </el-col>
        </el-row>
        <el-row :gutter="20">
          <el-col :span="24">
            <el-form-item label="审计结论" prop="conclusion">
              <el-input type="textarea" v-model="draftForm.conclusion" :rows="8" placeholder="请输入审计结论" />
            </el-form-item>
          </el-col>
        </el-row>
        <el-row :gutter="20">
          <el-col :span="24" style="display: flex; justify-content: end; align-items: center; margin-top: 20px;"> 
            <el-button v-if="!isView" type="primary" size="small" @click="handleAddIssue">添加问题</el-button>
          </el-col>
          <el-col :span="24">
            <el-form-item label="审计问题" prop="conclusion">
              <el-table :data="draftForm.customers" style="width: 100%; margin-top: 10px;">
                <el-table-column type="index" label="序号" width="60" />
                <el-table-column prop="issue_title" label="审计问题" min-width="200" />
                <el-table-column prop="level" label="风险等级" width="100" />
                <el-table-column prop="finder" label="问题发现人" width="160" />
                <el-table-column label="操作" width="220">
                  <template #default="scope">
                    <el-button type="info" link @click="handleViewIssue(scope.row)">查看</el-button>
                    <el-button v-if="!isView" type="primary" link @click="handleEditIssue(scope.row)">编辑</el-button>
                    <el-button v-if="!isView" type="danger" link @click="handleDeleteIssue(scope.row)">删除</el-button>
                  </template>
                </el-table-column>
              </el-table>
            </el-form-item>
          </el-col>
        </el-row>
      </el-form>
    </el-card>
    <!-- 问题弹窗保持不变 -->
    <el-dialog v-model="issueDialogVisible" :title="issueDialogTitle" width="1000px" :close-on-click-modal="false">
      <el-form :model="issueForm" label-width="120px" style="max-width: 900px" :disabled="issueDialogMode==='view'">
        <!-- <el-form-item label="客商名称" prop="customer_name">
          <el-input v-model="issueForm.customer_name" placeholder="请输入客商名称" />
        </el-form-item> -->
        <el-form-item label="风险等级" prop="level">
          <el-select v-model="issueForm.level" placeholder="请选择风险等级">
            <el-option label="高风险" value="高风险" />
            <el-option label="中风险" value="中风险" />
            <el-option label="低风险" value="低风险" />
          </el-select>
        </el-form-item>
        <el-form-item label="问题标题" prop="issue_title">
          <el-input v-model="issueForm.issue_title" placeholder="请输入问题标题" />
        </el-form-item>
        <el-form-item label="问题描述" prop="issue_desc">
          <el-input type="textarea" v-model="issueForm.issue_desc" :rows="6" placeholder="请输入问题描述" />
        </el-form-item>
        <el-form-item label="审计建议" prop="suggest">
          <el-input type="textarea" v-model="issueForm.suggest" :rows="6" placeholder="请输入审计建议" />
        </el-form-item>
        <el-form-item label="附件" prop="attach">
          <div style="display: flex; justify-content: end; align-items: center; width: 100%;">
            <el-upload
              v-if="issueDialogMode !== 'view'"
              :show-file-list="false"
              :before-upload="handleIssueAttachUpload"
            >
              <el-button type="primary" size="small">上传附件</el-button>
            </el-upload>
          </div>
          <el-table :data="issueForm.attach" style="width: 100%; margin-top: 8px;">
            <el-table-column prop="filename" label="附件名称" min-width="120" />
            <el-table-column prop="filesize" label="附件大小" width="100" />
            <el-table-column prop="upload_time" label="上传时间" width="200" />
            <el-table-column label="操作" width="120">
              <template #default="scope">
                <el-button type="primary" link @click="handleDownloadAttach(scope.row)">下载</el-button>
                <el-button v-if="issueDialogMode !== 'view'" type="danger" link @click="handleDeleteAttach(scope.row)">删除</el-button>
              </template>
            </el-table-column>
          </el-table>
        </el-form-item>
      </el-form>
      <template #footer>
        <span class="dialog-footer">
          <el-button @click="issueDialogVisible = false">取消</el-button>
          <el-button v-if="issueDialogMode!=='view'" type="primary" @click="handleIssueSubmit">确定</el-button>
        </span>
      </template>
    </el-dialog>
  </div>
  <div class="footer-btns">
    <el-button type="default" @click="$router.back()">返回</el-button>
    <el-button type="primary" @click="handleSubmit">保存</el-button>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted, computed, onBeforeUnmount, onActivated, onDeactivated } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { draftList } from './mock.js'
import { ElMessage } from 'element-plus'
import { fetchDraftInfo, fetchAuditProcess, fetchAuditDetailById } from '@/api/auditDraftApi'
import { projectList } from '../ProjectInfo/mock.js'
import { unitList } from '../ProjectMembers/mock.js'

const route = useRoute()
const router = useRouter()
const mode = ref(route.query.mode || 'add')
const isView = computed(() => mode.value === 'view')

const riskTplOptions = [
  '客商综合分析',
  '账龄综合分析',
  '应收账款综合占比分析',
  '周转率分析',
  '坏账准备分析'
]
const allAuditItems = ['客商信息', '账龄分析', '应收账款综合占比']

const draftForm = reactive({
  project_name: '',
  draft_name: '',
  audit_unit: '',
  audit_items: [],
  collector: '',
  issue_num: 0,
  create_time: '',
  update_time: '',
  risk_tpl: '',
  process: '',
  conclusion: '',
  customers: []
})

const issueDialogVisible = ref(false)
const issueDialogTitle = ref('')
const issueDialogMode = ref('add') // add/edit/view
const issueForm = reactive({
  customer_name: '',
  level: '',
  issue_title: '',
  issue_desc: '',
  suggest: '',
  finder: '',
  attach: []
})
let currentIssueIndex = -1

const projectOptions = ref([])
const projectLoading = ref(false)
function remoteProjectSearch(query) {
  if (!query) {
    projectOptions.value = projectList
    return
  }
  projectLoading.value = true
  setTimeout(() => {
    projectOptions.value = projectList.filter(item => item.project_name.includes(query))
    projectLoading.value = false
  }, 300)
}

// 监听AI助手关闭事件，mode=add时自动拉取接口数据
function handleAIPopoverClose() {
  console.log('AI助手关闭事件触发', mode.value, route.fullPath)
  if (mode.value === 'add') {
    loadDraftInfoFromApi()
    loadAuditProcessFromApi()
  }
}

const formRef = ref()
const rules = {
  project_name: [
    { required: true, message: '请选择项目名称', trigger: 'change' }
  ],
  draft_name: [
    { required: true, message: '请输入底稿名称', trigger: 'blur' }
  ],
  draft_code: [
    { required: true, message: '请输入底稿编号', trigger: 'blur' }
  ],
  audit_unit: [
    { required: true, message: '请选择被审计单位', trigger: 'change' }
  ],
  audit_items: [
    { required: true, message: '请选择审计事项', trigger: 'change' }
  ]
}

onMounted(() => {
  // 1. 获取draft_code
  const draft_code = route.query.draft_code
  if (draft_code) {
    // 2. 查找mock数据
    const draft = draftList.find(item => item.draft_code === draft_code)
    if (draft) {
      // 3. 回显数据到draftForm
      Object.assign(draftForm, JSON.parse(JSON.stringify(draft)))
    }
  }
  // 新增时，项目名称默认取全局面包屑选中项目且不可修改
  if (mode.value === 'add') {
    const savedCode = localStorage.getItem('global_project_code')
    if (savedCode) {
      // 获取project_name
      const project = projectList.find(p => p.project_code === savedCode)
      if (project) {
        draftForm.project_name = project.project_name
        draftForm.audit_unit = project.audit_unit // 自动带出
      }
    }
  }
  window.addEventListener('ai-popover-close', handleAIPopoverClose)
})
onBeforeUnmount(() => {
  window.removeEventListener('ai-popover-close', handleAIPopoverClose)
})
onActivated(() => {
  window.addEventListener('ai-popover-close', handleAIPopoverClose)
})
onDeactivated(() => {
  window.removeEventListener('ai-popover-close', handleAIPopoverClose)
})

// 拉取底稿基本信息
async function loadDraftInfoFromApi() {
  try {
    const { data } = await fetchDraftInfo()
    draftForm.project_name = data.project_name || ''
    draftForm.draft_name = data.name || ''
    draftForm.draft_code = data.code || ''
    draftForm.audit_unit = data.company_name || ''
    draftForm.audit_items = data.focus ? [data.focus] : []
    draftForm.collector = data.operator || ''
    draftForm.create_time = data.create_date || ''
    draftForm.update_time = data.update_date || ''
    draftForm.risk_tpl = data.model || ''
    draftForm.issue_num = 0
  } catch (e) {
    ElMessage.error('底稿信息接口请求失败')
  }
}
// 拉取审计过程信息
async function loadAuditProcessFromApi() {
  try {
    const { data } = await fetchAuditProcess()
    draftForm.process = data.process || ''
    draftForm.conclusion = data.conclusion || ''
    draftForm.customers = (data.customer || []).map(item => ({
      ...item,
      issue_title: (item.customer_name ? item.customer_name + ' - ' : '') + (item.title || ''),
      finder: 'AI审计助手',
      attach: []
    }))
    draftForm.issue_num = draftForm.customers.length
  } catch (e) {
    ElMessage.error('审计过程接口请求失败')
  }
}

function handleAddIssue() {
  issueDialogTitle.value = '添加问题'
  issueDialogMode.value = 'add'
  resetIssueForm()
  issueDialogVisible.value = true
  currentIssueIndex = -1
}
async function handleEditIssue(row) {
  issueDialogTitle.value = '修改问题'
  issueDialogMode.value = 'edit'
  if (mode.value === 'add' && row.detail_id) {
    await loadAuditDetailFromApi(row.detail_id)
  } else {
    Object.assign(issueForm, row)
  }
  issueDialogVisible.value = true
  currentIssueIndex = draftForm.customers.findIndex(i => i === row)
}
async function handleViewIssue(row) {
  issueDialogTitle.value = '问题详情'
  issueDialogMode.value = 'view'
  if (mode.value === 'add' && row.detail_id) {
    await loadAuditDetailFromApi(row.detail_id)
  } else {
    Object.assign(issueForm, row)
  }
  issueDialogVisible.value = true
  currentIssueIndex = draftForm.customers.findIndex(i => i === row)
}
function handleDeleteIssue(row) {
  const idx = draftForm.customers.findIndex(i => i === row)
  if (idx > -1) draftForm.customers.splice(idx, 1)
}
function resetIssueForm() {
  issueForm.customer_name = ''
  issueForm.level = ''
  issueForm.issue_title = ''
  issueForm.issue_desc = ''
  issueForm.suggest = ''
  issueForm.attach = []
}
function handleIssueSubmit() {
  if (issueDialogMode.value === 'add') {
    draftForm.customers.push({ ...issueForm })
  } else if (issueDialogMode.value === 'edit' && currentIssueIndex > -1) {
    draftForm.customers[currentIssueIndex] = { ...issueForm }
  }
  issueDialogVisible.value = false
}
function handleIssueAttachUpload(file) {
  issueForm.attach.push({
    filename: file.name,
    filesize: (file.size / 1024).toFixed(2) + 'KB', // 由B转为KB
    upload_time: new Date().toISOString().slice(0, 19).replace('T', ' ')
  })
  return false // 阻止自动上传
}
function handleDeleteAttach(row) {
  const idx = issueForm.attach.findIndex(f => f.filename === row.filename && f.upload_time === row.upload_time)
  if (idx > -1) issueForm.attach.splice(idx, 1)
}
function handleDownloadAttach(row) {
  // 模拟下载
  ElMessage.info('下载：' + row.filename)
}

// 拉取审计问题详情
async function loadAuditDetailFromApi(detail_id) {
  try {
    const { data } = await fetchAuditDetailById(detail_id)
    issueForm.customer_name = data.customer_name || ''
    issueForm.level = data.level || ''
    issueForm.issue_title = data.title || ''
    issueForm.issue_desc = data.desc || ''
    issueForm.suggest = data.suggest || ''
    issueForm.attach = (data.attach || []).map(a => ({
      filename: a.name,
      filesize: a.filesize,
      upload_time: a.dateTime,
      url: a.url
    }))
  } catch (e) {
    ElMessage.error('审计问题详情接口请求失败')
  }
}

function handleSubmit() {
  formRef.value.validate((valid) => {
    if (!valid) return
    // 保存到localStorage
    const newDraft = { ...draftForm }
    let localDrafts = JSON.parse(localStorage.getItem('draftList') || '[]')
    // 避免重复添加
    if (!localDrafts.find(d => d.draft_code === newDraft.draft_code)) {
      localDrafts.push(newDraft)
      localStorage.setItem('draftList', JSON.stringify(localDrafts))
    }
    // 返回index页面
    router.push({ path: '/audit-draft' })
  })
}
</script>

<style scoped>
.draft-detail {
  padding: 0;
}
.section-card {
  margin-bottom: 16px;
}
.section-title {
  font-weight: bold;
  font-size: 16px;
  margin-bottom: 12px;
}
.dialog-footer {
  display: flex;
  justify-content: flex-end;
  gap: 12px;
}
.footer-btns {
  display: flex;
  justify-content: center;
  margin-top: 32px;
}
</style> 