<template>
  <section class="vh-100 background2">
    <AdminNav />
    <div class="container" style="padding-top: 90px;">
      <h2 class="text-center text-white">List of Attendees</h2>
      <div
        v-if="attendees.length"
        v-for="attendee in attendees"
        :key="attendee.userid"
        class="container custom-alert mt-4 ms-2"
      >
        <div class="row text-center" style="color: white; padding: 10px;">
          <div class="col-auto"></div>
          <div class="col" style="font-size: 24px;">{{ attendee.username }}</div>
          <div class="col-auto"></div>
          <div class="col" style="font-size: 20px;">{{ attendee.email }}</div>
          <div class="col-auto"></div>
          <div class="col">
            <select
              class="form-select custom-select text-white"
              aria-label="Default select example"
              v-model="selectedTask[attendee.userid]"
            >
              <option disabled value="">Select a task to assign</option>
              <option v-for="task in tasks" :key="task.task_id" :value="task.task_id">
                {{ task.task_name }} | {{ task.event_name }}
              </option>
            </select>
          </div>
          <div class="col-auto">
            <button @click="assignTask(attendee.userid)" class="btn btn-light">Assign</button>
          </div>
          <div class="col-auto">
            <button @click="removeUser(attendee.userid)" class="btn btn-dark text-center">Remove</button>
          </div>

        </div>
      </div>
      <div v-else class="alert alert-warning text-center">
        No attendees found.
      </div>
    </div>

    <div class="container text-center mt-2" style="padding-top: 30px;">
      <router-link to="/admin-dashboard/attendee-list/add-attendee" class="btn btn-outline-light btn-custom1">Add New Attendee</router-link>
    </div>
  </section>
</template>

<script>
import AdminNav from './AdminNav.vue';
import axios from 'axios';

export default {
  name: 'AttendeeList',
  components: {
    AdminNav,
  },
  data() {
    return {
      attendees: [],
      tasks: [],
      selectedTask: {}, // Stores the selected task for each attendee
    };
  },
  methods: {
    async fetchAttendees() {
      try {
        const response = await axios.get('http://localhost:5000/api/attendees', {
          headers: { Authorization: `Bearer ${localStorage.getItem('access_token')}` },
        });
        if (response.data.status === 'success') {
          this.attendees = response.data.attendees;
        } else {
          console.error('Failed to fetch attendees:', response.data.message);
        }
      } catch (error) {
        console.error('Error fetching attendees:', error);
      }
    },
    async fetchTasks() {
      try {
        const response = await axios.get('http://localhost:5000/api/fetch-tasks', {
          headers: { Authorization: `Bearer ${localStorage.getItem('access_token')}` },
        });
        if (response.data.status === 'success') {
          this.tasks = response.data.tasks;
        } else {
          console.error('Failed to fetch tasks:', response.data.message);
        }
      } catch (error) {
        console.error('Error fetching tasks:', error);
      }
    },
    async removeUser(userid) {
        if (!confirm('Are you sure you want to remove this user?')) {
            return;
        }
        try {
            const response = await axios.post(
                'http://localhost:5000/api/remove-user',
                { userid },
                { headers: { Authorization: `Bearer ${localStorage.getItem('access_token')}` } }
            );
            if (response.data.status === 'success') {
                alert(response.data.message);
                // Refresh the attendees list
                this.attendees = this.attendees.filter(attendee => attendee.userid !== userid);
            } else {
                alert(response.data.message);
            }
        } catch (error) {
            console.error('Error removing user:', error);
            alert('Failed to remove user. Please try again.');
        }
    },
    async assignTask(userid) {
      const taskId = this.selectedTask[userid];
      if (!taskId) {
        alert('Please select a task before assigning.');
        return;
      }

      try {
        const response = await axios.post(
          'http://localhost:5000/api/assign-task',
          { task_id: taskId, userid },
          { headers: { Authorization: `Bearer ${localStorage.getItem('access_token')}` } }
        );
        if (response.data.status === 'success') {
          alert(response.data.message);
        } else {
          alert(response.data.message);
        }
      } catch (error) {
        console.error('Error assigning task:', error);
        alert('Failed to assign task. Please try again.');
      }
    },
  },
  mounted() {
    this.fetchAttendees();
    this.fetchTasks();
  },
};
</script>


  
  <style>

  .custom-select option:disabled {
    color: rgba(144, 238, 144, 0.8)
  }

  .btn-custom1{
    letter-spacing: 2px;
    font-size: 20px;
    border-radius: 0px;
    padding: 12px 25px;
  }

  .btn-custom1:hover{
    background-color: rgba(180, 236, 255, 0.8);
  }
  .background2 {
    background: rgb(92, 0, 131);
    background: linear-gradient(90deg, rgba(92, 0, 131, 1) 4%, rgba(0, 20, 69, 1) 36%, rgba(84, 0, 148, 1) 68%, rgba(0, 130, 145, 1) 100%);
  }

  .custom-select{
    background-color: rgba(91, 66, 232, 0.9);
    color: white;
  }
  .custom-alert{
    background-color: rgba(91, 66, 232, 0.347);
    transition: box-shadow 0.2s ease-in-out;
    border-radius: 10px;
  }

  .custom-alert .col, .col-auto{
    padding: 10px;
  }

  .custom-alert:hover {
    box-shadow: 0 0 15px 2px rgba(113, 215, 255, 0.8), 
    0 0 30px 5px rgba(0, 123, 255, 0.6);
}
  </style>
  