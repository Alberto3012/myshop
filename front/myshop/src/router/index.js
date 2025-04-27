import { createRouter, createWebHistory } from 'vue-router'
import Login from '../components/Login.vue'
import Register from '../components/Register.vue'
import Dashboard from '../components/Dashboard.vue'
import Detail from '../components/Detail.vue'
import { isLoggedIn } from '../api/userService';

const routes = [
  { path: '/', redirect: '/login' },
  { path: '/login', component: Login },
  { path: '/register', component: Register },
  {
    path: '/dashboard',
    component: Dashboard,
    beforeEnter: (to, from, next) => {
      if (isLoggedIn()) {
        next();
      } else {
        next('/login');
      }
    }
  },
  {
    path: '/detail/:id',
    component: Detail,
    beforeEnter: (to, from, next) => {
      if (isLoggedIn()) {
        next();
      } else {
        next('/login');
      }
    }
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
});

router.beforeEach((to, from, next) => {
  if (to.path === '/login' && isLoggedIn()) {
    next('/dashboard');
  } else {
    next();
  }
});

export default router
