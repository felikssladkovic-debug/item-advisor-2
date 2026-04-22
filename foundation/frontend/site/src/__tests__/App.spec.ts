import { fireEvent, render, screen, waitFor } from '@testing-library/vue'

import App from '../App.vue'

describe('site app', () => {
  afterEach(() => {
    vi.restoreAllMocks()
  })

  it('renders unauthenticated state', async () => {
    vi.spyOn(window, 'fetch').mockResolvedValueOnce(
      new Response(
        JSON.stringify({
          status: 'ok',
          data: { authenticated: false, user: null },
        }),
      ),
    )

    render(App)

    expect(await screen.findByText('Not authenticated')).toBeInTheDocument()
  })

  it('submits login and renders authenticated user', async () => {
    vi.spyOn(window, 'fetch')
      .mockResolvedValueOnce(
        new Response(
          JSON.stringify({
            status: 'ok',
            data: { authenticated: false, user: null },
          }),
        ),
      )
      .mockResolvedValueOnce(
        new Response(
          JSON.stringify({
            status: 'ok',
            data: {
              authenticated: true,
              user: {
                id: 'u1',
                email: 'manager@example.com',
                role: 'manager',
                created_at: '2026-01-01T00:00:00Z',
              },
            },
          }),
        ),
      )

    render(App)

    await screen.findByText('Not authenticated')
    await fireEvent.update(screen.getByLabelText('Email'), 'manager@example.com')
    await fireEvent.update(screen.getByLabelText('Password'), 'manager123')
    await fireEvent.click(screen.getByText('Login'))

    await waitFor(() => {
      expect(screen.getByText('Authenticated')).toBeInTheDocument()
      expect(screen.getByText('manager@example.com')).toBeInTheDocument()
    })
  })
})

