<template>
    <section class="vh-100 background3">
        <AdminNav />
        <div class="height-adjust">
            <div class="container main-content">
            <div class="container event-primary" v-if="event">
                <div class="row text-center justify-content-center">
                    <div class="col-auto"></div>
                    <div class="col-auto">
                        <h1 class="text-white">{{ event.event_name }}</h1>
                    </div>
                    <div class="col-auto"></div>
                    <div class="col">
                        <h4 class="text-white mt-3">{{ event.location }}</h4>
                    </div>
                    <div class="col">
                        <h4 class="text-white mt-3">{{ event.event_date }}</h4>
                    </div>
                </div>
                <div class="row">
                    <div class="col">
                        <p class="desc text-center mt-2">{{ event.description }}</p>
                    </div>
                </div>
            </div>
            <div v-else>
                <p class="text-white text-center mt-5">Loading event details...</p>
            </div>


            <div class="container mt-4">
                <h3 class="text-white">Pending Tasks:</h3>
                <div v-if="pendingTasks.length > 0">
                    <div v-for="task in pendingTasks" :key="task.task_id" class="container task-display mt-4">
                        <div class="row text-center mb-3">
                            <div class="col">
                                <h3 class="text-white mt-2">{{ task.task_name }}</h3>
                            </div>
                            <div class="col-auto">
                                <p class="text-white">
                                    {{ task.description }}
                                    <br>
                                    <span class="highlight1"><strong>Task Assigned to: </strong>{{ task.assigned_to }}</span>
                                </p>
                            </div>
                            <div class="col">
                                <router-link :to="`/admin-dashboard/event-dashboard/${event.event_id}/edit-task/${task.task_id}`" class="btn btn-outline-warning mt-2">Edit Task</router-link>
                            </div>
                            <div class="col">
                                <a href="#" class="btn btn-outline-danger mt-2" @click="deleteTask(task.task_id)">Delete Task</a>
                            </div>
                            <div class="col">
                                <a href="#" class="btn btn-outline-success" @click="markTaskAsCompleted(task.task_id)">Mark as Completed</a>
                            </div>
                        </div>
                    </div>
                </div>
                <div v-else>
                    <p class="text-white">No pending tasks found.</p>
                </div>
                
            </div>
                

            <div class="container mt-4">
                <h3 class="text-white">Completed Tasks:</h3>
                <div v-if="completedTasks.length > 0">
                    <div v-for="task in completedTasks" :key="task.task_id" class="container task-display mt-4">
                    <div class="row text-center mb-3">
                        <div class="col">
                            <h3 class="text-white mt-2">{{ task.task_name }}</h3>
                        </div>
                        <div class="col-auto">
                            <p class="text-white text-center">{{ task.description }}
                                <br>
                                <span class="highlight1"><strong>Task Completed by: </strong>{{ task.assigned_to }}</span>
                            </p>
                        </div>
                        <div class="col">
                            <a href="#" class="btn btn-outline-danger" @click="deleteTask(task.task_id)">Delete Task</a>
                        </div>
                    </div>
                </div>
                </div>
                <div v-else>
                    <p class="text-white">No completed tasks found.</p>
                </div>
            </div>


            <div class="container text-center mt-4" style="margin-top: 50px;" v-if="event">
                <router-link :to="`/admin-dashboard/event-dashboard/${event.event_id}/create-task`" class="create btn btn-outline-info">
                    Create New Task
                </router-link>
            </div>
        </div>
        </div>
    </section>
</template>



<style>
.highlight1{
    color: rgb(255, 255, 181);
    font-size: 18px;
}
.navbtn {
    letter-spacing: 2px;
}
.create{
    letter-spacing: 2px;
    font-size: 30px;
    border-radius: 0px;
    padding: 15px 45px;
}
.create:hover{
    background-color: rgba(49, 193, 255, 0.5);
}

@media (max-width: 768px) {
  .create {
    font-size: 20px;
    padding: 10px 30px;
  }
}

.button {
    margin-top: 0;
    margin-bottom: 0
}

.btn.btn-large {
    font-size: 18px;
    padding: 18px 35px
}
.background3 {
    background: rgb(0,0,0);
    background: linear-gradient(45deg, rgba(0,0,0,1) 0%, rgba(36,0,69,1) 50%, rgb(0, 56, 120) 100%);
}

.event-primary{
    padding: 20px;
    background-color: rgba(255, 255, 255, 0.09);
    border-radius: 15px
}

.task-display{
    padding: 30px;
    background-color: rgba(0, 0, 0, 0.4);
    border-radius: 15px
}
.task-display .btn{
    letter-spacing: 2px;
    border-radius: 0px;
    padding: 10px 20px;
}

@media (max-width: 768px) {
.task-display .btn{
    font-size: 13px;
    margin: 5px;
  }
}

.desc{
    color: rgba(211, 211, 211, 0.5);
}
</style>



<script>
import AdminNav from './AdminNav.vue';
import axios from 'axios';

export default {
    name: 'EventDashboard',
    components: {
        AdminNav,
    },
    data() {
        return {
            event: null, // To store the specific event details
            tasks: [], // To store tasks related to the event
            pendingTasks: [], // Tasks with status 0
            completedTasks: [], // Tasks with status 1
        };
    },
    mounted() {
        const eventId = this.$route.params.eventId; // Fetch eventId from route params
        if (eventId) {
            this.fetchEventDetails(eventId);
        } else {
            alert("Event ID is missing");
        }
    },
    methods: {
        async fetchEventDetails(eventId) {
            try {
                const response = await axios.get(`http://localhost:5000/api/event-dashboard/${eventId}`);
                if (response.data.status === 'success') {
                    this.event = response.data.event;
                    this.tasks = response.data.tasks;
                    localStorage.setItem('event_id', this.event.event_id);
                    this.categorizeTasks();
                } else {
                    console.error('Error:', response.data.message);
                }
            } catch (error) {
                console.error('Error fetching event:', error);
            }
        },
        categorizeTasks() {
            this.pendingTasks = this.tasks.filter(task => task.status === 0 || task.status === 1);
            this.completedTasks = this.tasks.filter(task => task.status === 2);
        },
        async deleteTask(taskId) {
            try {
                const response = await axios.delete(`http://localhost:5000/api/task/${taskId}/delete`);
                if (response.data.status === 'success') {
                    this.tasks = this.tasks.filter(task => task.task_id !== taskId);
                    this.categorizeTasks();
                    alert('Task deleted successfully');
                } else {
                    console.error('Error:', response.data.message);
                }
            } catch (error) {
                console.error('Error deleting task:', error);
            }
        },
        async markTaskAsCompleted(taskId) {
            try {
                const response = await axios.put(`http://localhost:5000/api/task/${taskId}/complete`);
                if (response.data.status === 'success') {
                    // Find the task and update its status
                    const taskIndex = this.tasks.findIndex(task => task.task_id === taskId);
                    if (taskIndex !== -1) {
                        this.tasks[taskIndex].status = 2; // Update status to "completed"
                    }
                    // Re-categorize tasks to reflect the changes
                    this.categorizeTasks();
                    alert('Task marked as completed');
                } else {
                    console.error('Error:', response.data.message);
                }
            } catch (error) {
                console.error('Error marking task as completed:', error);
            }
        }

    },
};
</script>

