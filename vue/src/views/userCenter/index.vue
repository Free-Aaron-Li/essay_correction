<!--
  Copyright (c) 2025. aaron.

  This program is under the GPL-3.0 license.
  if you have not received it or the program has several bugs, please let me know:
  <communicate_aaron@outlook.com>.
  -->
<script setup>
import avatar from './components/avatar.vue'
import userInfo from './components/userInfo.vue'
import resetPwd from './components/resetPwd.vue'
import {ref} from "vue";

const current_user = JSON.parse(sessionStorage.getItem("current_user"))

const activeTab = ref("userinfo")
</script>

<template>
  <div class="app-container">
    <el-row :gutter="20">
      <el-col :span="6">
        <el-card class="box-card">
          <template #header>
            <div class="clearfix">
              <span>个人信息</span>
            </div>
          </template>
          <div>
            <div class="text-center">
              <avatar :user="current_user"/>
            </div>
            <ul class="list-group list-group-striped">
              <li class="list-group-item">
                <svg-icon icon="user"/>&nbsp;&nbsp;用户名称
                <div class="pull-right">{{ current_user.username }}</div>
              </li>
              <li class="list-group-item">
                <svg-icon icon="phone"/>&nbsp;&nbsp;手机号码
                <div class="pull-right">{{ current_user.phone }}</div>
              </li>
              <li class="list-group-item">
                <svg-icon icon="email"/>&nbsp;&nbsp;用户邮箱
                <div class="pull-right">{{ current_user.email }}</div>
              </li>
              <li class="list-group-item">
                <svg-icon icon="peoples"/>&nbsp;&nbsp;所属角色
                <div class="pull-right">{{ current_user.roles }}</div>
              </li>
              <li class="list-group-item">
                <svg-icon icon="date"/>&nbsp;&nbsp;创建日期
                <div class="pull-right">{{ current_user.created_at }}</div>
              </li>
            </ul>
          </div>
        </el-card>
      </el-col>
      <el-col :span="18">
        <el-card>
          <template #header>
            <div class="clearfix">
              <span>基本资料</span>
            </div>
          </template>
          <el-tabs v-model="activeTab">
            <el-tab-pane label="基本资料" name="userinfo">
              <userInfo :user="current_user"/>
            </el-tab-pane>
            <el-tab-pane label="修改密码" name="resetPwd">
              <resetPwd :user="current_user"/>
            </el-tab-pane>
          </el-tabs>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<style lang="scss" scoped>
.list-group-striped > .list-group-item {
  border-left: 0;
  border-right: 0;
  border-radius: 0;
  padding-left: 0;
  padding-right: 0;
}

.list-group-item {
  border-bottom: 1px solid #e7eaec;
  border-top: 1px solid #e7eaec;
  margin-bottom: -1px;
  padding: 11px 0;
  font-size: 13px;
}

.pull-right {
  float: right !important;
}

::v-deep .el-card__body {
  height: 230px;
}

::v-deep .box-card {
  height: 450px;
}
</style>