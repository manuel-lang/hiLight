<template>

  <div class="wrapper">
    
    <div class="container" style="margin-top: 10px;margin-bottom: 10px;">
      <h4>Hello {{user}}!</h4>
      <form class="toggle">

        <input v-model="custom" type="radio" id="choice1" name="choice" value="true">
        <label for="choice1">Custom</label>

        <input v-model="custom" type="radio" id="choice2" name="choice" value="false">
        <label for="choice2">Automatic</label>

        <div id="flap"><span class="content"></span></div>
      </form>
    </div>

    

    <div v-dragged="onDragged"  class="butter-wrapper"  @click="changeButter" @touchmove="prevent"> 
      <canvas ref="gameCanvas" id="gameCanvas" height="300" width="300"></canvas>
      <div class="img-hold"></div>
    </div>
    <!-- 
         <vue-slider :dot-size=20
         :enable-cross=false
         :tooltip=false
         v-model="percent" class="slider" @callback="updateSlider">
         </vue-slider>
    -->

    <hr/>
    <h4>Light: {{percent}}%</h4>
    </div>

</template>


<script>
 const axios = require('axios');

 String.prototype.capitalize = function() {
     return this.charAt(0).toUpperCase() + this.slice(1)
  }
 
 export default {

   name: 'hello',

   data : function() {
     return {
       info : 'This is info',
       percent : 45,
       custom : false,
       user : '',
       upper : 270,
       down : 63,
       isDragging : false
     }
   },

   watch : {

     custom : function(){
       this.cloud()
     },

     percent : function(){
       this.slide()
       
     }

   },

   beforeRouteEnter (to, from, next) {
     next(vm => {
       if (to.params.user !== undefined){
	 vm.setUser(to.params.user);
       }
       else{
         vm.pollUser()
       }
     })
   },

   beforeRouteUpdate (to, from, next) {
     if (to.params.user !== undefined){
       this.setUser(to.params.user)       
     }else{
       this.pollUser()
     }
     next();
   },

   mounted () {
          
     /* this.$nextTick(function () {
      *   window.setInterval(() => {
      *     this.poll();
      *   },1000);
      * }) */
     
   },

   methods : {

     prevent : function (event) {
       /* console.log('something happened') */
       event.preventDefault()
       /* event.stopPropagation() */
     },
     
     onDragged : function ({ el, deltaX, deltaY, offsetX, offsetY, clientX, clientY, first, last }) {

       if (first) {
         this.isDragging = true
         return
       }
       if (last) {
         this.isDragging = false
         return
       }


       var canvas = this.$refs['gameCanvas'];
       var rect = canvas.getBoundingClientRect();
       var x = clientX - rect.left;
       var y =clientY - rect.top;
       this.repaint(canvas, canvas.height - y)
       this.cloud()
     },

     cloud : function () {

       let cust = this.custom.toString().capitalize()

       let data = {
         "name": this.user,
         "wert" : parseInt(this.percent),
         "custom" : cust
       }
       
       console.log(data)
       
       axios.put('https://c2xolt5232.execute-api.eu-central-1.amazonaws.com/xxx//profiles/name', data)
              .then(res => {
              })
       
       
     },

     updateSlider : function(e) {
       this.cloud()
     },

     slide : function () {
       let r = (this.upper - this.down)* (this.percent/100.0) + this.down;
       var canvas = this.$refs['gameCanvas'];
       this.repaint(canvas, r);
     },

     changeButter : function(event) {
       var canvas = this.$refs['gameCanvas'];
       var mousePos = this.getMousePos(canvas, event);
       var m_y = mousePos.y
       this.repaint(canvas, canvas.height-m_y);
       this.cloud()
     },

     repaint : function (canvas, r) {
       var ctx = canvas.getContext("2d");

       this.percent = (100*(r - this.down) / (this.upper - this.down)).toFixed(0);
       if (this.percent > 100) this.percent = 100;
       if (this.percent < 0) this.percent = 0;


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
     },

     pollUser : function() {

       axios.get('https://c2xolt5232.execute-api.eu-central-1.amazonaws.com/xxx/activeuser')
            .then(response => {
              this.user = response.data;
              axios.get("https://c2xolt5232.execute-api.eu-central-1.amazonaws.com/xxx/profiles/" + this.user)
                   .then(response => {
                     this.percent = response.data.wert
		     this.custom = response.data.custom == "True";
                     this.slide()
                     this.cloud()
                   });
            });
     },

     setUser : function(user) {
       axios.put('https://c2xolt5232.execute-api.eu-central-1.amazonaws.com/xxx/activeuser', {"username":user})
       axios.get("https://c2xolt5232.execute-api.eu-central-1.amazonaws.com/xxx/profiles/" + user)
            .then(response => {
              this.percent = response.data.wert
	      this.custom = response.data.custom == "True";
              this.user = response.data.name
              this.slide()
              this.cloud()
	    });
     },

     poll : function () {
       this.pollUser()
     }
     

   }
   
 }
</script>

<style scoped>

 .slider .vue-slider-dot  {
   background: rgb(165, 205, 80);
   
 }

 .butter-wrapper{

   margin-left: 20px;
   margin: auto;
   
   height : 300px;
   width : 330px;
   background-color: rgb(80, 50, 145);
   display: flex;
   z-index: 1;
 }

 #gameCanvas{
   position: absolute;
   z-index: 100;
   width : 330px;
   margin: auto;
   height : 300px;
 }

 .img-hold{
   width : 330px;
   height: 300px;
   margin: auto;
   z-index: 110;
   position: absolute;
   background-image: url('..//assets/mask_hd_ne.png') ;
   background-repeat: repeat;
   background-size: 340px, 100%;
   background-position:center center;

 }

 .container {
   perspective: 800px;
   width: 320px;
   margin-left : 20px;
   margin: auto;
   padding : 3px;
   background-color:white;
 }

 .toggle {
   position: relative;
   border: solid 6px rgb(165, 205, 80);
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
   height: calc(100% + 4px * 2);
   width: calc(50% + 2px);
   display: flex;
   justify-content: center;
   align-items: center;
   font-size: 16px;
   background-color: rgb(165, 205, 80);
   transform-style: preserve-3d;
   transform-origin: left;
   transition: transform cubic-bezier(0.4, 0, 0.2, 1) .5s;
   border-top-right-radius: 55px;
   border-bottom-right-radius: 55px;
   z-index: -100;
   
 }

 .toggle>#flap>.content {
   color: #333;
   transition: transform 0s linear .25s;
   transform-style: preserve-3d;
   z-index: -100;
 }

 .wrapper {
   margin: auto;
   top : 0px;
   margin-bottom: 0px;
 }

</style>
