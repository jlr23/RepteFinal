<script setup>
import { computed, ref, onMounted } from 'vue';
import BattleCard from '@/components/BattleCard.vue';
import myApi from '@/servicies/Api.js';
import myApi2 from '@/servicies/Api2.js'
import { addIcons } from 'oh-vue-icons';
import { CoReload, GiBoxingRing } from 'oh-vue-icons/icons';
import { useSessionStore } from '@/stores/session';

addIcons(CoReload, GiBoxingRing)

const sessionStore = useSessionStore()
const ch1 = ref([])
const ch2 = ref([])
const characters = ref([]);
const search = ref('');
const loading = ref(false)
const error = ref(null)
const battle = ref([])
const winner = ref(null)
const battleStart = ref(false)
const startAnimation = ref(false)

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

const handleCardClick = (id) => {

    const currentBattle = battle.value;
    const index = currentBattle.indexOf(id);
    if (index !== -1) {
        currentBattle.splice(index, 1);
    } else {
        currentBattle.push(id);
    }
    searchCharacters(id)
};

const searchCharacters = (id) => {
    return characters.value.find(character => character.id === id);

}

const filterCharacter = computed(() => {
    if (sessionStore.user && sessionStore.user.id == 1) {
        if (characters.value.length === 0) {
            return []
        }
        return characters.value.filter((character) => {
            return character.Name.toLowerCase().includes(search.value.toLowerCase())
        })
    }
    else {
        const filteredByIdUser = characters.value.filter((character) => character.IdUser === 1 || (sessionStore.user && sessionStore.user.id === character.IdUser))
        if (filteredByIdUser.length === 0) {
            return []
        }
        return filteredByIdUser.filter((character) => {
            return character.Name.toLowerCase().includes(search.value.toLowerCase())
        })
    }
});

const startFight = async (pers1, pers2) => {
    startAnimation.value = true;
    await sleep(3000);
    startAnimation.value = false;
    battleStart.value = true
    await sleep(3000);
    battleStart.value = false
    console.log(pers1)
    let atacant, defensor
    if (pers1.Speed >= pers2.Speed) {
        atacant = pers1
        defensor = pers2
    } else {
        atacant = pers2
        defensor = pers1
    }
    if (atacant.Atack > defensor.Defense) {
        console.log(`${atacant.Name} gana el combate.`)
        winner.value = atacant
    } else if (atacant.Atack < defensor.Defense) {
        console.log(`${defensor.Name} gana el combate.`)
        winner.value = defensor
    }
    await sleep(3000);
    winner.value = null

}

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
})


</script>


<template>
    <div class="characters">
        <h1>Battle</h1>
        <div v-if="loading"> <v-icon name="co-reload" animation="spin" scale="10" /></div>
        <div v-if="error">{{ error }}</div>
        <div v-if="battle.length > 0 && battle.length < 3" class="battle">
            <div v-if="battle[0] && !winner && !battleStart" class=" player" :class="{ 'player1': startAnimation }">
                <p style="font-size: 2rem;">{{ searchCharacters(battle[0]).Name }}</p>
                <img :src="searchCharacters(battle[0]).Image" alt="{{searchCharacters(battle[0]).Name}}">
            </div>
            <div v-if="battle.length == 2 && !winner && !battleStart">
                <button @click="startFight(searchCharacters(battle[0]), searchCharacters(battle[1]))">FIGHT</button>
            </div>
            <div v-if="battle[1] && !winner && !battleStart" class="player" :class="{ 'player2': startAnimation }">
                <p style="font-size: 2rem;">{{ searchCharacters(battle[1]).Name }}</p>
                <img :src="searchCharacters(battle[1]).Image" alt="{{searchCharacters(battle[1]).Name}}">
            </div>
            <div  v-if="winner && !battleStart" class="player winner">
                <p style="font-size: 2rem;">Winner is: {{ winner.Name }}</p>
                <img :src="winner.Image" alt="{{winner.Name}}" style="filter: drop-shadow(0 0 15px gold)">
            </div>
            <img v-if="battleStart" style="margin-left: 250px;"
                src="https://mistergif.com/media/2/guante-boxeo-15497.gif">

        </div>
        <input v-if="!loading" v-model="search" type="text" placeholder="type to search..."></input>
        <section class="cards" v-if="!loading">
            <BattleCard v-for="character in filterCharacter" :key="character.id" :info="character"
                @cardClick="handleCardClick" />
        </section>
    </div>
</template>

<style scoped>
.battle {
    display: flex;
    align-items: center;
    max-height: 350px;
    gap: 50px;
}

button {
    cursor: pointer;
    font-size: 30px;
    animation: flame 3s infinite alternate;
    background-color: transparent;
}

.player {
    display: flex;
    height: 350px;
}

.player img {
    display: inline;
}

.player1 {
    filter: drop-shadow(0 0 15px rgb(113, 199, 56));
    animation: slideRight 3s forwards;
}

.player2 {
    filter: drop-shadow(0 0 15px rgb(255, 38, 0));
    animation: slideLeft 3s forwards;
}

@keyframes slideRight {
    from {
        transform: translateX(0);
    }

    to {
        transform: translateX(260px);
    }
}

@keyframes slideLeft {
    from {
        transform: translateX(0);
    }

    to {
        transform: translateX(-270px);
    }
}

.characters {
    width: 100%;
    min-height: 100vh;
    display: contents;
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