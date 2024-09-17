import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/location',
      name: 'location',
      component: () => import('@/views/LocationView.vue')
    },
    {
      path: '/listCharacters',
      name: 'characters',
      component: () => import('@/views/CharactersView.vue')
    },
    {
      path: '/createCharacter',
      name: 'createCharacter',
      component: () => import('@/views/CreateCharacterView.vue')
    },
    {
      path: '/battle',
      name: 'battle',
      component: () => import('@/views/BattleView.vue')
    },
    {
      path: '/1vs1',
      name: '1vs1',
      component: () => import('@/views/Battle1vs1View.vue')
    },
    {
      path: '/fight/:listCharacters',
      name: 'fight',
      props: true,
      component: () => import('@/views/FightView.vue')
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('@/views/LogInView.vue')
    },
    {
      path: '/signup',
      name: 'signup',
      component: () => import('@/views/SignUpView.vue')
    },
    {
      path: '/myList',
      name: 'myList',
      component: () => import('@/views/MyList.vue')
    },
    {
      path:'/single/:characterId',
      name:'single',
      props: true,
      component: () => import('@/views/SingleCharacter.vue')
    }
  ]
})

export default router
