<!--
  Copyright (c) 2025. aaron.

  This program is under the GPL-3.0 license.
  if you have not received it or the program has several bugs, please let me know:
  <communicate_aaron@outlook.com>.
  -->
<script setup>
import {ref, watch} from 'vue'
import store from "@/store";
import {useRouter} from 'vue-router'


const editableTabsValue = ref(store.state.editableTabsValue)
const editableTabs = ref(store.state.editableTabs)

const removeTab = (targetName) => {
  const tabs = editableTabs.value
  let activeName = editableTabsValue.value
  if (activeName === targetName) {
    tabs.forEach((tab, index) => {
      if (tab.name === targetName) {
        const nextTab = tabs[index + 1] || tabs[index - 1]
        if (nextTab) {
          activeName = nextTab.name
        }
      }
    })
  }

  editableTabsValue.value = activeName
  editableTabs.value = tabs.filter((tab) => tab.name !== targetName)

  // 更新维护 tabs
  store.state.editableTabsValue = editableTabsValue.value
  store.state.editableTabs = editableTabs.value

  router.push({path: activeName})
}

const router = useRouter()
const clickTab = (target) => {
  router.push({name: target.props.label})
}

const refreshTabs = () => {
  editableTabsValue.value = store.state.editableTabsValue
  editableTabs.value = store.state.editableTabs
}

watch(store.state, () => {
  refreshTabs()
}, {deep: true, immediate: true})
</script>

<template>
  <el-tabs
      v-model="editableTabsValue"
      class="demo-tabs"
      closable
      type="card"
      @tab-remove="removeTab"
      @tab-click="clickTab"
  >
    <el-tab-pane
        v-for="item in editableTabs"
        :key="item.name"
        :label="item.title"
        :name="item.name"
    >
    </el-tab-pane>
  </el-tabs>
</template>

<style>
.demo-tabs > .el-tabs__content {
  padding: 32px;
  color: #6b778c;
  font-size: 32px;
  font-weight: 600;
}

.el-tabs--card > .el-tabs__header .el-tabs__item.is-active {
  background-color: lightgray;
}

.el-main {
  padding: 0;
}

.el-tabs__content {
  padding: 0 !important;;
}
</style>
