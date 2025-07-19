
# 🏡 AirBnB Clone Backend

This is the backend of a full-stack AirBnB clone built with **Django** and **Django REST Framework**. It provides RESTful and GraphQL APIs for managing users, properties, bookings, payments, reviews, and messaging. It also features caching, JWT authentication, search/filtering, and PostgreSQL integration.

## 📦 Tech Stack

| Layer        | Technology                      |
|--------------|----------------------------------|
| Framework    | Django, Django REST Framework    |
| DB           | PostgreSQL                       |
| Auth         | JWT (SimpleJWT)                  |
| Async Tasks  | Celery + Redis                   |
| Caching      | Redis                            |
| Deployment   | Railway / Docker (optional)      |
| Docs         | DRF + Swagger/OpenAPI            |

## ⚙️ Features

- User authentication (JWT)
- Property management with images
- Booking and availability logic
- Payment flow (mock or Stripe-ready)
- Reviews system
- Secure APIs with throttling and logging
- Search, filtering, and pagination
- Admin panel for all models
- Environment-based configuration via `.env`

## 🚀 Quickstart

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/airbnb-clone-backend.git
cd airbnb-clone-backend
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file:

```
DJANGO_SECRET_KEY=your-secret
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost

DB_NAME=airbnb_db
DB_USER=airbnb_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

### 5. Apply Migrations & Create Superuser

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### 6. Run Server

```bash
python manage.py runserver
```

## 🔐 Authentication

Uses **JWT** via `SimpleJWT`:

- Login: `POST /api/token/`
- Refresh: `POST /api/token/refresh/`

All secure routes require:
```
Authorization: Bearer <access_token>
```

## 🗃 API Endpoints

### 🔐 Users
| Method | Endpoint          | Description           |
|--------|-------------------|-----------------------|
| GET    | `/users/`         | List users            |
| POST   | `/users/`         | Register new user     |
| GET    | `/users/{id}/`    | Retrieve user         |

### 🏠 Properties
| Method | Endpoint               | Description              |
|--------|------------------------|--------------------------|
| GET    | `/properties/`         | List/filter/search       |
| POST   | `/properties/`         | Create new property      |
| PUT    | `/properties/{id}/`    | Update listing           |

### 📅 Bookings
| Method | Endpoint              | Description            |
|--------|-----------------------|------------------------|
| GET    | `/bookings/`          | List user’s bookings   |
| POST   | `/bookings/`          | Create booking         |

### 💳 Payments
| Method | Endpoint          | Description            |
|--------|-------------------|------------------------|
| POST   | `/payments/`      | Process payment        |

### ✍️ Reviews
| Method | Endpoint             | Description              |
|--------|----------------------|--------------------------|
| GET    | `/reviews/`          | List all reviews         |
| POST   | `/reviews/`          | Add review               |

## 📚 API Documentation

Swagger/OpenAPI available at:

```
/api/docs/ or /swagger/
```

## 🪵 Logging & Throttling

- All user requests (IP + timestamp + location) are logged
- Throttling on login and payment routes (e.g. `5/min`)

## 🚀 Deployment with Railway

1. Push project to GitHub
2. Create a new Railway project → Deploy from GitHub
3. Add environment variables via Railway UI
4. Enable PostgreSQL plugin (copy DB credentials)
5. Set build command:  
   ```
   pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput
   ```
6. Set start command:  
   ```
   gunicorn project_name.wsgi
   ```

## 📁 Project Structure

```
airbnb_clone_backend/
│
├── core_app/         # Users, messaging, middleware, utils
├── listings_app/     # Property CRUD
├── bookings_app/     # Booking flow
├── payments_app/     # Payment endpoints
├── reviews_app/      # Ratings and reviews
├── users_app/        # Custom user logic & auth
├── media/            # Uploaded images
├── staticfiles/      # Static assets
├── .env              # Local environment
├── requirements.txt
└── manage.py
```

## 🛠 Requirements

- Python 3.10+
- PostgreSQL 13+
- Redis (for caching + Celery)
- pip, virtualenv
