<script setup lang="ts">
import { onMounted, ref } from 'vue'

import { fetchAuthState, login, logout } from './api'
import type { AuthState } from './types'

const authState = ref<AuthState | null>(null)
const email = ref('')
const password = ref('')
const errorMessage = ref('')
const loading = ref(true)

async function loadAuthState() {
  loading.value = true
  errorMessage.value = ''
  try {
    authState.value = await fetchAuthState()
  } catch {
    errorMessage.value = 'Unable to load authentication state.'
  } finally {
    loading.value = false
  }
}

async function submitLogin() {
  errorMessage.value = ''
  try {
    authState.value = await login(email.value, password.value)
    password.value = ''
  } catch {
    errorMessage.value = 'Login failed.'
  }
}

async function submitLogout() {
  await logout()
  await loadAuthState()
}

onMounted(loadAuthState)
</script>

<template>
  <main class="page">
    <section class="panel">
      <h1>ItemAdvisor Foundation</h1>
      <p class="lead">Public site root page.</p>

      <p v-if="loading">Loading auth state...</p>
      <p v-else-if="errorMessage" class="error">{{ errorMessage }}</p>

      <template v-else-if="authState?.authenticated && authState.user">
        <p class="status">Authenticated</p>
        <dl class="details">
          <div>
            <dt>User ID</dt>
            <dd>{{ authState.user.id }}</dd>
          </div>
          <div>
            <dt>Email</dt>
            <dd>{{ authState.user.email }}</dd>
          </div>
          <div>
            <dt>Role</dt>
            <dd>{{ authState.user.role }}</dd>
          </div>
        </dl>
        <button type="button" @click="submitLogout">Logout</button>
      </template>

      <template v-else>
        <p class="status">Not authenticated</p>
        <form class="form" @submit.prevent="submitLogin">
          <label>
            Email
            <input v-model="email" type="email" autocomplete="username" required />
          </label>
          <label>
            Password
            <input
              v-model="password"
              type="password"
              autocomplete="current-password"
              required
            />
          </label>
          <button type="submit">Login</button>
        </form>
      </template>
    </section>
  </main>
</template>

