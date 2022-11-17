<template>
    <div class="column is-4 is-offset-4"> 
        <h1 class="title">Log in</h1>
        <form @submit.prevent="submitForm">
            <div class="field">
                <label>Username</label>
                <input type="text" class="input" v-model="username">
            </div>
            <div class="field">
                <label>Password</label>
                <input type="password" class="input" v-model="password">
            </div>
            <div class="field">
                <button class="button is-dark">Log in</button>
            </div>
            <!-- notification  -->
            <div class="notification is-danger" v-if="errors.length">
                <p v-for="err in errors" v-bind:key="err">{{ err }}</p>
            </div>
            <!-- sign up -->
            <router-link to="/sign-up">click here</router-link> to sign up!
        </form>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'LogIn',
    data() {
        return {
            username: '',
            password: '',
            errors: []
        }
    },
    mounted() {
        document.title = 'Log In'
    },
    methods: {
        async submitForm() {
            axios.defaults.headers.common["Authorization"] = ""

            localStorage.removeItem("token")

            const formData = {
                username: this.username,
                password: this.password
            }

            await axios
                .post("/api/v1/token/login/", formData)
                .then(response => {
                    const token = response.data.auth_token
                    this.$store.commit('setToken', token)
                    axios.defaults.headers.common["Authorization"] = "Token " + token

                    localStorage.setItem("token", token)

                    const toPath = this.$route.query.to || '/cart'

                    this.$router.push(toPath)
                })
                .catch(error => {
                    if (error.response) {
                        for (const property in error.response.data) {
                            this.errors.push(`${property}: ${error.response.data[property]}`)
                        }
                    } else {
                        this.errors.push('Something went wrong. Please try again')
                        
                        console.log(JSON.stringify(error))
                    }
                })
        }
    }
}
</script>