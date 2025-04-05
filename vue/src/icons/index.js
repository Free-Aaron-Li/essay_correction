/*
 * Copyright (c) 2025. aaron.
 *
 * This program is under the GPL-3.0 license.
 * if you have not received it or the program has several bugs, please let me know:
 * <communicate_aaron@outlook.com>.
 */

import SvgIcon from '@/components/SvgIcon'

const svgRequired = require.context('./svg', false, /\.svg$/)
svgRequired.keys().forEach((item) => svgRequired(item))

export default (app) => {
    app.component('svg-icon', SvgIcon)
}
