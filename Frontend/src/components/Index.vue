<template>
    <NavHome/>
    <section class="vh-100 background">
  <div class="container py-5 h-100">
    <div class="row d-flex justify-content-center align-items-center h-100">
      <div class="col col-xl-10">
        <div class="card" style="border-radius: 1rem;">
          <div class="row g-0">
            <div class="col-md-6 col-lg-5 d-none d-md-block">
              <img src="../assets/img/login.jpg"
                alt="login form" class="img-fluid" style="border-radius: 1rem 0 0 1rem; height: 100%;" />
            </div>
            <div class="col-md-6 col-lg-7 d-flex align-items-center">
              <div class="card-body p-4 p-lg-5 text-black">

                <form @submit.prevent="handleLogin">

                  <div class="d-flex align-items-center mb-3 pb-1">
                    <!-- <i class="fas fa-cubes fa-2x me-3" style="color: #ff6219;"></i> -->
                    <span class="h1 fw-bold mb-0">Attendee Login</span>
                  </div>

                  <h5 class="fw-normal mb-3 pb-3" style="letter-spacing: 1px;">Sign into your account</h5>

                  <p :class="{'alert-success': loginSuccess, 'alert-danger': !loginSuccess}" v-if="loginMessage" style="color: red;">
                    {{ loginMessage }}
                  </p>

                  <div data-mdb-input-init class="form-outline mb-4">
                    <input type="email" id="useremail" class="form-control form-control-lg" v-model="email" />
                    <label class="form-label" for="useremail">Email address</label>
                  </div>

                  <div data-mdb-input-init class="form-outline mb-4">
                    <input type="password" id="userpass" class="form-control form-control-lg" v-model="password" />
                    <label class="form-label" for="userpass">Password</label>
                  </div>

                  <div class="pt-1 mb-4">
                    <button data-mdb-button-init data-mdb-ripple-init class="btn btn-dark btn-lg btn-block" type="submit">Login</button>
                  </div>

                  <!-- <a class="small text-muted" href="#!">Forgot password?</a> -->
                  <p class="mb-5 pb-lg-2" style="color: #393f81;">Don't have an account? <router-link to="/user-signup"
                      style="color: #393f81;">Register here</router-link></p>
                  <!-- <a href="#!" class="small text-muted">Terms of use.</a>
                  <a href="#!" class="small text-muted">Privacy policy</a> -->
                </form>

              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="container headline2">
      <h1 class="headl text-center"><strong>Event Management App</strong></h1>
    </div>
  </div>
</section>
</template>


<style>
.background{
    background: rgb(2,0,36);
    background: linear-gradient(315deg, rgba(2,0,36,1) 0%, rgba(118,22,159,1) 52%, rgb(0, 149, 241) 100%);
}
</style>


<script>
import NavHome from './NavHome.vue';
import axios from 'axios';

export default {
  name: "Login",
  components: {
    NavHome
  },
  data() {
    return {
      email: '',
      password: '',
      loginMessage: '',
      loginSuccess: false
    };
  },
  methods: {
  handleLogin() {
    const loginData = {
      email: this.email,
      password: this.password,
    };

    axios.post("http://127.0.0.1:5000/api/login", loginData)
      .then((response) => {
        if (response.data.status === "success") {
          this.loginMessage = "Login Successful!";
          this.loginSuccess = true;
          const userId = response.data.user.userid;
          localStorage.setItem('user_id', userId);
          this.$router.push(`/attendee-dashboard/${userId}`); // Redirect to dashboard
        } else {
          this.loginMessage = response.data.message; // Backend error message
          this.loginSuccess = false;
        }
      })
      .catch((error) => {
        // Handle errors from the backend
        if (error.response && error.response.data) {
          this.loginMessage = error.response.data.error_message || "An error occurred.";
        } else {
          this.loginMessage = "A network error occurred. Please try again.";
        }
        this.loginSuccess = false;
      });
  },
},
};
</script>