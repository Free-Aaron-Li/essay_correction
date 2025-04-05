/*
 * Copyright (c) 2025. aaron.
 *
 * This program is under the GPL-3.0 license.
 * if you have not received it or the program has several bugs, please let me know:
 * <communicate_aaron@outlook.com>.
 */

import {createApp} from 'vue'
import App from './App.vue'
import SvgIcon from './icons'
import router from './router'
import store from "./store";
import 'element-plus/dist/index.css'
import ElementPlus from "element-plus";
import '@/assets/styles/border.css'
import '@/assets/styles/reset.css'

const app = createApp(App)
SvgIcon(app)
app.use(store)
app.use(router)
app.use(ElementPlus) // 需要手动设置，才能正常渲染ElementPlus
app.mount('#app')
