# 🛒 E-Commerce Backend API (Django + DRF)

A fully functional **E-Commerce Backend REST API** built using **Django**, **Django REST Framework**, and **JWT Authentication**, deployed on **Render**. This project supports user authentication, product management, cart operations, and order management.

This project is designed to demonstrate **real-world backend skills** suitable for **internships and entry-level backend roles**.

---

## 🚀 Live Deployment

* **Backend Base URL**:
  [https://ecommerce-backend-u24e.onrender.com](https://ecommerce-backend-u24e.onrender.com)

* **Admin Panel**:
  [https://ecommerce-backend-u24e.onrender.com/admin/](https://ecommerce-backend-u24e.onrender.com/admin/)

---

## 🔐 Authentication

* JWT Authentication using **djangorestframework-simplejwt**
* Token-based access for protected APIs

---

## 📦 API Endpoints

### 👤 Authentication & Users

| Method | Endpoint         | Description                         |
| ------ | ---------------- | ----------------------------------- |
| POST   | `/api/register/` | Register a new user                 |
| POST   | `/api/token/`    | Generate JWT access & refresh token |

---

### 🛍️ Products

| Method | Endpoint         | Description              |
| ------ | ---------------- | ------------------------ |
| GET    | `/api/products/` | List all products        |
| POST   | `/api/products/` | Add product (Admin only) |

---

### 🛒 Cart

| Method | Endpoint         | Description              |
| ------ | ---------------- | ------------------------ |
| GET    | `/api/cart/`     | View logged-in user cart |
| POST   | `/api/cart/`     | Create cart item         |
| POST   | `/api/cart/add/` | Add product to cart      |

---

### 📦 Orders

| Method | Endpoint       | Description        |
| ------ | -------------- | ------------------ |
| GET    | `/api/orders/` | View user orders   |
| POST   | `/api/orders/` | Create a new order |

---

## 🔄 Application Flow (How It Works)

### 👨‍💼 Admin Flow

1. Admin logs in via `/admin/`
2. Adds products through Django Admin Panel
3. Products become available via `/api/products/`

### 👤 User Flow

1. User registers using `/api/register/`
2. User logs in using `/api/token/`
3. JWT **Access Token** is used in headers:

   ```
   Authorization: Bearer <access_token>
   ```
4. User views products
5. Adds products to cart
6. Places orders

---

## 🧪 API Testing

* APIs tested using **Postman**
* Includes authentication, cart, and order workflows

📬 **Postman Collection**:
[https://rdeekshitha184-3372244.postman.co/workspace/Deekshitha-R's-Workspace~f5b6358d-8de4-4c86-8b55-970d4dae5cd4/collection/51652683-d9a92b45-42df-466c-a017-a64dd247316b?action=share&source=copy-link&creator=51652683](https://rdeekshitha184-3372244.postman.co/workspace/Deekshitha-R's-Workspace~f5b6358d-8de4-4c86-8b55-970d4dae5cd4/collection/51652683-d9a92b45-42df-466c-a017-a64dd247316b?action=share&source=copy-link&creator=51652683)

---

## 🛠️ Tech Stack

* **Backend**: Django, Django REST Framework
* **Authentication**: JWT (SimpleJWT)
* **Database**: PostgreSQL (Render)
* **Deployment**: Render
* **API Testing**: Postman

---

## 📂 GitHub Repository

🔗 [https://github.com/rdeekshitha184-ship-it/ecommerce-backend](https://github.com/rdeekshitha184-ship-it/ecommerce-backend)

---

## 🎯 Why This Project?

* Real-world REST API architecture
* Authentication & authorization
* CRUD operations
* Deployment-ready backend
* Suitable for internships & placements

---

---

## Project Screenshots

### 🔐 Admin Panel
![Admin Panel](screenshots/Screenshot%202026-02-18%20203254.png)

---

### 🔐 Authentication Panel
![User Registration](screenshots/Screenshot%202026-02-18%20203436.png)

---

### 🛍 Product API
![Products](screenshots/Screenshot%202026-02-18%20203453.png)

---

### 🧾 Orders API
![Orders](screenshots/Screenshot%202026-02-18%20203239.png)

---

### 🛒 Cart API
![Cart](screenshots/carts.png)


## 👩‍💻 Author

**Deekshitha R**
6th Semester | Backend & AIML Enthusiast

---
> ⚠️ Note: This project was deployed on Render (free tier), which may sleep or expire.
⭐ *If you like this project, don’t forget to star the repository!*
