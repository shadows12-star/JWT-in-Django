# JWT Authentication in Django

A focused practice project demonstrating how to implement **JSON Web Token (JWT) authentication** in a Django REST Framework API using `djangorestframework-simplejwt`.

---

## What This Project Covers

| Concept | Details |
|---|---|
| JWT token generation | Obtain access + refresh token pair via `/api/token/` |
| Token refresh | Get a new access token via `/api/token/refresh/` |
| Protected endpoints | `POST /app/post/` requires a valid JWT |
| Public endpoints | `GET /app/post/` accessible without authentication |
| `IsAuthenticatedOrReadOnly` | Global default permission class |
| `IsAuthenticated` | Per-view permission override |
| Access token lifetime | 50 minutes |
| Refresh token lifetime | 1 day |

---

## How JWT Works Here

```
1. Client sends credentials → POST /api/token/
2. Server returns { access, refresh } tokens
3. Client includes access token in header → Authorization: Bearer <access_token>
4. Server validates the token on protected routes
5. When access token expires → POST /api/token/refresh/ with refresh token
6. Server returns a new access token
```

---

## API Endpoints

| Method | Endpoint | Auth Required | Description |
|---|---|---|---|
| POST | `/api/token/` | No | Obtain access + refresh token |
| POST | `/api/token/refresh/` | No | Refresh an expired access token |
| GET | `/app/post/` | No | Public — returns welcome message |
| POST | `/app/post/` | Yes | Protected — returns the authenticated user's name |

---

## Example Usage

### 1. Obtain Tokens

```bash
POST /api/token/
Content-Type: application/json

{
  "username": "your_username",
  "password": "your_password"
}
```

Response:
```json
{
  "access": "eyJhbGciOiJIUzI1NiIs...",
  "refresh": "eyJhbGciOiJIUzI1NiIs..."
}
```

### 2. Access a Protected Endpoint

```bash
POST /app/post/
Authorization: Bearer <access_token>
```

Response:
```json
{
  "message": "data is created by your_username"
}
```

### 3. Refresh an Expired Access Token

```bash
POST /api/token/refresh/
Content-Type: application/json

{
  "refresh": "eyJhbGciOiJIUzI1NiIs..."
}
```

---

## Project Structure

```
JWT-in-Django/
├── app/
│   ├── views.py       # posts view with permission classes
│   └── urls.py
├── projectalpha/
│   ├── settings.py    # JWT config, DRF auth settings
│   └── urls.py        # Token obtain + refresh routes
└── manage.py
```

---

## Tech Stack

| Layer | Technology |
|---|---|
| Framework | Django 6, Django REST Framework |
| JWT | djangorestframework-simplejwt |
| Database | SQLite |
| Language | Python 3 |

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/shadows12-star/JWT-in-Django.git
cd JWT-in-Django
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install django djangorestframework djangorestframework-simplejwt
```

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. Create a user to test with

```bash
python manage.py createsuperuser
```

### 6. Run the server

```bash
python manage.py runserver
```

You can test the endpoints using **Postman**, **Insomnia**, or **curl**.

---

## JWT Configuration (settings.py)

```python
from datetime import timedelta

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ),
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=50),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
}
```

---

## Learning Notes

- `IsAuthenticatedOrReadOnly` is set globally — GET requests are open, write requests require a valid token
- The `POST /app/post/` view uses `@permission_classes([IsAuthenticated])` to enforce authentication regardless of the global setting
- `request.user.username` works because simplejwt decodes the token and attaches the user to the request automatically

---

## License

Open source for learning purposes. MIT License recommended.
