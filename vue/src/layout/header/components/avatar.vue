<!--
  Copyright (c) 2025. aaron.

  This program is under the GPL-3.0 license.
  if you have not received it or the program has several bugs, please let me know:
  <communicate_aaron@outlook.com>.
  -->
<script setup>
import {ArrowDown} from '@element-plus/icons-vue'
import requestUtil, {getServerUrl} from '@/utils/request'
import router from '@/router'
import Cookies from "js-cookie";
import store from "@/store";

const current_user = JSON.parse(sessionStorage.getItem("current_user"))

const square_url = current_user.avatar === null
    ? getServerUrl() + 'media/user_avatar/default.jpg'
    : getServerUrl() + 'media/user_avatar/' + current_user.avatar
console.log(square_url)

const logout = () => {
  // 删除 Session
  window.sessionStorage.clear()
  // 获取所有 Cookie 的键并逐一删除
  Object.keys(Cookies.get()).forEach((cookieName) => {
    Cookies.remove(cookieName);
  });
  // 重置 tabs
  store.commit('RESET_TAB')
  router.replace("/login")
}
</script>

<template>
  <el-dropdown>
    <span class="el-dropdown-link">
      <el-avatar :size="40" :src="square_url" shape="square"/>
      &nbsp;&nbsp;&nbsp;{{ current_user.username }}
      <el-icon class="el-icon--right">
        <arrow-down/>
      </el-icon>
    </span>
    <template #dropdown>
      <el-dropdown-menu>
        <el-dropdown-item>个人中心</el-dropdown-item>
        <el-dropdown-item @click="logout">安全退出</el-dropdown-item>
      </el-dropdown-menu>
    </template>
  </el-dropdown>
</template>

<style lang="scss" scoped>
.el-dropdown-link {
  cursor: pointer;
  color: var(--el-color-primary);
  display: flex;
  align-items: center;
}
</style>