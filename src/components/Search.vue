<template>
  <div class="content">
    <h1>{{ msg }}</h1>
    <input type="text" style="width:300px" class="form-control typeahead tt-input"
      placeholder="Enter place name" id="search-input" autocomplete="on" />
    <input type='hidden' id='flag' value="todos"/>
  </div>
</template>
<script>

// var urlRoot = '//jsonplaceholder.typicode.com';
// var todos = {
//   url: urlRoot + '/todos',
//   prepare: function(query, settings) {
//     settings.url += '?q=' + query;
//     return settings;
//   },
//   filter: function(data) {
//   	return $.map(data, function(obj) {
//     	console.log(obj)
//     	return {
//         Id: obj.id,
//         Value: obj.title
//       };
//     });
//   }
// };
//
// var taSource = new Bloodhound({
//   datumTokenizer: Bloodhound.tokenizers.obj.whitespace('Value'),
//   queryTokenizer: Bloodhound.tokenizers.whitespace,
//   identify: function(obj) {
//     return obj.Value;
//   },
//   remote: todos
// });
//
// taSource.initialize(true);
//
// $('#search-input').typeahead({
//   hint: true,
//   highlight: true,
//   minLength: 3
// }, {
//   name: 'myMatches',
//   source: taSource,
//   display: 'Value'
// });

export default {
  name: 'Search',
  data () {
    return {
      msg: 'Map/Search component'
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
</style>
