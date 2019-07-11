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

      <li class="mdl-list__item">
        <router-link class="mdl-navigation__link" to="/main" @click.native="hideMenu">
          <span class="mdl-list__item-primary-content">
            <i class="material-icons mdl-list__item-icon">home</i>
            Home
          </span>
        </router-link>
      </li> 
      
      <li class="mdl-list__item">
        <router-link class="mdl-navigation__link" to="/demo" @click.native="hideMenu">
          <span class="mdl-list__item-primary-content">
            <i class="material-icons mdl-list__item-icon">important_devices</i>
            Demo
          </span>
        </router-link>
      </li>

      <hr/>

      <li class="mdl-list__item" v-for="user in users">
        <router-link class="mdl-navigation__link" :to="'/main/' + user.name" @click.native="hideMenu">
          <span class="mdl-list__item-primary-content">
            <i class="material-icons mdl-list__item-icon">person</i>
            {{user.name}}
          </span>
        </router-link>
      </li>
      
    </nav>
  </div>
  
  <main class="mdl-layout__content">
    <div class="page-content main-section">
      <router-view></router-view>
    </div>
  </main>
  
  <footer class="footer">
    <img style=" margin:5px;" alt="" width="175" height="45px" src="@/assets/eye.png"/>
  </footer> 
  
</div>
</template>


<script>
const axios = require('axios');

require('material-design-lite')

export default {

    name: 'app',
    data (){
        return {
            users : []
        }
    },

    mounted (){
        axios.get('https://c2xolt5232.execute-api.eu-central-1.amazonaws.com/xxx/profiles')
            .then(response => (this.users = response.data));
    },
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

body{
    margin: 0;
    background: #f9f9f9;
    background: -moz-linear-gradient(45deg, #f9f9f9 48%, #dceff4 98%);
    background: -webkit-linear-gradient(45deg, #f9f9f9 48%,#dceff4 98%); /* Chrome10-25,Safari5.1-6 */
    background: linear-gradient(45deg, #f9f9f9 48%,#dceff4 98%);
    filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#f9f9f9', endColorstr='#dceff4',GradientType=1 );
    
} 

.footer {
    border-top: solid 1px rgb(80, 50, 145);
    display: flex;
    justify-content: center;
}

#app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    color: #149B60;
}

main {
  text-align: center;
  margin-top: 2px;
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

.cards {
    display: flex;
    flex-direction: row;
    width : 100%;
    justify-content: space-evenly;
    flex-wrap: nowrap;
}


.card {
    box-shadow: 0px 0px 20px -5px ;
    width : 22vmin;
    height : 22vmin;
    background-color : rgb(45, 190, 205);
    border : solid 2px rgb(80, 50, 145);
    margin : 5px;
    justify-content: center;
    border-radius : 20px;
}

.card.active {
    border : solid 2px rgb(45, 190, 205);
    background-color : rgb(80, 50, 145);
}

.card:hover {
    border : solid 2px rgb(45, 190, 205);
    background-color : rgb(80, 50, 145);
    transition: background-color 500ms linear;
}

</style>
