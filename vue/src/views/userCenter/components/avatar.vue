<!--
  Copyright (c) 2025. aaron.

  This program is under the GPL-3.0 license.
  if you have not received it or the program has several bugs, please let me know:
  <communicate_aaron@outlook.com>.
  -->
<script setup>
import {defineProps, ref} from "vue";
import requestUtil, {getServerUrl} from "@/utils/request";
import {ElMessage} from 'element-plus'
import {Plus} from '@element-plus/icons-vue'

const props = defineProps(
    {
      user: {
        type: Object,
        default: () => {
        },
        required: true
      }
    }
)

const headers = ref({
  Authorization: window.sessionStorage.getItem('token')
})

const form = ref({
  id: -1,
  avatar: ''
})

const formRef = ref(null)

const imageUrl = ref("")

form.value = props.user;
imageUrl.value = getServerUrl() + 'media/user_avatar/' + form.value.avatar

const handleAvatarSuccess = (res) => {
  imageUrl.value = getServerUrl() + 'media/user_avatar/' + res.title
  form.value.avatar = res.title;
}

// 提交验证
const beforeAvatarUpload = (file) => {
  const isJPG = file.type === 'image/jpeg'
  const isLt2M = file.size / 1024 / 1024 < 2

  if (!isJPG) {
    ElMessage.error('图片必须是jpg格式')
  }
  if (!isLt2M) {
    ElMessage.error('图片大小不能超过2M!')
  }
  return isJPG && isLt2M
}

const handleConfirm = async () => {
  let result = await requestUtil.post("user/update_avatar", form.value);
  let data = result.data;
  if (data.code === 200) {
    ElMessage.success("执行成功！")
  } else {
    ElMessage.error(data.error_info);
  }

}
</script>

<template>
  <el-form
      ref="formRef"
      :model="form"
      label-width="100px"
      style="text-align: center;padding-bottom:10px"
  >
    <el-upload
        :action="getServerUrl()+'user/upload_image'"
        :before-upload="beforeAvatarUpload"
        :headers="headers"
        :on-success="handleAvatarSuccess"
        :show-file-list="false"
        class="avatar-uploader"
        name="avatar"
    >
      <img v-if="imageUrl" :src="imageUrl" alt="avatar" class="avatar"/>
      <el-icon v-else class="avatar-uploader-icon">
        <Plus/>
      </el-icon>
    </el-upload>
    <el-button @click="handleConfirm">确认更换</el-button>
  </el-form>
</template>

<style>
.avatar-uploader .el-upload {
  border: 1px dashed #d9d9d9;
  border-radius: 6px;
  cursor: pointer;
  position: relative;
  overflow: hidden;
}

.avatar-uploader .el-upload:hover {
  border-color: #409eff;
}

.el-icon.avatar-uploader-icon {
  font-size: 28px;
  color: #8c939d;
  width: 178px;
  height: 178px;
  text-align: center;
}

.avatar {
  width: 120px;
  height: 120px;
  display: block;
}
</style>
