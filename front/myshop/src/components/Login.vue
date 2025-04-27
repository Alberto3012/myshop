<template>
  <div class="login-container">
    <h2>Iniciar sesión</h2>
    <form @submit.prevent="handleLogin">
      <div class="input-group">
        <label for="username">Usuario:</label>
        <input v-model="username" type="text" id="username" pattern="^[a-zA-Z0-9]+$" required placeholder="Tu usuario" />
      </div>

      <div class="input-group">
        <label for="password">Contraseña:</label>
        <input v-model="password" type="password" id="password" required placeholder="Tu contraseña" />
      </div>

      <button type="submit" class="login-btn">Entrar</button>
    </form>
    <p class="signup-link">¿No tienes cuenta? <router-link to="/register">Regístrate</router-link></p>
  </div>
</template>

<script>
import { loginUser } from '../api/userService';
import { saveToken } from '../api/userService';
import { saveIsAdmin } from '../api/userService';

export default {
  name: 'Login',
  data() {
    return {
      username: '',
      password: ''
    };
  },
  methods: {
    async handleLogin() {
      console.log("Formulario enviado");
      try {
        const user = await loginUser(this.username, this.password);
        saveToken(user.access_token);
        saveIsAdmin(user.is_admin);
        console.log('Usuario logueado con éxito:', user);
        this.$router.push('/dashboard');
      } catch (error) {
        console.error('Error al iniciar sesión:', error.message);
      }
    }
  }
};
</script>

<style scoped>
.login-container {
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

button.login-btn {
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

button.login-btn:hover {
  background-color: #45a049;
}

.signup-link {
  text-align: center;
  margin-top: 20px;
}

.signup-link a {
  color: #4CAF50;
  text-decoration: none;
}

.signup-link a:hover {
  text-decoration: underline;
}
</style>
