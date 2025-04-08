<!--
  Copyright (c) 2025. aaron.

  This program is under the GPL-3.0 license.
  if you have not received it or the program has several bugs, please let me know:
  <communicate_aaron@outlook.com>.
  -->
<script setup>
import Header from '@/layout/header'
import Menu from '@/layout/menu'
import Tabs from '@/layout/tabs'
import Footer from '@/layout/footer'
</script>

<template>
  <div class="app-wrapper">
    <el-container>
      <el-aside class="sidebar-container" width="200px">
        <Menu/>
      </el-aside>
      <el-container>
        <el-header>
          <Header/>
        </el-header>
        <el-main>
          <Tabs/>
          <router-view/>
        </el-main>
        <el-footer>
          <Footer/>
        </el-footer>
      </el-container>
    </el-container>
  </div>
</template>

<style scoped>

.app-wrapper {
  position: relative;
  width: 100%;
  height: 100%;
}

.sidebar-container {
  background-color: #2d3a4b;
  height: 100%;
}

.el-container {
  height: 100%
}

.el-header {
  padding-left: 0;
  padding-right: 0;
}

.ul.el-menu {
  border-right-width: 0;
}
</style>
