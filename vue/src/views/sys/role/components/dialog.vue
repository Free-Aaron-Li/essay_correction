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

const props = defineProps(
    {
      id: {
        type: Number,
        default: -1,
        required: true
      },
      dialogTitle: {
        type: String,
        default: '',
        required: true
      },
      dialogVisible: {
        type: Boolean,
        default: false,
        required: true
      }
    }
)

const form = ref({
  id: -1,
  name: "",
  code: "",
  remark: ""
})

const rules = ref({
  name: [
    {required: true, message: '请输入角色名称'}
  ],
  code: [
    {required: true, message: '请输入权限字符'}
  ]
})

const formRef = ref(null)

const initFormData = async (id) => {
  const res = await requestUtil.get("role/action?id=" + id);
  form.value = res.data.role;
}

watch(
    () => props.dialogVisible,
    () => {
      let id = props.id;
      if (id !== -1) {
        initFormData(id)
      } else {
        form.value = {
          id: -1,
          name: "",
          code: "",
          remark: ""
        }

      }
    }
)

const emits = defineEmits(['update:modelValue', 'initRoleList'])

const handleClose = () => {
  emits('update:modelValue', false)
}

const handleConfirm = () => {
  formRef.value.validate(async (valid) => {
    if (valid) {
      let result = await requestUtil.post("role/save", form.value);
      let data = result.data;
      if (data.code === 200) {
        ElMessage.success("角色创建成功！")
        formRef.value.resetFields();
        emits("initRoleList")
        handleClose();
      } else {
        ElMessage.error(data.msg);
      }
    } else {
      console.log("角色创建失败")
    }
  })
}
</script>
<template>
  <el-dialog
      :title="dialogTitle"
      model-value="dialogVisible"
      width="30%"
      @close="handleClose"
  >
    <el-form
        ref="formRef"
        :model="form"
        :rules="rules"
        label-width="100px"
    >
      <el-form-item label="角色名称" prop="name">
        <el-input v-model="form.name"/>
      </el-form-item>

      <el-form-item label="权限字符" prop="code">
        <el-input v-model="form.code"/>
      </el-form-item>

      <el-form-item label="备注" prop="remark">
        <el-input v-model="form.remark" :rows="4" type="textarea"/>
      </el-form-item>

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
