<template>
    <div class="form-body">
      <div class="container">
        <div class="row justify-content-center align-items-center vh-100">
          <div class="col-md-8 col-lg-6">
            <div class="card cd bg-transparent border-light text-white p-4">
                <div class="row">
                    <div class="col-1"></div>
                    <div class="col-10"><h3 class="text-center">Add New Attendee</h3></div>
                    <div class="col-1"><router-link to="/admin-dashboard/attendee-list" type="button" class="btn-close close" aria-label="Close"></router-link></div>
                </div>
              <p class="text-center">Fill in the data below.</p>
              <form class="requires-validation" @submit.prevent="handleSignup" novalidate>
                <div class="mb-3">
                  <input class="form-control" type="text" id="username" name="username" placeholder="Attendee Name" v-model="username" required />
                </div>
                <div class="mb-3">
                  <input class="form-control" type="email" id="useremail" name="email" placeholder="Email Address" v-model="email" required />
                </div>
                <div class="mb-3">
                    <input class="form-control" is="userpass" name="password" type="password" placeholder="Password" v-model="password" required />
                </div>
                <div class="d-grid">
                  <button id="submit" type="submit" class="sub-but btn btn-info btn-lg">
                    Submit Attendee Details
                  </button>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'CreateAttendee',
    data(){
        return{
            username: '',
            email: '',
            password: '',
        };
    },
    methods: {
        handleSignup(){
            if (!this.username.trim()) {
                alert("Attendee name cannot be empty.");
                return;
            }
            if (!this.email.trim() || !this.email.includes("@")) {
                alert("Please provide a valid email address.");
                return;
            }
            if (!this.password.trim() || this.password.length < 1) {
                alert("Please provide a valid password.");
                return;
            }

            
            const userData = {
                username: this.username,
                email: this.email,
                password: this.password,
                message: null
            };
            axios.post("http://127.0.0.1:5000/api/signup", userData)
            .then((response) => {
                if (response.data.status === "success") {
                    this.$router.push("/admin-dashboard/attendee-list");
                    alert("New Attendee Added! User can now login using those credentials.");
                } else {
                    alert(response.data.message);
                }
            })
            .catch((error) => {
                console.error(error);
                alert("An error occurred while onboarding the New Attendee.");
            });
        },
    },
};
</script>