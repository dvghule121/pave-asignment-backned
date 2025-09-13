# Django Backend with Django REST Framework

This project provides a robust and scalable backend solution built with Django and Django REST Framework. It serves as the API for a web application, offering functionalities such as user management, data handling, and more. The primary goal is to deliver a solid foundation for rapid development and seamless integration with a frontend application.

## Features

- **Django 4.2.7**: Utilizes the latest stable version of Django for robust web development.
- **Django REST Framework 3.14.0**: Provides powerful tools for building Web APIs, including serialization, authentication, and viewsets.
- **CORS headers configured for frontend integration**: Enables seamless communication with frontend applications hosted on different domains.
- **Basic API endpoints for user management**: Includes endpoints for creating, retrieving, updating, and deleting user accounts.
- **Admin interface**: Django's built-in administrative interface for managing application data.

## Setup

1. **Set up a virtual environment** (recommended):
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Database Setup (PostgreSQL)**:
   This project uses PostgreSQL as its database. You need to set up your PostgreSQL database and configure the following environment variables:

   - `DB_NAME`: Your PostgreSQL database name
   - `DB_USER`: Your PostgreSQL username
   - `DB_PASSWORD`: Your PostgreSQL password
   - `DB_HOST`: Your PostgreSQL host (e.g., `localhost` or a Docker service name)
   - `DB_PORT`: Your PostgreSQL port (e.g., `5432`)

   You can create a `.env` file in the `backend` directory with these variables, for example:
   ```
   DB_NAME=pave_db
   DB_USER=pave_user
   DB_PASSWORD=your_password
   DB_HOST=localhost
   DB_PORT=5432
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Create superuser (optional):
   ```bash
   python manage.py createsuperuser
   ```

6. Start development server:
   ```bash
   python manage.py runserver
   ```

## API Endpoints

The following API endpoints are available. All endpoints are accessible under the `/api/` prefix. Detailed schema information can be found in the Swagger UI.

- **API Overview**: `http://127.0.0.1:8000/api/` - Provides an overview of all available API endpoints.
- **Users List**: `http://127.0.0.1:8000/api/users/` - Retrieve a list of all users or create a new user.
- **User Detail**: `http://127.0.0.1:8000/api/users/<id>/` - Retrieve, update, or delete a specific user by ID.
- **Admin Interface**: `http://127.0.0.1:8000/admin/` - Django's built-in administrative interface.
- **DRF Auth**: `http://127.0.0.1:8000/api-auth/` - Login and logout views for the browsable API.

## Default Superuser

- **Username**: admin
- **Password**: admin123
- **Email**: admin@example.com

## CORS Configuration

The backend is configured to accept requests from:
- `http://localhost:3000` (React default)
- `http://localhost:5173` (Vite default)
- `http://127.0.0.1:3000`
- `http://127.0.0.1:5173`
- `https://pave-asignment-frontend.vercel.app`

## Project Structure

```
backend/
├── backend/          # Main project settings and URL configurations
│   ├── settings.py   # Django settings, including DRF, CORS, and database configurations
│   ├── urls.py       # Main URL dispatcher for the entire project
│   └── ...           # Other core project files
├── api/              # API application for handling business logic and data serialization
│   ├── views.py      # API views that handle requests and return responses
│   ├── urls.py       # URL patterns specific to the API application
│   ├── serializers.py # Defines how complex data types are converted to and from Python datatypes
│   ├── models.py     # Database models defining the structure of application data
│   └── ...           # Other API-related files (e.g., admin, tests)
├── manage.py         # Django's command-line utility for administrative tasks
└── db.sqlite3        # Default SQLite database file (used in development)
```

## API Documentation

To access the API documentation (Swagger UI), ensure the Django development server is running and navigate to:

`http://127.0.0.1:8000/api/schema/swagger-ui/`