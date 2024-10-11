import axios from "axios";
import { onUpdated, withDirectives } from "vue";

const api = axios.create({
    baseURL:'https://retoolapi.dev/yZ1Btm',
    withCredentials: false,
    headers:{
        Accept: 'application/json',
        'Content-Type': 'application/json'
    }
})

export default {
    getDirectory(){
        return api.get('/data')
    },

    getDirectoryById( id ){
        return api.get('/data/'+id) 
    },
    createUser(user){
        return api.post("/data/",user)
    },
    updateUser(id,user){
        return api.put('/data/'+id,user)
    },
    delateUser(id){
        return api.delete('/data/'+id)
    }
}