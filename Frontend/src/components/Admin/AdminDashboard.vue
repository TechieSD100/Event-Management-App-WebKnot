<template>
    <AdminNav />
    <div class="container height-adjust">
      <div class="container main-content">
      <h1 class="heading">List of Events</h1>
  
      <div class="row">
        <!-- Event Cards -->
        
          <div v-if="events.length" class="col-md-4 mt-4" v-for="event in events" :key="event.event_id">
          <router-link :to="`/admin-dashboard/event-dashboard/${event.event_id}`">
          <div class="card profile-card-5">
            <div class="card-img-block">
              <img
                class="card-img-top"
                src="../../assets/img/events/event1.jpg"
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
              <div class="text-center">
                <router-link :to="`/admin-dashboard/edit-event/${event.event_id}`" class="work btn btn-outline-dark m-2">
                  Edit Event
                </router-link>
                <button @click="deleteEvent(event.event_id)" class="work btn btn-outline-danger m-2">
                  Delete Event
                </button>
              </div>
            </div>
          </div>
        </router-link>
        </div>
        
  
        <!-- No Events Disclaimer -->
        <div v-else class="col-12 text-center">
          <br />
          <div class="alert alert-danger" role="alert">
            <h5>No events to display. Please add a new event.</h5>
          </div>
        </div>
  
        <!-- Add New Event Card -->
        <div class="col-md-4 mt-4 rem-under">
          <router-link to="/admin-dashboard/create-event" class="click">
            <div class="card add">
              <span class="ico">+</span>
              <span>Create New Event</span>
            </div>
          </router-link>
        </div>
      </div>
    </div>
    </div>
  </template>
  
  <script>
  import AdminNav from './AdminNav.vue';
  import axios from 'axios';
  
  export default {
    name: 'AdminDashboard',
    components: {
      AdminNav,
    },
    data() {
      return {
        events: [],
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
      async deleteEvent(eventId) {
        if (!confirm('Are you sure you want to delete this event?')) {
          return;
        }
        try {
          const response = await axios.delete(`http://localhost:5000/api/delete-event/${eventId}`);
          if (response.data.status === 'success') {
            alert(response.data.message);
            this.fetchEvents();
            this.$router.push("/admin-dashboard");
          } else {
            alert('Failed to delete event: ' + response.data.message);
          }
        } catch (error) {
          console.error('Error deleting event:', error);
          alert('An error occurred while deleting the event.');
        }
      },
      formatDate(dateString) {
        const date = new Date(dateString);
        const options = { day: '2-digit', month: '2-digit', year: 'numeric' };
        return date.toLocaleDateString('en-GB', options); // Format as DD-MM-YYYY
      },
    },
  };
  </script>
  
  <style>
  body {
    background: rgb(2, 0, 36);
    background: linear-gradient(270deg, rgba(2, 0, 36, 1) 0%, rgba(82, 0, 140, 1) 100%);
  }

  .height-adjust{
    margin-top: 50px;
  }
  
  .main-content {
    padding-top: 60px;
  }
  
  .heading {
    color: white;
    text-align: center;
  }
  
  .work {
    letter-spacing: 2px;
  }
  
  .add {
    background-color: rgba(255, 255, 255, 0.17);
    border: white dotted 4px;
    border-radius: 20px;
    color: white;
    font-size: 28px;
    text-align: center;
    padding: 10px;
    padding-bottom: 40px;
    margin-top: 70px;
    margin-bottom: 60px;
    text-decoration: none;
  }
  
  .add .ico {
    font-size: 120px;
    text-decoration: none;
  }
  
  .click {
    text-decoration: none;
  }
  
  .profile-card-5 {
    margin-top: 20px;
  }
  
  .card {
    margin-left: 10px;
    margin-right: 10px;
  }
  
  .profile-card-5 .btn {
    border-radius: 2px;
    text-transform: uppercase;
    font-size: 12px;
    padding: 7px 20px;
  }
  
  .profile-card-5 .card-img-block {
    width: 91%;
    margin: 0 auto;
    position: relative;
    top: -20px;
  }
  
  .profile-card-5 .card-img-block img {
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.63);
  }
  
  .profile-card-5 h5 {
    color: #4e5e30;
    font-weight: 600;
  }
  
  .profile-card-5 p {
    font-size: 14px;
    font-weight: 300;
  }
  
  .profile-card-5 .btn-primary {
    background-color: #4e5e30;
    border-color: #4e5e30;
  }
  </style>
  