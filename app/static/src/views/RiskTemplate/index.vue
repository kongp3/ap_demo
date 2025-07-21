<template>
  <div class="risk-template">
    <ProjectBreadcrumb :main="'审计配置'" :sub="'风险模版'" projectless />
    <el-card class="search-card" shadow="never">
      <el-form class="search-form" :model="searchForm" inline>
        <el-form-item label="模版名称">
          <el-input
            v-model="searchForm.templateName"
            placeholder="请输入模版名称"
            clearable
            style="width: 220px"
            @keyup.enter="handleSearch"
          />
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
          <span>模版列表</span>
          <el-button type="primary" @click="handleAdd">新增模版</el-button>
        </div>
      </template>

      <el-table
        :data="pagedData"
        style="width: 100%"
        v-loading="loading"
      >
        <el-table-column type="index" label="序号" width="60" />
        <el-table-column prop="id" label="模版编码" width="200" />
        <el-table-column prop="name" label="模版名称" min-width="200" />
        <el-table-column prop="creator" label="创建人" width="120" />
        <el-table-column prop="create_time" label="创建日期" width="200" />
        <el-table-column prop="status" label="是否启用" width="100">
          <template #default="{ row }">
            <el-tag :type="row.status === '启用' ? 'success' : 'info'">
              {{ row.status }}
            </el-tag>
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
import { ref, reactive, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { ElMessage, ElMessageBox } from 'element-plus'
import { getAllTemplates } from './mock.js'
import ProjectBreadcrumb from '@/components/ProjectBreadcrumb.vue'

const router = useRouter()

// 响应式数据
const loading = ref(false)
const tableData = ref([])
const currentPage = ref(1)
const pageSize = ref(10)

// 搜索表单
const searchForm = reactive({
  templateName: ''
})

// 计算属性
const filteredData = computed(() => {
  let data = tableData.value
  if (searchForm.templateName) {
    data = data.filter(item => 
      item.name && item.name.includes(searchForm.templateName)
    )
  }
  return data
})

const pagedData = computed(() => {
  const start = (currentPage.value - 1) * pageSize.value
  return filteredData.value.slice(start, start + pageSize.value)
})

// 搜索
const handleSearch = () => {
  currentPage.value = 1
}

// 重置
const handleReset = () => {
  searchForm.templateName = ''
  currentPage.value = 1
}

// 分页变化
const handlePageChange = (page) => {
  currentPage.value = page
}

// 新增
const handleAdd = () => {
  router.push('/risk-template/detail')
}

// 查看
const handleView = (row) => {
  router.push({
    path: '/risk-template/detail',
    query: { 
      model_id: row.id,
      mode: 'view'
    }
  })
}

// 编辑
const handleEdit = (row) => {
  router.push({
    path: '/risk-template/detail',
    query: { 
      model_id: row.id,
      mode: 'edit'
    }
  })
}

// 删除
const handleDelete = async (row) => {
  try {
    await ElMessageBox.confirm(`确定要删除模版"${row.name}"吗？`, '提示', {
      confirmButtonText: '确定',
      cancelButtonText: '取消',
      type: 'warning'
    })
    
    // 这里调用删除API
    ElMessage.success('删除成功')
    loadData()
  } catch (error) {
    // 用户取消删除
  }
}

// 加载数据
const loadData = () => {
  loading.value = true
  
  // 模拟API调用
  setTimeout(() => {
    // 使用mock数据
    const mockData = getAllTemplates()
    
    // 添加创建人字段（mock数据中没有，这里模拟）
    const dataWithCreator = mockData.map(item => ({
      ...item,
      creator: '系统管理员'
    }))
    
    tableData.value = dataWithCreator
    loading.value = false
  }, 500)
}

// 页面加载时获取数据
onMounted(() => {
  loadData()
})
</script>

<style scoped>
.risk-template {
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