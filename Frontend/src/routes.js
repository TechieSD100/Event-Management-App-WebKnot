import { createRouter, createWebHistory } from 'vue-router'
import Index from './components/Index.vue'
import AdminLogin from './components/AdminLogin.vue';
import SignUp from './components/SignUp.vue';
import AdminDashboard from './components/Admin/AdminDashboard.vue';
import CreateEvent from './components/Admin/CreateEvent.vue';
import EditEvent from './components/Admin/EditEvent.vue'
import AttendeeList from './components/Admin/AttendeeList.vue';
import EventDashboard from './components/Admin/EventDashboard.vue';
import CreateTask from './components/Admin/CreateTask.vue';
import EditTask from './components/Admin/EditTask.vue';



const routes = [
    { path: '/', redirect: '/login'},
    { name: 'Index', component: Index, path: '/login' },
    { name: 'AdminLogin', component: AdminLogin, path: '/admin-login'},
    { name: 'SignUp', component: SignUp, path: '/user-signup' },
    { name: 'AdminDashboard', component: AdminDashboard, path: '/admin-dashboard' },
    { name: 'CreateEvent', component: CreateEvent, path: '/admin-dashboard/create-event' },
    { name: 'EditEvent', component: EditEvent, path: '/admin-dashboard/edit-event/:eventId' },
    { name: 'AttendeeList', component: AttendeeList, path: '/admin-dashboard/attendee-list' },
    { name: 'EventDashboard', component: EventDashboard, path: '/admin-dashboard/event-dashboard/:eventId' },
    { name: 'CreateTask', component: CreateTask, path: '/admin-dashboard/event-dashboard/:eventId/create-task' },
    { name: 'EditTask', component: EditTask, path: '/admin-dashboard/event-dashboard/:eventId/edit-task/:taskId' }
]

// Creating router instance
const router = createRouter({
    history: createWebHistory(),
    routes
});

export default router;