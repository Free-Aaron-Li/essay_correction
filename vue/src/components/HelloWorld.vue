<!--
  Copyright (c) 2025. aaron.

  This program is under the GPL-3.0 license.
  if you have not received it or the program has several bugs, please let me know:
  <communicate_aaron@outlook.com>.
  -->

<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <p>
      For a guide and recipes on how to configure / customize this project,<br>
      check out the
      <a href="https://cli.vuejs.org" rel="noopener" target="_blank">vue-cli documentation</a>.
    </p>
    <h3>Installed CLI Plugins</h3>
    <ul>
      <li><a href="https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-babel" rel="noopener"
             target="_blank">babel</a></li>
      <li><a href="https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-router" rel="noopener"
             target="_blank">router</a></li>
      <li><a href="https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-vuex" rel="noopener"
             target="_blank">vuex</a></li>
    </ul>
    <h3>Essential Links</h3>
    <ul>
      <li><a href="https://vuejs.org" rel="noopener" target="_blank">Core Docs</a></li>
      <li><a href="https://forum.vuejs.org" rel="noopener" target="_blank">Forum</a></li>
      <li><a href="https://chat.vuejs.org" rel="noopener" target="_blank">Community Chat</a></li>
      <li><a href="https://twitter.com/vuejs" rel="noopener" target="_blank">Twitter</a></li>
      <li><a href="https://news.vuejs.org" rel="noopener" target="_blank">News</a></li>
    </ul>
    <h3>Ecosystem</h3>
    <ul>
      <li><a href="https://router.vuejs.org" rel="noopener" target="_blank">vue-router</a></li>
      <li><a href="https://vuex.vuejs.org" rel="noopener" target="_blank">vuex</a></li>
      <li><a href="https://github.com/vuejs/vue-devtools#vue-devtools" rel="noopener" target="_blank">vue-devtools</a>
      </li>
      <li><a href="https://vue-loader.vuejs.org" rel="noopener" target="_blank">vue-loader</a></li>
      <li><a href="https://github.com/vuejs/awesome-vue" rel="noopener" target="_blank">awesome-vue</a></li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
