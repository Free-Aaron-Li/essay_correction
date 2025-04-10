<!--
  Copyright (c) 2025. aaron.

  This program is under the GPL-3.0 license.
  if you have not received it or the program has several bugs, please let me know:
  <communicate_aaron@outlook.com>.
  -->
<script setup>
import {ref} from "vue"
import Dialog from './components/dialog.vue'
import RoleDialog from './components/role_dialog.vue'
import requestUtil, {getServerUrl} from '@/utils/request'
import {Search, Delete, DocumentAdd, Edit, Tools, RefreshRight} from "@element-plus/icons-vue/global";
import {ElMessage} from "element-plus";

const tableData = ref([
  {
    id: 1,
    username: '',
    password: '',
    avatar: '',
    email: '',
    phone: '',
    status: 1,
    created_at: '',
    last_login_time: '',
    remark: '',
    role_list: [],
    user_type: 0,
  }
])
const total = ref(0)
const queryForm = ref({
  query: '',
  pageNum: 1,
  pageSize: 10,
})
const dialogVisible = ref(false)
const dialogTitle = ref('')
const id = ref(-1)
const multipleSelection = ref([])
const delBtnStatus = ref(true)
const roleDialogVisible = ref(false)
const RoleList = ref([])

const handleSelectionChange = (selection) => {
  multipleSelection.value = selection
  delBtnStatus.value = selection.length === 0
}

const handleDialogValue = (userId) => {
  if (userId) {
    id.value = userId
    dialogTitle.value = '用户修改'
  } else {
    id.value = -1
    dialogTitle.value = '用户添加'
  }
  dialogVisible.value = true
}

const initUserList = async () => {
  const res = await requestUtil.post('user/search', queryForm.value)
  tableData.value = res.data.user_list
  total.value = res.data.total
}

const handleSizeChange = (pageSize) => {
  queryForm.value.pageSize = pageSize
  queryForm.value.pageNum = 1
  initUserList()
}

const handleCurrentChange = (pageNum) => {
  queryForm.value.pageNum = pageNum
  initUserList()
}

const handleDelete = async (id) => {
  let ids = []
  if (id) {
    ids.push(id)
  } else {
    multipleSelection.value.forEach(item => {
      ids.push(item.id)
    })
  }
  const res = await requestUtil.del('user/action', ids)
  if (res.data.code === 200) {
    ElMessage({
      type: 'success',
      message: '删除成功！'
    })
    await initUserList()
  } else {
    ElMessage({
      type: 'error',
      message: res.data.msg
    })
  }
}

const handleResetPassword = async (id) => {
  const res = await requestUtil.get('user/reset_pwd_default?id=' + id)
  if (res.data.code === 200) {
    ElMessage({
      type: 'success',
      message: '重置密码成功！'
    })
    await initUserList()
  } else {
    ElMessage({
      type: 'error',
      message: res.data.msg
    })
  }
}

const statusChangeHandle = async (row) => {
  let res = await requestUtil.post('user/status', {id: row.id, status: row.status})
  if (res.data.code === 200) {
    ElMessage({
      type: 'success',
      message: '状态切换成功！'
    })
  } else {
    ElMessage({
      type: 'error',
      message: res.data.msg
    })
  }
  await initUserList()
}

const handleRoleDialogValue = (userId, roleList) => {
  id.value = userId
  RoleList.value = roleList
  roleDialogVisible.value = true
}

initUserList()
</script>

<template>
  <div class="app-container">
    <!-- 搜索 -->
    <el-row :gutter="20" class="header">
      <el-col :span="7">
        <el-input v-model="queryForm.query" clearable placeholder="请输入用户名..."></el-input>
      </el-col>
      <el-button :icon="Search" type="primary" @click="initUserList">搜索</el-button>
      <el-button :icon="DocumentAdd" type="success" @click="handleDialogValue()">新增</el-button>
      <el-popconfirm title="您确定批量删除这些记录吗？" @confirm="handleDelete(null)">
        <template #reference>
          <el-button :disabled="delBtnStatus" :icon="Delete" type="danger">批量删除</el-button>
        </template>
      </el-popconfirm>
    </el-row>

    <!--  表格 -->
    <el-table :data="tableData" stripe style="width: 100%" @selection-change="handleSelectionChange">
      <el-table-column type="selection" width="55"/>

      <el-table-column align="center" label="头像" prop="avatar" width="80">
        <template v-slot="scope">
          <img :src="getServerUrl()+'media/user_avatar/'+scope.row.avatar" alt="avatar" height="50" width="50"/>
        </template>
      </el-table-column>

      <el-table-column align="center" label="用户名" prop="username" width="100"/>

      <el-table-column align="center" label="角色" prop="roles" width="200">
        <template v-slot="scope">
          <el-tag v-for="item in scope.row.role_list" size="small" type="warning"> {{ item.name }}</el-tag>
        </template>
      </el-table-column>

      <el-table-column align="center" label="邮箱" prop="email" width="200"/>
      <el-table-column align="center" label="手机号" prop="phone" width="120"/>

      <el-table-column align="center" label="状态" prop="status" width="200">
        <template v-slot="{row}">
          <el-switch v-model="row.status" :active-value="1" :inactive-value="0"
                     active-text="正常" inactive-text="禁用" @change="statusChangeHandle(row)"></el-switch>
        </template>
      </el-table-column>

      <el-table-column align="center" label="创建时间" prop="created_at" width="200"/>
      <el-table-column align="center" label="最后登录时间" prop="last_login_time" width="200"/>
      <el-table-column label="备注" prop="remark"/>

      <!-- 操作 -->
      <el-table-column align="center" fixed="right" label="操作" prop="action" width="400">
        <template v-slot="scope">
          <el-button :icon="Tools" type="primary" @click="handleRoleDialogValue(scope.row.id,scope.row.roleList)">分配角色
          </el-button>

          <!-- 操作修改，不能为管理员 -->
          <el-popconfirm v-if="scope.row.user_type!==0" title="您确定要对这个用户重置密码吗？"
                         @confirm="handleResetPassword(scope.row.id)">
            <template #reference>
              <el-button :icon="RefreshRight" type="warning">重置密码</el-button>
            </template>
          </el-popconfirm>
          <el-button v-if="scope.row.user_type!==0" :icon="Edit" type="primary"
                     @click="handleDialogValue(scope.row.id)"></el-button>
          <el-popconfirm v-if="scope.row.user_type!==0" title="您确定要删除这条记录吗？"
                         @confirm="handleDelete(scope.row.id)">
            <template #reference>
              <el-button :icon="Delete" type="danger"/>
            </template>
          </el-popconfirm>
        </template>
      </el-table-column>
    </el-table>
    <el-pagination
        v-model:current-page="queryForm.pageNum"
        v-model:page-size="queryForm.pageSize"
        :page-sizes="[100, 200, 300, 400]"
        :total="total"
        layout="total, sizes, prev, pager, next, jumper"
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
    />
    <Dialog :id="id" v-model="dialogVisible" :dialogTitle="dialogTitle" :dialogVisible="dialogVisible"
            @initUserList="initUserList"></Dialog>
    <RoleDialog :id="id" v-model="roleDialogVisible" :RoleList="RoleList" :roleDialogVisible="roleDialogVisible"
                @initUserList="initUserList"></RoleDialog>
  </div>
</template>

<style lang="scss" scoped>
.header {
  padding-bottom: 16px;
  box-sizing: border-box;
}

.el-pagination {
  float: right;
  padding: 20px;
  box-sizing: border-box;
}

::v-deep th.el-table__cell {
  word-break: break-word;
  background-color: #f8f8f9 !important;
  color: #515a6e;
  height: 40px;
  font-size: 13px;

}

.el-tag--small {
  margin-left: 5px;
}
</style>