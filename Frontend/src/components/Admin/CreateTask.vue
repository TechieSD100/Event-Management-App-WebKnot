<template>
  <div class="form-body">
    <div class="container">
      <div class="row justify-content-center align-items-center vh-100">
        <div class="col-md-8 col-lg-6">
          <div class="card cd bg-transparent border-light text-white p-4">
            <div class="row">
              <div class="col-1"></div>
              <div class="col-10">
                <h3 class="text-center">Create New Task</h3>
              </div>
              <div class="col-1">
                <router-link :to="`/admin-dashboard/event-dashboard/${eventId}`" type="button" class="btn-close close" aria-label="Close"></router-link>
              </div>
            </div>
            <p class="text-center">Fill in the data below.</p>
            <form @submit.prevent="submitTask" class="requires-validation" novalidate>
              <div class="mb-3">
                <input
                  v-model="taskName"
                  class="form-control"
                  type="text"
                  name="taskName"
                  placeholder="Task Name"
                  required
                />
              </div>
              <div class="mb-3">
                <textarea
                  v-model="description"
                  class="form-control"
                  name="description"
                  placeholder="Task Description"
                  required
                ></textarea>
              </div>
              <div class="mb-3">
                <!-- Show Event Name -->
                <input
                  class="form-control"
                  type="text"
                  :value="event.event_name"
                  placeholder="Event Name"
                  disabled
                />
                <!-- Hidden field for Event ID -->
                <input
                  type="hidden"
                  v-model="event.event_id"
                  name="eventId"
                />
              </div>
              <div class="d-grid">
                <button id="submit" type="submit" class="sub-but btn btn-info btn-lg">
                  Submit Task Details
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
import axios from "axios";

export default {
  name: "CreateTask",
  data() {
    return {
      taskName: "",
      description: "",
      event: {}, // To store event details
      eventId: localStorage.getItem('event_id')
    };
  },
  mounted() {
    const eventId = this.$route.params.eventId; // Extract event ID from the URL
    if (eventId) {
      this.fetchEventDetails(eventId);
    } else {
      alert("Event ID is missing in the URL.");
    }
  },
  methods: {
    async fetchEventDetails(eventId) {
      try {
        const response = await axios.get(`http://localhost:5000/api/event-dashboard/${eventId}`);
        if (response.data.status === "success") {
          this.event = response.data.event;
        } else {
          console.error(response.data.message);
        }
      } catch (error) {
        console.error("Error fetching event details:", error);
      }
    },
    async submitTask() {
      const eventId = this.event.event_id; // Extract event ID from the event object
      if (!this.taskName || !this.description) {
        alert("Please fill in all the required fields.");
        return;
      }
      try {
        const response = await axios.post(`http://localhost:5000/api/event-dashboard/${eventId}/create-task`, {
          task_name: this.taskName,
          description: this.description,
        });
        if (response.data.status === "success") {
          alert("Task created successfully!");
          this.$router.push(`/admin-dashboard/event-dashboard/${eventId}`);
        } else {
          console.error(response.data.message);
        }
      } catch (error) {
        console.error("Error submitting task:", error);
      }
    },
  },
};
</script>

