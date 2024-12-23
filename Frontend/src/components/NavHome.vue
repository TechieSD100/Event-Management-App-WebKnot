<template>
    <div class="mask fixed-top d-flex justify-content-center align-items-center" 
         style="background-color: rgba(0, 0, 0, 0); z-index: 1050;">
      <div class="text-white text-center">
        <router-link to="/admin-login" class="btn btn-outline-light btn-lg m-2" role="button">Admin Login</router-link>
        <router-link to="/login" class="btn btn-outline-light btn-lg m-2" role="button">Attendee Login</router-link>
        <router-link to="/user-signup" class="btn btn-outline-light btn-lg m-2" role="button">Attendee Registration</router-link>
      </div>
    </div>
  </template>
  
  <script>
  import router from '@/routes';

  export default {
    name: "NavHome",
  };
  </script>
  
  <style scoped>
  .mask {
    width: 100%;
  }
  </style>
  


  