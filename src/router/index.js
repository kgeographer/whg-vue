import Vue from 'vue'
import Router from 'vue-router'

import Home from '@/components/Home'
import About from '@/components/About'
import Blog from '@/components/Blog'
import Search from '@/components/Search'
import Contribute from '@/components/Contribute'
import UsingAPI from '@/components/UsingAPI'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {path: '/usingapi', component: UsingAPI},
    {path: '/contribute', component: Contribute},
    {path: '/search', component: Search},
    {path: '/blog', component: Blog},
    {path: '/about', component: About},
    {path: '/', component: Home}
  ]
})
