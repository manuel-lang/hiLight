<template>

  <section>

    <div class="wrapper">
      <div class="container">
        <form class="toggle">

          <input v-model="custom" type="radio" id="choice1" name="choice" value="creative">
          <label for="choice1">Custom</label>

          <input v-model="automatic" type="radio" id="choice2" name="choice" value="productive">
          <label for="choice2">Automatic</label>
          
          <div id="flap"><span class="content"></span></div>
          
          
        </form>
      </div>

      <hr/>

      <div v-on:click="changeButter" class="butter-wrapper">
        <canvas  ref="gameCanvas" id="gameCanvas" height="300" width="300"></canvas>

        <div class="img-hold"></div>
        
      </div>
      
      
      <hr/>

      <!-- Slider with Starting Value -->
      <input v-model="percent" class="mdl-slider mdl-js-slider" type="range"
             min="0" max="100" value="45" tabindex="0">

      
      <hr/>
      <h4>Light: {{percent}}%</h4>
    </div>

    
  </section>

  

</template>

<script>
const axios = require('axios');
 export default {
   
   name: 'hello',
   
   data () {
     return {
       info : 'This is info',
       percent : 45,
       custom : false,
       automatic : false,
       user : ''
     }
   },
   
   beforeRouteEnter (to, from, next) {
     next(vm => {
       axios.get('https://c2xolt5232.execute-api.eu-central-1.amazonaws.com/xxx/profiles/name', {'name' : to.params.user})
            .then(response => {
              /* console.log(response.data) */
              /* this.percent = response.data.wert
               * this.custom = response.data.custom */
              vm.percent = 85;
              vm.custom = false;
              vm.automatic = true;
            });  
     })
   },
   
   beforeRouteUpdate (to, from, next) {
     
     axios.get('https://c2xolt5232.execute-api.eu-central-1.amazonaws.com/xxx/profiles/name', {'name' : to.params.user})
          .then(response => {
            /* console.log(response.data)  */
            /* this.percent = response.data.wert
             * this.custom = response.data.custom */
            vm.percent = 85;
            vm.custom = false;
            vm.automatic = true;
          });  
     next();
     
   },
      
   methods : {
     
     changeButter : function(event){
       var canvas = this.$refs['gameCanvas'];
       var ctx = canvas.getContext("2d");
       var mousePos = this.getMousePos(canvas, event);
       var m_y = mousePos.y
       this.repaint(canvas, canvas.height-m_y);
     },

     repaint : function (canvas, r){
       var ctx = canvas.getContext("2d");
       ctx.fillStyle = "rgb(45, 190, 205)";
       ctx.clearRect(0, 0, canvas.width, canvas.height);
       ctx.beginPath();
       ctx.arc(canvas.width/2,
               canvas.height+70,
               r+80, 0 , 2 * Math.PI);
       ctx.fill();
     },
     
     getMousePos : function (canvas, evt) {
       var rect = canvas.getBoundingClientRect();
       return {
         x: evt.clientX - rect.left,
         y: evt.clientY - rect.top
       };
     }
     
   },
   
   mounted () {}
 }
</script>

<style >

.butter-wrapper{
  
  width : 90%;
  margin: auto;
  height : 300px;
  background-color: rgb(80, 50, 145);
  display: flex;
  align-items: center;
  z-index: 1;
  }

  #gameCanvas{
  position: absolute;
  z-index: 100;
  width : 90%;
  margin: auto;
  height : 300px;
  }

  .img-hold{
  
  width : 90%;
  margin: auto;
  height: 300px;
  z-index: 110;
  position: absolute;
  background-image: url('..//assets/mask_hd.png') ;
  background-repeat: no-repeat;
  background-size: 340px, cover;
  background-position: bottom;
  }

  
  .container {
  perspective: 800px;
  max-width: 250px;
  margin : auto;
  }

  .toggle {
  position: relative;
  border: solid 6px #04da97;
  border-radius: 35px;
  transition: transform cubic-bezier(0, 0, 0.30, 2) .4s;
  transform-style: preserve-3d;
  perspective: 800px;
  }
  
  .toggle>input[type="radio"] {
  display: none;
  }

  .toggle>#choice1:checked~#flap {
  transform: rotateY(-180deg);
  /* display: hidden; */
  }

  .toggle>#choice1:checked~#flap>.content {
  transform: rotateY(-180deg);
  }

  .toggle>#choice2:checked~#flap {
  transform: rotateY(0deg);
  }

  #choice2:checked~#choice2 {
  display: none;
  }

  #choice1:checked~#choice1 {
  display: none;
  }

  .toggle>label {
  display: inline-block;
  min-width: 100px;
  padding: 3px;
  font-size: 16px;
  text-align: center;
  color: black;
  cursor: pointer;
  /* z-index:5; */
  }

  .toggle>label,
  .toggle>#flap {
  font-weight: bold;
  text-transform: capitalize;
  
  }

  .toggle>#flap {
  position: absolute;
  top: calc( 0px - 6px);
  left: 50%;
  height: calc(100% + 5px * 2);
  width: calc(50% + 2px);
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 16px;
  background-color: #04da97;
  border-top-right-radius: #04da97;
  border-bottom-right-radius: #04da97;
  transform-style: preserve-3d;
  transform-origin: left;
  transition: transform cubic-bezier(0.4, 0, 0.2, 1) .5s;
  border-radius: 55px;
  z-index: -100;
  }

  .toggle>#flap>.content {   
  color: #333;
  transition: transform 0s linear .25s;
  transform-style: preserve-3d;
  z-index: -100;
  }

</style>
