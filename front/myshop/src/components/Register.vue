<template>
  <div class="register-container">
    <h2>Crear cuenta</h2>
    <form @submit.prevent="handleRegister">
      <div class="input-group">
        <label for="email">Correo electrónico:</label>
        <input v-model="email" type="email" id="email" required placeholder="Tu correo electrónico" />
      </div>
      <div class="input-group">
        <label for="username">Nombre de usuario:</label>
        <input v-model="username" type="text" id="username" required placeholder="Tu nombre de usuario" />
      </div>
      <div class="input-group">
        <label for="first_name">Primer nombre:</label>
        <input v-model="firstName" type="text" id="first_name" required placeholder="Tu primer nombre" />
      </div>
      <div class="input-group">
        <label for="last_name">Apellido:</label>
        <input v-model="lastName" type="text" id="last_name" required placeholder="Tu apellido" />
      </div>
      <div class="input-group">
        <label for="password">Contraseña:</label>
        <input v-model="password" type="password" id="password" required placeholder="Tu contraseña" />
      </div>
      <div class="input-group">
        <label for="confirmPassword">Confirmar contraseña:</label>
        <input v-model="confirmPassword" type="password" id="confirmPassword" required placeholder="Confirma tu contraseña" />
      </div>
      <button type="submit" class="register-btn">Registrarse</button>
    </form>
    <p class="login-link">¿Ya tienes cuenta? <router-link to="/login">Inicia sesión</router-link></p>
  </div>
</template>

<script>
import { registerUser } from '../api/userService';

export default {
  name: 'Register',
  data() {
    return {
      email: '',
      username: '',
      firstName: '',
      lastName: '',
      password: '',
      confirmPassword: ''
    };
  },
  methods: {
    async handleRegister() {
      if (this.password !== this.confirmPassword) {
        alert('Las contraseñas no coinciden');
        return;
      }
      try {
        const user = await registerUser(this.username, this.password, this.firstName, this.lastName, this.email);
        console.log('Usuario registrado con éxito:', user);
        this.$router.push('/login');
      } catch (error) {
        console.error('Error al registrar el usuario:', error.message);
        alert('Error al registrar la cuenta. Intenta de nuevo.');
      }
    }
  }
}
</script>

<style scoped>
.register-container {
  max-width: 400px;
  margin: 50px auto;
  padding: 40px;
  border: 1px solid #ddd;
  border-radius: 8px;
  background-color: #f9f9f9;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

h2 {
  text-align: center;
  margin-bottom: 30px;
  font-size: 24px;
  color: #333;
}

.input-group {
  margin-bottom: 20px;
}

.input-group label {
  display: block;
  font-size: 14px;
  font-weight: bold;
  color: #555;
  margin-bottom: 8px;
}

.input-group input {
  display: block;
  width: 100%;
  padding: 12px;
  font-size: 16px;
  border: 1px solid #ddd;
  border-radius: 4px;
  background-color: #fff;
  transition: all 0.3s ease;
}

.input-group input:focus {
  border-color: #4CAF50;
  outline: none;
}

button.register-btn {
  width: 100%;
  padding: 12px;
  background-color: #4CAF50;
  color: white;
  font-size: 16px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: all 0.3s ease;
}

button.register-btn:hover {
  background-color: #45a049;
}

.login-link {
  text-align: center;
  margin-top: 20px;
}

.login-link a {
  color: #4CAF50;
  text-decoration: none;
}

.login-link a:hover {
  text-decoration: underline;
}
</style>
