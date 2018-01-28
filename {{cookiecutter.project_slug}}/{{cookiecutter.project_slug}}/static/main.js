import Vue from 'vue'

import axios from 'axios'
import router from './router'
import {store} from './store'
import Meta from 'vue-meta'
{% if cookiecutter.analytics == 'Google Analytics' %}import VueAnalytics from 'vue-analytics'{% endif %}
{% if cookiecutter.analytics == 'Yandex Metrika' %}import VueYandexMetrika from 'vue-yandex-metrika'{% endif %}
{% if cookiecutter.use_sentry == 'y' %}import VueRaven from 'vue-raven'{% endif %}
{% if cookiecutter.use_progressbar == 'y' %}import VueProgressBar from 'vue-progressbar'{% endif %}

import Main from './Main.vue'

// Axios csrf settings
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

{% if cookiecutter.use_sentry == 'y' %}
// Sentry for logging frontend errors
if (process.env.NODE_ENV === 'production') {Vue.use(VueRaven, {dsn: SENTRY_PUBLIC_DSN})}
{% endif %}

{% if cookiecutter.analytics == 'Google Analytics' %}
// more info: https://github.com/MatteoGabriele/vue-analytics
Vue.use(VueAnalytics, {id: GOOGLE_ANALYTICS, router})
{% endif %}
{% if cookiecutter.analytics == 'Yandex Metrika' %}
// more info: https://github.com/vchaptsev/vue-yandex-metrika
Vue.use(VueYandexMetrika, {id: YANDEX_METRIKA, env: process.env.NODE_ENV, router})
{% endif %}

{% if cookiecutter.use_progressbar == 'y' -%}// Progress bar interceptors
axios.interceptors.request.use((config) => { router.app.$Progress.start(); return config }, function (error) { router.app.$Progress.fail(); return Promise.reject(error) })
axios.interceptors.response.use((response) => { router.app.$Progress.finish(); return response }, function (error) { router.app.$Progress.fail(); return Promise.reject(error) })
{% endif %}

Vue.use(Meta)
{% if cookiecutter.use_progressbar == 'y' %}Vue.use(VueProgressBar){% endif %}

/* eslint-disable no-new */
new Vue({
  el: '#main',
  router,
  store,
  render: h => h(Main)
})
