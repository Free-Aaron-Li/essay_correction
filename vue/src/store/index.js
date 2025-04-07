/*
 * Copyright (c) 2025. aaron.
 *
 * This program is under the GPL-3.0 license.
 * if you have not received it or the program has several bugs, please let me know:
 * <communicate_aaron@outlook.com>.
 */

import {createStore} from 'vuex'

export default createStore({
    state: {
        editableTabsValue: '/index',
        editableTabs: [
            {
                title: '首页',
                name: '/index',
            }
        ],
    },
    getters: {},
    mutations: {
        ADD_TABS: (state, tab) => {
            if (state.editableTabs.findIndex(e => e.name === tab.path) === -1) {
                state.editableTabs.push({
                    title: tab.name,
                    name: tab.path
                })
            }
            state.editableTabsValue = tab.path
        },
        RESET_TAB: (state) => {
            state.editableTabsValue = '/index'
            state.editableTabs = [
                {
                    title: '首页',
                    name: '/index',
                }
            ]
        }
    },
    actions: {},
    modules: {}
})
