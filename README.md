# 🛒 Marketplace API

A **production-ready Django REST API** for a marketplace platform where users can create, browse, and manage classified advertisements.

This project demonstrates real-world backend development concepts including authentication, permissions, image uploads, pagination, filtering, search, and deployment.

---

# 🚀 Live API

Base URL:

```
https://marketplace-api-uyuh.onrender.com
```

Example endpoint:

```
GET /api/ads/
```

---

# ✨ Features

* User registration
* JWT Authentication
* Create, update and delete ads
* Owner-based permissions
* Image upload support
* Pagination
* Filtering
* Search functionality
* PostgreSQL database support
* Production deployment on Render

---

# 🧰 Tech Stack

Backend:

* Python
* Django
* Django REST Framework

Authentication:

* JWT (SimpleJWT)

Database:

* PostgreSQL

Deployment:

* Render

---

# 📂 Project Structure

```
marketplace-api-v2
│
├── ads
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── admin.py
│
├── config
│   ├── settings.py
│   ├── urls.py
│
├── manage.py
├── requirements.txt
└── README.md
```

---

# 🔐 Authentication

The API uses **JWT authentication**.

### Get Token

```
POST /api/token/
```

Example request:

```
{
  "username": "user",
  "password": "password"
}
```

Response:

```
{
  "access": "JWT_ACCESS_TOKEN",
  "refresh": "JWT_REFRESH_TOKEN"
}
```

Use the access token in headers:

```
Authorization: Bearer <access_token>
```

---

# 👤 User Registration

Create a new user:

```
POST /api/register/
```

Example request:

```
{
  "username": "manas",
  "email": "manas@email.com",
  "password": "password123"
}
```

---

# 📢 Ads API

### Get All Ads

```
GET /api/ads/
```

### Create Ad

```
POST /api/ads/
```

Requires authentication.

### Get Ad Details

```
GET /api/ads/{id}/
```

### Update Ad

```
PUT /api/ads/{id}/
```

Owner only.

### Delete Ad

```
DELETE /api/ads/{id}/
```

Owner only.

---

# 🔎 Search

Search ads by keyword:

```
GET /api/ads/?search=bike
```

---

# 🎯 Filtering

Filter ads by fields:

```
GET /api/ads/?location=Indore
GET /api/ads/?price=35000
```

---

# 📄 Pagination

Example:

```
GET /api/ads/?page=2
```

---

# 🖼 Image Upload

Ads support image uploads using multipart form data.

Example field:

```
image: file
```

---

# ⚙️ Local Development Setup

Clone repository:

```
git clone https://github.com/ManasRathore15/marketplace-api-v2.git
```

Enter project folder:

```
cd marketplace-api-v2
```

Create virtual environment:

```
python -m venv env
```

Activate environment:

```
env\Scripts\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

Run migrations:

```
python manage.py migrate
```

Run server:

```
python manage.py runserver
```

---

# 🌐 Deployment

The project is deployed on **Render**.

Deployment stack:

```
Django
Gunicorn
PostgreSQL
Render
```

---

# 👨‍💻 Author

**Manas Rathore**

Final year CSIT student
Python Backend Developer (aspiring)

Location:

```
Indore, Madhya Pradesh
```

---

# ⭐ Future Improvements

* Docker support
* Redis caching
* Celery background jobs
* API documentation (Swagger)
* CI/CD pipeline

---
