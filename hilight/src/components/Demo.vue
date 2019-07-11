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
          color="#82C7EB"
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
          color="#82C7EB"
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

      <div ref="1:1" class="card" @click="window_update(1,1)"></div>
      <div ref="1:2" class="card" @click="window_update(1,2)"></div>
      <div ref="1:3" class="card" @click="window_update(1,3)"></div>
    </div>

    <div class = "cards">
      <div ref="2:1" class="card" @click="window_update(2,1)"></div>                       
      <div ref="2:2" class="card" @click="window_update(2,2)"></div>
      <div ref="2:3" class="card" @click="window_update(2,3)"></div>
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
       detection : false
     }
   },

   watch: {

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
		 
		 load () {
			 
			 for (index = 0; index < res.data.length; ++index) {
				 if (res[index].id == "paint")
					 {
						 this.paint = res[index].demo == "True"
					 }

				 if (res[index].id == "detection")
					 {
						 this.detection = res[index].demo == "True"
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

<style>

</style>
