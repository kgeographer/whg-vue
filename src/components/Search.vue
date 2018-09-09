<template>
  <div class="content">
    <h1>{{ msg }}</h1>
    <input type="text" class="typeahead form-control" id="name_search" placeholder="Enter place name">
  </div>
</template>

<script>
var $ = require('jquery')
require("typeahead.js/dist/typeahead.jquery.min.js")
var Bloodhound = require("typeahead.js/dist/bloodhound.min.js")

export default {
  name: 'Search',
  data () {
    return {
      msg: 'Map/Search'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  h1, h2 {
    font-weight: normal;
  }
  ul {
    list-style-type: none;
    padding: 0;
  }
  li {
    display: inline-block;
    margin: 0 10px;
  }
  a {
    color: #42b983;
  }
  input {font-size: 1em;}
</style>
