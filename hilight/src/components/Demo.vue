<template>
  <section>
    
    <div class="mdl-shadow--3dp lower-wrapper">

      <div class = "mdl-grid ">

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

      <!-- 
           <div class = "mdl-grid">
           <div class = "mdl-cell mdl-cell--2-col">
           <h4 class="mdl-switch__label">Bluetooth Mode:</h4>
           </div>
           <div class="mdl-layout-spacer"></div>
           
           <div class = "mdl-cell mdl-cell--1-col " style="justify-content: right">
           <toggle-button
           color="rgb(165, 205, 80)"
           :sync="true"
           :labels="true" />          
           </div>
           </div> -->
      
      
    </div>    
    
    

    
    <div class="mdl-shadow--3dp lower-wrapper">

      <div class = "mdl-grid">
        <div class="mdl-layout-spacer"></div>
        <div class = "mdl-cell mdl-cell--1-col">
          <span><h4>Windows:</h4></span>
        </div>
        <div class="mdl-layout-spacer"></div>
      </div>

      
      <div class = "cards">
        <div v-bind:class="{ active: windows[0][0] == 1 }" ref="0:0" class="card" @click="window_update(0,0)"></div>
        <div v-bind:class="{ active: windows[0][1] == 1 }" ref="0:1" class="card" @click="window_update(0,1)"></div>
        <div v-bind:class="{ active: windows[0][2] == 1 }" ref="0:2" class="card" @click="window_update(0,2)"></div>
      </div>

      <div class = "cards">
        <div v-bind:class="{ active: windows[1][0] == 1 }" ref="1:0" class="card" @click="window_update(1,0)"></div>                       
        <div v-bind:class="{ active: windows[1][1] == 1 }" ref="1:1" class="card" @click="window_update(1,1)"></div>
        <div v-bind:class="{ active: windows[1][2] == 1 }" ref="1:2" class="card" @click="window_update(1,2)"></div>
      </div>

    </div>
    
  </section>
</template>



<script>

 const axios = require('axios');

 var interpolateColor = function(color1, color2, factor) {
   if (arguments.length < 3) { factor = 0.5; }
   var result = color1.slice();
   for (var i=0;i<3;i++) {
     result[i] = Math.round(result[i] + factor*(color2[i]-color1[i]));
   }
   return result;
 };

 
 export default {
   
   name: 'demo',
   
   data () {
     return {
       paint : false,
       detection : false,
       windows : [
         [0,0,0],
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


     this.poll();

     /* this.$nextTick(function () {
      *   window.setInterval(() => {
      *     this.poll();
      *   },1000);
      * }) */     
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
       
       this.update_paint()
       this.update_det()
       this.sendWindowsState()
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

       if(this.paint)
       {
         this.windows[x][y] = (this.windows[x][y] + 1) % 2
         this.$forceUpdate();
         this.sendWindowsState()
       }
       
       /* 
        *        if (this.windows[x][y] == 1){
        *        }else{         
        *        }    */    
       
     },

     sendWindowsState(){

       var data = []

       data.push({
         id : '0',
         winVal : this.windows[0][0] == 0 ? 0 : 100
       })

       
       data.push({
         id : '1',
         winVal : this.windows[1][0] == 0 ? 0 : 100
       })

       
       data.push({
         id : '2',
         winVal : this.windows[0][1] == 0 ? 0 : 100
       })

       data.push({
         id : '3',
         winVal : this.windows[1][1] == 0 ? 0 : 100
       })

       data.push({
         id : '4',
         winVal : this.windows[0][2] == 0 ? 0 : 100
       })

       data.push({
         id : '5',
         winVal : this.windows[1][2] == 0 ? 0 : 100
       })

       console.log(data)
       
       axios.put('https://c2xolt5232.execute-api.eu-central-1.amazonaws.com/xxx/winstate', data).
            then(res => {
              console.log(res.data)
            });


       
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

         this.$refs['0:0'].style.backgroundColor = ""
         this.$refs['1:0'].style.backgroundColor = ""         
         this.$refs['0:1'].style.backgroundColor = ""
         this.$refs['1:1'].style.backgroundColor = ""
         this.$refs['0:2'].style.backgroundColor = ""
         this.$refs['1:2'].style.backgroundColor = ""

         this.windows[0][0] = 0
         this.windows[0][1] = 0
         this.windows[0][2] = 0
         this.windows[1][0] = 0
         this.windows[1][1] = 0
         this.windows[1][2] = 0
         
         this.$forceUpdate();         
       }else{
         this.poll()
       }
       
     },

     updateWindows(res){

       var vals = {}
       for(var i = 0; i < 6 ; i++)
       {
         let winVal = res.data[i].winVal;
         if (winVal > 100) winVal = 100;
         if (winVal <= 0) winVal = 1;
         
         let col = interpolateColor([80, 50, 145], [45, 190, 205], winVal/100);
         vals[res.data[i].id] = 'rgb(' + col[0] + ',' + col[1] + ',' + col[2] + ')'
       }

       /* console.log(res.data)
        * console.log(vals) */

       this.$refs['0:0'].style.backgroundColor = vals['0']
       this.$refs['1:0'].style.backgroundColor = vals['1']
       
       this.$refs['0:1'].style.backgroundColor = vals['2']
       this.$refs['1:1'].style.backgroundColor = vals['3']

       this.$refs['0:2'].style.backgroundColor = vals['4']
       this.$refs['1:2'].style.backgroundColor = vals['5']
       
     },
     
     poll(){
       if (!this.paint){
         axios.get('https://c2xolt5232.execute-api.eu-central-1.amazonaws.com/xxx/winstate')
              .then(this.updateWindows);
       }
       
       
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
   transition: background-color 500ms cubic-bezier(0.42, 0.0, 0.58, 1.0);
 }

 .card.active {
   border : solid 2px rgb(45, 190, 205);
   background-color : rgb(80, 50, 145);
   transition: background-color 500ms cubic-bezier(0.42, 0.0, 0.58, 1.0);
   
   /* filter : grayscale(100%) */
   
 }

 .lower-wrapper{
   width: 90%;
   margin: auto;
   padding: 5px;
   margin-top: 10px;
   margin-bottom: 10px;
   
 }
 

 /* 
    .card:hover {
    border : solid 2px rgb(45, 190, 205);
    background-color : rgb(80, 50, 145);
    transition: background-color 500ms linear;
    }
  */
 
</style>
