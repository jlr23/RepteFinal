<template>
    <div>
        <form @submit.prevent="onSubmit">
            <label for="location">Location:</label>
            <input id="location" type="text" v-model="query" @input="fetchLocations"
                placeholder="Cerca localitats..." />
            <ul v-if="locs.length">
                <li v-for="location in locs" :key="location.place_id" @click="selectLocation(location)">
                    {{ location.display_name }}
                </li>
            </ul>
            <button type="submit">Search</button>
        </form>

        <div v-if="selectedLocation">
            <h3>Selected Location:</h3>
            <p>Name: {{ selectedLocation.display_name }}</p>
            <p>Latitude: {{ selectedLocation.lat }}</p>
            <p>Longitude: {{ selectedLocation.lon }}</p>
            <!--<button @click="saveLocation()">Afegeix a Favorits</button>-->
        </div>
    </div>
</template>

<script setup>
import { ref, defineExpose } from 'vue';
import axios from 'axios';
import locations from '@/servicies/location.js';
import osm from '@/servicies/location.js';
//import { useSessionStore } from '@/stores/session.js';

//const sessionStore = useSessionStore();


const query = ref('');
const locs = ref([]);
const selectedLocation = ref(null);

const fetchLocations = async () => {
    if (query.value.length > 2) {
        const response = await axios.get('https://nominatim.openstreetmap.org/search', {
            params: {
                q: query.value,
                format: 'json',
                addressdetails: 1,
            },
        });
        locs.value = response.data;
        console.log(response.data);
    } else {
        locs.value = [];
    }
};

const selectLocation = (location) => {
    selectedLocation.value = location;
    locs.value = [];
    query.value = location.display_name;
    defineExpose(selectedLocation)
};

const onSubmit = () => {
    if (selectedLocation.value) {
        console.log('Selected location:', selectedLocation.value);
    }
};

const newLoc = ref({
    userID: '',
    location: '',
    latitude: '',
    longitude: '',
});



/*const saveLocation = async () => {


    newLoc.value.userID = sessionStore.user.id;
    newLoc.value.location = selectedLocation.value.display_name;
    newLoc.value.latitude = selectedLocation.value.lat;
    newLoc.value.longitude = selectedLocation.value.lon;

    console.log(newLoc.value);

    try {
        await locations.createLocation({
            "userID": newLoc.value.userID,
            "location": newLoc.value.location,
            "latitude": newLoc.value.latitude,
            "longitude": newLoc.value.longitude,
        });
        alert('Localització afegida correctament!');

    } catch (error) {
        alert('Error en crear l\'usuari: ' + error.message);
    }
}*/

defineExpose({
    selectedLocation
});
</script>


<style scoped>
form {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
}

label {
    margin: 0.5rem 0;
}

input {
    margin-bottom: 1rem;
}

ul {
    list-style: none;
    padding: 0;
    margin: 0;
    border: 1px solid #ccc;
    max-height: 200px;
    overflow-y: auto;
    width: 100%;
}

li {
    padding: 0.5rem;
    cursor: pointer;
}

li:hover {
    color: black;
    background-color: #f0f0f0;
}

button {
    margin-top: 1rem;
}

div {
    margin-top: 2rem;
}
</style>