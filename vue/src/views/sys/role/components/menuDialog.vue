<!--
  Copyright (c) 2025. aaron.

  This program is under the GPL-3.0 license.
  if you have not received it or the program has several bugs, please let me know:
  <communicate_aaron@outlook.com>.
  -->
<script setup>
import {defineEmits, defineProps, ref, watch} from "vue";
import requestUtil, {getServerUrl} from "@/utils/request";
import {ElMessage} from 'element-plus'

const defaultProps = {
  children: 'children',
  label: 'name'
}

const props = defineProps(
    {
      id: {
        type: Number,
        default: -1,
        required: true
      },
      menuDialogVisible: {
        type: Boolean,
        default: false,
        required: true
      }
    }
)

const form = ref({
  id: -1
})

const treeData = ref([]);
const formRef = ref(null)
const treeRef = ref(null)

const initFormData = async (id) => {
  const res = await requestUtil.get("menu/tree_list");
  treeData.value = res.data.tree_list;
  form.value.id = id;
  const res2 = await requestUtil.get("role/menus?id=" + id);
  treeRef.value.setCheckedKeys(res2.data.menu_id_list)
}

watch(
    () => props.menuDialogVisible,
    () => {
      let id = props.id;
      if (id !== -1) {
        initFormData(id)
      }
    }
)

const emits = defineEmits(['update:modelValue', 'initRoleList'])

const handleClose = () => {
  emits('update:modelValue', false)
}

const handleConfirm = async () => {
  let menuIds = treeRef.value.getCheckedKeys();
  let result = await requestUtil.post("role/grant", {"id": form.value.id, "menu_ids": menuIds});
  let data = result.data;
  if (data.code === 200) {
    ElMessage.success("权限分配成功！")
    emits("initRoleList")
    handleClose();
  } else {
    ElMessage.error(data.msg);
  }
}
</script>
<template>
  <el-dialog
      model-value="menuDialogVisible"
      title="分配权限"
      width="30%"
      @close="handleClose"
  >
    <el-form
        ref="formRef"
        :model="form"
        label-width="100px"
    >
      <el-tree
          ref="treeRef"
          :check-strictly=true
          :data="treeData"
          :default-expand-all=true
          :props="defaultProps"
          node-key="id"
          show-checkbox
      />
    </el-form>

    <template #footer>
      <span class="dialog-footer">
        <el-button type="primary" @click="handleConfirm">确认</el-button>
        <el-button @click="handleClose">取消</el-button>
      </span>
    </template>
  </el-dialog>
</template>

<style lang="scss" scoped>

</style>
