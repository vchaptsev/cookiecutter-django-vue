import Vue from 'vue'

import axios from 'axios'
import router from './router'
import {store} from './store'
import Meta from 'vue-meta'
{% if cookiecutter.analytics == 'Google Analytics' %}import VueAnalytics from 'vue-analytics'{% endif %}
{% if cookiecutter.analytics == 'Yandex Metrika' %}import VueYandexMetrika from 'vue-yandex-metrika'{% endif %}
{% if cookiecutter.use_sentry == 'y' %}import VueRaven from 'vue-raven'{% endif %}

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

Vue.use(Meta)

/* eslint-disable no-new */
new Vue({
  el: '#main',
  router,
  store,
  render: h => h(Main)
})
