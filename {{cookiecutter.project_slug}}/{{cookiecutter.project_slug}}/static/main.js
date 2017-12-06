import Vue from 'vue'

import axios from 'axios'
import router from './router'
import {store} from './store'
import Meta from 'vue-meta'
{% if cookiecutter.analytics == 'Google Analytics' %}import VueAnalytics from 'vue-analytics'{% endif %}
{% if cookiecutter.analytics == 'Yandex Metrika' %}import VueYandexMetrika from 'vue-yandex-metrika'{% endif %}

{% if cookiecutter.use_progressbar == 'y' %}import VueProgressBar from 'vue-progressbar'{% endif %}
{% if cookiecutter.use_vue_material == 'y' %}
import VueMaterial from 'vue-material'
import 'vue-material/dist/vue-material.css'{% endif %}

import Main from './Main.vue'

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

{% if cookiecutter.analytics == 'Google Analytics' %}
// more info: https://github.com/MatteoGabriele/vue-analytics
Vue.use(VueAnalytics, {id: analytics, router})
{% endif %}
{% if cookiecutter.analytics == 'Yandex Metrika' %}
// more info: https://github.com/vchaptsev/vue-yandex-metrika
Vue.use(VueYandexMetrika, {id: metrika, env: process.env.NODE_ENV, router})
{% endif %}

{% if cookiecutter.use_progressbar == 'y' -%}// Progress bar interceptors
axios.interceptors.request.use((config) => {router.app.$Progress.start(); return config}, function (error) {router.app.$Progress.fail(); return Promise.reject(error)});
axios.interceptors.response.use((response) => {router.app.$Progress.finish(); return response}, function (error) {router.app.$Progress.fail(); return Promise.reject(error)}){% endif -%}

Vue.use(Meta)
{% if cookiecutter.use_progressbar == 'y' %}Vue.use(VueProgressBar){% endif %}
{% if cookiecutter.use_vue_material == 'y' %}Vue.use(VueMaterial){% endif %}

new Vue({
    el: '#main',
    router,
    store,
    render: h=> h(Main)
})
