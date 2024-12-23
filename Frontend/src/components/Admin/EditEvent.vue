<template>
    <div class="form-body">
      <div class="container">
        <div class="row justify-content-center align-items-center vh-100">
          <div class="col-md-8 col-lg-6">
            <div class="card cd bg-transparent border-light text-white p-4">
              <div class="row">
                <div class="col-1"></div>
                <div class="col-10"><h3 class="text-center">Edit Event</h3></div>
                <div class="col-1"><router-link to="/admin-dashboard" type="button" class="btn-close close" aria-label="Close"></router-link></div>
              </div>
              <p class="text-center">Edit the data below.</p>
              <form @submit.prevent="updateEvent" class="requires-validation" novalidate>
                <div class="mb-3">
                  <input v-model="event.event_name" class="form-control" type="text" placeholder="Event Name" required />
                </div>
                <div class="mb-3">
                  <textarea v-model="event.description" class="form-control" placeholder="Description" required></textarea>
                </div>
                <div class="mb-3">
                  <input v-model="event.location" class="form-control" type="text" placeholder="Location" required />
                </div>
                <div class="mb-3">
                  <input v-model="event.event_date" class="form-control" type="date" required />
                  <label for="date" class="date-label">&nbsp;&nbsp;Event Date</label>
                </div>
                <div class="d-grid">
                  <button id="submit" type="submit" class="sub-but btn btn-info btn-lg">
                    Submit Updated Details
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
    name: 'EditEvent',
    data() {
      return {
        event: {
          event_name: '',
          description: '',
          location: '',
          event_date: '',
        },
      };
    },
    mounted() {
      const eventId = this.$route.params.eventId; // Get eventId from route params
      if (eventId) {
        this.fetchEventDetails(eventId);
      } else {
        alert("Event ID is missing");
      }
    },
    methods: {
      async fetchEventDetails(eventId) {
        try {
          const response = await axios.get(`http://localhost:5000/api/event-details/${eventId}`);
          if (response.data.status === 'success') {
            this.event = response.data.event;
          } else {
            alert('Error fetching event details: ' + response.data.message);
          }
        } catch (error) {
          console.error('Error fetching event details:', error);
        }
      },
      async updateEvent() {
        const eventId = this.$route.params.eventId;
        try {
          const response = await axios.put(`http://localhost:5000/api/edit-event/${eventId}`, this.event);
          if (response.data.status === 'success') {
            alert(response.data.message);
            this.$router.push('/admin-dashboard'); // Navigate back to dashboard
          } else {
            alert('Failed to update event: ' + response.data.message);
          }
        } catch (error) {
          console.error('Error updating event:', error);
          alert('An error occurred while updating the event.');
        }
      },
    },
  };
  </script>
  
  <style scoped>
  @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;700;900&display=swap');
  
  *, body {
    font-family: 'Poppins', sans-serif;
    font-weight: 400;
  }
  
  .form-body {
    padding: 20px;
  }
  
  .close {
    background-color: white;
    color: white;
    font-size: 20px;
    margin-left: -15px;
  }
  
  .cd {
    border-radius: 20px;
    box-shadow: 0px 4px 10px rgba(255, 255, 255, 0.3);
    border: white solid 4px;
  }
  
  textarea {
    resize: none;
    height: 120px;
  }
  
  textarea:focus,
  input:focus {
    background-color: #ebeff8;
    border-color: #495057;
  }
  
  .sub-but {
    box-shadow: none !important;
  }
  
  .sub-but:hover {
    background-color: #94e9f7;
  }
  
  .date-label {
    color: #b5cbffa0;
  }
  </style>
  