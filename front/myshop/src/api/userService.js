const API_URL = 'http://127.0.0.1:8000/api/user/'

const TOKEN_KEY = 'auth_token';
const IS_ADMIN = 'isAdmin';

//lo mejor es almacenarlo en el sessionStorage o usar otras cosas como las cookies httonly pero 
//por temas de rapidez en este proyecto se va a guardar en en localStorage a pesar de ser menos seguro

export function saveToken(token) {
  localStorage.setItem(TOKEN_KEY, token);
}

export function getToken() {
  return localStorage.getItem(TOKEN_KEY);
}

export function removeToken() {
  localStorage.removeItem(TOKEN_KEY);
}

export function isLoggedIn() {
  return !!getToken();
}

export function saveIsAdmin(isAdmin) {
  localStorage.setItem(IS_ADMIN, isAdmin);
}

export function removeIsAdmin() {
  localStorage.removeItem(IS_ADMIN);
}

export function getIsAdmin() {
  return localStorage.getItem(IS_ADMIN);
}

export async function loginUser(username, password) {
  const response = await fetch(`${API_URL}login/`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      username: username,
      password: password
    })
  })

  if (!response.ok) {
    const errorData = await response.json()
    throw new Error(errorData.detail || 'Error al iniciar sesión')
  }

  return await response.json()
}

export async function registerUser(username, password, first_name, last_name, email) {
  const response = await fetch(`${API_URL}register/`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      username: username,
      password: password,
      first_name: first_name,
      last_name: last_name,
      email: email
    })
  })

  if (!response.ok) {
    const errorData = await response.json()
    throw new Error(errorData.detail || 'Error al registrar usuario')
  }

  return await response.json()
}
