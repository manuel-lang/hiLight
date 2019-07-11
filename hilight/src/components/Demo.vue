<template>
  <section>
    
    <div class = "mdl-grid">

      <div class = "mdl-cell mdl-cell--2-col">
        <h4 class="mdl-switch__label">Detection Mode:</h4>
      </div>
      <div class="mdl-layout-spacer"></div>
      <div class = "mdl-cell mdl-cell--1-col " style="justify-content: right">

        <toggle-button 
          v-model="detection"
          color="rgb(165, 205, 80)"
          :sync="true"
          :labels="true"
          @change="update_det"
        />

        
      </div>
    </div>

    <div class = "mdl-grid">
      <div class = "mdl-cell mdl-cell--2-col">
        <h4 class="mdl-switch__label">Paint Mode:</h4>
      </div>
      <div class="mdl-layout-spacer"></div>
      
      <div class = "mdl-cell mdl-cell--1-col " style="justify-content: right">

        <toggle-button 
          v-model="paint"
          color="rgb(165, 205, 80)"
          :sync="true"
          :labels="true"
          @change="update_paint"/>
        
      </div>
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
      <div v-bind:class="{ active: windows[0][0] == 1 }" ref="1:1" class="card" @click="window_update(0,0)"></div>
      <div v-bind:class="{ active: windows[0][1] == 1 }" ref="1:2" class="card" @click="window_update(0,1)"></div>
      <div v-bind:class="{ active: windows[0][2] == 1 }" ref="1:3" class="card" @click="window_update(0,2)"></div>
    </div>

    <div class = "cards">
      <div v-bind:class="{ active: windows[1][0] == 1 }" ref="2:1" class="card" @click="window_update(1,0)"></div>                       
      <div v-bind:class="{ active: windows[1][1] == 1 }" ref="2:2" class="card" @click="window_update(1,1)"></div>
      <div v-bind:class="{ active: windows[1][2] == 1 }" ref="2:3" class="card" @click="window_update(1,2)"></div>
    </div>
    
  </section>
</template>


<script>

 const axios = require('axios');
 
 export default {
   
   name: 'demo',
   
   data () {
     return {
       paint : false,
       detection : false,
       windows : [
         [1,0,0],
         [0,0,0]]
     }
   },
   
   watch : {
     paint: function() {
       this.cloud()
     },
     
     detection: function() {
       this.cloud()
     }         
   },
   
   beforeRouteEnter (to, from, next) {
     next(vm => {
       axios.get('https://c2xolt5232.execute-api.eu-central-1.amazonaws.com/xxx/operationmode')
            .then(vm.load);
     })
   },
   
   beforeRouteUpdate (to, from, next) {
     axios.get('https://c2xolt5232.execute-api.eu-central-1.amazonaws.com/xxx/operationmode')
          .then(this.load);
     
     next();
     
   },
   
   mounted () {
     
     axios.get('https://c2xolt5232.execute-api.eu-central-1.amazonaws.com/xxx/operationmode')
          .then(this.load);		 
     
     /* 
      *      this.$nextTick(function () {
      *        window.setInterval(() => {
      *          this.poll();
      *        },1000);
      *      }) */
     
   },
   
   methods : {
     
     load (res) {
       
       for (var index = 0; index < res.data.length; ++index) {

         if (res.data[index].id == "paint")
         {
           this.paint = res.data[index].demo == "True"
         }
         
         if (res.data[index].id == "detection")
         {
           this.detection = res.data[index].demo == "True"
         }
       }
     },
     
     cloud(){
       let paint = this.paint ? "True" : "False";
       let detection = this.detection ? "True" : "False";
       
       axios.put('https://c2xolt5232.execute-api.eu-central-1.amazonaws.com/xxx/operationmode',
                 {
                   'detection' : detection,
                   'paint':paint
                 }
       );
       
     },
     
     window_update(x,y) {

       this.windows[x][y] = (this.windows[x][y] + 1) % 2
       this.$forceUpdate();
       if (this.windows[x][y] == 1){
         
       }else{
         
       }
       
       
     },
     
     update_det (){
       
       if (this.detection)
       {
         this.paint = false;
       }
       
       if (this.paint){
         this.detection = false;
       }
       
     },
     
     update_paint (){
       
       if (this.paint){
         this.detection = false;
       }
       
     },
     
     poll(){
     }
   }
 }
</script>

<style scoped>

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

 /* 
    .card:hover {
    border : solid 2px rgb(45, 190, 205);
    background-color : rgb(80, 50, 145);
    transition: background-color 500ms linear;
    }
  */
 
</style>
