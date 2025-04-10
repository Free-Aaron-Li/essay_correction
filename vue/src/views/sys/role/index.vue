<!--
  Copyright (c) 2025. aaron.

  This program is under the GPL-3.0 license.
  if you have not received it or the program has several bugs, please let me know:
  <communicate_aaron@outlook.com>.
  -->
<script setup>
import {ref} from 'vue'
import Dialog from './components/dialog'
import MenuDialog from './components/menuDialog'
import requestUtil, {getServerUrl} from '@/utils/request'
import {Search, Delete, DocumentAdd, Edit, Tools, RefreshRight} from "@element-plus/icons-vue/global";
import {ElMessage} from "element-plus";

const total = ref(0)
const tableData = ref([])
const queryForm = ref({
  query: '',
  page_num: 1,
  page_size: 10
})

const initRoleList = async () => {
  const res = await requestUtil.post("role/search", queryForm.value)
  tableData.value = res.data.role_list;
  total.value = res.data.total;
}

const handleSizeChange = (pageSize) => {
  queryForm.value.page_num = 1;
  queryForm.value.page_size = pageSize;
  initRoleList();
}

const handleCurrentChange = (pageNum) => {
  queryForm.value.page_num = pageNum;
  initRoleList();
}

const id = ref(-1)
const dialogVisible = ref(false)
const dialogTitle = ref('')
const menuDialogVisible = ref(false)

const handleDialogValue = (roleId) => {
  if (roleId) {
    id.value = roleId
    dialogTitle.value = '角色修改'
  } else {
    id.value = -1
    dialogTitle.value = '角色添加'
  }
  dialogVisible.value = true
}

const handleMenuDialogValue = (roleId) => {
  if (roleId) {
    id.value = roleId
  }
  menuDialogVisible.value = true
}

const multipleSelection = ref([])
const delBtnStatus = ref(true)

const handleSelectionChange = (selection) => {
  multipleSelection.value = selection
  delBtnStatus.value = selection.length === 0
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
  const res = await requestUtil.del("role/action", ids)
  if (res.data.code === 200) {
    ElMessage({
      type: 'success',
      message: '删除成功！'
    })
  } else {
    ElMessage({
      type: 'error',
      message: res.data.msg
    })
  }
  await initRoleList()
}

initRoleList();
</script>

<template>
  <div class="app-container">
    <el-row :gutter="20" class="header">
      <el-col :span="7">
        <el-input v-model="queryForm.query" clearable placeholder="请输入角色名..."></el-input>
      </el-col>
      <el-button :icon="Search" type="primary" @click="initRoleList">搜索</el-button>
      <el-button :icon="DocumentAdd" type="success" @click="handleDialogValue()">新增</el-button>
      <el-popconfirm title="您确定批量删除这些记录吗？" @confirm="handleDelete(null)">
        <template #reference>
          <el-button :disabled="delBtnStatus" :icon="Delete" type="danger">批量删除</el-button>
        </template>
      </el-popconfirm>
    </el-row>

    <el-table
        :data="tableData"
        stripe
        style="width: 100%"
        @selection-change="handleSelectionChange">
      <el-table-column type="selection" width="55"/>
      <el-table-column align="center" label="角色名" prop="name" width="100"/>
      <el-table-column align="center" label="权限字符" prop="code" width="200"/>
      <el-table-column align="center" label="创建时间" prop="create_time" width="200"/>
      <el-table-column label="备注" prop="remark"/>

      <el-table-column align="center" fixed="right" label="操作" prop="action" width="400">
        <template v-slot="scope">
          <el-button :icon="Tools" type="primary" @click="handleMenuDialogValue(scope.row.id)">分配权限</el-button>

          <el-button v-if="scope.row.user_type!==0" :icon="Edit" type="primary"
                     @click="handleDialogValue(scope.row.id)"/>

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
        v-model:currentPage="queryForm.page_num"
        v-model:page-size="queryForm.page_size"
        :page-sizes="[10, 20, 30, 40,50]"
        :total="total"
        layout="total, sizes, prev, pager, next, jumper"
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
    />
  </div>
  <Dialog :id="id" v-model="dialogVisible" :dialogTitle="dialogTitle" :dialogVisible="dialogVisible"
          @initRoleList="initRoleList"></Dialog>
  <MenuDialog :id="id" v-model="menuDialogVisible" :menuDialogVisible="menuDialogVisible"
              @initRoleList="initRoleList"></MenuDialog>
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
