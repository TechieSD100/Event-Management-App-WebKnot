<template>
    <div class="form-body">
      <div class="container">
        <div class="row justify-content-center align-items-center vh-100">
          <div class="col-md-8 col-lg-6">
            <div class="card cd bg-transparent border-light text-white p-4">
                <div class="row">
                    <div class="col-1"></div>
                    <div class="col-10"><h3 class="text-center">Create New Event</h3></div>
                    <div class="col-1"><router-link to="/admin-dashboard" type="button" class="btn-close close" aria-label="Close"></router-link></div>
                </div>
              <p class="text-center">Fill in the data below.</p>
              <form class="requires-validation" @submit.prevent="submitEvent" novalidate>
                <div class="mb-3">
                  <input class="form-control" type="text" name="name" placeholder="Event Name" v-model="eventName" required />
                </div>
                <div class="mb-3">
                  <textarea class="form-control" type="text" name="description" placeholder="Description" v-model="description" required></textarea>
                </div>
                <div class="mb-3">
                  <input class="form-control" type="text" name="location" placeholder="Location" v-model="location" required />
                </div>
                <div class="mb-3">
                  <input class="form-control" type="date" name="date" v-model="eventDate" required />
                  <label for="date" class="date-label">&nbsp;&nbsp;Event Date</label>
                </div>
                <div class="d-grid">
                  <button id="submit" type="submit" class="sub-but btn btn-info btn-lg">
                    Submit Event Details
                  </button>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  



<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;700;900&display=swap');

*, body {
    font-family: 'Poppins', sans-serif;
    font-weight: 400;
}


.form-body {
  padding: 20px;
}

.close{
    background-color: white;
    color: white;
    font-size: 20px;
    margin-left: -15px;
}

.cd{
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


.date-label{
    color: #b5cbffa0;
}

</style>



<script>
import axios from "axios";

export default {
  name: "CreateEvent",
  data() {
    return {
      eventName: "",
      description: "",
      location: "",
      eventDate: "",
    };
  },
  methods: {
    submitEvent() {
      axios
        .post("http://localhost:5000/api/create-event", {
          event_name: this.eventName,
          description: this.description,
          location: this.location,
          event_date: this.eventDate,
        })
        .then((response) => {
          alert("Event created successfully!");
          // Reset the form fields
          this.eventName = "";
          this.description = "";
          this.location = "";
          this.eventDate = "";
          this.$router.push("/admin-dashboard");
        })
        .catch((error) => {
          if (error.response) {
            // Handle API errors
            alert(error.response.data.error_message);
          } else {
            alert("Error creating event. Please try again.");
          }
        });
    },
  },
};
</script>