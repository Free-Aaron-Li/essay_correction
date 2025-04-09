<!--
  Copyright (c) 2025. aaron.

  This program is under the GPL-3.0 license.
  if you have not received it or the program has several bugs, please let me know:
  <communicate_aaron@outlook.com>.
  -->
<script setup>
import {defineProps, ref} from 'vue'
import requestUtil from "@/utils/request";
import {ElMessage} from "element-plus";

const props = defineProps({
  user: {
    type: Object,
    default: () => {
    },
    required: true,
  }
})

// 格式
const form = ref({
  id: -1,
  phone: '',
  email: '',
})

// 用户表单的组件引用
const userRef = ref(null)

// 初始化，从父页面传来的 user 数据
// 绑定表单数据
form.value = props.user

// 规则检查
const rules = ref({
  email: [
    {required: true, message: "邮箱地址不能为空", trigger: "blur"},
    {
      type: "email",
      message: "请输入正确的邮箱地址",
      trigger: ["blur", "change"],
    },
  ],
  phone: [
    {required: true, message: "手机号码不能为空", trigger: "blur"},
    {
      pattern: /^1[3-9][0-9]\d{8}$/,
      message: "请输入正确的手机号码",
      trigger: "blur",
    },
  ],
});

// 提交
const handleSubmit = () => {
  if (!userRef.value) {
    console.error('userRef 未绑定到实际的组件上！');
    return;
  }

  userRef.value.validate(async (valid) => {
    if (valid) {
      let result = await requestUtil.post("user/save", form.value);
      let data = result.data;
      if (data.code === 200) {
        ElMessage.success("执行成功！")
        window.sessionStorage.setItem("current_user", JSON.stringify(form.value))
      }
    }
  })
}
</script>

<template>
  <el-form ref="userRef" :model="form" :rules="rules" label-width="100px">
    <el-form-item label="手机号码：" prop="phone">
      <el-input v-model="form.phone" maxlength="11"/>
    </el-form-item>
    <el-form-item label="用户邮箱：" prop="email">
      <el-input v-model="form.email" maxlength="50"/>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="handleSubmit">保存</el-button>
    </el-form-item>
  </el-form>
</template>

<style lang="scss" scoped>

</style>