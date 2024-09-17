<script setup>
import { computed, ref, onMounted } from 'vue';
import CharacterCard from '@/components/CharacterCard.vue';
import myApi from '@/servicies/Api.js';
import myApi2 from "@/servicies/Api2.js"
import { useSessionStore } from '@/stores/session';
import { addIcons } from 'oh-vue-icons';
import { CoReload } from 'oh-vue-icons/icons';

addIcons(CoReload)
const sessionStore = useSessionStore()
const characters = ref([]);
const ch1 = ref([])
const ch2 = ref([])
const search = ref('');
const loading = ref(false)
const error = ref(null)

onMounted(async () => {
    loading.value = true
    try {
        const response = await myApi.getCharacters();
        ch1.value = response.data;
        const response2 = await myApi2.getCharacters()
        ch2.value = response2.data

        characters.value = ch1.value.map((item, index) => {
            return {
                ...item,
                ...ch2.value[index]
            }
        })
    } catch (error) {
        error.value = 'Error al carregar personatges: ' + error.message
    } finally {
        loading.value = false
    }
});

const filterCharacter = computed(() => {
    const filteredByIdUser = characters.value.filter((character) => sessionStore.user && sessionStore.user.id === character.IdUser)
    if (filteredByIdUser.length === 0) {
        return []
    }
    return filteredByIdUser.filter((character) => {
        return character.Name.toLowerCase().includes(search.value.toLowerCase())
    })

});
</script>


<template>
    <div class="characters">
        <h1 style="color: aliceblue;">My list</h1>
        <input v-model="search" type="text" placeholder="type to search..."></input>
        <br>
        <div v-if="loading"> <v-icon name="co-reload" animation="spin" scale="10" /></div>
        <div v-if="error">{{ error }}</div>
        <section class="cards" v-if="!loading">
            <CharacterCard v-for="character in filterCharacter" :key="character.id" :info="character" />
        </section>
    </div>
</template>

<style scoped>
.characters {
    width: 100%;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 20px;
}

h1 {
    font-size: 3rem;
    color: #ff4500;
    text-shadow: 0 0 20px #ff4500, 0 0 30px #ff4500, 0 0 40px #ff4500, 0 0 50px #ff4500, 0 0 60px #ff4500, 0 0 70px #ff4500;
    animation: flame 3s infinite alternate;
}

@keyframes flame {
    0% {
        color: #ff4500;
        text-shadow: 0 0 20px #ff4500, 0 0 30px #ff4500, 0 0 40px #ff4500, 0 0 50px #ff4500, 0 0 60px #ff4500, 0 0 70px #ff4500;
    }

    25% {
        color: #ff6347;
        text-shadow: 0 0 20px #ff6347, 0 0 30px #ff6347, 0 0 40px #ff6347, 0 0 50px #ff6347, 0 0 60px #ff6347, 0 0 70px #ff6347;
    }

    50% {
        color: #ff7f50;
        text-shadow: 0 0 20px #ff7f50, 0 0 30px #ff7f50, 0 0 40px #ff7f50, 0 0 50px #ff7f50, 0 0 60px #ff7f50, 0 0 70px #ff7f50;
    }

    75% {
        color: #ffa07a;
        text-shadow: 0 0 20px #ffa07a, 0 0 30px #ffa07a, 0 0 40px #ffa07a, 0 0 50px #ffa07a, 0 0 60px #ffa07a, 0 0 70px #ffa07a;
    }

    100% {
        color: #ff4500;
        text-shadow: 0 0 20px #ff4500, 0 0 30px #ff4500, 0 0 40px #ff4500, 0 0 50px #ff4500, 0 0 60px #ff4500, 0 0 70px #ff4500;
    }
}

input {
    margin-top: 1rem;
    background: white url('https://w7.pngwing.com/pngs/248/125/png-transparent-goku-bola-de-drac-dragon-ball-shenron-goku-television-dragon-orange.png') no-repeat;
    background-size: contain;
    background-position-x: right;
    width: inherit;
    height: 2rem;
    font-size: 1.5rem;
    padding-right: 2rem;
    padding-left: 0.5rem;
}

.cards {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 10px;
    width: 100%;
    max-width: 1200px;
    margin-top: 20px;
}

@media (max-width: 1024px) {
    .cards {
        grid-template-columns: repeat(3, 1fr);
    }
}

@media (max-width: 768px) {
    .cards {
        grid-template-columns: repeat(2, 1fr);
    }
}

@media (max-width: 480px) {
    .cards {
        grid-template-columns: 1fr;
    }
}
</style>