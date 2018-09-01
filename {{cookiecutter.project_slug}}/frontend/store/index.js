import Vue from 'vue'
import Vuex from 'vuex'

{% if cookiecutter.custom_user == 'y' %}
import users from './services/users'
import auth from './modules/auth'{% endif %}

Vue.use(Vuex)

export const store = new Vuex.Store({
  modules: {
    {% if cookiecutter.custom_user == 'y' %}
    users,
    auth{% endif %}
  }
})
