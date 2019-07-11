<template>

  <div class="wrapper">
    
    <div class="container mdl-shadow--3dp">
      <h4>Hello {{user}}!</h4>
      <form class="toggle">

        <input v-model="custom" type="radio" id="choice1" name="choice" value="true">
        <label for="choice1">Custom</label>

        <input v-model="custom" type="radio" id="choice2" name="choice" value="false">
        <label for="choice2">Automatic</label>

        <div id="flap"><span class="content"></span></div>
      </form>
    </div>
    <hr/>

    <div v-on:click="changeButter" class="butter-wrapper mdl-shadow--3dp">
      <canvas  ref="gameCanvas" id="gameCanvas" height="300" width="300"></canvas>
      <div class="img-hold"></div>
    </div>


    <hr/>

    <!-- Slider with Starting Value -->
    <input @change="slide" v-model="percent" class="mdl-slider mdl-js-slider" type="range"
           min="0" max="100" >


    <hr/>
    <h4>Light: {{percent}}%</h4>

  </div>

</template>

<script>
const axios = require('axios');
 export default {

   name: 'hello',

   data : function() {
     return {
       info : 'This is info',
       percent : 45,
       custom : false,
       user : '',
       upper : 270,
       down : 63
     }
   },

   watch : {

     custom : function(){
       this.cloud()
     },

     percent : function(){
       this.cloud()
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

   methods : {

     cloud : function () {
       let data = {
         "name": this.user,
         "wert" : parseInt(this.percent),
         "custom" : this.demo ? "True" : "False"
       }
       /* console.log(data) */
       axios.put('https://c2xolt5232.execute-api.eu-central-1.amazonaws.com/xxx//profiles/name', data)
              .then(res => {
                /* console.log(res) */
              })
     },

     slide : function (){
       let r = (this.upper - this.down)* (this.percent/100.0) + this.down;
       var canvas = this.$refs['gameCanvas'];
       this.repaint(canvas, r);
     },

     changeButter : function(event){
       var canvas = this.$refs['gameCanvas'];
       var mousePos = this.getMousePos(canvas, event);
       var m_y = mousePos.y
       this.repaint(canvas, canvas.height-m_y);
     },

     repaint : function (canvas, r){
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

		 pollUser : function(){
			 axios.get('https://c2xolt5232.execute-api.eu-central-1.amazonaws.com/xxx/activeuser')
            .then(response => {
              this.user = response.data;
              axios.get("https://c2xolt5232.execute-api.eu-central-1.amazonaws.com/xxx/profiles/" + to.params.user)
                   .then(response => {
                     console.log(response.data)
                     this.percent = response.data.wert
										 this.custom = response.data.custom
                     this.slide()
                     this.cloud()
                   });
            });
		 },

		 setUser : function(user) {
			 axios.put('https://c2xolt5232.execute-api.eu-central-1.amazonaws.com/xxx/activeuser', {"username":user})
       axios.get("https://c2xolt5232.execute-api.eu-central-1.amazonaws.com/xxx/profiles/" + user)
            .then(response => {
              console.log(response.data) 
              this.percent = response.data.wert
							this.custom = response.data.custom
              this.user = to.params.user
              this.slide()
              this.cloud()
						});
		 },

		 poll : function (){
			 pollUser()
		 }
		 

   },

   mounted () {
		 
		 /* 
      *      this.$nextTick(function () {
      *        window.setInterval(() => {
      *          this.poll();
      *        },1000);
      *      }) */
		 
   }
 }
</script>

<style scoped>

 .butter-wrapper{

   margin-left: 20px;
   
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
   margin-top : 7px;
   margin-left : 20px;
   padding : 3px;
   background-color:white;
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

 .wrapper {
   position: absolute;
   top : 0px;
 }

</style>
