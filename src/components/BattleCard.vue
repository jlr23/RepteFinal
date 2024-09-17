<script setup>
import { ref, onMounted } from 'vue';
import { addIcons } from 'oh-vue-icons';
import { CoReload } from 'oh-vue-icons/icons';

addIcons(CoReload)

const props = defineProps(['info']);
const emits = defineEmits(['cardClick']);
const backgroundLoaded = ref(false);
const isSelected = ref(false)

const toggleSelection = () => {
    isSelected.value = !isSelected.value
    emits('cardClick', props.info.id);
}

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
    <article v-if="backgroundLoaded" :class="{ 'card': !isSelected, 'card_selected': isSelected }" 
        @click="toggleSelection()">
        <h2>{{ props.info.Name }}</h2>
        <div class="image-container">
            <img :src="props.info.Image" alt="{{props.info.Name}}">
        </div>
    </article>
</template>

<style scoped>
.card {
    color: black;
    border-radius: 8%;
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
    overflow: hidden;
    view-timeline-name: --reveal;
    animation-timeline: --reveal;
    animation-name: appear;
    animation-fill-mode: both;
    animation-duration: 1s;
    position: relative;
    z-index: 1;
}

.card_selected {
    color: black;
    border-radius: 8%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    margin: 10px;
    transition: 0.3s;
    background-image: url('https://web.dragonball-api.com/images-compress/89980.webp');
    background-size: cover;
    cursor: pointer;
    overflow: hidden;
    border-color: #007bff;
    box-shadow: 10px 10px 20px turquoise;
    view-timeline-name: --reveal;
    animation-timeline: --reveal;
    animation-name: appear;
    animation-fill-mode: both;
    animation-duration: 1s;
    position: relative;
    z-index: 1;
}

@keyframes appear {
    0% {
        opacity: 0;
    }
    35% {
        opacity: 0.85;
    }
    100% {
        opacity: 1;
    }
}

.image-container {
    position: relative;
    width: 150px;
    height: 150px;
    overflow: hidden;
    margin: 10px;
}

.card img {
    display: block;
    width: 100%;
    height: auto;
    object-fit: cover;
    transition: 0.6s;
}

.card_selected img {
    display: block;
    width: 100%;
    height: auto;
    object-fit: cover;
    transition: 0.6s;
}

h2 {
    word-wrap: break-word;
}

.card:hover {
    .image-container {
        filter: drop-shadow(0 0 6px gold)
    }

    .image-container::after {
        opacity: 0;
    }

    color: gold;

    transform: translateY(-10px);
    box-shadow: 10px 10px 20px gold;
}
</style>
