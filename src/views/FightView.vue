<script setup>
import myApi from "@/servicies/Api.js"
import myApi2 from "@/servicies/Api2.js"
import { ref, onMounted, computed } from "vue";
import { addIcons } from 'oh-vue-icons';
import { CoReload } from 'oh-vue-icons/icons';

addIcons(CoReload)

const props = defineProps(['listCharacters'])
const loading = ref(false)
const error = ref(null)
const characters = ref([])
const shift = ref(null)
const dialogText = ref('')
const initialHealth = ref([])
const hitCharacterIndex = ref(7);
const attackUp = ref(7)
const defenseUp = ref(7)
const showGif = ref(false)
const showGif2 = ref(false)
const winer = ref(false)

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

const getLifeStyle = (life, index) => {
    const lifePercentage = (life / initialHealth.value[index]) * 100;

    let backgroundColor;
    if (lifePercentage > 75) {
        backgroundColor = 'lime';
    } else if (lifePercentage > 50) {
        backgroundColor = 'yellow';
    } else if (lifePercentage > 25) {
        backgroundColor = 'orange';
    } else {
        backgroundColor = 'red';
    }

    return {
        width: `${lifePercentage}%`,
        backgroundColor: backgroundColor
    };
};

const getRandom = (min, max) => {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

const limpDialogText = async () => {
    await sleep(2000)
    dialogText.value = ""
}

const recalc = (valor) => {
    characters.value[revertShift()].Life -= valor
    if (characters.value[revertShift()].Life < 0) {
        characters.value[revertShift()].Life = 0
        winer.value = characters.value[shift.value]
    }
}

const shiftChange = () => {
    if (shift.value == 1) shift.value = 0
    else shift.value = 1
}

const revertShift = () => {
    if (shift.value == 1) return 0
    else return 1
}

const attack = async () => {
    if (characters.value[revertShift()].Dodge < getRandom(0, 99)) {
        if (characters.value[shift.value].Atack > characters.value[revertShift()].Defense) {
            let valor = characters.value[shift.value].Atack - characters.value[revertShift()].Defense
            dialogText.value = characters.value[shift.value].Name + (" has done damage")
            hitCharacterIndex.value = revertShift()
            if (shift.value == 0) showGif.value = true
            else showGif2.value = true
            recalc(valor)
        } else {
            dialogText.value = characters.value[revertShift()].Name + (" has more defense")
        }
    }
    else {
        dialogText.value = characters.value[shift.value].Name + (" has failed")
    }
    await limpDialogText()
    hitCharacterIndex.value = 7;
    showGif.value = false
    showGif2.value = false;
    shiftChange()
}

const augmentAttack = async () => {
    let value = getRandom(10, 200)
    characters.value[shift.value].Atack += value
    dialogText.value = "Increased attack " + value + ", Attack now: " + characters.value[shift.value].Atack
    attackUp.value = shift.value
    await limpDialogText()
    attackUp.value = 7
    shiftChange()
}

const augmentDefense = async () => {
    let value = getRandom(10, 150)
    characters.value[shift.value].Defense += value
    dialogText.value = "Increased defense " + value + ", Defense now: " + characters.value[shift.value].Defense
    defenseUp.value = shift.value
    await limpDialogText()
    defenseUp.value = 7
    shiftChange()
}

onMounted(async () => {
    loading.value = true
    try {
        const ids = props.listCharacters.split(",")
        for (const id of ids) {
            const ch1 = await myApi.getCharacterById(id);
            const ch2 = await myApi2.getCharacterById(id);

            const character = {
                ...ch1.data,
                ...ch2.data
            }
            characters.value.push(character);
            initialHealth.value.push(character.Life)
        }
        if (characters.value[0].Speed >= characters.value[1].Speed) {
            shift.value = 0
        } else {
            shift.value = 1
        }

    } catch (err) {
        error.value = 'Error al carregar personatges: ' + error.message
    } finally {
        const backgroundImage = new Image();
        backgroundImage.src = 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/59aa88c3-8682-4e07-b69c-326a55b7687e/dbbfgcx-4058d783-07f2-4288-a511-8debc936601d.jpg/v1/fill/w_1024,h_514,q_75,strp/dragonball_world_tournament_stage_by_aniartluke82_dbbfgcx-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9NTE0IiwicGF0aCI6IlwvZlwvNTlhYTg4YzMtODY4Mi00ZTA3LWI2OWMtMzI2YTU1Yjc2ODdlXC9kYmJmZ2N4LTQwNThkNzgzLTA3ZjItNDI4OC1hNTExLThkZWJjOTM2NjAxZC5qcGciLCJ3aWR0aCI6Ijw9MTAyNCJ9XV0sImF1ZCI6WyJ1cm46c2VydmljZTppbWFnZS5vcGVyYXRpb25zIl19.J4zftHN2-BbGPnbzonVrvGh0mhYY2feeruLusg5SAu0';

        backgroundImage.onload = () => {
            loading.value = false;
        };
        backgroundImage.onerror = () => {
            loading.value = true
            error.value = "Error carregar imatge"
        };
    }
});
</script>

<template>

    <div v-if="loading"> <v-icon name="co-reload" animation="spin" scale="5" /></div>
    <div v-if="!loading && (shift == 1 || shift == 0)">
        <h1 v-if="!winer">Turn for {{ characters[shift].Name }}, {{ dialogText }}</h1>
        <h1 v-if="winer"> {{ winer.Name }} wins </h1>
        <div v-if="!winer" class="ring">
            <img v-if="showGif" class="attack-gif"
                src="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/5f740e1a-c01a-43ab-983a-74c2cccab619/dffd98q-33b01d47-41d1-42ef-aa72-7b20b99918ec.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzVmNzQwZTFhLWMwMWEtNDNhYi05ODNhLTc0YzJjY2NhYjYxOVwvZGZmZDk4cS0zM2IwMWQ0Ny00MWQxLTQyZWYtYWE3Mi03YjIwYjk5OTE4ZWMuZ2lmIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.rgM-mSTaXipRCXqDKtNf3L2zXt9kPbhFQ5JFVROM8ck"
                alt="Attack Animation">
            <img v-if="showGif2" class="attack-gif"
                src="https://vignette.wikia.nocookie.net/mugen/images/e/ea/GohanCFSK4.gif/revision/latest?cb=20150405125507"
                alt="Attack Animation">
            <div class="player" v-for="(character, index) in characters" :key="index">
                <img :alt="character.Name" :src="character.Image"
                    :class="{ 'hit': hitCharacterIndex == index, 'highlight': shift == index }">
                <img v-if="attackUp == index" class="attackaugment"
                    src="https://www.gifss.com/armas/espadas/images/espada-11.gif">
                <img v-if="defenseUp == index" class="defenseaugment"
                    src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fassets.badlion.net%2Fstore%2Fimages%2Fproducts%2Fshield83-3.gif&f=1&nofb=1&ipt=e4fbaffb3619ffd06e642a7ce563d9831e37b082ac10ae40d47d61935e9d8d37&ipo=images">
                <div class="life">
                    <div class="life-inner" :style="getLifeStyle(character.Life, index)"></div>
                    <span class="life-value">{{ character.Life }}</span>
                </div>
            </div>
        </div>
        <div v-if="winer" class="fireworks">
            <img :alt="winer.Name" :src="winer.Image" class="winer">
        </div>
        <div v-if="!winer" class="actions">
            <button @click="attack()">Attack</button>
            <button @click="augmentAttack()">Augment Attack</button>
            <button @click="augmentDefense()">Augment Defence</button>
        </div>
    </div>

</template>

<style scoped>
.ring {
    margin-top: 10px;
    display: flex;
    align-items: center;
    background-image: url('https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/59aa88c3-8682-4e07-b69c-326a55b7687e/dbbfgcx-4058d783-07f2-4288-a511-8debc936601d.jpg/v1/fill/w_1024,h_514,q_75,strp/dragonball_world_tournament_stage_by_aniartluke82_dbbfgcx-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9NTE0IiwicGF0aCI6IlwvZlwvNTlhYTg4YzMtODY4Mi00ZTA3LWI2OWMtMzI2YTU1Yjc2ODdlXC9kYmJmZ2N4LTQwNThkNzgzLTA3ZjItNDI4OC1hNTExLThkZWJjOTM2NjAxZC5qcGciLCJ3aWR0aCI6Ijw9MTAyNCJ9XV0sImF1ZCI6WyJ1cm46c2VydmljZTppbWFnZS5vcGVyYXRpb25zIl19.J4zftHN2-BbGPnbzonVrvGh0mhYY2feeruLusg5SAu0');
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    padding-left: 10px;
    padding-right: 10px;
    padding-top: 10px;
    gap: 150px;
}



.fireworks {
    justify-content: center;
    margin-top: 10px;
    display: flex;
    align-items: center;
    background-image: url('https://img1.picmix.com/output/stamp/thumb/1/6/0/8/718061_1a0f1.gif');
    background-size: cover;
    background-position: center;
    width: 500px;
}

.player {
    display: flex;
    height: 350px;
}

.player img {
    display: inline;
}

.actions {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 10px;
    margin: 10px 0;
}

.winer {
    display: flex;
    height: 350px;
    display: inline;
    filter: drop-shadow(0 0 26px rgb(255, 217, 0));
    animation: shadowPulse 2s infinite;
}

@keyframes shadowPulse {

    0%,
    100% {
        filter: drop-shadow(0 0 6px rgb(255, 217, 0));
    }

    50% {
        filter: drop-shadow(0 0 20px rgb(255, 217, 0));
    }
}


.actions button {
    font-size: large;
    width: 33%;
    cursor: pointer;
    border-radius: 15%;
    padding: 10px 20px;
    background-color: #28a745;
    color: white;
    transition: background-color 0.3s ease;
}

.actions button:hover {
    background-color: #1a692c;
}

.life {
    display: flex;
    justify-content: center;
    align-items: center;
    font-family: Arial, Helvetica, sans-serif;
    box-sizing: border-box;
    width: 200px;
    height: 30px;
    border: 1px solid black;
    margin: 10px 0;
    position: relative;
    background-color: transparent;
}

.life-value {
    position: absolute;
    width: 100%;
    text-align: center;
    color: black;
    line-height: 30px;
    z-index: 1;
}

.life-inner {
    height: 100%;
    transition: width 0.3s, background-color 0.3s;
    position: absolute;
    left: 0;
    top: 0;
    border-radius: 5px;
}

.highlight {
    filter: drop-shadow(0 0 26px rgb(255, 217, 0));
}

.hit {
    animation: shake .3s infinite;
}

@keyframes shake {
    0% {
        rotate: 0deg;
    }

    20% {
        rotate: -2deg;
    }

    40% {
        rotate: 2deg;
    }

    60% {
        rotate: -2deg;
    }

    80% {
        rotate: 2deg;
    }

    100% {
        rotate: 0deg;
    }
}

.attack-gif {
    width: 400px;
    height: auto;
    position: absolute;
    right: 42%;
    top: 50%
}

.attack-gif2 {
    width: 400px;
    height: auto;
    position: absolute;
    right: 42%;
    top: 50%
}

.attackaugment {
    position: absolute;
    width: 200px;
}

.defenseaugment {
    position: absolute;
    transform: translateY(100px);
    width: 160px;
}
</style>
