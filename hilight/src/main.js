// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import ToggleButton from 'vue-js-toggle-button'
import VDragged from 'v-dragged'
import VueSlider from 'vue-slider-component'

Vue.config.productionTip = false
Vue.use(ToggleButton)
Vue.use(VDragged) 
// Vue.use(VueSlider) 
Vue.component('VueSlider', VueSlider)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: { App }
})
