<!--
  Copyright (c) 2025. aaron.

  This program is under the GPL-3.0 license.
  if you have not received it or the program has several bugs, please let me know:
  <communicate_aaron@outlook.com>.
  -->
<script setup>
import breadcrumb from './components/breadcrumb.vue'
import avatar from './components/avatar.vue'
</script>

<template>
  <div class="navbar">
    <breadcrumb/>
    <div class="navbar-right">
      <avatar/>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.navbar {
  width: 100%;
  height: 60px;
  overflow: hidden;
  background-color: #F5F5F5;
  box-shadow: 0 1px 4px rgba(0, 21, 41, 0.08);
  padding: 0 16px;
  display: flex;
  align-items: center;
  box-sizing: border-box;
  position: relative;

  .navbar-right {
    flex: 1;
    display: flex;
    align-items: center;
    justify-content: flex-end;

    ::v-deep .navbar-item {
      display: inline-block;
      margin-left: 18px;
      font-size: 22px;
      color: #5a5e66;
      box-sizing: border-box;
      cursor: pointer;
    }
  }
}
</style>