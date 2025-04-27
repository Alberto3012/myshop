<template>
  <div class="dashboard-container">
    <header>
      <h1>Catálogo de Teléfonos</h1>
      <input 
        v-model="searchQuery" 
        type="text" 
        placeholder="Buscar teléfono..."
        @input="filterPhones"
      />
      <button v-if="isAdmin" @click="toggleCreatePhoneForm" class="create-phone-btn">Nuevo Teléfono</button>
      <button @click="logout" class="logout-btn">Logout</button>
    </header>

    <div class="cards-container">
      <div 
        v-for="phone in filteredPhones" 
        :key="phone.id" 
        class="phone-card"
        @click="goToDetail(phone.id)"
      >
        <h2>{{ phone.model }}</h2>
        <p>{{ phone.brand }}</p>
        <p><strong>Precio:</strong> {{ phone.price }} €</p>
      </div>
    </div>

    <div v-if="isCreateFormVisible" class="create-phone-form">
      <h2>Crear Nuevo Teléfono</h2>
      <form @submit.prevent="createPhone">
        <label for="model">Modelo:</label>
        <input type="text" v-model="newPhone.model" id="model" required />

        <label for="brand">Marca:</label>
        <input type="text" v-model="newPhone.brand" id="brand" required />

        <label for="price">Precio:</label>
        <input type="number" v-model="newPhone.price" id="price" required />

        <label for="camera">Cámara:</label>
        <input type="text" v-model="newPhone.camera" id="camera" required />

        <label for="screen_resolution">Resolución de Pantalla:</label>
        <input type="text" v-model="newPhone.screen_resolution" id="screen_resolution" required />

        <label for="storage">Almacenamiento:</label>
        <input type="text" v-model="newPhone.storage" id="storage" required />

        <label for="color">Color:</label>
        <input type="text" v-model="newPhone.color" id="color" required />

        <label for="so">Sistema Operativo:</label>
        <input type="text" v-model="newPhone.so" id="so" required />

        <label for="height">Alto:</label>
        <input type="text" v-model="newPhone.height" id="height" required />

        <label for="width">Ancho:</label>
        <input type="text" v-model="newPhone.width" id="width" required />

        <label for="depth">Profundidad:</label>
        <input type="text" v-model="newPhone.depth" id="depth" required />

        <label for="weight">Peso:</label>
        <input type="text" v-model="newPhone.weight" id="weight" required />

        <button type="submit">Añadir Teléfono</button>
      </form>
    </div>
  </div>
</template>

<script>
import { getPhones, createPhone } from '../api/phoneService';
import { getIsAdmin, removeIsAdmin, removeToken} from '../api/userService';

export default {
  name: 'Dashboard',
  data() {
    return {
      phones: [],
      filteredPhones: [],
      searchQuery: '',
      isCreateFormVisible: false, 
      newPhone: { 
        model: '',
        brand: '',
        price: '',
        camera: '',
        screen_resolution: '',
        storage: '',
        color: '',
        so: '',
        height: '',
        width: '',
        depth: '',
        weight: ''
      }
    };
  },
  computed: {
    isAdmin() {
        return getIsAdmin() === 'true';
    }
  },
  async mounted() {
    try {
      const data = await getPhones();
      this.phones = data;
      this.filteredPhones = data;
    } catch (error) {
      console.error('Error al cargar teléfonos:', error.message);
    }
  },
  methods: {
    goToDetail(phoneId) {
      this.$router.replace(`/detail/${phoneId}`);
    },
    logout() {
      removeIsAdmin();
      removeToken();
      window.location.reload();
    },
    toggleCreatePhoneForm() {
      this.isCreateFormVisible = !this.isCreateFormVisible;
    },
    filterPhones() {
      const query = this.searchQuery.toLowerCase();
      this.filteredPhones = this.phones.filter(
        phone => 
          phone.model.toLowerCase().includes(query) ||
          phone.brand.toLowerCase().includes(query) ||
          phone.price.toString().includes(query)
      );
    },
    async createPhone() {
      try {
        const response = await createPhone(this.newPhone);
        if (response) {
          window.location.reload();  
        }
      } catch (error) {
        console.error('Error al crear el teléfono:', error);
      }
    }
  }
};
</script>

<style scoped>
.dashboard-container {
  padding: 20px;
}
header {
  text-align: center;
  margin-bottom: 20px;
}
input {
  padding: 8px;
  border-radius: 5px;
  border: 1px solid #ddd;
  margin-bottom: 10px;
  width: 200px;
}
button.create-phone-btn {
  background-color: green;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  margin-left: 10px;
}
button.create-phone-btn:hover {
  background-color: darkgreen;
}
.cards-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 16px;
}
.phone-card {
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 15px;
  cursor: pointer;
  transition: all 0.3s ease;
}
.phone-card:hover {
  background: #f9f9f9;
  transform: translateY(-3px);
}
.create-phone-form {
  margin-top: 30px;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 8px;
  background-color: #f9f9f9;
}
.create-phone-form label {
  display: block;
  margin-bottom: 5px;
}
.create-phone-form input {
  width: 100%;
  padding: 8px;
  margin-bottom: 10px;
  border-radius: 5px;
  border: 1px solid #ddd;
}
.create-phone-form button {
  background-color: #4CAF50;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}
.create-phone-form button:hover {
  background-color: #45a049;
}
.logout-btn {
  background-color: red;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  margin-left: 10px;
}
.logout-btn:hover {
  background-color: darkred;
}
</style>
