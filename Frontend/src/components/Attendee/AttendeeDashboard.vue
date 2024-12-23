<template>
    <section class="vh-100 background3">
        <AttendeeNav/>
        <div class="container height-adjust">
            <div class="container main-content">
            <div class="container front">
                <h1 class="display text-center">Welcome to the Event Management App</h1>
            </div>
            <h1 class="heading">List of Events</h1>
  
  <div class="row">
    <!-- Event Cards -->
    
    <div v-if="events.length" class="col-md-4 mt-4" v-for="event in events" :key="event.event_id">
      <div class="card profile-card-5 userpc">
        <div class="card-img-block">
          <img
            class="card-img-top"
            src="../../assets/img/events/event2.jpg"
            alt="Card image cap"
            style="border-radius: 15px;"
          />
        </div>
        <div class="card-body pt-0">
          <h5 class="card-title">{{ event.event_name }}</h5>
          <p class="card-text">{{ event.description }}</p>
          <div class="row" style="padding-left: 5px; padding-right: 10px; padding-bottom: 10px">
            <div class="col">
              <p class="card-text text-left" style="font-size: 20px;"><b>{{ event.location }}</b></p>
            </div>
            <div class="col">
              <p class="card-text" style="font-size: 20px; text-align: right;"><b>{{ formatDate(event.event_date) }}</b></p>
            </div>
          </div>
        </div>
      </div>
    </div>
    

    <!-- No Events Disclaimer -->
    <div v-else class="col-12 text-center">
      <br />
      <div class="alert alert-danger" role="alert">
        <h5>No events are available as of now.</h5>
      </div>
        </div>
        </div>
        </div>
        </div>
    </section>

    <div class="full fixed-top" v-if="isRemoved == 1">
      <h4 class="centered-text" style="color: red;">Your account has been removed by the admin.</h4>
      <p>Please contact the admin to seek for validity.</p><br>
      <a class="btn btn-danger" @click="logout0">Logout</a>
    </div>
</template>

<style>
@import url('https://fonts.googleapis.com/css2?family=Oswald:wght@200..700&display=swap');
</style>

<style>
.full{
  background-color: white;
  width: 100%;
  height: 100%;
  text-align: center;
}
.full h4{
  margin-top: 18%;
}

.height-adjust{
    padding-bottom: 80px;
}
.front{
    background: linear-gradient(135deg, rgba(16,81,98,1) 0%, rgba(66,6,122,1) 24%, rgba(12,0,23,1) 50%, rgba(63,11,106,1) 78%, rgba(0,63,74,1) 100%);
    padding: 30px;
    border-radius: 20px;
    margin-bottom: 40px;
}
.display{
    font-size: 60px;
    font-family: "Oswald", serif;
  font-optical-sizing: auto;
  font-weight: 400;
  font-style: normal;
  color: lightblue;
  transition: 0.5s ease-in-out;
}

@media (max-width: 768px) {
.display{
    font-size: 30px;
    letter-spacing: 1px;
  }
  .front{
    padding: 15px;
  }
  .front:hover .display{
    letter-spacing: 1px;
}
}
.front:hover .display{
    letter-spacing: 2px;
}
.background3{
    background: rgb(25,126,153);
background: linear-gradient(135deg, rgba(25,126,153,1) 0%, rgba(103,7,194,1) 24%, rgba(36,0,69,1) 50%, rgba(92,16,154,1) 78%, rgba(0,103,120,1) 100%);
}
.userpc{
    transition: 0.3s ease-in-out;
}
.userpc:hover{
    margin-top: 50px;

}
</style>

<script>
import AttendeeNav from './AttendeeNav.vue';
import axios from 'axios';

export default{
    name: 'AttendeeDashboard',
    components: {
        AttendeeNav,
    },
    data() {
      return {
        events: [],
        userId: localStorage.getItem("user_id"),
      };
    },
    mounted() {
      this.fetchEvents();
    },
    methods: {
      async fetchEvents() {
        try {
          const response = await axios.get('http://localhost:5000/api/events', {
            headers: { Authorization: `Bearer ${localStorage.getItem('access_token')}` }
          });
          if (response.data.status === 'success') {
            this.events = response.data.events;
          } else {
            console.error('Failed to fetch events: ', response.data.message);
          }
        } catch (error) {
          console.error('Error fetching events:', error);
        }
      },
      formatDate(dateString) {
        const date = new Date(dateString);
        const options = { day: '2-digit', month: '2-digit', year: 'numeric' };
        return date.toLocaleDateString('en-GB', options); // Format as DD-MM-YYYY
      },
      logout0() {
      localStorage.removeItem('access_token');
      this.$router.push('/login');
      window.alert('You are logged out.');
    }
    },
};
</script>