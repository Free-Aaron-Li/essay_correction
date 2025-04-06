<!--
  Copyright (c) 2025. aaron.

  This program is under the GPL-3.0 license.
  if you have not received it or the program has several bugs, please let me know:
  <communicate_aaron@outlook.com>.
  -->

<template>
  <el-button type="primary" @click="handleLogin">测试登陆</el-button>
  <el-button type="success" @click="handleUserList">测试获取用户信息列表</el-button>
</template>

<script setup>

import requestUtil from "@/utils/request";

const handleLogin = async () => {
  let result = await requestUtil.get("user/jwt_test")
  let data = result.data
  if (data.code === 200) {
    const token = data.token
    console.log("登陆成功，token=" + token)
    window.sessionStorage.setItem("token", token)
  } else {
    console.log("登陆出错！")
  }
}

const handleUserList = async () => {
  let result = await requestUtil.get("user/test")
  let data = result.data
  if (data.code === 200) {
    const userList = data.data;
    console.log("用户信息列表，userList=" + userList)
  } else {
    console.log("登陆出错！")
  }
}
</script>
