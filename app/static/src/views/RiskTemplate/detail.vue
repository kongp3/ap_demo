<template>
  <div class="risk-template-detail">
    <ProjectBreadcrumb :main="'审计配置'" :sub="'风险模版'" projectless />
    <el-card class="section-card" shadow="never">
      <el-form :model="templateInfo" label-width="100px" :disabled="isViewMode">
        <el-row :gutter="20">
          <el-col :span="12">
            <el-form-item label="模版名称" prop="name">
              <el-input 
                v-model="templateInfo.name" 
                placeholder="请输入模版名称"
              />
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="创建人">
              <el-input 
                v-model="templateInfo.creator" 
                placeholder="系统管理员"
                readonly
              />
            </el-form-item>
          </el-col>
        </el-row>
        <el-row :gutter="20">
          <el-col :span="12">
            <el-form-item label="创建时间">
              <el-input 
                v-model="templateInfo.create_time" 
                placeholder="2024-01-15 10:30:00"
                readonly
              />
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="是否启用">
              <el-switch
                v-model="templateInfo.status"
                :active-value="'启用'"
                :inactive-value="'禁用'"
                :disabled="isViewMode"
              />
            </el-form-item>
          </el-col>
        </el-row>
      </el-form>
    </el-card>

    <el-card class="section-card" shadow="never" style="margin-top: 20px;">
      <template #header>
        <div class="card-header">
          <span>模版配置</span>
          <el-button v-if="!isViewMode" type="primary" size="small" @click="handleAddRule">
            <el-icon><Plus /></el-icon>
            新增规则
          </el-button>
        </div>
      </template>
      <el-table
        :data="ruleData"
        style="width: 100%; margin-top: 10px;"
        v-loading="loading"
      >
        <el-table-column type="index" label="序号" width="60" />
        <el-table-column prop="dimension" label="维度" width="180">
          <template #default="{ row }">
            <el-select 
              v-model="row.dimension" 
              placeholder="请选择维度"
              :disabled="isViewMode"
              style="width: 100%"
            >
              <el-option
                v-for="option in dimensionOptions"
                :key="option.value"
                :label="option.label"
                :value="option.value"
              />
            </el-select>
          </template>
        </el-table-column>
        <el-table-column prop="index" label="维度别名" width="240">
          <template #default="{ row }">
            <el-input 
              v-model="row.index" 
              placeholder="请输入维度别名"
              :disabled="isViewMode"
            />
          </template>
        </el-table-column>
        <el-table-column prop="desc" label="描述" min-width="120">
          <template #default="{ row }">
            <el-input 
              v-model="row.desc" 
              placeholder="请输入描述"
              :disabled="isViewMode"
            />
          </template>
        </el-table-column>
        <el-table-column prop="level" label="等级" width="140">
          <template #default="{ row }">
            <el-input 
              v-model="row.level" 
              placeholder="请输入等级"
              :disabled="isViewMode"
            />
          </template>
        </el-table-column>
        <el-table-column prop="score" label="分数" width="140">
          <template #default="{ row }">
            <el-input-number 
              v-model="row.score" 
              :min="0" 
              :max="100"
              :disabled="isViewMode"
              style="width: 100%"
            />
          </template>
        </el-table-column>
        <el-table-column prop="weight" label="权重" width="160">
          <template #default="{ row }">
            <el-input-number 
              v-model="row.weight" 
              :min="0" 
              :max="1" 
              :precision="2"
              :step="0.01"
              :disabled="isViewMode"
              style="width: 100%"
            />
          </template>
        </el-table-column>
        <el-table-column label="操作" width="80" v-if="!isViewMode">
          <template #default="{ row, $index }">
            <el-button type="danger" link @click="handleDeleteRule($index)">
              <el-icon><Delete /></el-icon>
              删除
            </el-button>
          </template>
        </el-table-column>
      </el-table>
    </el-card>

    <div class="footer-btns">
      <el-button type="default" @click="handleReturn">返回</el-button>
      <el-button 
        v-if="!isViewMode" 
        type="primary" 
        @click="handleSave"
      >
        保存
      </el-button>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, computed, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { ElMessage } from 'element-plus'
import {
  Plus,
  Delete
} from '@element-plus/icons-vue'
import { getTemplateDetail, getTemplateById, dimensionOptions } from './mock.js'

const router = useRouter()
const route = useRoute()

// 响应式数据
const loading = ref(false)
const isViewMode = ref(false)
const modelId = ref(null)

// 模版信息
const templateInfo = reactive({
  name: '',
  creator: '',
  create_time: '',
  status: '启用'
})

// 规则数据
const ruleData = ref([])

// 计算属性
const pageTitle = computed(() => {
  if (isViewMode.value) return '查看风险模版'
  if (modelId.value) return '编辑风险模版'
  return '新增风险模版'
})

// 新增规则
const handleAddRule = () => {
  ruleData.value.push({
    id: Date.now(), // 临时ID
    model_id: modelId.value || 1,
    dimension: '',
    index: '',
    desc: '',
    level: '',
    score: 0,
    weight: 0.1,
    remark: ''
  })
}

// 删除规则
const handleDeleteRule = (index) => {
  ruleData.value.splice(index, 1)
}

// 返回
const handleReturn = () => {
  router.push('/risk-template')
}

// 保存
const handleSave = () => {
  // 验证必填字段
  if (!templateInfo.name) {
    ElMessage.warning('请输入模版名称')
    return
  }

  if (!templateInfo.status) {
    ElMessage.warning('请选择是否启用')
    return
  }

  if (ruleData.value.length === 0) {
    ElMessage.warning('请至少添加一条规则')
    return
  }

  // 验证规则数据
  for (let i = 0; i < ruleData.value.length; i++) {
    const rule = ruleData.value[i]
    if (!rule.dimension || !rule.index || !rule.desc || !rule.level) {
      ElMessage.warning(`第${i + 1}条规则信息不完整`)
      return
    }
  }

  // 这里调用保存API
  ElMessage.success('保存成功')
  router.push('/risk-template')
}

// 加载数据
const loadData = () => {
  loading.value = true
  
  setTimeout(() => {
    if (modelId.value) {
      // 编辑或查看模式，加载模版信息
      const template = getTemplateById(modelId.value)
      if (template) {
        Object.assign(templateInfo, template)
      }
      
      // 加载规则数据
      const rules = getTemplateDetail(modelId.value)
      ruleData.value = rules.map(rule => ({ ...rule }))
    } else {
      // 新增模式，初始化空数据
      ruleData.value = []
    }
    
    loading.value = false
  }, 500)
}

// 页面加载时初始化
onMounted(() => {
  const query = route.query
  modelId.value = query.model_id ? parseInt(query.model_id) : null
  isViewMode.value = query.mode === 'view'
  
  loadData()
})
</script>

<style scoped>
.risk-template-detail {
  padding: 0;
}

.section-card {
  margin-bottom: 16px;
}

.section-title {
  font-size: 16px;
  font-weight: 600;
  color: #303133;
  margin-bottom: 16px;
  border-bottom: 1px solid #ebeef5;
  padding-bottom: 8px;
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.footer-btns {
  display: flex;
  justify-content: center;
  gap: 12px;
  margin-top: 20px;
  padding-top: 20px;
  border-top: 1px solid #ebeef5;
}
</style> 