<!--
  Copyright (c) 2025. aaron.

  This program is under the GPL-3.0 license.
  if you have not received it or the program has several bugs, please let me know:
  <communicate_aaron@outlook.com>.
  -->
<script setup>
import store from '@/store'
import {
  HomeFilled
} from '@element-plus/icons-vue'

const menu_list = JSON.parse(sessionStorage.getItem("menu_list"))
const openTab = (item) => {
  store.commit('ADD_TABS', item)
}
</script>
<template>
  <el-menu
      :default-active="'/index'"
      active-text-color="#ffd04b"
      background-color="#2d3a4b"
      class="el-menu-vertical-demo"
      router
      text-color="#fff"
  >
    <el-menu-item index="/index" @click="openTab({name:'首页',path:'index'})">
      <el-icon>
        <home-filled/>
      </el-icon>
      <span>首页</span>
    </el-menu-item>

    <el-sub-menu v-for="menu in menu_list" :index="menu.path">
      <template #title>
        <el-icon>
          <svg-icon :icon="menu.icon"/>
        </el-icon>
        <span>{{ menu.name }}</span>
      </template>
      <el-menu-item v-for="item in menu.children" :index="item.path" @click="openTab(item)">
        <el-icon>
          <svg-icon :icon="item.icon"/>
        </el-icon>
        <span>{{ item.name }}</span>
      </el-menu-item>
    </el-sub-menu>
  </el-menu>
</template>

<style lang="scss" scoped>

</style>