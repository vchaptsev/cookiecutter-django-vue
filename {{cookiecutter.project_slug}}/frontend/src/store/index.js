import Vue from 'vue'
import Vuex from 'vuex'

import users from '@/store/services/users'
import auth from '@/store/modules/auth'

Vue.use(Vuex)

const store = new Vuex.Store({
  modules: {
    users,
    auth
  }
})

export default store
