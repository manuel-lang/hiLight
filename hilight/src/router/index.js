import Vue from 'vue'
import Router from 'vue-router'
import Main from '@/components/Main'
import Demo from '@/components/Demo'

Vue.use(Router)

export default new Router({
  routes: [
      {
          path: '/',
          name: 'Main',
          component: Main
      },
      {
          path: '/demo',
          name: 'Demo',
          component: Demo
      }
  ]
})
