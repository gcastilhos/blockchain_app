import Vue from 'vue'
import App from './App.vue'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap-vue/dist/bootstrap-vue.min.css'
import store from './store/store'

Vue.config.productionTip = false
localStorage.clear()

new Vue({
  store,
  render: h => h(App),
}).$mount('#app')
