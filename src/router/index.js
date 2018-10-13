import Vue from 'vue'
import Router from 'vue-router'

import Home from '@/components/Home'
import About from '@/components/About'
import Search from '@/components/Search'
import Maps from '@/components/Maps'
import Contribute from '@/components/Contribute'
import UsingAPI from '@/components/UsingAPI'
// TODO: read Wordpress content into blog component
// import Blog from '@/components/Blog'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {path: '/usingapi', component: UsingAPI},
    {path: '/contribute', component: Contribute},
    {path: '/search', component: Search},
    {path: '/maps', component: Maps},
    {path: '/about', component: About},
    {path: '/', component: Home},
    {path: '/api/places'},
    // {path: '/blog', component: Blog},
  ]
})
