/*
 * Copyright (c) 2025. aaron.
 *
 * This program is under the GPL-3.0 license.
 * if you have not received it or the program has several bugs, please let me know:
 * <communicate_aaron@outlook.com>.
 */

import {createRouter, createWebHashHistory} from 'vue-router'

const routes = [
    {
        path: '/',
        name: '主页',
        component: () => import('../layout/index.vue'),
        redirect: '/index',
        children: [
            {
                path: "/index",
                name: '首页',
                component: () => import('../views/index/index.vue')
            },
            {
                path: '/sys/user',
                name: '用户管理',
                component: () => import('../views/sys/user/index.vue')
            },
            {
                path: '/sys/role',
                name: '角色管理',
                component: () => import('../views/sys/role/index.vue')
            },
            {
                path: '/sys/menu',
                name: '菜单管理',
                component: () => import('../views/sys/menu/index.vue')
            },
            {
                path: '/bsns/department',
                name: '部门管理',
                component: () => import('../views/bsns/Department')
            },
            {
                path: '/bsns/post',
                name: '岗位管理',
                component: () => import('../views/bsns/Post')
            },
            {
                path: '/userCenter',
                name: '个人中心',
                component: () => import('../views/userCenter/index.vue')
            }
        ]
    },
    {
        path: '/about',
        name: '关于',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
    },
    {
        path: '/login',
        name: '登陆',
        component: () => import('../views/Login.vue')
    },
]

const router = createRouter({
    history: createWebHashHistory(),
    routes
})

export default router
