<template>
    <div class="form-body">
        <div class="container">
            <div class="row justify-content-center align-items-center vh-100">
                <div class="col-md-8 col-lg-6">
                    <div class="card cd bg-transparent border-light text-white p-4">
                        <div class="row">
                            <div class="col-1"></div>
                            <div class="col-10">
                                <h3 class="text-center">Edit Task</h3>
                            </div>
                            <div class="col-1">
                                <router-link :to="`/admin-dashboard/event-dashboard/${eventId}`" type="button" class="btn-close close" aria-label="Close"></router-link>
                            </div>
                        </div>
                        <p class="text-center">Edit the data below.</p>
                        <form @submit.prevent="submitTaskDetails">
                            <div class="mb-3">
                                <input
                                    class="form-control"
                                    type="text"
                                    v-model="task.task_name"
                                    placeholder="Task Name"
                                    required
                                />
                            </div>
                            <div class="mb-3">
                                <textarea
                                    class="form-control"
                                    v-model="task.description"
                                    placeholder="Task Description"
                                    required
                                ></textarea>
                            </div>

                            <div class="mb-3">
                                <label for="assigned-attendee">Assign Different Attendee:</label>
                                <select v-model="assignedUserId" class="form-select">
                                    <option v-for="user in users" :key="user.userid" :value="user.userid">
                                        {{ user.username }}
                                    </option>
                                    <option :value="null">Assign Later</option>
                                </select>
                            </div>

                            <div class="mb-3">
                                <input
                                    class="form-control"
                                    type="text"
                                    :value="eventName"
                                    placeholder="Event Name"
                                    disabled
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
    name: "EditTask",
    data() {
        return {
            task: {},
            assignedUserId: null,
            users: [],
            eventName: "",
            eventId: localStorage.getItem("event_id"),
        };
    },
    mounted() {
        const taskId = this.$route.params.taskId;
        if (taskId) {
            this.fetchTaskDetails(taskId);
        } else {
            alert("Task ID is missing");
        }
    },
    methods: {
        async fetchTaskDetails(taskId) {
            try {
                const response = await axios.get(`http://localhost:5000/api/task/${taskId}`);
                if (response.data.status === "success") {
                    this.task = response.data.task;
                    this.assignedUserId = response.data.assigned_user?.userid || null;
                    this.eventName = response.data.event?.event_name || "";
                    this.fetchUsers(); // Load users for assignment
                } else {
                    console.error("Error:", response.data.message);
                }
            } catch (error) {
                console.error("Error fetching task details:", error);
            }
        },
        async fetchUsers() {
            try {
                const response = await axios.get(`http://localhost:5000/api/get-users`); // Add API endpoint for users
                if (response.data.status === "success") {
                    this.users = response.data.users;
                } else {
                    console.error("Error:", response.data.message);
                }
            } catch (error) {
                console.error("Error fetching users:", error);
            }
        },
        async submitTaskDetails() {
            try {
                const response = await axios.put(
                    `http://localhost:5000/api/task/${this.task.task_id}/update`,
                    {
                        task_name: this.task.task_name,
                        description: this.task.description,
                        status: this.task.status,
                        assigned_user_id: this.assignedUserId,
                    }
                );
                if (response.data.status === "success") {
                    alert("Task updated successfully");
                    this.$router.push(`/admin-dashboard/event-dashboard/${this.task.event_id}`);
                } else {
                    console.error("Error:", response.data.message);
                }
            } catch (error) {
                console.error("Error updating task:", error);
            }
        },
    },
};
</script>
