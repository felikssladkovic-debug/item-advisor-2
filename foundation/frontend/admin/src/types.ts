export type Role = 'user' | 'manager'

export interface User {
  id: string
  email: string
  role: Role
  created_at: string
}

export interface ApiSuccess<T> {
  status: 'ok'
  data: T
}

export interface ApiError {
  status: 'error'
  error: {
    code: string
    message: string
  }
}

