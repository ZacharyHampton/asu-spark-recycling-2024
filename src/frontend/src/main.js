import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import './assets/index.css'
import App from './App.vue'
import HomeView from './views/HomeView.vue'
import ProductView from './views/ProductView.vue'

const router = createRouter({
    history: createWebHistory(),
    routes: [
        { path: '/', component: HomeView },
        { name: 'product', path: '/product/:id', component: ProductView },
    ]
});

const app = createApp(App)

app.use(router);

app.mount('#app')