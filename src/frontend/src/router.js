import { createMemoryHistory, createRouter } from 'vue-router'

import HomeView from './views/HomeView.vue'
import ProductView from './views/ProductView.vue'

const routes = [
  { path: '/', component: HomeView },
  { path: '/product/:id', component: ProductView },
]

export const router = createRouter({
  history: createMemoryHistory(),
  routes,
})

export default {
  router
}