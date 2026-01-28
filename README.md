
# 🛒 Django E-Commerce Backend API

A Django REST Framework–based **E-Commerce Backend API** that supports user authentication, product management, cart operations, and order processing.
This project is built to demonstrate **real-world backend architecture** and RESTful API design.

---

## 🚀 Features

* 🔐 User Registration & Login (JWT Authentication)
* 📦 Product Management (CRUD via Admin Panel & APIs)
* 🛒 Cart Management (Add / View Cart Items)
* 📑 Order Management (Create & View Orders)
* 🛠️ Django Admin Panel Support
* 🔗 RESTful APIs using Django REST Framework

---

## 🧰 Tech Stack

* **Backend:** Django, Django REST Framework
* **Authentication:** JWT (JSON Web Tokens)
* **Database:** SQLite (can be switched to PostgreSQL/MySQL)
* **API Testing:** Postman
* **Language:** Python

---

## 📂 Project Structure

```
ecommerce_backend/
│
├── manage.py
├── db.sqlite3
│
├── ecommerce_api/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── accounts/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
├── products/
├── cart/
├── orders/
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/rdeekshitha-ship-it/ecommerce-backend.git
cd ecommerce-backend
```

---

### 2️⃣ Create & Activate Virtual Environment

```bash
python -m venv venv
```

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 5️⃣ Create Superuser (Admin)

```bash
python manage.py createsuperuser
```

---

### 6️⃣ Run the Server

```bash
python manage.py runserver
```

Server will start at:

```
http://127.0.0.1:8000/
```

---

## 🔑 API Endpoints (Sample)

| Feature  | Endpoint         | Method     |
| -------- | ---------------- | ---------- |
| Register | `/api/register/` | POST       |
| Login    | `/api/login/`    | POST       |
| Products | `/api/products/` | GET        |
| Cart     | `/api/cart/`     | GET / POST |
| Orders   | `/api/orders/`   | GET / POST |

🔐 **Authorization:**
Use JWT token in headers:

```
Authorization: Bearer <access_token>
```

---

## 🧪 Testing APIs

* Use **Postman**
* Set method (GET / POST)
* Add `Authorization` header for protected routes
* Send JSON body for POST requests

---

## 👩‍💻 Admin Panel

Access Django Admin:

```
http://127.0.0.1:8000/admin/
```

From here you can:

* Add products
* Manage users
* View carts & orders

---

## 🎯 Project Purpose

This project was built to:

* Understand Django REST Framework deeply
* Learn real-world backend workflows
* Practice authentication & authorization
* Prepare for internships & backend developer roles

---

## 📌 Future Improvements

* Payment Gateway Integration
* Product Categories
* Order Status Tracking
* Deployment (Render / Railway / AWS)
* Swagger API Documentation

---

## 🙋‍♀️ Author

**Deekshitha R**
Aspiring Backend Developer | Django & Python Enthusiast

---

## ⭐ If you like this project

Give it a ⭐ on GitHub — it motivates me to build more!


