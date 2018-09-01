import Vue from 'vue'
import VueRouter from 'vue-router'

import FirstComponent from './components/FirstComponent.vue'

const routes = [
  {path: '*', component: FirstComponent}
]

Vue.use(VueRouter)
const router = new VueRouter({
  scrollBehavior (to, from, savedPosition) { return {x: 0, y: 0} },
  mode: 'history',
  routes
})

export default router
