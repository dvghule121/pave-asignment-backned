# Django Backend with Django REST Framework

This is a Django backend project with Django REST Framework (DRF) setup.

## Features

- Django 4.2.7
- Django REST Framework 3.14.0
- CORS headers configured for frontend integration
- Basic API endpoints for user management
- Admin interface

## Setup

1. Install dependencies:
   ```bash
   pip install -r ../requirements.txt
   ```

2. Run migrations:
   ```bash
   python manage.py migrate
   ```

3. Create superuser (optional):
   ```bash
   python manage.py createsuperuser
   ```

4. Start development server:
   ```bash
   python manage.py runserver
   ```

## API Endpoints

- **API Overview**: `http://127.0.0.1:8000/api/`
- **Users List**: `http://127.0.0.1:8000/api/users/`
- **User Detail**: `http://127.0.0.1:8000/api/users/<id>/`
- **Admin Interface**: `http://127.0.0.1:8000/admin/`
- **DRF Auth**: `http://127.0.0.1:8000/api-auth/`

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

## Project Structure

```
backend/
├── backend/          # Main project settings
│   ├── settings.py   # Django settings with DRF config
│   ├── urls.py       # Main URL configuration
│   └── ...
├── api/              # API application
│   ├── views.py      # API views
│   ├── urls.py       # API URL patterns
│   └── ...
├── manage.py         # Django management script
└── db.sqlite3        # SQLite database
```