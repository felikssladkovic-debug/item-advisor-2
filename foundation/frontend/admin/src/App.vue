<script setup lang="ts">
import { onMounted, ref } from 'vue'

import { fetchUsers } from './api'
import type { User } from './types'

const users = ref<User[]>([])
const loading = ref(true)
const message = ref('')

onMounted(async () => {
  try {
    users.value = await fetchUsers()
  } catch (error) {
    message.value = error instanceof Error ? error.message : 'Unable to load users.'
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <main class="page">
    <section class="panel">
      <h1>Admin Users</h1>
      <p class="lead">Manager-only read-only user list.</p>

      <p v-if="loading">Loading users...</p>
      <p v-else-if="message" class="message">{{ message }}</p>

      <table v-else>
        <thead>
          <tr>
            <th>Email</th>
            <th>Role</th>
            <th>Created</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="user in users" :key="user.id">
            <td>{{ user.email }}</td>
            <td>{{ user.role }}</td>
            <td>{{ new Date(user.created_at).toLocaleString() }}</td>
          </tr>
        </tbody>
      </table>
    </section>
  </main>
</template>

