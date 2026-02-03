
# RestAPI_CRUD_Operation

A complete CRUD API project built with Django REST Framework using Class-Based Views.

## 📋 Table of Contents

- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [API Endpoints](#api-endpoints)
- [Usage Examples](#usage-examples)
- [Project Structure](#project-structure)
- [Code Examples](#code-examples)

## ✨ Features

- ✅ CRUD Operations using Class-Based Views
- ✅ RESTful API Design
- ✅ JSON Response Format
- ✅ Model Serialization
- ✅ Database Integration
- ✅ Comprehensive Error Handling
- ✅ Django Admin Integration

## 🛠 Technologies

- **Python** 3.8+
- **Django** 4.x
- **Django REST Framework** 3.x
- **SQLite** (default database)

## 📦 Installation

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Linux/Mac
# or
venv\Scripts\activate  # On Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run database migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a superuser (optional)

```bash
python manage.py createsuperuser
```

### 6. Run the development server

```bash
python manage.py runserver
```

The API will be available at: `http://127.0.0.1:8000/info`

## 🔌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/items/` | Get all items |
| POST | `/api/items/` | Create a new item |
| GET | `/api/items/{id}/` | Get a specific item |
| PUT | `/api/items/{id}/` | Update an entire item |
| PATCH | `/api/items/{id}/` | Partially update an item |
| DELETE | `/api/items/{id}/` | Delete an item |

## 💡 Usage Examples

### Get all items (GET)

```bash
curl -X GET http://127.0.0.1:8000/api/items/
```

**Response:**
```json
[
  {
    "id": 1,
    "teacher_name": "hello",
    "course_name": "Django",
    "course_duration": 4,
    "seat":100
  }
]
### Delete an item (DELETE)

```bash
curl -X DELETE http://127.0.0.1:8000/api/items/1/
` ``

## 📁 Project Structure

```
django-rest-class-based-view/
│
├── class/
│   ├── migrations/
│   ├── __init__.py
│   ├── models.py          # Data models
│   ├── serializers.py     # Serializers
│   ├── views.py           # Class-Based Views
│   ├── urls.py            # API URL routing
│   └── admin.py           # Admin configuration
│
├── project/
│   ├── __init__.py
│   ├── settings.py        # Project settings
│   ├── urls.py            # Main URL configuration
│   └── wsgi.py
│
├── manage.py
├── requirements.txt       # Dependencies
├── .gitignore
└── README.md
```

## 📋 Requirements (requirements.txt)

```txt
Django>=4.2.0
djangorestframework>=3.14.0
```



### Using Postman

1. Import the API endpoints into Postman
2. Set the request method (GET, POST, PUT, PATCH, DELETE)
3. Add the appropriate URL
4. For POST/PUT/PATCH requests, add JSON body
5. Send the request

## 🔧 Configuration

### Settings.py additions

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',  # Add this
    'class',  # Your app
]

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

Your Name - [@yourusername](https://github.com/yourusername)

Project Link: [https://github.com/yourusername/django-rest-api](https://github.com/yourusername/django-rest-api)

## 🙏 Acknowledgments

- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework Documentation](https://www.django-rest-framework.org/)
- Python Community



