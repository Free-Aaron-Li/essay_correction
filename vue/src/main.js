/*
 * Copyright (c) 2025. aaron.
 *
 * This program is under the GPL-3.0 license.
 * if you have not received it or the program has several bugs, please let me know:
 * <communicate_aaron@outlook.com>.
 */

import {createApp} from 'vue'
import App from './App.vue'
import router from './router'
import 'element-plus/dist/index.css'
import ElementPlus from "element-plus";

const app = createApp(App)
app.use(ElementPlus) // 需要手动设置，才能正常渲染ElementPlus
app.use(router).mount('#app')
