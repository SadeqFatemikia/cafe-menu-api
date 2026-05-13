# ☕ Cafe Menu API

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.x-green.svg)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/DRF-3.15-red.svg)](https://www.django-rest-framework.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A RESTful API for managing cafe menu, built with Django REST Framework.

## ✨ Features

- ✅ **Full CRUD operations** for menu items and categories
- ✅ **Nested category serialization** (automatically shows full category details)
- ✅ **Django Admin Panel** for easy data management
- ✅ **Environment variables** support (python-dotenv)
- ✅ **Clean, maintainable code** following DRY principles

## 🛠️ Tech Stack

| Category | Technologies |
|----------|-------------|
| Backend | Python 3.10+, Django 5.x, Django REST Framework |
| Database | SQLite (development) / PostgreSQL (production ready) |
| Tools | python-dotenv, Git |

## 🚀 Installation

### Prerequisites
- Python 3.10 or higher
- Git
- pip (Python package manager)

### Setup Instructions

```bash
# 1. Clone the repository
git clone https://github.com/SadeqFatemikia/cafe-menu-api.git
cd cafe-menu-api

# 2. Create and activate virtual environment
python -m venv venv
source venv/bin/activate      # On Linux/Mac
venv\Scripts\activate          # On Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up environment variables
# Create a .env file in the project root and add:
# SECRET_KEY=your-secret-key-here
# DEBUG=True

# 5. Run migrations
python manage.py migrate

# 6. Create superuser (for admin panel)
python manage.py createsuperuser

# 7. Run development server
python manage.py runserver
📡 API Endpoints
Method	Endpoint	Description
GET	/api/menu/	List all menu items
POST	/api/menu/	Create new menu item
GET	/api/menu/{id}/	Get single menu item
PUT	/api/menu/{id}/	Update full menu item
PATCH	/api/menu/{id}/	Partial update
DELETE	/api/menu/{id}/	Delete menu item
📝 Sample API Request & Response
POST /api/menu/
Request Body:

json
{
    "name": "Espresso",
    "description": "Strong and bold coffee",
    "price": 25000,
    "category_id": 1,
    "is_available": true,
    "preparation_time": 5,
    "priority_order": 1
}
Response:

json
{
    "id": 1,
    "name": "Espresso",
    "price": "25000.00",
    "category": {
        "id": 1,
        "name": "Coffee",
        "icon": "☕",
        "priority_order": 1
    },
    "is_available": true,
    "preparation_time": 5
}
🗂️ Project Structure
text
cafe-menu-api/
├── core/                    # Project configuration
│   ├── settings.py
│   └── urls.py
├── menu/                    # Main application
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── admin.py
│   └── urls.py
├── .env                     # Environment variables (git ignored)
├── .gitignore
├── manage.py
└── README.md
🧪 Testing with Postman
Start the server: python manage.py runserver

Open Postman and create requests:

GET http://127.0.0.1:8000/api/menu/ - Get all items

POST http://127.0.0.1:8000/api/menu/ - Create new item

GET http://127.0.0.1:8000/api/menu/1/ - Get item by ID

📂 Admin Panel Access
URL: http://127.0.0.1:8000/admin

Login with your superuser credentials

🔧 Future Improvements
Add JWT authentication

Add filtering, searching and pagination

Add Redis caching

Dockerize the application

Write unit tests

Add Swagger/OpenAPI documentation

📄 License
This project is for learning and portfolio purposes.

👨‍💻 Author
 Sadeq Fatemikia

GitHub: @SadeqFatemikia

Email: Sadeghfk6@gmail.com

⭐ Show Your Support
If this project helped you, please give it a ⭐️ on GitHub!
