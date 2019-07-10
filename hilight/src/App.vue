<template>
  <div class="mdl-layout mdl-js-layout mdl-layout--fixed-header">

    <header class="mdl-layout__header">
      <div class="mdl-layout__header-row">
        <span class="mdl-layout-title">HiLight</span>
      </div>
    </header>

    <div class="mdl-layout__drawer">
      <span class="mdl-layout-title">HiLight</span>
      <nav class="mdl-navigation">
        <router-link class="mdl-navigation__link" to="/" @click.native="hideMenu">Home</router-link>
        <router-link class="mdl-navigation__link" to="/demo" @click.native="hideMenu">Demo</router-link>
      </nav>
    </div>
    
    <main class="mdl-layout__content">
      <div class="page-content">
        <router-view></router-view>
      </div>
    </main>

    <footer class = "mdl-mega-footer">
      
    </footer>
      
  </div>
</template>

<script>
 require('material-design-lite')
 export default {
   name: 'app',

   methods: {
     hideMenu: function () {
       document.getElementsByClassName('mdl-layout__drawer')[0].classList.remove('is-visible')
       document.getElementsByClassName('mdl-layout__obfuscator')[0].classList.remove('is-visible')
     }
   }
   
 }
</script>

<style>

 @import url('https://fonts.googleapis.com/icon?family=Material+Icons');
 @import url('https://code.getmdl.io/1.3.0/material.deep_purple-teal.min.css');
 body {
   margin: 0;
 }

 #app {
   font-family: 'Avenir', Helvetica, Arial, sans-serif;
   color: #149B60;
 }

 main {
   text-align: center;
   margin-top: 40px;
 }

 header {
   margin: 0;
   height: 56px;
   padding: 0 16px 0 24px;
   background-color: #503292;
   color: #C747A7;
 }

 
 footer {
   margin: 0;
   height: 5px;
   padding: 0 16px 0 24px;
   background-color: #503292;
   color: #C747A7;
 }



 header span {
   display: block;
   position: relative;
   font-size: 20px;
   line-height: 1;
   letter-spacing: .02em;
   font-weight: 400;
   box-sizing: border-box;
   padding-top: 16px;
 }
</style>
