<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useSessionStore } from '@/stores/session.js';
import { useRouter } from 'vue-router';

const sessionStore = useSessionStore()
const router = useRouter()

const logout = async () => {
  sessionStore.logout()
  router.push('/login')
}

</script>

<template>
  <header>
    <img alt="Dragon ball logo" class="logo"
      src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Flogos-marcas.com%2Fwp-content%2Fuploads%2F2021%2F02%2FDragon-Ball-Emblema.png&f=1&nofb=1&ipt=ba95fb820c6244e2a33325821f5bfeaf3df24a46faaf986ad1ebf1cd2f2d3516&ipo=images" />
    <div class="wrapper">
      <nav>
        <RouterLink to="/listCharacters">List of Characters</RouterLink>
        <RouterLink to="/location">Location</RouterLink>
        <RouterLink  v-if="sessionStore.user" to="/createCharacter">Create Character</RouterLink>
        <RouterLink to="/battle">Battle</RouterLink>
        <RouterLink to="/1vs1">1vs1</RouterLink>
        <RouterLink to="/login" v-if="!sessionStore.user">Login</RouterLink>
        <RouterLink v-if="!sessionStore.user"  to="/signup">Sign up</RouterLink>
        <RouterLink  v-if="sessionStore.user" to="/myList">My list of characters</RouterLink>
        <RouterLink v-if="sessionStore.user">
          <button @click="logout()">Logout</button>
        </RouterLink>
      </nav>
      <div class="progress"></div>
    </div>
  </header>
  <div class="content">
    <RouterView />
  </div>
</template>

<style scoped>
button{
  color: chartreuse;
  background-color: transparent;
  cursor: pointer;
}

header {
  line-height: 1.5;
  max-height: 100vh;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
  position: static;
  top: 0;
  left: 0;
  width: 300px;
  height: 150px;
}

nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding-right: calc(var(--section-gap) / 2);
    height: 150px;
    width: 100%;
    position: fixed;
    background-color: var(--color-background);
    top: 0;
    left: 0;
    z-index: 1000;
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: contents;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }

  .content {
    padding-top: var(--section-gap);
  }

  @supports (animation-timeline: scroll()){
    @keyframes grow-progress {
      from { transform: scaleX(0); }
      to { transform: scaleX(1); }
    }
  }

  .progress::after{
    content: '';
    position: fixed;
    left: 0;
    top: 150px;
    width: 100%;
    height: 7px;
    background: linear-gradient(80deg, rgb(192, 160, 18), rgb(209, 53, 13));
    z-index: 4;

    transform-origin: 0 50% ;
    animation: grow-progress auto linear;
    animation-timeline: scroll();
  }
}
</style>
