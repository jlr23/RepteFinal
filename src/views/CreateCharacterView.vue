<script setup>
import { ref, onMounted, watch } from 'vue';
import NominatimSearcher from '@/components/NominatimSearcher.vue'
import Api from '@/servicies/Api.js'
import Api2 from '@/servicies/Api2.js'
import { addIcons } from 'oh-vue-icons';
import { BiCardImage, OiPersonFill, HiDocumentText, FaUserShield, GiSwordBrandish, CoSpeedometer, CoLocationPin, FaBattleNet, HiSolidHeart, GiDodging} from 'oh-vue-icons/icons';
import { useSessionStore } from '@/stores/session';

addIcons(BiCardImage, OiPersonFill, HiDocumentText, FaUserShield, GiSwordBrandish, CoSpeedometer, CoLocationPin, FaBattleNet, HiSolidHeart, GiDodging )

const sessionStore = useSessionStore()
const searcherRef = ref('');
const character = ref({
    name: '',
    atack: '',
    image: '',
    speed: '',
    defense: '',
    latitude: '',
    longitude: '',
    description: '',
    race: '',
    life: '',
    dodge: '',
    idUser: '',
})

const submitForm = async () => {
    try {
        console.log(character.value.name)
        await Api.createCharacter({
            Name: character.value.name.toString,
            Atack: character.value.atack,
            Image: character.value.image,
            Speed: character.value.speed,
            Defense: character.value.defense,
            Latitude: character.value.latitude,
            Longitude: character.value.longitude,
            Description: character.value.description,
            Race: character.value.race
        })
        await Api2.createCharacter({
            Name: character.value.name,
            Dodge: character.value.dodge,
            Life: character.value.life,
            IdUser: sessionStore.user.id
        })
        alert('Character created!' + character.value.name)
        character.value = {
            name: '',
            atack: '',
            image: '',
            speed: '',
            defense: '',
            latitude: '',
            longitude: '',
            description: '',
            race: '',
            life: '',
            dodge: '',
            idUser: '',
        }
    } catch (error) {
        alert('Error en crear el personatge: ' + error.message)
    }
}

const randomNumber = () => {
    return Math.floor(Math.random() * 200) + 1;
}

const getRandom = (min, max) => {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

const setAttack = () => {
    character.value.atack = randomNumber()
}

const setDefense = () => {
    character.value.defense = randomNumber()
}

const setSpeed = () => {
    character.value.speed = randomNumber()
}

const setLife = () => {
    character.value.life = getRandom(1000,2000)
}

const setDodge = () => {
    character.value.dodge = getRandom(2,70)
}

const check = () => {
    return Object.values(character.value).every(value => value !== '');
}

onMounted(() => {
    watch(
        () => searcherRef.value?.selectedLocation,
        (newLocation) => {
            if (newLocation) {
                character.value.latitude = newLocation.lat
                character.value.longitude = newLocation.lon
                console.log('Selected Location:', newLocation);
            }
        }
    );
    console.log(sessionStore.user.id)
    character.value.idUser = sessionStore.user.id
});
</script>

<template>
    <div class="about">
        <img class="shenron" alt="Shenron"
            src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.pngplay.com%2Fwp-content%2Fuploads%2F12%2FShenron-Transparent-Image.png&f=1&nofb=1&ipt=11b2e3a69ba12e70d3de4d6e66c163b8b3375684a9b58ff64fc6e2881989c523&ipo=images">
        <div class="formulari">
            <h1 style="font-weight: bold;">Create your Character</h1>
            <form @submit.prevent="submitForm">
                <div class="input-group">
                    <div class="label-icon-group">
                        <v-icon name="oi-person-fill" scale="1.5" />
                        <label for="name">Name:</label>
                    </div>
                    <input v-model="character.name" id="name" type="text" required placeholder="Pepito" />
                </div>
                <div class="input-group">
                    <div class="label-icon-group">
                        <v-icon name="fa-battle-net" scale="1.5" />
                        <label for="name">Race:</label>
                    </div>
                    <input v-model="character.race" id="race" type="text" required placeholder="Saiyan" />
                </div>
                <div class="input-group">
                    <div class="label-icon-group">
                        <v-icon name="bi-card-image" scale="1.5" />
                        <label for="image">Image:</label>
                    </div>
                    <input v-model="character.image" id="image" type="url" required placeholder="https//prova.com" />
                </div>
                <div class="input-group">
                    <div class="label-icon-group">
                        <v-icon name="hi-document-text" scale="1.5" />
                        <label for="description">Description:</label>
                    </div>
                    <textarea v-model="character.description" id="description" type="text" required
                        placeholder="text area...."></textarea>
                </div>
                <div class="input-group">
                    <div class="label-icon-group">
                        <button type="button" @click="setAttack"><v-icon name="gi-sword-brandish" scale="1.5" />
                            Generate Random Attack</button>
                        <p>Attack Value: {{ character.atack }}</p>
                    </div>
                </div>
                <div class="input-group">
                    <div class="label-icon-group">
                        <button type="button" @click="setDefense"> <v-icon name="fa-user-shield" scale="1.5" /> Generate
                            Random Defense</button>
                        <p>Defense Value: {{ character.defense }}</p>
                    </div>
                </div>
                <div class="input-group">
                    <div class="label-icon-group">
                        <button type="button" @click="setLife"> <v-icon name="hi-solid-heart" scale="1.5" /> Generate
                            Random Life</button>
                        <p>Life Value: {{ character.life }}</p>
                    </div>
                </div>
                <div class="input-group">
                    <div class="label-icon-group">
                        <button type="button" @click="setDodge"> <v-icon name="gi-dodging" scale="1.5" /> Generate
                            Random Dodge</button>
                        <p>Dodge Value: {{ character.dodge }}</p>
                    </div>
                </div>
                <div class="input-group">
                    <div class="label-icon-group">
                        <button type="button" @click="setSpeed"><v-icon name="co-speedometer" scale="1.5" /> Generate
                            Random Speed</button>
                        <p>Speed Value: {{ character.speed }}</p>
                    </div>
                </div>
                <div class="input-group">
                    <div class="label-icon-group">
                        <v-icon name="co-location-pin" scale="1.5" />
                        <NominatimSearcher ref="searcherRef" />
                    </div>
                </div>
                <button v-if="check()" type="submit">Crear</button>
            </form>
        </div>
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
}

.shenron {
    position: relative;
}

.formulari {
    position: absolute;
    margin: 10px;
    padding: 20px;
    border-radius: 5%;
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
    max-width: 400px;
    background-color: hsla(160, 100%, 37%, 0.5);
    font-family: 'Roboto', sans-serif;
}

.formulari label,
p {
    font-weight: 800;
}

.input-group {
    width: 350px;
    margin-bottom: 10px;
    display: table-caption;
}

.label-icon-group {
    display: flex;
    align-items: center;
    margin-bottom: 5px;
}

.label-icon-group button {
    cursor: pointer;
}
</style>