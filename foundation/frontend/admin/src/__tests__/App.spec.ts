import { render, screen } from '@testing-library/vue'

import App from '../App.vue'

describe('admin app', () => {
  afterEach(() => {
    vi.restoreAllMocks()
  })

  it('renders users list for manager response', async () => {
    vi.spyOn(window, 'fetch').mockResolvedValueOnce(
      new Response(
        JSON.stringify({
          status: 'ok',
          data: [
            {
              id: 'u1',
              email: 'manager@example.com',
              role: 'manager',
              created_at: '2026-01-01T00:00:00Z',
            },
          ],
        }),
      ),
    )

    render(App)

    expect(await screen.findByText('manager@example.com')).toBeInTheDocument()
  })

  it('renders forbidden message', async () => {
    vi.spyOn(window, 'fetch').mockResolvedValueOnce(
      new Response(
        JSON.stringify({
          status: 'error',
          error: {
            code: 'forbidden',
            message: 'Manager role required.',
          },
        }),
        { status: 403 },
      ),
    )

    render(App)

    expect(await screen.findByText('Manager role required.')).toBeInTheDocument()
  })
})

