import { useEffect, useState } from "react";
import { Link, Navigate, Outlet, Route, Routes, useNavigate } from "react-router-dom";

import { getAdminUsers } from "./api";
import { AuthProvider, useAuth } from "./auth";

function Layout({ children }) {
  return <div className="shell">{children}</div>;
}

function ProtectedRoute() {
  const { user, loading } = useAuth();
  if (loading) {
    return (
      <Layout>
        <p>Loading session...</p>
      </Layout>
    );
  }
  if (!user) {
    return <Navigate to="/login" replace />;
  }
  return <Outlet />;
}

function ManagerRoute() {
  const { user, loading } = useAuth();
  if (loading) {
    return (
      <Layout>
        <p>Loading session...</p>
      </Layout>
    );
  }
  if (!user) {
    return <Navigate to="/login" replace />;
  }
  if (user.role !== "manager") {
    return <Navigate to="/site" replace />;
  }
  return <Outlet />;
}

function LoginPage() {
  const { user, login } = useAuth();
  const navigate = useNavigate();
  const [formState, setFormState] = useState({
    email: "",
    password: "",
    error: "",
    submitting: false,
  });

  if (user) {
    return <Navigate to="/site" replace />;
  }

  async function handleSubmit(event) {
    event.preventDefault();
    setFormState((state) => ({ ...state, error: "", submitting: true }));
    try {
      await login(formState.email, formState.password);
      navigate("/site", { replace: true });
    } catch (error) {
      setFormState((state) => ({
        ...state,
        error: error.message,
        submitting: false,
      }));
      return;
    }
    setFormState((state) => ({ ...state, submitting: false }));
  }

  return (
    <Layout>
      <section className="card auth-card">
        <p className="eyebrow">ItemAdvisor Foundation</p>
        <h1>Sign in</h1>
        <form onSubmit={handleSubmit}>
          <label>
            Email
            <input
              type="email"
              value={formState.email}
              onChange={(event) =>
                setFormState((state) => ({ ...state, email: event.target.value }))
              }
              required
            />
          </label>
          <label>
            Password
            <input
              type="password"
              value={formState.password}
              onChange={(event) =>
                setFormState((state) => ({ ...state, password: event.target.value }))
              }
              required
            />
          </label>
          {formState.error ? <p className="error">{formState.error}</p> : null}
          <button type="submit" disabled={formState.submitting}>
            {formState.submitting ? "Signing in..." : "Sign in"}
          </button>
        </form>
      </section>
    </Layout>
  );
}

function SitePage() {
  const { user, logout } = useAuth();
  const navigate = useNavigate();

  async function handleLogout() {
    await logout();
    navigate("/login", { replace: true });
  }

  return (
    <Layout>
      <section className="card">
        <p className="eyebrow">Site Page</p>
        <h1>Welcome back</h1>
        <p className="lead">This is the authenticated landing page for the first generated slice.</p>
        <dl className="identity">
          <div>
            <dt>Email</dt>
            <dd>{user.email}</dd>
          </div>
          <div>
            <dt>Role</dt>
            <dd>{user.role}</dd>
          </div>
        </dl>
        <nav className="nav-row">
          <Link to="/site">Site</Link>
          {user.role === "manager" ? <Link to="/admin/users">Admin Users</Link> : null}
          <button type="button" className="ghost-button" onClick={handleLogout}>
            Log out
          </button>
        </nav>
      </section>
    </Layout>
  );
}

function AdminUsersPage() {
  const { user } = useAuth();
  const [state, setState] = useState({ loading: true, error: "", users: [] });

  useEffect(() => {
    let active = true;
    async function loadUsers() {
      try {
        const payload = await getAdminUsers();
        if (active) {
          setState({ loading: false, error: "", users: payload.users });
        }
      } catch (error) {
        if (active) {
          setState({ loading: false, error: error.message, users: [] });
        }
      }
    }
    loadUsers();
    return () => {
      active = false;
    };
  }, []);

  return (
    <Layout>
      <section className="card">
        <p className="eyebrow">Admin Users</p>
        <h1>Known users</h1>
        <p className="lead">Managers can review seeded and persisted users.</p>
        <p className="meta">Signed in as {user.email}</p>
        <nav className="nav-row">
          <Link to="/site">Back to site</Link>
        </nav>
        {state.loading ? <p>Loading users...</p> : null}
        {state.error ? <p className="error">{state.error}</p> : null}
        {!state.loading && !state.error ? (
          <table>
            <thead>
              <tr>
                <th>Email</th>
                <th>Role</th>
                <th>Created at</th>
              </tr>
            </thead>
            <tbody>
              {state.users.map((listedUser) => (
                <tr key={listedUser.id}>
                  <td>{listedUser.email}</td>
                  <td>{listedUser.role}</td>
                  <td>{new Date(listedUser.created_at).toLocaleString()}</td>
                </tr>
              ))}
            </tbody>
          </table>
        ) : null}
      </section>
    </Layout>
  );
}

export default function App() {
  return (
    <AuthProvider>
      <Routes>
        <Route path="/login" element={<LoginPage />} />
        <Route element={<ProtectedRoute />}>
          <Route path="/site" element={<SitePage />} />
        </Route>
        <Route element={<ManagerRoute />}>
          <Route path="/admin/users" element={<AdminUsersPage />} />
        </Route>
        <Route path="*" element={<Navigate to="/site" replace />} />
      </Routes>
    </AuthProvider>
  );
}
