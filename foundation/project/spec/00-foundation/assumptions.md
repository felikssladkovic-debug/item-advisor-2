# Assumptions

- The system is a single application for initial internal use.
- MongoDB is available and is the application database.
- Environment variables in the repository `.env` file represent the initial local-development baseline.
- The backend and frontend run as separate services during development.
- The manager seed user is the only actor allowed to access the admin users page.
- Passwords may be stored using a one-way hash generated at seed time.
