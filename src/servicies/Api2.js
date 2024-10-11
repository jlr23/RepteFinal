import axios from "axios";
import { onUpdated, withDirectives } from "vue";

const api = axios.create({
    baseURL:'https://retoolapi.dev/O4IXtN',
    withCredentials: false,
    headers:{
        Accept: 'application/json',
        'Content-Type': 'application/json'
    }
})

export default {
    getCharacters(){
        return api.get('/characters2')
    },

    getCharacterById( id ){
        return api.get('/characters2/'+id) 
    },
    createCharacter(character){
        return api.post("/characters2/",character)
    },
    updateCharacter(id,character){
        return api.put('/characters2/'+id,character)
    },
    delateCharacter(id){
        return api.delete('/characters2/'+id)
    }
}