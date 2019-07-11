<template>
  <section>
    
    <div class = "mdl-grid">

      <div class = "mdl-cell mdl-cell--2-col">
        <h4 class="mdl-switch__label">Demo Mode:</h4>
      </div>
      <div class="mdl-layout-spacer"></div>
      <div class = "mdl-cell mdl-cell--1-col " style="justify-content: right">
        <label style="margin-left:auto" class="mdl-switch mdl-js-switch mdl-js-ripple-effect" for="switch-1">
          <input v-model="demo" type="checkbox" id="switch-1" class="mdl-switch__input" checked>
          <span class="mdl-switch__label"></span>
        </label>
      </div>
    </div>
    <hr/>

    <div class = "mdl-grid">
      <div class="mdl-layout-spacer"></div>
      <div class = "mdl-cell mdl-cell--1-col">
        <span><h4>Windows:</h4></span>
      </div>
      <div class="mdl-layout-spacer"></div>
    </div>
    
    <div class = "cards">

      <div class="card"></div>
      <div class="card active"></div>
      <div class="card"></div>
    </div>

    <div class = "cards">
      <div class="card"></div>                       
      <div class="card active"></div>
      <div class="card"></div>
    </div>
    
  </section>
</template>

<script>

 const axios = require('axios');
 
 export default {
   
   name: 'demo',
   
   data () {
     return {
       demo : false
     }
   },

   watch: {
     demo: function() {
       let dem = this.demo ? "True" : "False";
       axios.put('https://c2xolt5232.execute-api.eu-central-1.amazonaws.com/xxx/operationmode', {'demo' : dem});
     }
   },

   beforeRouteEnter (to, from, next) {
     next(vm => {
       axios.get('https://c2xolt5232.execute-api.eu-central-1.amazonaws.com/xxx/operationmode')
            .then(res => {
              vm.demo = res.data == "True"
            });
     })
   },
   
   beforeRouteUpdate (to, from, next) {
     axios.get('https://c2xolt5232.execute-api.eu-central-1.amazonaws.com/xxx/operationmode')
          .then(res => {
            this.demo = res == "True"
          });
       
     next();
     
   },

   mounted () {
     axios.get('https://c2xolt5232.execute-api.eu-central-1.amazonaws.com/xxx/operationmode')
          .then(res => {
            this.demo = res.data == "True"
          });
     
   }
 }
</script>

<style>

</style>
