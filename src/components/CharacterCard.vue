<script setup>
import { ref, onMounted } from 'vue';
import { addIcons } from 'oh-vue-icons';
import { CoReload } from 'oh-vue-icons/icons';

addIcons(CoReload)

const props = defineProps(['info']);
const backgroundLoaded = ref(false);

onMounted(() => {
    const backgroundImage = new Image();
    backgroundImage.src = 'https://web.dragonball-api.com/images-compress/89980.webp';

    backgroundImage.onload = () => {
        backgroundLoaded.value = true;
    };
});
</script>

<template>
    <article v-if="!backgroundLoaded">
        <div> <v-icon name="co-reload" animation="spin" scale="5" /></div>
    </article>
    <article v-if="backgroundLoaded" class="card" data-aos="fade-up"
        @click="$router.push({ name: 'single', params: { characterId: props.info.id } })">
        <h2>{{ props.info.Name }}</h2>
        <div class="image-container">
            <img :src="props.info.Image" alt="">
        </div>
        <button @click="$router.push({ name: 'single', params: { characterId: props.info.id } })">View more... </button>
    </article>
</template>

<style scoped>
.card {
    color: black;
    background-color: #333;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    margin: 10px;
    transition: 0.3s;
    background-image: url('https://web.dragonball-api.com/images-compress/89980.webp');
    background-size: cover;
    cursor: pointer;
}

.image-container {
    position: relative;
    width: 150px;
    height: 150px;
    overflow: hidden;
    margin: 10px;
}

.image-container::after {
    content: "";
    position: absolute;
    left: 0;
    bottom: 0;
    width: 100%;
    height: 50%;
    background: linear-gradient(to bottom, rgba(255, 255, 255, 0) 0%, rgba(255, 255, 255, 0.5) 50%, rgba(255, 255, 255, 1) 100%);
    pointer-events: none;
    transition: opacity 0.6s ease;
}

.card img {
    display: block;
    width: 100%;
    height: auto;
    object-fit: cover;
    transition: 0.6s;
}

.card:hover {
    .image-container {
        filter: drop-shadow(0 0 6px gold)
    }

    .image-container::after {
        opacity: 0;
    }

    color: gold;

    button {
        color: gold
    }

    transform: translateY(-10px);
    box-shadow: 10px 10px 20px gold;
}

.card button {
    color: rgb(54, 54, 54);
    background-color: transparent;
    cursor: pointer;
    margin-bottom: 10px;
    background-color: rgb(205, 255, 238);
}
</style>
