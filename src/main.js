import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { createPinia } from 'pinia'
import { OhVueIcon } from "oh-vue-icons";
import AOS from 'aos';
import 'aos/dist/aos.css';

const app = createApp(App)
AOS.init();
app.use(router)
app.component("v-icon",OhVueIcon)
app.use(createPinia())
app.mount('#app')
