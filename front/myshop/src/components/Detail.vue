<template>
    <div class="detail-container">
        <header class="detail-header">
            <h1>{{ phone.model }}</h1>
        </header>

        <div class="detail-body">
            <div class="left-card">
                <img :src="phoneImage" alt="Imagen del teléfono" v-if="phoneImage" />
                <p v-else>Cargando imagen...</p>
            </div>

            <div class="right-cards">
                <div v-if="!isEditing">
                    <div class="specs-card">
                        <h3>Especificaciones</h3>
                        <ul>
                            <li><strong>Marca:</strong> {{ phone.brand }}</li>
                            <li><strong>Precio:</strong> {{ phone.price }} €</li>
                            <li><strong>Modelo:</strong> {{ phone.model }}</li>
                            <li><strong>Bateria:</strong> {{ phone.battery }}</li>
                            <li><strong>Camara:</strong> {{ phone.camera }}</li>
                            <li><strong>Resolución de pantalla:</strong> {{ phone.screen_resolution }}</li>
                            <li><strong>Almacenamiento:</strong> {{ phone.storage }}</li>
                            <li><strong>Color:</strong> {{ phone.color }}</li>
                            <li><strong>S.O.:</strong> {{ phone.so }}</li>
                            <li><strong>Alto:</strong> {{ phone.height }}</li>
                            <li><strong>Ancho:</strong> {{ phone.width }}</li>
                            <li><strong>Profundidad:</strong> {{ phone.depth }}</li>
                            <li><strong>Peso:</strong> {{ phone.weight }}</li>
                        </ul>
                    </div>

                    <div v-if="isAdmin" class="admin-options">
                        <h3>Opciones de Admin</h3>
                        <button @click="deletePhone">Eliminar Teléfono</button>
                        <br><br><br>
                        <button @click="toggleEdit">Actualizar Teléfono</button>
                    </div>
                </div>

                <div v-if="isEditing">
                    <div class="specs-card">
                        <h3>Actualizar Teléfono</h3>
                        <form @submit.prevent="updatePhone">
                            <label>Marca:</label>
                            <input v-model="formData.brand" type="text" />

                            <label>Precio:</label>
                            <input v-model="formData.price" type="text" />

                            <label>Modelo:</label>
                            <input v-model="formData.model" type="text" />

                            <label>Batería:</label>
                            <input v-model="formData.battery" type="text" />

                            <label>Camara:</label>
                            <input v-model="formData.camera" type="text" />

                            <label>Resolución de Pantalla:</label>
                            <input v-model="formData.screen_resolution" type="text" />

                            <label>Almacenamiento:</label>
                            <input v-model="formData.storage" type="text" />

                            <label>Color:</label>
                            <input v-model="formData.color" type="text" />

                            <label>S.O.:</label>
                            <input v-model="formData.so" type="text" />

                            <label>Alto:</label>
                            <input v-model="formData.height" type="text" />

                            <label>Ancho:</label>
                            <input v-model="formData.width" type="text" />

                            <label>Profundidad:</label>
                            <input v-model="formData.depth" type="text" />

                            <label>Peso:</label>
                            <input v-model="formData.weight" type="text" />

                            <button type="submit" :disabled="!isFormValid">Enviar</button>
                        </form>
                    </div>

                    <div v-if="isAdmin" class="admin-options">
                        <button @click="toggleEdit">Cancelar Edición</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { getPhoneById } from '../api/phoneService';
import { fetchPhoneImage } from '../api/phoneImages.js';
import { deletePhoneById } from '../api/phoneService';
import { updatePhoneService } from '../api/phoneService';
import { getIsAdmin } from '../api/userService';

export default {
    name: 'Detail',
    data() {
        return {
            phone: {},
            phoneImage: '',
            isEditing: false,
            formData: {}
        };
    },
    computed: {
        isAdmin() {
            return getIsAdmin() === 'true';
        },
        isFormValid() {
            return Object.values(this.formData).every(value => value);
        }
    },
    async mounted() {
        try {
            const phoneId = this.$route.params.id;
            const phone = await getPhoneById(phoneId);
            this.phone = phone[0];
            this.formData = { ...this.phone };
            this.loadPhone();
        } catch (error) {
            console.error('Error al obtener el teléfono:', error);
        }
    },
    methods: {

        async deletePhone() {
            try {
                const phoneId = this.$route.params.id;
                const response = await deletePhoneById(phoneId);
                alert(response.message);
                this.$router.replace(`/dashboard`);
            } catch (error) {
                console.error('Error al eliminar el teléfono:', error);
                alert('Hubo un problema al eliminar el teléfono');
            }
        },

        async loadPhone() {
            this.phoneImage = await fetchPhoneImage(this.phone.model);
        },

        toggleEdit() {
            this.isEditing = !this.isEditing;
        },
        async updatePhone() {
            try {
                const updatedPhone = { ...this.phone, ...this.formData };
                const response = await updatePhoneService(updatedPhone);
                this.phone = response;
                alert('Teléfono actualizado con éxito');
                window.location.reload();
            } catch (error) {
                console.error('Error al actualizar el teléfono:', error);
                alert('Hubo un problema al actualizar el teléfono');
            }
        },
    }
};
</script>

<style scoped>
.detail-container {
    padding: 20px;
}

.detail-header {
    text-align: center;
    margin-bottom: 20px;
}

.detail-body {
    display: flex;
    justify-content: space-between;
}

.left-card {
    width: 40%;
    text-align: center;
}

.left-card img {
    max-width: 100%;
    height: auto;
}

.right-cards {
    width: 55%;
}

.specs-card,
.admin-options {
    margin-bottom: 20px;
    padding: 15px;
    border: 1px solid #ddd;
    border-radius: 8px;
}

.specs-card h3,
.admin-options h3 {
    margin-bottom: 10px;
}

button {
    background-color: red;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background-color: darkred;
}

form {
    display: grid;
    gap: 10px;
}

form input {
    padding: 8px;
    border-radius: 5px;
    border: 1px solid #ddd;
}

form button {
    background-color: green;
    color: white;
}

form button:disabled {
    background-color: #aaa;
}
</style>