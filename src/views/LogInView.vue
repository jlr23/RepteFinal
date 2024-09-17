<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { useSessionStore } from '@/stores/session.js';
import { addIcons } from 'oh-vue-icons';
import { MdAlternateemailSharp, RiLockPasswordFill, FaUserCircle } from 'oh-vue-icons/icons';

addIcons(MdAlternateemailSharp, RiLockPasswordFill, FaUserCircle);

const email = ref('');
const password = ref('');
const sessionStore = useSessionStore();
const router = useRouter();
const error = ref(false);

const submitForm = async () => {
    await sessionStore.login(email.value, password.value);
    console.log(sessionStore.user);
    if (sessionStore.user) {
        alert("Welcome " + sessionStore.user.Name)
        router.push('/listCharacters');
    } else {
        error.value = sessionStore.error;
    }
};


</script>

<template>
    <div class="about">
        <img class="balls"
            src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.pinimg.com%2Foriginals%2F50%2Fef%2F1a%2F50ef1ab338d0471788fa28095b21f15c.png&f=1&nofb=1&ipt=fefedb8c470357b52b7c2ce144b89c9594f798a40b923c22c2da8a9dd80c3ea5&ipo=images"
            alt="dragon balls">
        <div class="formulari">
            <h1>Login</h1>
            <v-icon name="fa-user-circle" scale="5" />
            <form @submit.prevent="submitForm">
                <div class="input-group">
                    <div class="label-icon-group">
                        <v-icon name="md-alternateemail-sharp" scale="1.5" />
                        <label for="email">Email:</label>
                    </div>
                    <input v-model="email" id="email" type="email" required placeholder="xxxx@email.com" />
                </div>
                <div class="input-group">
                    <div class="label-icon-group">
                        <v-icon name="ri-lock-password-fill" />
                        <label for="password">Password:</label>
                    </div>
                    <input v-model="password" id="password" type="password" required placeholder="*******" />
                </div>
                <button type="submit">Login</button>
            </form>
            <div v-if="error" class="error">{{ error }}</div>
        </div>
    </div>
</template>

<style scoped>
.about {
    position: relative;
    margin: 10px;
    display: flex;
    flex-direction: column;
    align-items: center;
    color: aliceblue;
    width: 340px;
    overflow: visible;
}

.balls {
    position: absolute;
    width: 170%;
    height: 100%;
    object-fit: cover;
    z-index: 1;
    filter: drop-shadow(0 0 5px gold);
    animation: shadowPulse 2s infinite;
}

@keyframes shadowPulse {

0%,
100% {
    filter: drop-shadow(0 0 6px gold);
}

50% {
    filter: drop-shadow(0 0 20px gold);
}
}

.formulari {
    margin: 10px;
    padding: 20px;
    background-color: rgba(25, 146, 56, 0.8);
    border-radius: 5%;
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
    max-width: 400px;
    z-index: 2;
    text-align: center;
}

form {
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
}

.input-group {
    width: 100%;
    margin-bottom: 10px;
}

.label-icon-group {
    display: flex;
    align-items: center;
    margin-bottom: 5px;
}

h1 {
    font-weight: bold;
}

label {
    margin-left: 10px;
    display: inline-block;
    font-weight: bold;
}

input {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-sizing: border-box;
}

button {
    padding: 10px 20px;
    background-color: #333;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    width: 100%;
}

button:hover {
    background-color: #555;
}

.error {
    color: rgb(0, 0, 0);
    margin-top: 10px;
}
</style>
