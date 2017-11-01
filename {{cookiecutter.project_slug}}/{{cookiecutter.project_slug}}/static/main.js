import Vue from 'vue'

import axios from 'axios'
import router from './router'
import {store} from './store'
import Meta from 'vue-meta'

import VueProgressBar from 'vue-progressbar'
{% if cookiecutter.use_vue_material == 'y' %} 
import VueMaterial from 'vue-material'
import 'vue-material/dist/vue-material.css'
{% endif %}

import Main from './Main.vue'

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

{% if cookiecutter.use_yandex_metrika == 'y' -%}
router.afterEach ((to, from, next) => {
    if (!DEBUG) {metrika.hit(to.path)} // YandexMetrika hit
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
{% if cookiecutter.use_vue_material == 'y' %} 
Vue.use(VueMaterial)
{% endif %}

new Vue({
    el: '#main',
    router,
    store,
    render: h=> h(Main)
})
