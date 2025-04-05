<!--
  - Copyright (c) 2025. aaron.
  -
  - This program is under the GPL-3.0 license.
  - if you have not received it or the program has several bugs, please let me know:
  - <communicate_aaron@outlook.com>.
  -->

<template>
  <div class="mb-4">
    <el-button>Default</el-button>
    <el-button type="primary">Primary</el-button>
    <el-button type="success">Success</el-button>
    <el-button type="info">Info</el-button>
    <el-button type="warning">Warning</el-button>
    <el-button type="danger">Danger</el-button>
  </div>

  <div class="mb-4">
    <el-button plain>Plain</el-button>
    <el-button plain type="primary">Primary</el-button>
    <el-button plain type="success">Success</el-button>
    <el-button plain type="info">Info</el-button>
    <el-button plain type="warning">Warning</el-button>
    <el-button plain type="danger">Danger</el-button>
  </div>

  <div class="mb-4">
    <el-button round>Round</el-button>
    <el-button round type="primary">Primary</el-button>
    <el-button round type="success">Success</el-button>
    <el-button round type="info">Info</el-button>
    <el-button round type="warning">Warning</el-button>
    <el-button round type="danger">Danger</el-button>
  </div>

  <div>
    <el-button :icon="Search" circle/>
    <el-button :icon="Edit" circle type="primary"/>
    <el-button :icon="Check" circle type="success"/>
    <el-button :icon="Message" circle type="info"/>
    <el-button :icon="Star" circle type="warning"/>
    <el-button :icon="Delete" circle type="danger"/>
  </div>
</template>

<script setup>
import {Check, Delete, Edit, Message, Search, Star,} from '@element-plus/icons-vue'
</script>
