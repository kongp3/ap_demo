<template>
  <div class="plan-detail">
    <el-card class="section-card" shadow="never">
      <div class="section-title">基本信息</div>
      <el-form :model="planForm" label-width="100px" :disabled="isView">
        <el-row :gutter="20">
          <el-col :span="12">
            <el-form-item label="项目名称" prop="project_name">
              <el-select
                v-model="planForm.project_name"
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
        </el-row>
        <el-row :gutter="20">
          <el-col :span="12">
            <el-form-item label="方案名称" prop="plan_name">
              <el-input v-model="planForm.plan_name" placeholder="请输入方案名称" />
            </el-form-item>
          </el-col>
        </el-row>
        <el-row :gutter="20">
          <el-col :span="6">
            <el-form-item label="编制日期" prop="date">
              <el-date-picker v-model="planForm.date" type="date" placeholder="请选择编制日期" style="width: 100%" value-format="YYYY-MM-DD" />
            </el-form-item>
          </el-col>
        </el-row>
        <el-row :gutter="20">
          <el-col :span="12">
            <el-form-item label="编制依据" prop="source">
              <el-input type="textarea" v-model="planForm.source" placeholder="请输入编制依据" :rows="6" />
            </el-form-item>
          </el-col>
        </el-row>
        <el-row :gutter="20">
          <el-col :span="12">
            <el-form-item label="备注" prop="remark">
              <el-input type="textarea" v-model="planForm.remark" placeholder="请输入备注" :rows="6" />
            </el-form-item>
          </el-col>
        </el-row>
      </el-form>
    </el-card>

    <el-card class="section-card" shadow="never" style="margin-top: 20px;">
      <div class="section-title">方案事项</div>
      <el-row :gutter="20">
        <el-col :span="4">
          <el-tree
            :data="treeData"
            :props="treeProps"
            node-key="item_code"
            highlight-current
            default-expand-all
            @node-click="handleNodeClick"
            :expand-on-click-node="false"
            :disabled="isView"
          >
            <template #default="{ node, data }">
              <span>{{ data.item_name }}</span>
              <span v-if="!isView" style="margin-left: 8px;">
                <el-button size="mini" type="text" @click.stop="addNode(data)">添加</el-button>
                <el-button size="mini" type="text" @click.stop="removeNode(data, node)">删除</el-button>
              </span>
            </template>
          </el-tree>
        </el-col>
        <el-col :span="20">
          <el-card v-if="currentLeaf" class="item-detail-card" shadow="never">
            <div class="section-title">事项详情</div>
            <el-form :model="currentLeaf.details" label-width="180px" :disabled="isView">
              <el-form-item label="事项编号" prop="item_code">
                <el-input v-model="currentLeaf.details.item_code" placeholder="请输入事项编号" />
              </el-form-item>
              <el-form-item label="事项名称" prop="item_name">
                <el-input v-model="currentLeaf.details.item_name" placeholder="请输入事项名称" />
              </el-form-item>
              <el-form-item label="审计程序和方法" prop="method">
                <el-input type="textarea" v-model="currentLeaf.details.method" placeholder="请输入审计程序和方法" :rows="4" />
              </el-form-item>
              <el-form-item label="相关法律法规和监管规定" prop="source">
                <el-input type="textarea" v-model="currentLeaf.details.source" placeholder="请输入相关法律法规和监管规定" :rows="4" />
              </el-form-item>
              <el-form-item label="需提供材料" prop="material">
                <el-input type="textarea" v-model="currentLeaf.details.material" placeholder="请输入需提供材料" :rows="4" />
              </el-form-item>
            </el-form>
          </el-card>
          <el-empty v-else description="请选择左侧叶子节点进行编辑" />
        </el-col>
      </el-row>
    </el-card>

    <el-card class="section-card" shadow="never" style="margin-top: 20px;">
      <div class="section-title">附件列表</div>
      <div class="section-title" style="display: flex; justify-content: end; align-items: center;">
        <div v-if="!isView">
          <el-upload
            :show-file-list="false"
            :before-upload="handleUpload"
          >
            <el-button type="primary" size="small">添加附件</el-button>
          </el-upload>
        </div>
      </div>
      <el-table :data="fileList" style="width: 100%; margin-top: 10px;">
        <el-table-column prop="name" label="附件名称" min-width="180" />
        <el-table-column prop="size" label="附件大小" width="100" />
        <el-table-column prop="creator" label="创建人" width="100" />
        <el-table-column prop="create_time" label="创建时间" width="160" />
        <el-table-column label="操作" width="180">
          <template #default="scope">
            <el-button type="primary" link @click="handleDownload(scope.row)">下载</el-button>
            <el-button v-if="!isView" type="danger" link @click="handleRemoveFile(scope.row)">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
    </el-card>
    <div class="footer-btns">
      <el-button type="default" @click="$router.back()">返回</el-button>
      <el-button type="primary" @click="handleSubmit">保存</el-button>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, computed, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { ElMessage, ElMessageBox } from 'element-plus'
import { auditPlanList } from './mock.js'
import { projectList } from '../ProjectInfo/mock.js'
import { projectNameList } from '../ProjectInfo/mock.js'

const route = useRoute()
const mode = ref(route.query.mode || 'add')
const isView = computed(() => mode.value === 'view')

const planForm = reactive({
  project_name: '',
  plan_name: '',
  date: '',
  source: '',
  remark: ''
})

// 审计事项树
const treeData = ref([])
const treeProps = { children: 'childs', label: 'item_name' }
const currentLeaf = ref(null)

// 附件列表
const fileList = ref([])

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

function getFirstLeaf(nodes) {
  if (!nodes) return null
  for (const node of nodes) {
    if (node.childs && node.childs.length > 0) {
      const found = getFirstLeaf(node.childs)
      if (found) return found
    } else {
      return node
    }
  }
  return null
}

onMounted(() => {
  if (route.query.plan_code) {
    const plan = auditPlanList.find(p => p.plan_code === route.query.plan_code)
    if (plan) {
      planForm.project_name = plan.project_name
      planForm.plan_name = plan.plan_name
      planForm.date = plan.date
      planForm.source = plan.source
      planForm.remark = plan.remark
      treeData.value = plan.items && plan.items.length > 0 ? plan.items : [
        { item_code: '03', item_name: '审计事项库', details: {}, childs: [] }
      ]
      fileList.value = plan.attach ? plan.attach.map(f => ({
        name: f.filename,
        size: (f.filesize / 1024).toFixed(2) + 'KB',
        creator: f.createor,
        create_time: f.create_date
      })) : []
    } else {
      treeData.value = [
        { item_code: '03', item_name: '审计事项库', details: {}, childs: [] }
      ]
      fileList.value = []
    }
  } else {
    // 新增时，项目名称默认选中当前面包屑项目
    const savedCode = localStorage.getItem('global_project_code')
    if (savedCode) {
      const project = projectNameList.find(p => p.project_code === savedCode)
      if (project) {
        planForm.project_name = project.project_name
      }
    }
    treeData.value = [
      { item_code: '03', item_name: '审计事项库', details: {}, childs: [] }
    ]
    fileList.value = []
  }
  // 默认选中第一个叶子节点
  setTimeout(() => {
    const leaf = getFirstLeaf(treeData.value)
    if (leaf) currentLeaf.value = leaf
  }, 0)
})

function handleNodeClick(data, node) {
  // 只允许叶子节点编辑
  if (!data.childs || data.childs.length === 0) {
    currentLeaf.value = data
  } else {
    currentLeaf.value = null
  }
}
function addNode(parent) {
  if (!parent.childs) parent.childs = []
  const newCode = parent.item_code + (parent.childs.length + 1)
  parent.childs.push({
    item_code: newCode,
    item_name: '新事项',
    details: {
      item_code: newCode,
      item_name: '新事项',
      method: '',
      source: '',
      material: ''
    },
    childs: []
  })
}
function removeNode(data, node) {
  ElMessageBox.confirm('确定要删除该节点及其所有子节点吗？', '提示', {
    confirmButtonText: '确定',
    cancelButtonText: '取消',
    type: 'warning',
  }).then(() => {
    const parent = node.parent.data
    if (parent.childs) {
      const idx = parent.childs.findIndex(i => i.item_code === data.item_code)
      if (idx > -1) parent.childs.splice(idx, 1)
      currentLeaf.value = null
    }
  }).catch(() => {})
}
// 附件相关
function handleUpload(file) {
  fileList.value.push({
    name: file.name,
    size: (file.size / 1024 / 1024).toFixed(2) + 'MB',
    creator: '张三',
    create_time: new Date().toISOString().slice(0, 16).replace('T', ' ')
  })
  ElMessage.success('上传成功')
  return false // 阻止自动上传
}
function handleRemoveFile(row) {
  const idx = fileList.value.findIndex(f => f.name === row.name)
  if (idx > -1) fileList.value.splice(idx, 1)
  ElMessage.success('删除成功')
}
function handleDownload(row) {
  ElMessage.info('模拟下载：' + row.name)
}
</script>

<style scoped>
.plan-detail {
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
.item-detail-card {
  margin-left: 10px;
}
.footer-btns {
  display: flex;
  justify-content: center;
  margin-top: 32px;
}
</style> 