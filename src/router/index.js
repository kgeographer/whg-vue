import Vue from 'vue'
import Router from 'vue-router'

import Home from '@/components/Home'
import About from '@/components/About'
import Blog from '@/components/Blog'
import Search from '@/components/Search'
import Contribute from '@/components/Contribute'
import UsingAPI from '@/components/UsingAPI'
import UserAuth from '@/components/UserAuth'

Vue.use(Router)

const router = new Router({
  mode: 'history',
  routes: [
    {path: '/usingapi', component: UsingAPI, name: ''},
    {path: '/contribute', component: Contribute, name: ''},
    {path: '/search', component: Search, name: ''},
    {path: '/blog', component: Blog, name: ''},
    {path: '/about', component: About, name: ''},
    {path: '/', component: Home, name: ''},
    {path: '/auth', component: UserAuth, name: 'UserAuth',
    }
  ]
})

router.beforeEach((to, from, next) => {
  if (sessionStorage.getItem('authToken') !== null || to.path !== '/blog') {
    next()
  } else {
    next('/auth')
  }
})
export default router
