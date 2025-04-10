<!--
  Copyright (c) 2025. aaron.

  This program is under the GPL-3.0 license.
  if you have not received it or the program has several bugs, please let me know:
  <communicate_aaron@outlook.com>.
  -->
<script setup>
import {Search, Delete, DocumentAdd, Edit, Tools, RefreshRight} from '@element-plus/icons-vue'
import {ref} from 'vue'
import requestUtil, {getServerUrl} from "@/utils/request";
import {ElMessage, ElMessageBox} from 'element-plus'
import Dialog from './components/dialog'

const tableData = ref([])

const initMenuList = async () => {
  const res = await requestUtil.get("menu/tree_list");
  tableData.value = res.data.tree_list;
}

const id = ref(-1)
const dialogVisible = ref(false)
const dialogTitle = ref('')

const handleDialogValue = (menuId) => {
  if (menuId) {
    id.value = menuId;
    dialogTitle.value = "菜单修改"
  } else {
    id.value = -1;
    dialogTitle.value = "菜单添加"
  }
  dialogVisible.value = true
}

const handleDelete = async (id) => {
  const res = await requestUtil.del("menu/action", id)
  if (res.data.code === 200) {
    ElMessage({
      type: 'success',
      message: '执行成功!'
    })
    await initMenuList();
  } else {
    ElMessage({
      type: 'error',
      message: res.data.msg,
    })
  }
}

initMenuList();
</script>
<template>
  <div class="app-container">
    <el-row class="header">
      <el-button :icon="DocumentAdd" type="success" @click="handleDialogValue()">新增</el-button>
    </el-row>

    <el-table
        :data="tableData"
        :tree-props="{ children: 'children', hasChildren: 'hasChildren' }"
        border
        default-expand-all
        row-key="id"
        stripe
        style="width: 100%; margin-bottom: 20px"
    >
      <el-table-column label="菜单名称" prop="name" width="180"/>
      <el-table-column align="center" label="图标" prop="icon" width="70">
        <template v-slot="scope">
          <el-icon>
            <svg-icon :icon="scope.row.icon"/>
          </el-icon>
        </template>
      </el-table-column>
      <el-table-column align="center" label="排序" prop="order_num" width="70"/>
      <el-table-column label="权限标识" prop="perms" width="200"/>
      <el-table-column label="组件路径" prop="path" width="180"/>
      <el-table-column align="center" label="菜单类型" prop="menu_type" width="120">
        <template v-slot="scope">
          <el-tag v-if="scope.row.menuType === 'M'" effect="dark" size="small" type="danger">目录</el-tag>
          <el-tag v-else-if="scope.row.menuType === 'C'" effect="dark" size="small" type="success">菜单</el-tag>
        </template>
      </el-table-column>
      <el-table-column align="center" label="创建时间" prop="create_time"/>
      <el-table-column align="center" fixed="right" label="操作" prop="action" width="300">
        <template v-slot="scope">
          <el-button :icon="Edit" type="primary" @click="handleDialogValue(scope.row.id)"/>
          <el-popconfirm title="您确定要删除这条记录吗？" @confirm="handleDelete(scope.row.id)">
            <template #reference>
              <el-button :icon="Delete" type="danger"/>
            </template>
          </el-popconfirm>
        </template>
      </el-table-column>
    </el-table>

  </div>
  <Dialog :id="id" v-model="dialogVisible" :dialogTitle="dialogTitle" :dialogVisible="dialogVisible"
          :tableData="tableData" @initMenuList="initMenuList"></Dialog>
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
