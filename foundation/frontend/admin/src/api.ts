import type { ApiError, ApiSuccess, User } from './types'

export async function fetchUsers(): Promise<User[]> {
  const response = await fetch('/api/v1/admin/users', {
    credentials: 'include',
  })

  if (response.status === 403) {
    const error: ApiError = await response.json()
    throw new Error(error.error.message)
  }

  if (response.status === 401) {
    throw new Error('Authentication required.')
  }

  if (!response.ok) {
    throw new Error('Unable to load users.')
  }

  const body: ApiSuccess<User[]> = await response.json()
  return body.data
}

