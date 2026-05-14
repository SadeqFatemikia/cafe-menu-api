# ☕ Cafe Menu API

A RESTful API for managing cafe menu, built with Django REST Framework.

## ✨ Features

- ✅ **CRUD operations** for menu items and categories
- ✅ **Nested category serialization** (full category details in menu item response)
- ✅ **Django Admin Panel** for easy data management
- ✅ **REST API** with proper status codes
- ✅ **Environment variables** support (python-dotenv)
- ✅ **Git ignored** sensitive files

## 🛠️ Tech Stack

- Python 3.10+
- Django 5.x
- Django REST Framework
- SQLite (development) / PostgreSQL (production ready)
- python-dotenv

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/SadeqFatemikia/cafe-menu-api.git
cd cafe-menu-api
2. Create and activate virtual environment
bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install dependencies
bash
pip install -r requirements.txt
4. Set up environment variables
Create a .env file in the project root:

env
SECRET_KEY=your-secret-key-here
DEBUG=True
5. Run migrations
bash
python manage.py migrate
6. Create superuser (for admin panel)
bash
python manage.py createsuperuser
7. Run development server
bash
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
    "description": "Strong and bold",
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
├── core/               # Project settings
│   ├── settings.py
│   └── urls.py
├── menu/               # Main app
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── admin.py
│   └── urls.py
├── .env                # Environment variables (git ignored)
├── .gitignore
├── manage.py
└── README.md
🧪 Testing with Postman
Import the following endpoints into Postman:

GET http://127.0.0.1:8000/api/menu/ - Get all items

POST http://127.0.0.1:8000/api/menu/ - Create new item

GET http://127.0.0.1:8000/api/menu/1/ - Get item by ID

📂 Admin Panel Access
URL: http://127.0.0.1:8000/admin

Login with superuser credentials

🔧 Future Improvements
Add JWT authentication

Add filtering, searching and pagination

Add Redis caching

Dockerize the application

Write unit tests

Add Swagger documentation

📄 License
This project is for learning purposes.

👨‍💻 Author
Mohammad Sadeq Fatemikia

GitHub: @SadeqFatemikia

Email: Sadeghfk6@gmail.com