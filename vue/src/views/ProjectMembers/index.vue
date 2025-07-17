<template>
  <div class="project-members">
    <el-card class="list-card" shadow="never">
      <template #header>
        <div class="card-header">
          <span>成员列表</span>
          <el-button type="primary" @click="handleAdd">新增成员</el-button>
        </div>
      </template>
      <el-table :data="pagedData" style="width: 100%" v-loading="loading">
        <el-table-column type="index" label="序号" width="60" />
        <el-table-column prop="username" label="成员姓名" min-width="120" />
        <el-table-column prop="role" label="项目角色" min-width="120" />
        <el-table-column prop="organization" label="所属审计机构" min-width="120" />
        <el-table-column label="操作" width="220" align="right">
          <template #default="scope">
            <el-button type="primary" link @click="handleEdit(scope.row)">修改</el-button>
            <el-button type="info" link @click="handleView(scope.row)">查看成员信息</el-button>
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

    <!-- 新增/查看/修改弹窗 -->
    <el-dialog
      v-model="dialogVisible"
      :title="dialogTitle"
      width="400px"
      :close-on-click-modal="false"
    >
      <el-form
        ref="formRef"
        :model="form"
        :rules="rules"
        label-width="100px"
        class="dialog-form"
      >
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
        <el-form-item label="所属审计机构" prop="organization">
          <el-input v-model="form.organization" placeholder="请输入所属审计机构" :disabled="dialogMode==='view'" />
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
import { ref, reactive, computed } from 'vue'
import { ElMessage, ElMessageBox } from 'element-plus'

const mockData = [
  { code: '1', username: '张三', role: '项目组长', organization: '集团审计部' },
  { code: '2', username: '李四', role: '项目主审', organization: 'A公司' },
  { code: '3', username: '王五', role: '项目成员', organization: 'B公司' }
]

const userOptions = ['张三', '李四', '王五', '赵六']
const roleOptions = ['项目组长', '项目主审', '项目组员']

const loading = ref(false)
const tableData = ref([...mockData])
const dialogVisible = ref(false)
const dialogTitle = ref('')
const dialogMode = ref('add') // add/edit/view
const currentCode = ref('')
const formRef = ref()
const form = reactive({
  username: '',
  role: '',
  organization: ''
})
const rules = {
  username: [ { required: true, message: '请选择成员姓名', trigger: 'change' } ],
  role: [ { required: true, message: '请选择项目角色', trigger: 'change' } ],
  organization: [ { required: true, message: '请输入所属审计机构', trigger: 'blur' } ]
}

// 分页
const currentPage = ref(1)
const pageSize = ref(10)
const pagedData = computed(() => {
  const start = (currentPage.value - 1) * pageSize.value
  return tableData.value.slice(start, start + pageSize.value)
})
function handlePageChange(page) {
  currentPage.value = page
}

function handleAdd() {
  dialogTitle.value = '新增成员'
  dialogMode.value = 'add'
  resetForm()
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
        organization: form.organization
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
</script>

<style scoped>
.project-members {
  padding: 0;
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