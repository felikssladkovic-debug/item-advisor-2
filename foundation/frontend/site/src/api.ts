import type { ApiSuccess, AuthState } from './types'

export async function fetchAuthState(): Promise<AuthState> {
  const response = await fetch('/api/v1/auth/me', {
    credentials: 'include',
  })
  const body: ApiSuccess<AuthState> = await response.json()
  return body.data
}

export async function login(email: string, password: string): Promise<AuthState> {
  const response = await fetch('/api/v1/auth/login', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    credentials: 'include',
    body: JSON.stringify({ email, password }),
  })

  if (!response.ok) {
    throw new Error('Login failed')
  }

  const body: ApiSuccess<AuthState> = await response.json()
  return body.data
}

export async function logout(): Promise<void> {
  await fetch('/api/v1/auth/logout', {
    method: 'POST',
    credentials: 'include',
  })
}

