import axios from "axios";
import { onUpdated, withDirectives } from "vue";

const api = axios.create({
    baseURL:'https://retoolapi.dev/dxsSPY',
    withCredentials: false,
    headers:{
        Accept: 'application/json',
        'Content-Type': 'application/json'
    }
})

export default {
    getCharacters(){
        return api.get('/characters')
    },

    getCharacterById( id ){
        return api.get('/characters/'+id) 
    },
    createCharacter(character){
        return api.post("/characters/",character)
    },
    updateCharacter(id,character){
        return api.put('/characters/'+id,character)
    },
    delateCharacter(id){
        return api.delete('/characters/'+id)
    }
}