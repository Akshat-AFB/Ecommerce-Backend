
# Ecommerce Backend

This is the backend of an E-Commerce application built using Django REST Framework.
It handles user authentication, product management, cart functionality, order processing, and more.

## 🚀 Features

- User Registration & Login with JWT Authentication
- Role-based access for Admin and Customers
- Product CRUD operations (Admin only)
- Cart management (add/remove/update items)
- Order placement and tracking
- Pagination for product listings
- Modular code structure (routes, services, repositories, schemas)
- Secure API endpoints (using DRF permissions)
- Django admin panel for backend management

## 🛠️ Tech Stack

- **Backend:** Django, Django REST Framework
- **Auth:** JWT (JSON Web Tokens)
- **Database:** SQLite (default, can switch to PostgreSQL)
- **Environment:** Python 3.x, pip, venv

## 📁 Project Structure

```
Ecommerce-Backend/
├── authentication/        # Auth logic (JWT, permissions)
├── models/                # Django models (User, Product, Cart, Order)
├── repositories/          # DB interaction layer
├── services/              # Business logic
├── routes/                # API endpoint definitions
├── schemas/               # Pydantic-like serializers
├── main.py                # Entry point (WSGI/ASGI)
├── requirements.txt       # Python dependencies
└── README.md              # Project info
```

## 🔐 Authentication

- Login & Register endpoints return a JWT token.
- Use the token as a `Bearer` token in the Authorization header.

```
Authorization: Bearer <your_token>
```

## 🔧 Setup Instructions

```bash
# 1. Clone the repository
$ git clone https://github.com/Akshat-AFB/Ecommerce-Backend.git
$ cd Ecommerce-Backend

# 2. Set up virtual environment
$ python3 -m venv venv
$ source venv/bin/activate

# 3. Install dependencies
(venv) $ pip install -r requirements.txt

# 4. Apply migrations
(venv) $ python manage.py migrate

# 5. Run the server
(venv) $ python manage.py runserver
```

## 📬 API Endpoints

| Method | Endpoint                                | Description                    |
|--------|-----------------------------------------|--------------------------------|
| POST   | /api/register/                          | Register new user              |
| POST   | /api/login/                             | Login & get JWT                |
| GET    | /api/products/                          | List products                  |
| GET    | /api/products/{int:pk}/                 | Detail Product View            |
| PUT    | /api/products/{int:pk}/update/          | Update Product (Admin)         |
| DELETE | /api/products/{int:pk}/delete/          | Delete Product (Admin)         |
| POST   | /api/products/create/                   | Create Product (Admin)         |
| GET    | /api/cart/                              | View user's cart               |
| POST   | /api/cart/add/                          | Add item to cart               |
| DELETE | /api/cart/remove/{int:pk}/              | Remove from cart               |
| POST   | /api/cart/change/{int:product_id}/      | Change cart item quantity      |
| POST   | /api/orders/place/                      | Place an order                 |
| GET    | /api/orders/                            | View orders                    |
| POST   | /api/orders/cancel/{int:order_id}/      | Cancel order                   |

## 📬 API Repsponses Screenshots


## 👥 Contributors

- Akshat AFB

## 📝 License

MIT License (add actual license content if needed)

---

Feel free to update this README as your project evolves!
