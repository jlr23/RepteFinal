<script setup>
import myApi from "@/servicies/Api.js"
import myApi2 from "@/servicies/Api2.js"
import { ref, onMounted } from "vue";
import { RouterLink } from "vue-router";
import { addIcons } from 'oh-vue-icons';
import { CoReload } from 'oh-vue-icons/icons';
import wetherApi from "@/servicies/wether.js";

addIcons(CoReload)

const character = ref({})
const character1 = ref({})
const character2 = ref({})
const props = defineProps(['characterId'])
const loading = ref(false)
const error = ref(null)
const wether = ref({})
const showDescription = ref(false)

onMounted(async () => {
    loading.value = true
    console.log(props.characterId)
    try {
        await myApi.getCharacterById(props.characterId).then((response) => {
            character1.value = response.data;
        });

        await myApi2.getCharacterById(props.characterId).then((response) => {
            character2.value = response.data;
        })

        character.value = {
            ...character1.value,
            ...character2.value
        }

        if (character.value && character.value.Latitude && character.value.Longitude) {
            await wetherApi.getWether(character.value.Latitude, character.value.Longitude).then((response) => {
                wether.value = response.data;
                console.log(wether);
            });
        } else {
            throw new Error("Latitud o Longitud indefinida en el personatge");
        }

    } catch (error) {
        error.value = 'Error al carregar personatges: ' + error.message
    } finally {
        loading.value = false
    }
});

const getGlowClass = (race) => {

    if (!race) {
        return '';
    }

    if (race.startsWith && race.startsWith('Nucleico')) {
        return 'glow-red';
    }
    switch (race) {
        case 'Saiyan':
            return 'glow-yellow';
        case 'Human':
            return 'glow-aliceblue';
        case 'Frieza Race':
            return 'glow-pink';
        case 'Android':
            return 'glow-metallic';
        case 'Namekian':
            return 'glow-green';
        case 'God':
            return 'glow-purple';
        case 'Angel':
            return 'glow-blue';
        default:
            return 'glow';
    }
};

const getGlowColor = (race) => {
    if (!race) {
        return '';
    }

    if (race.startsWith && race.startsWith('Nucleico')) {
        return '#ff6347';
    }
    switch (race) {
        case 'Saiyan':
            return '#ffcc00';
        case 'Human':
            return 'aliceblue';
        case 'Frieza Race':
            return 'pink';
        case 'Android':
            return '#c0c0c0';
        case 'Namekian':
            return '#00ff00';
        case 'God':
            return '#ff00ff';
        case 'Angel':
            return '#00bfff';
        default:
            return '#b3ff66';
    }
}

const weatherIcon = (weather) => {
    switch (weather) {
        case 'Rain':
            return 'https://bmcdn.nl/assets/weather-icons/v3.0/fill/svg/rain.svg'
        case 'Mist':
            return 'https://bmcdn.nl/assets/weather-icons/v3.0/fill/svg/mist.svg'
        case 'Clouds':
            return 'https://bmcdn.nl/assets/weather-icons/v3.0/fill/svg/cloudy.svg'
        case 'Clear':
            return 'https://bmcdn.nl/assets/weather-icons/v3.0/fill/svg/clear-day.svg'
        case 'Haze':
            return 'https://bmcdn.nl/assets/weather-icons/v3.0/fill/svg/haze.svg'
        case 'Drizzle':
            return 'https://bmcdn.nl/assets/weather-icons/v3.0/fill/svg/drizzle.svg'
        case 'Smoke':
            return 'https://bmcdn.nl/assets/weather-icons/v3.0/fill/svg/smoke.svg'
        case 'Thunderstorm':
            return 'https://bmcdn.nl/assets/weather-icons/v3.0/fill/svg/thunderstorms-extreme.svg'
        case 'Snow':
            return 'https://bmcdn.nl/assets/weather-icons/v3.0/fill/svg/snow.svg'
        default:
            return 'https://bmcdn.nl/assets/weather-icons/v3.0/fill/svg/not-available.svg'
    }
}

const toggleDescription = () => {
    showDescription.value = !showDescription.value
}

</script>

<template>
    <div v-if="loading"> <v-icon name="co-reload" animation="spin" scale="10" /></div>
    <div v-if="error">{{ error }}</div>
    <div class="single" v-if="!loading">
        <h1 :class="['glow-title', getGlowClass(character.Race)]">{{ character.Name }}</h1>
        <img :src="character.Image" alt="" :style="{ '--glow-color': getGlowColor(character.Race) }" class="imatge">
        <div>
            <section :style="{ '--glow-color': getGlowColor(character.Race) }" class="character-details">
                <p><strong>Race: </strong>{{ character.Race }}</p>
                <p><strong>Attack: </strong> {{ character.Atack }}</p>
                <p><strong>Defense: </strong> {{ character.Defense }}</p>
                <p><strong>Speed: </strong> {{ character.Speed }}</p>
                <p><strong>Life: </strong> {{ character.Life }}</p>
                <p><strong>Dodge: </strong> {{ character.Dodge }}%</p>
                <div class="arrow-container">
                    <strong>Description:</strong>
                    <div class="arrow" :class="{ down: showDescription }" @click="toggleDescription">&#9654;</div>
                    <div class="more-info" :class="{ show: showDescription }">
                        <p>{{ character.Description }}</p>
                    </div>
                </div>
            </section>
            <section v-if="!loading && wether" class="card_weather">
                <h2>Weather</h2>
                <p v-if="wether.name"><strong>City: </strong>{{ wether.name }}</p>
                <p v-if="wether.weather && wether.weather.length > 0">
                    <strong>Weather: </strong>{{ wether.weather[0].main }}
                </p>
                <p v-if="wether.weather && wether.weather.length > 0">
                    <strong>Description: </strong>{{ wether.weather[0].description }}
                </p>
                <img v-if="wether.weather && wether.weather.length > 0" alt="weatherIMG"
                    :src="weatherIcon(wether.weather[0].main)">
            </section>
        </div>


    </div>

    <nav>
        <RouterLink to="/listCharacters"> <--Back </RouterLink>
    </nav>
</template>

<style scoped>
.single {
    margin-top: 2rem;
    display: flex;
    align-items: center;
    color: aliceblue;
    align-items: flex-start;
    width: 100%;
    box-sizing: border-box;
}

.card_weather {
    color: aliceblue;
    border: solid turquoise;
    padding: 15px;
    margin: 5px;
    margin-bottom: 20px;
    width: fit-content;
    font-size: 20px;
    border-radius: 10%;
}

.single img {
    width: 25%;
    margin-right: 20px;
}

.imatge {
    filter: drop-shadow(0 0 6px var(--glow-color));
    animation: shadowPulse 2s infinite;
}

@keyframes shadowPulse {

    0%,
    100% {
        filter: drop-shadow(0 0 6px var(--glow-color));
    }

    50% {
        filter: drop-shadow(0 0 12px var(--glow-color));
    }
}

.glow-title {
    margin-left: 1rem;
    font-size: 3rem;
}

.glow-yellow {
    color: #ffcc00;
    text-shadow: 0 0 10px #ffcc00, 0 0 20px #ffcc00, 0 0 30px #ffcc00;
    animation: glow-animation 3s infinite alternate;
}

.glow-pink {
    color: pink;
    text-shadow: 0 0 10px pink, 0 0 20px pink, 0 0 30px pink;
    animation: glow-animation-pink 3s infinite alternate;
}

.glow-metallic {
    color: #c0c0c0;
    text-shadow: 0 0 10px #c0c0c0, 0 0 20px #c0c0c0, 0 0 30px #c0c0c0;
    animation: glow-animation-metallic 3s infinite alternate;
}

@keyframes glow-animation {
    0% {
        color: #fff700;
        text-shadow: 0 0 10px #fff700, 0 0 20px #fff700, 0 0 30px #fff700;
    }

    50% {
        color: #ffcc00;
        text-shadow: 0 0 10px #ffcc00, 0 0 20px #ffcc00, 0 0 30px #ffcc00;
    }

    100% {
        color: #d4a200;
        text-shadow: 0 0 10px #d4a200, 0 0 20px #d4a200, 0 0 30px #d4a200;
    }
}

@keyframes glow-animation-pink {
    0% {
        color: #ff99cc;
        text-shadow: 0 0 10px #ff99cc, 0 0 20px #ff99cc, 0 0 30px #ff99cc;
    }

    50% {
        color: pink;
        text-shadow: 0 0 10px pink, 0 0 20px pink, 0 0 30px pink;
    }

    100% {
        color: #ff66a3;
        text-shadow: 0 0 10px #ff66a3, 0 0 20px #ff66a3, 0 0 30px #ff66a3;
    }
}

@keyframes glow-animation-metallic {
    0% {
        color: #c0c0c0;
        text-shadow: 0 0 10px #c0c0c0, 0 0 20px #c0c0c0, 0 0 30px #c0c0c0;
    }

    50% {
        color: #d3d3d3;
        text-shadow: 0 0 10px #d3d3d3, 0 0 20px #d3d3d3, 0 0 30px #d3d3d3;
    }

    100% {
        color: #b0b0b0;
        text-shadow: 0 0 10px #b0b0b0, 0 0 20px #b0b0b0, 0 0 30px #b0b0b0;
    }
}

.glow-green {
    color: #00ff00;
    text-shadow: 0 0 10px #00ff00, 0 0 20px #00ff00, 0 0 30px #00ff00;
    animation: glow-animation-green 3s infinite alternate;
}

.glow-aliceblue {
    color: aliceblue;
    text-shadow: 0 0 10px aliceblue, 0 0 20px aliceblue, 0 0 30px aliceblue;
    animation: glow-animation-aliceblue 3s infinite alternate;
}

@keyframes glow-animation-green {
    0% {
        color: #b3ff66;
        text-shadow: 0 0 10px #b3ff66, 0 0 20px #b3ff66, 0 0 30px #b3ff66;
    }

    50% {
        color: #00ff00;
        text-shadow: 0 0 10px #00ff00, 0 0 20px #00ff00, 0 0 30px #00ff00;
    }

    100% {
        color: #006600;

        text-shadow: 0 0 10px #006600, 0 0 20px #006600, 0 0 30px #006600;
    }
}

@keyframes glow-animation-aliceblue {
    0% {
        color: #f0f8ff;
        text-shadow: 0 0 10px #f0f8ff, 0 0 20px #f0f8ff, 0 0 30px #f0f8ff;
    }

    50% {
        color: #00bfff;
        text-shadow: 0 0 10px #00bfff, 0 0 20px #00bfff, 0 0 30px #00bfff;
    }

    100% {
        color: #4b0082;
        text-shadow: 0 0 10px #4b0082, 0 0 20px #4b0082, 0 0 30px #4b0082;
    }
}

.glow-purple {
    color: #ff00ff;
    text-shadow: 0 0 10px #ff00ff, 0 0 20px #ff00ff, 0 0 30px #ff00ff;
    animation: glow-animation-purple 3s infinite alternate;
}

@keyframes glow-animation-purple {
    0% {
        color: #ff66ff;
        text-shadow: 0 0 10px #ff66ff, 0 0 20px #ff66ff, 0 0 30px #ff66ff;
    }

    50% {
        color: #ff00ff;
        text-shadow: 0 0 10px #ff00ff, 0 0 20px #ff00ff, 0 0 30px #ff00ff;
    }

    100% {
        color: #990099;
        text-shadow: 0 0 10px #990099, 0 0 20px #990099, 0 0 30px #990099;
    }
}

.glow-blue {
    color: #00bfff;
    text-shadow: 0 0 10px #00bfff, 0 0 20px #00bfff, 0 0 30px #00bfff;
    animation: glow-animation-blue 3s infinite alternate;
}

@keyframes glow-animation-blue {
    0% {
        color: #87ceeb;
        text-shadow: 0 0 10px #87ceeb, 0 0 20px #87ceeb, 0 0 30px #87ceeb;
    }

    50% {
        color: #00bfff;
        text-shadow: 0 0 10px #00bfff, 0 0 20px #00bfff, 0 0 30px #00bfff;
    }

    100% {
        color: #1e90ff;
        text-shadow: 0 0 10px #1e90ff, 0 0 20px #1e90ff, 0 0 30px #1e90ff;
    }
}

.glow-red {
    color: #ff6347;
    text-shadow: 0 0 10px #ff6347, 0 0 20px #ff6347, 0 0 30px #ff6347;
    animation: glow-animation-red 3s infinite alternate;
}

@keyframes glow-animation-red {
    0% {
        color: #fa8072;
        text-shadow: 0 0 10px #fa8072, 0 0 20px #fa8072, 0 0 30px #fa8072;
    }

    50% {
        color: #ff6347;
        text-shadow: 0 0 10px #ff6347, 0 0 20px #ff6347, 0 0 30px #ff6347;
    }

    100% {
        color: #ff4500;
        text-shadow: 0 0 10px #ff4500, 0 0 20px #ff4500, 0 0 30px #ff4500;
    }
}

.character-details {
    white-space: pre-line;
    font-size: 20px;
    position: relative;
    padding: 20px;
    border: 2px solid transparent;
    overflow: hidden;
    width: 100%;
    margin-bottom: 10px;
}

.character-details::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    border: 2px solid var(--glow-color);
    box-shadow: 0 0 10px var(--glow-color);
    animation: border-animation 2s linear infinite;
}

.character-details::after {
    content: '';
    position: absolute;
    width: 20px;
    height: 20px;
    background: radial-gradient(circle, var(--glow-color) 20%, transparent 70%);
    border-radius: 50%;
    animation: wave-animation 8s linear infinite;
}

strong {
    font-weight: bold;
    font-size: 25px;
}

@keyframes border-animation {
    0% {
        box-shadow: 0 0 10px var(--glow-color);
    }

    50% {
        box-shadow: 0 0 20px var(--glow-color);
    }

    100% {
        box-shadow: 0 0 10px var(--glow-color);
    }
}

@keyframes wave-animation {
    0% {
        top: -10px;
        left: -10px;
    }

    25% {
        top: -10px;
        left: calc(100% - 10px);
    }

    50% {
        top: calc(100% - 10px);
        left: calc(100% - 10px);
    }

    75% {
        top: calc(100% - 10px);
        left: -10px;
    }

    100% {
        top: -10px;
        left: -10px;
    }
}

.arrow-container {
    position: relative;
    display: flex;
    align-items: baseline;
    flex-direction: row;
    flex-wrap: wrap;
}

.arrow {
    margin-left: 1rem;
    cursor: pointer;
    transition: transform 0.3s ease;
    z-index: 2;
    position: relative;
}

.arrow.down {
    cursor: pointer;
    transform: rotate(90deg);
}

.more-info {
    display: none;
    margin-top: 10px;
    text-align: justify;
    font-size: 18px;
}

.more-info.show {
    display: block;
}
</style>
