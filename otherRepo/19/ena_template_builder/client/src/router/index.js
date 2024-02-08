import { createRouter, createWebHistory } from 'vue-router'
import LandingView from '../views/LandingView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'intro',
      component: LandingView
    },
    {
      path: '/study',
      name: 'study',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/StudyView.vue')
    },
    {
      path: '/experiment',
      name: 'experiment',
      component: () => import('../views/ExperimentView.vue')
    },
    {
      path: '/run',
      name: 'run',
      component: () => import('../views/RunView.vue')
    },
    {
      path: '/sample',
      name: 'sample',
      component: () => import('../views/SampleView.vue')
    },
    {
      path: '/submit',
      name: 'submit',
      component: () => import('../views/SubmitView.vue')
    },
    {
      path: '/success',
      name: 'success',
      component: () => import('../views/SuccessView.vue')
    }
  ]
})

export default router
