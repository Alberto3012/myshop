import { getToken } from './userService.js';


const API_URL = 'http://127.0.0.1:8000/api/phone/';

export async function getPhones() {
  const response = await fetch(`${API_URL}phones/`, {
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${getToken()}`
    }
  });

  if (!response.ok) {
    throw new Error('Error al obtener los teléfonos');
  }
  return await response.json();
}
export async function createPhone(phone) {
    const response = await fetch(`${API_URL}newPhone/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${getToken()}`,
        },
        body: JSON.stringify(phone),
    });

    if (!response.ok) {
        throw new Error('Error al crear el teléfono');
    }

    return await response.json();
}

export async function getPhoneById(phoneId) {
    console.log(phoneId);
  const response = await fetch(`${API_URL}phones/${phoneId}`, {
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${getToken()}`
    }
  });

  if (!response.ok) {
    throw new Error('Error al obtener los teléfonos');
  }

  return await response.json();
}

export async function deletePhoneById(phoneId) {
    console.log(phoneId);
    
    const response = await fetch(`${API_URL}delete/${phoneId}`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${getToken()}`
      }
    });
  
    if (!response.ok) {
      throw new Error('Error al eliminar el teléfono');
    }
  
    return await response.json();
}

export async function updatePhoneService(phone) {
    console.log(phone.id);
    const response = await fetch(`${API_URL}phones/${phone.id}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${getToken()}`,
        },
        body: JSON.stringify(phone),
    });

    if (!response.ok) {
        throw new Error('Error al actualizar el teléfono');
    }

    return await response.json();
}
