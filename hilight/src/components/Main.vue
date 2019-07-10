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

      <canvas v-on:click="changeButter" ref="gameCanvas" id="gameCanvas" height="300" width="300"></canvas>
      
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
     }
   },

   methods : {
     
     changeButter : function(event){
       var canvas = this.$refs['gameCanvas'];
       var ctx = canvas.getContext("2d");
       var mousePos = this.getMousePos(canvas, event);
       var m_y = mousePos.y
       var ctx = canvas.getContext("2d");
       ctx.fillStyle = "rgb(255,255,0)";
       ctx.clearRect(0, 0, canvas.width, canvas.height);
       ctx.beginPath();
       ctx.arc(canvas.width/2,
               canvas.height,
               canvas.height-m_y, 0 , 2 * Math.PI);
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

   mounted () {
     // axios.get('https://api.coindesk.com/v1/bpi/currentprice.json')
     //    .then(response => (this.info = response))
   }
 }
</script>

<style scoped>
 

 .butterly {
   width : 90%;
   margin: auto;
   height : 300px;
   background-color: red;
   display: flex;
   align-items: center;
 }
 .cirlce {
   /* position: absolute; */
   display: flex;
   margin-top: 100px;
   margin: auto;
   width : 50px;
   height : 50px;
   background-color: blue;
   border-radius: 50%;
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
