<template>
  <div id="app">
    <div>
    <router-link to="/">Home</router-link> ::
    <router-link to="/search">Search</router-link> ::
    <router-link to="/maps">Maps</router-link> ::
    <router-link to="/contribute">Contribute</router-link> ::
    <router-link to="/usingapi">Using the API</router-link> ::
    <router-link to="/about">About</router-link>
    <!-- <router-link to="/blog">Blog</router-link> :: -->
  </div>
  <router-view></router-view>
  </div>
</template>

<script>
  export default {
    name: 'App'
  }
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 20px;
}
/* @import'~bootstrap/dist/css/bootstrap.css' */
</style>
