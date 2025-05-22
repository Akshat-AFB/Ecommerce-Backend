
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

Register User
<img width="1300" alt="Screenshot 2025-05-22 at 3 50 46 PM" src="https://github.com/user-attachments/assets/3e598dd1-b92b-4bcd-93c7-5e7b939abae1" />
<img width="1295" alt="Screenshot 2025-05-22 at 3 51 08 PM" src="https://github.com/user-attachments/assets/02244c2e-d2b3-46d0-82b2-58ca30956525" />

Login User
<img width="1300" alt="Screenshot 2025-05-22 at 3 51 24 PM" src="https://github.com/user-attachments/assets/f406f6e2-70f7-4637-91d2-55ad0813a154" />
<img width="1297" alt="Screenshot 2025-05-22 at 3 54 04 PM" src="https://github.com/user-attachments/assets/3be9e3fd-f9c6-4058-b26c-5858a8c24cba" />

Create Product
<img width="1296" alt="Screenshot 2025-05-22 at 3 58 50 PM" src="https://github.com/user-attachments/assets/e865af19-333a-40c4-ad31-ce13d5afb0f5" />

View Products with Limit and Offset
<img width="1400" alt="Screenshot 2025-05-22 at 4 09 36 PM" src="https://github.com/user-attachments/assets/fe3ad6e8-5285-41b5-9b61-c9986b901fa8" />

View cart
<img width="1398" alt="Screenshot 2025-05-22 at 4 09 57 PM" src="https://github.com/user-attachments/assets/e7be7cf6-4a80-438c-83cc-3d2eb1db25bc" />

Add to cart
<img width="1398" alt="Screenshot 2025-05-22 at 4 17 05 PM" src="https://github.com/user-attachments/assets/efd6fdb1-b327-456d-9b18-d9e314b047d7" />

View updated cart
<img width="1402" alt="Screenshot 2025-05-22 at 4 18 32 PM" src="https://github.com/user-attachments/assets/f538d483-d29a-456a-b46a-3ee83f33a6c6" />

Place Order from cart
<img width="1396" alt="Screenshot 2025-05-22 at 4 32 28 PM" src="https://github.com/user-attachments/assets/29d65c93-5d58-4156-a817-e63469fb6ba2" />

Cancel order by ID
<img width="1403" alt="Screenshot 2025-05-22 at 4 34 55 PM" src="https://github.com/user-attachments/assets/8edd2876-f772-4745-87fb-ca2cc117de47" />

View Orders
<img width="1397" alt="Screenshot 2025-05-22 at 4 35 22 PM" src="https://github.com/user-attachments/assets/bc9e61a6-ad45-4a5b-9365-b4bc0e29ae45" />

## 👥 Contributors

- Akshat AFB

## 📝 License

MIT License (add actual license content if needed)

---

Feel free to update this README as your project evolves!
