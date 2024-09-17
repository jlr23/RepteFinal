<script setup>
import { onMounted, ref } from 'vue';
import 'leaflet/dist/leaflet.css';
import L from 'leaflet';
import services from '@/servicies/Api.js';
import Api2 from '@/servicies/Api2.js'
import { useSessionStore } from '@/stores/session';

const sessionStore = useSessionStore()
const map = ref(null);
const characters = ref([])
const ch1 = ref([])
const ch2 = ref([])

const fetchUsers = async () => {
    const response = await services.getCharacters()
    ch1.value = response.data
    const response2 = await Api2.getCharacters()
    ch2.value = response2.data

    characters.value = ch1.value.map((item, index) => {
        return {
            ...item,
            ...ch2.value[index]
        }
    })
}

onMounted(async () => {
    await fetchUsers()

    map.value = L.map('map').setView([41.1555564, 1.1076133], 10);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19
    }).addTo(map.value);
    characters.value.forEach(character => {
        if (sessionStore.user) {
            if (sessionStore.user.id == 1) {
                L.marker([character.Latitude, character.Longitude])
                    .addTo(map.value)
                    .bindPopup(`<b style="font-size: 15px;">${character.Name}</b><img width="70%" height="100" src="${character.Image}" alt="Character Picture">`);
            } else {
                if (character.IdUser == 1 || character.IdUser == sessionStore.user.id) {
                    L.marker([character.Latitude, character.Longitude])
                        .addTo(map.value)
                        .bindPopup(`<b style="font-size: 15px;">${character.Name}</b><img width="70%" height="100" src="${character.Image}" alt="Character Picture">`);
                }
            }
        } else if (character.IdUser == 1) {
            L.marker([character.Latitude, character.Longitude])
                .addTo(map.value)
                .bindPopup(`<b style="font-size: 15px;">${character.Name}</b><img width="70%" height="100" src="${character.Image}" alt="Character Picture">`);
        }
    }
    )
});
</script>

<template>
    <div id="map" style="height: 500px; width:700px; margin-top: 10px;"></div>
</template>


<style>
#map {
    height: 500px;
}
</style>