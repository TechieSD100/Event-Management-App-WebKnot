<template>
    <nav class="navbar fixed-top navbar-expand-lg bg-dark border-bottom border-body" data-bs-theme="dark">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Admin Dashboard</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
        <li class="nav-item me-3">
          <router-link class="navbtn nav-link btn btn-outline-success" to="/admin-dashboard">Events</router-link>
        </li>
        <li class="nav-item me-3">
          <router-link to="/admin-dashboard/attendee-list" class="navbtn nav-link btn btn-outline-info">Attendees</router-link>
        </li>
        <li class="nav-item me-3 text-center">
          <a class="navbtn btn btn-outline-danger" @click="logout">Logout</a>
        </li>
      </ul>
    </div>
  </div>
</nav>
</template>

<style>
a{
    color: white;
}
</style>


<script>
  import router from '@/routes';

  export default {
    name: "AdminNav",
    methods: {
    logout() {
      localStorage.removeItem('access_token');
      this.$router.push('/admin-login');
      window.alert('You are logged out.');
    }
  }
  };
</script>