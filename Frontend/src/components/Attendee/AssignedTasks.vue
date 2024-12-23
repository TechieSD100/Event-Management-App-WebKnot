<template>
    <section class="vh-100 background4">
        <AttendeeNav />
        <div class="container height-adjust">
            <div class="container main-content">
                <div class="container">
                    <h1 class="text-center text-white">Your Assigned Tasks</h1>
                </div>

                <!-- Pending Tasks -->
                <div class="container mt-4">
                    <h3 class="text-white">Pending Tasks:</h3>
                    <div v-if="pendingTasks.length">
                    <div v-for="task in pendingTasks"
                    :key="task.task_id" class="container task-display mt-4">
                        <div
                            
                            class="row text-center mb-3"
                        >
                            <div class="col">
                                <h3 class="text-white mt-2"><strong>{{ task.task_name }}</strong></h3>
                            </div>
                            <div class="col-auto">
                                <p class="text-white">{{ task.description }}</p>
                            </div>
                            <div class="col">
                                <h4 class="text-white mt-2">{{ task.event_name }}</h4>
                            </div>
                            <div class="col">
                                <button
                                    @click="updateTaskStatus(task.task_id, 2)"
                                    class="btn btn-outline-success"
                                >
                                    Mark as Completed
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
                    <div v-else class="text-white">No pending tasks.</div>
                </div>

                <!-- Completed Tasks -->
                <div class="container mt-4" style="padding-top: 35px;">
                    <h3 class="text-white">Completed Tasks:</h3>
                    <div v-if="completedTasks.length">
                    <div v-for="task in completedTasks"
                    :key="task.task_id" class="container task-display">
                        <div
                            
                            class="row text-center mb-3"
                        >
                            <div class="col">
                                <h3 class="text-white mt-2"><strong>{{ task.task_name }}</strong></h3>
                            </div>
                            <div class="col-auto">
                                <p class="text-white">{{ task.description }}</p>
                            </div>
                            <div class="col">
                                <h4 class="text-white mt-2">{{ task.event_name }}</h4>
                            </div>
                            <div class="col">
                                <button
                                    @click="updateTaskStatus(task.task_id, 1)"
                                    class="btn btn-outline-warning"
                                >
                                    Mark as Pending
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
                    <div v-else class="text-white">No completed tasks.</div>
                </div>
            </div>
        </div>
    </section>
</template>



<style>
.background4{
    background: rgb(0,1,1);
    background: linear-gradient(225deg, rgba(0,1,1,1) 0%, rgba(82,5,120,1) 50%, rgba(0,94,111,1) 100%);
}
.task-display{
    padding-bottom: 10px;
}
</style>

<script>
import AttendeeNav from './AttendeeNav.vue';
import axios from 'axios';

export default {
    name: 'AssignedTasks',
    components: {
        AttendeeNav,
    },
    data() {
        return {
            userId: localStorage.getItem("user_id"),
            pendingTasks: [],
            completedTasks: [],
        };
    },
    methods: {
        async fetchTasks() {
            try {
                const response = await axios.get(`http://localhost:5000/api/user-tasks/${this.userId}`, {
                headers: { Authorization: `Bearer ${localStorage.getItem("access_token")}` },
            });


                if (response.data.status === 'success') {
                    const tasks = response.data.tasks;
                    this.pendingTasks = tasks.filter(task => task.status === 1);
                    this.completedTasks = tasks.filter(task => task.status === 2);
                } else {
                    console.error(response.data.message);
                }
            } catch (error) {
                console.error('Error fetching tasks:', error);
            }
        },
        async updateTaskStatus(taskId, newStatus) {
            try {
                const response = await axios.post(
                'http://localhost:5000/api/update-task-status',
                { task_id: taskId, status: newStatus }, // JSON payload
                { headers: { Authorization: `Bearer ${localStorage.getItem("access_token")}` } }
            );



                if (response.data.status === 'success') {
                    this.fetchTasks();
                } else {
                    console.error(response.data.message);
                }
            } catch (error) {
                console.error('Error updating task status:', error);
            }
        }
    },
    mounted() {
        this.fetchTasks();
    },
};
</script>
