<!--
  Copyright (c) 2025. aaron.

  This program is under the GPL-3.0 license.
  if you have not received it or the program has several bugs, please let me know:
  <communicate_aaron@outlook.com>.
  -->
<script setup>
import {watch} from "vue";
import {useRoute} from "vue-router";
import store from "@/store";

const route = useRoute()
watch(route, (to, from) => {
  if (to.name === '个人中心') {
    let obj = {
      name: to.name,
      path: to.path
    }
    store.commit('ADD_TABS', obj)
  }
}, {deep: true, immediate: true})
</script>

<template>
  <router-view/>
</template>

<style>
html, body, #app {
  height: 100%;
}

.app-container {
  padding: 20px;
}
</style>
