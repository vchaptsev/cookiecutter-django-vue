import Vue from 'vue'

import axios from 'axios'
import router from './router'
import {store} from './store'
import Meta from 'vue-meta'

import VueProgressBar from 'vue-progressbar'

import Main from './Main.vue'

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

{% if cookiecutter.use_yandex_metrika == 'y' -%}
router.afterEach ((to, from, next) => {
    // YandexMetrika hit
    if (!DEBUG) {metrika.hit(to.path)}
})
{% endif %}

// Progress bar interceptors
axios.interceptors.request.use((config) => {
    router.app.$Progress.start()
    return config
}, function (error) {
    router.app.$Progress.fail()
    return Promise.reject(error)
});
axios.interceptors.response.use((response) => {
    router.app.$Progress.finish()
    return response
}, function (error) {
    router.app.$Progress.fail()
    return Promise.reject(error)
})

Vue.use(Meta)
Vue.use(VueProgressBar)

new Vue({
    el: '#main',
    router,
    store,
    render: h=> h(Main)
})
