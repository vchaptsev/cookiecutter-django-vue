import Vue from 'vue'
import store from '@/store'
import router from '@/router'

{% if cookiecutter.api == "REST" %}
import axios from 'axios'
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'
{% elif cookiecutter.api == "GraphQL" %}
import { createProvider } from '@/apollo'
{% endif %}

{% if cookiecutter.analytics == 'Google Analytics' %} import VueAnalytics from 'vue-analytics'{% endif %}
{% if cookiecutter.analytics == 'Yandex Metrika' %} import VueYandexMetrika from 'vue-yandex-metrika'{% endif %}
{% if cookiecutter.use_sentry == 'y' %}
import * as Sentry from "@sentry/vue"
import { Integrations } from "@sentry/tracing";
{% endif %}

import App from '@/App.vue'
import './registerServiceWorker'

Vue.config.productionTip = false

{% if cookiecutter.use_sentry == 'y' %}
// Sentry for logging frontend errors
Sentry.init({
  Vue: Vue,
  dsn: process.env.VUE_APP_SENTRY_PUBLIC_DSN,
  integrations: [new Integrations.BrowserTracing()],
  tracingOptions: {
    trackComponents: true,
  },
  logError: process.env.NODE_ENV === 'development'
});
{% endif %}

{% if cookiecutter.analytics == 'Google Analytics' %}
// more info: https://github.com/MatteoGabriele/vue-analytics
Vue.use(VueAnalytics, {
  id: process.env.VUE_APP_GOOGLE_ANALYTICS,
  router
})
{% endif %}

{% if cookiecutter.analytics == 'Yandex Metrika' %}
// more info: https://github.com/vchaptsev/vue-yandex-metrika
Vue.use(VueYandexMetrika, {
  id: process.env.VUE_APP_YANDEX_METRIKA,
  env: process.env.NODE_ENV,
  router
})
{% endif %}

new Vue({
  router,
  store,
  {% if cookiecutter.api == "GraphQL" %}provide: createProvider().provide(), {% endif %}
render: h => h(App)
}).$mount('#app')
