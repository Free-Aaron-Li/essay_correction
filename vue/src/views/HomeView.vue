<!--
  - Copyright (c) 2025. aaron.
  -
  - This program is under the GPL-3.0 license.
  - if you have not received it or the program has several bugs, please let me know:
  - <communicate_aaron@outlook.com>.
  -->

<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'HomeView',
  components: {
    HelloWorld
  }
}
</script>
