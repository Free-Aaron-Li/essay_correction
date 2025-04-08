<!--
  Copyright (c) 2025. aaron.

  This program is under the GPL-3.0 license.
  if you have not received it or the program has several bugs, please let me know:
  <communicate_aaron@outlook.com>.
  -->
<script setup>
import {HomeFilled} from "@element-plus/icons-vue";
import {ref, watch} from 'vue'
import {useRoute} from 'vue-router'

const route = useRoute()

const breadcrumbList = ref([])

const initBreadcrumbList = () => {
  breadcrumbList.value = route.matched
}

watch(route, () => {
  initBreadcrumbList()
}, {deep: true, immediate: true})
</script>

<template>
  <el-icon>
    <homeFilled/>
  </el-icon>
  <el-breadcrumb separator="/">
    <el-breadcrumb-item v-for="(item,index) in breadcrumbList">
      <span>
      {{ item.name }}
      </span>
    </el-breadcrumb-item>
  </el-breadcrumb>
</template>


<style lang="scss" scoped>

</style>