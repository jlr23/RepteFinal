<script setup>
import { ref, onMounted, watch } from 'vue';
import { useRouter } from 'vue-router';
import { useSessionStore } from '@/stores/session.js';
import { addIcons } from 'oh-vue-icons';
import { MdAlternateemailSharp, RiLockPasswordFill, FaUserCircle } from 'oh-vue-icons/icons';
import useer from '@/servicies/user.js'

addIcons(MdAlternateemailSharp, RiLockPasswordFill, FaUserCircle);


const sessionStore = useSessionStore();
const router = useRouter();
const error = ref(false);
const user = ref({
    name: '',
    email: '',
    password: ''
})
const searcherRef = ref('');
const newLoc = ref();

const submitForm = async () => {
    try {
        console.log(user.value)
        await useer.createUser({
            Name: user.value.name,
            Email: user.value.email,
            Password: user.value.password
        })
        alert('Usuari creat correctament!')
        await sessionStore.login(user.value.email, user.value.password);
        console.log(sessionStore.user);
        if (sessionStore.user) {
            router.push('/listCharacters');
            alert("Welcome " + sessionStore.user.Name)
        } else {
            error.value = sessionStore.error;
        }
        user.value = {
            name: '',
            email: '',
            password: ''
        }

    } catch (error) {
        alert('Error en crear l\'usuari: ' + error.message)
    }
}
</script>

<template>
    <div class="about">
        <div class="formulari">
            <h1>Sign Up</h1>
            <v-icon name="fa-user-circle" scale="5" />
            <form @submit.prevent="submitForm">
                <div class="input-group">
                    <div class="label-icon-group">
                        <v-icon name="fa-user-circle" scale="1.5" />
                        <label for="name">Name:</label>
                    </div>
                    <input v-model="user.name" id="name" type="text" required placeholder="Pepito" />
                </div>
                <div class="input-group">
                    <div class="label-icon-group">
                        <v-icon name="md-alternateemail-sharp" scale="1.5" />
                        <label for="email">Email:</label>
                    </div>
                    <input v-model="user.email" id="email" type="email" required placeholder="xxxx@email.com" />
                </div>
                <div class="input-group">
                    <div class="label-icon-group">
                        <v-icon name="ri-lock-password-fill" scale="1.5" />
                        <label for="password">Password:</label>
                    </div>
                    <input v-model="user.password" id="password" type="password" required placeholder="*******" />
                </div>
                <button type="submit">Sign Up</button>
            </form>
            <div v-if="error" class="error">{{ error }}</div>
        </div>
        <img class="goku" alt="goku" src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.gifcen.com%2Fwp-content%2Fuploads%2F2021%2F03%2Fgoku-gif-19.gif&f=1&nofb=1&ipt=cb3f42d7a74972d1f9ab51e1c7a1cc87c16a625e85089a9738ae5f7358263946&ipo=images">
    </div>
</template>

<style scoped>
textarea {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-sizing: border-box;
    resize: none;
    min-height: 100px;
}

.about {
    margin: 10px;
    display: flex;
    flex-direction: column;
    align-items: center;
    color: aliceblue;
    overflow: hidden;
}

.goku{
    position: absolute;
    height: 100%;
    object-fit: cover;
    transform: translateY(-190px);
    z-index: -1;
}

.formulari {
    margin: 10px;
    padding: 20px;
    background-color: rgb(25, 146, 56);
    border-radius: 5%;
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 400px;
    max-width: 400px;
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

.input-group button {
    background-color: transparent;
    font-weight: bold;
    display: flex;
    font-size: medium
}

.input-group button:hover {
    color: green;
    background-color: transparent;
}

.error {
    color: red;
    margin-top: 10px;
}
</style>
