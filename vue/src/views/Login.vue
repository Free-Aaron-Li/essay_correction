<!--
  Copyright (c) 2025. aaron.

  This program is under the GPL-3.0 license.
  if you have not received it or the program has several bugs, please let me know:
  <communicate_aaron@outlook.com>.
  -->

<template>
  <div class="login">
    <el-form ref="loginRef" :model="loginForm" :rules="loginRules" class="login-form">
      <h3 class="title">作文批改系统</h3>
      <el-form-item prop="username">
        <el-input
            v-model="loginForm.username"
            auto-complete="off"
            placeholder="账号"
            size="large"
            type="text"
        >
          <template #prefix>
            <svg-icon icon="user"/>
          </template>
        </el-input>
      </el-form-item>
      <el-form-item prop="password">
        <el-input
            v-model="loginForm.password"
            auto-complete="off"
            placeholder="密码"
            size="large"
            type="password"
        >
          <template #prefix>
            <svg-icon icon="password"/>
          </template>
        </el-input>
      </el-form-item>
      <el-checkbox v-model="loginForm.rememberMe" style="margin:0 0 25px 0;">记住密码</el-checkbox>
      <el-form-item style="width:100%;">
        <el-button
            size="large"
            style="width:100%;"
            type="primary"
            @click.prevent="handleLogin"
        >
          <span>登 录</span>
        </el-button>
      </el-form-item>
    </el-form>
    <!--  底部  -->
    <div class="el-login-footer">
      <span>Copyright © 2025 <a href="https://github.com/Free-Aaron-Li" target="_blank">Aaron.Li</a> 版权所有.</span>
    </div>
  </div>
</template>

<script setup>
import {ref} from 'vue'
import qs from 'qs'
import requestUtil from '@/utils/request'
import {ElMessage} from "element-plus";
import Cookies from 'js-cookie'
import {decrypt, encrypt} from "@/utils/jsencrypt";

const loginForm = ref({
  username: '',
  password: '',
  rememberMe: false,
})

const loginRef = ref(null)

// 定义规则不允许为空
const loginRules = ref({
  username: [{required: true, trigger: 'blur', message: "请输入您的账号"}],
  password: [{required: true, trigger: 'blur', message: "请输入您的密码"}]
})

// 登陆逻辑
const handleLogin = () => {
  loginRef.value.validate(async (valid) => {
    if (valid) {
      let result = await requestUtil.post("user/login?" + qs.stringify(loginForm.value))
      let data = result.data
      if (data.code === 200) {
        ElMessage.success(data.info)
        window.sessionStorage.setItem("token", data.token)
        // 勾选“记住密码”
        // 在cookie中保存用户名和密码
        if (loginForm.value.rememberMe) {
          Cookies.set('username', encrypt(loginForm.value.username), {expires: 30})
          Cookies.set('password', encrypt(loginForm.value.password), {expires: 30})
          Cookies.set('rememberMe', loginForm.value.rememberMe, {expires: 30})
        } else {
          Cookies.remove('username')
          Cookies.remove('password')
          Cookies.remove('rememberMe')
        }
      } else {
        ElMessage.error(data.info)
      }
    } else {
      console.log('验证失败！')
    }
  })
}

// 从Cookie中获取值
function getCookie() {
  const username = Cookies.get('username')
  const password = Cookies.get('password')
  const rememberMe = Cookies.get('rememberMe')
  loginForm.value = {
    // 如果未定义，取空值；如果定义，则解密
    username: username === undefined ? loginForm.value.username : decrypt(username),
    password: password === undefined ? loginForm.value.password : decrypt(password),
    rememberMe: rememberMe === undefined ? false : Boolean(rememberMe)
  }
}

getCookie()
</script>

<style lang="scss" scoped>
a {
  color: white
}

.login {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
  background-image: url("../assets/images/background.png");
  background-size: cover;
}

.title {
  margin: 0 auto 30px auto;
  text-align: center;
  color: #707070;
}

.login-form {
  border-radius: 6px;
  background: #ffffff;
  width: 400px;
  padding: 25px 25px 5px 25px;

  .el-input {
    height: 40px;

    input {
      display: inline-block;
      height: 40px;
    }
  }

  .input-icon {
    height: 39px;
    width: 14px;
    margin-left: 0;
  }
}

.login-tip {
  font-size: 13px;
  text-align: center;
  color: #bfbfbf;
}

.login-code {
  width: 33%;
  height: 40px;
  float: right;

  img {
    cursor: pointer;
    vertical-align: middle;
  }
}

.el-login-footer {
  height: 40px;
  line-height: 40px;
  position: fixed;
  bottom: 0;
  width: 100%;
  text-align: center;
  color: #fff;
  font-family: "Noto Serif CJK SC", serif;
  font-size: 12px;
  letter-spacing: 1px;
}

.login-code-img {
  height: 40px;
  padding-left: 12px;
}
</style>
