# 🛒 E-Commerce Backend API

This is a **Node.js + Express** backend for an e-commerce platform that sells mobile phones. The API supports core features such as product listings, user authentication, cart management, order processing, and a mock payment system. It follows **SOLID principles**, uses clean code architecture, and supports pagination for both products and order history.

---

## 🚀 Features

- ✅ Product listing with pagination
- 🔍 Product detail view
- 👤 User registration and login
- 🛒 Cart management
- 📦 Order placement and history
- 💳 Mock payment processing
- 🔐 Simple authentication (header-based)
- ✅ Clean architecture with service separation
- 🧪 Basic error handling and modular design

---

## 🧱 Tech Stack

- **FastAPI(Python)**
- **In-memory storage** (for simplicity)
- **Postman** for API testing

---


Each folder contains a modular service class for handling business logic related to its domain.

---

## 🧪 API Endpoints

### 🔹 Product

| Method | Endpoint               | Description               |
|--------|------------------------|---------------------------|
| GET    | `/products/` | List all products (paginated) |
| GET    | `/products/{product_id}`    | Get product detail by ID  |

### 🔹 User

| Method | Endpoint            | Description       |
|--------|---------------------|-------------------|
| POST   | `/users/register` | Register user     |
| POST   | `/users/login`    | Login user        |

### 🔹 Cart

| Method | Endpoint      | Description            |
|--------|---------------|------------------------|
| POST   | `/cart/add`   | Add product to cart    |
| GET    | `/cart/{user_id}`   | View user cart         |
| PUT    | `/cart/remove`   | Remove item from cart        |

### 🔹 Order

| Method | Endpoint         | Description                        |
|--------|------------------|------------------------------------|
| POST   | `/orders/createOrder`    | Place order           |
| GET    | `/{user_id}`    | View user's order history (paginated) |
| PUT    | `/{user_id}/{order_id}`    | Cancel order |


## 🖼️ Postman Screenshots

### 📦 List of Products
![alt text](/img/1.png)

### 🔍 Particular Product
![alt text](/img/2.png)

### 📝 User Registration
![alt text](/img/3.png)

### 🔐 User Login
![alt text](/img/4.png)

### 🛒 Add to Cart
![alt text](/img/5.png)

### 🧾 View Cart
![alt text](/img/6.png)
![alt text](/img/7.png)

### ✅ Place Order
![alt text](/img/8.png)

### 📜 View Orders
![alt text](/img/9.png)

### 💳 Payment Success
![alt text](/img/10.png)

---

## 🔐 Authentication

For protected routes like `/api/cart` and `/api/orders`, add a header:
```http
user_id: your_user_id

