import { defineStore } from "pinia";
import services from '@/servicies/user.js'

export const useSessionStore = defineStore('session',{
    state:() =>({
        user: JSON.parse(localStorage.getItem('user')) || null,
        error: null
    }),
    actions:{
        async login(email, password) {
            try{
                const response = await services.getDirectory()
                const users = response.data
                const user = users.find(u => u.Email === email && u.Password === password)
                if (user){
                    this.user = user
                    localStorage.setItem('user', JSON.stringify(user))
                    this.error = null;
                } else{
                    this.user = null;
                    this. error = 'Email o password no vàlids';
                }
            } catch (err){
                this.error = 'S\'ha produït un error durant el login'
            }
        },
        logout(){
            this.user =null
            localStorage.removeItem('user')
        },
        updateUser(updatedUser){
            if (this.user && this.user.id === updatedUser.id){
                this.user = updatedUser
                localStorage.setItem('user', JSON.stringify(updatedUser))
            }
        }
    }
})
