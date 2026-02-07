# Note Taker

A modern, full-stack note-taking application built with Django and PostgreSQL. Create, edit, view, and delete notes with a clean, responsive interface - all operations happen seamlessly through modals.

 

## 🚀 Live Demo

**[View Live App](#)** _(Coming Soon)_

## ✨ Features

- ✅ **Create Notes** - Quick note creation via modal
- ✅ **Edit Notes** - In-place editing without page reload
- ✅ **View Notes** - Full note preview in modal
- ✅ **Delete Notes** - Safe deletion with confirmation
- ✅ **Responsive Design** - Works on desktop, tablet, and mobile
- ✅ **Modern UI** - Clean interface with Bootstrap 5
- ✅ **PostgreSQL Database** - Robust data storage for development
- ✅ **SQLite for Production** - Lightweight deployment option

## 🛠️ Tech Stack

**Backend:**
- Django 5.1
- PostgreSQL (Development)
- SQLite (Production)

**Frontend:**
- HTML5
- CSS3
- Bootstrap 5.3
- Vanilla JavaScript

## 📋 Prerequisites

- Python 3.9+
- PostgreSQL (for local development)
- pip
- virtualenv

## ⚙️ Local Setup

### 1. Clone the Repository
```bash
git clone https://github.com/Bencruz6/Note_Taker.git
cd note-taker
```

### 2. Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up PostgreSQL Database
```bash
# Access PostgreSQL
sudo -u postgres psql

# Create database and user
CREATE DATABASE Note_DB;
CREATE USER your_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE Note_DB TO your_user;
\q
```

### 5. Configure Environment

Update `NoteApp/settings.py` with your database credentials:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'Note_DB',  
        'USER': 'your_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 6. Run Migrations
```bash
export ENVIRONMENT=development  # Enables DEBUG mode
python manage.py migrate
python manage.py collectstatic --noinput
```

### 7. Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

### 8. Run Development Server
```bash
python manage.py runserver
```

Visit **http://localhost:8000** in your browser.

## 🌐 Deployment (PythonAnywhere)

### Prerequisites
- PythonAnywhere account (free tier available)

### Steps

1. **Upload Code**
```bash
   # On PythonAnywhere Bash console
   git clone https://github.com/YOUR_USERNAME/note-taker.git
   cd note-taker
```

2. **Create Virtual Environment**
```bash
   mkvirtualenv noteapp --python=python3.9
   pip install -r requirements.txt
```

3. **Run Migrations**
```bash
   python manage.py migrate
   python manage.py collectstatic --noinput
```

4. **Configure WSGI**
   
   Edit `/var/www/YOUR_USERNAME_pythonanywhere_com_wsgi.py`:
```python
   import sys
   import os

   path = '/home/YOUR_USERNAME/note-taker'
   if path not in sys.path:
       sys.path.append(path)

   os.environ['DJANGO_SETTINGS_MODULE'] = 'NoteApp.settings'

   from django.core.wsgi import get_wsgi_application
   application = get_wsgi_application()
```

5. **Set Static Files**
   - URL: `/static/`
   - Directory: `/home/YOUR_USERNAME/note-taker/staticfiles`

6. **Reload Web App**

## 📁 Project Structure
```
note-taker/
├── NoteApp/              # Django project settings
│   ├── settings.py       # Configuration
│   ├── urls.py          # URL routing
│   └── wsgi.py          # WSGI config
├── notes/               # Notes app
│   ├── models.py        # Note model
│   ├── views.py         # View logic
│   ├── forms.py         # Django forms
│   ├── urls.py          # App URLs
│   └── templates/       # HTML templates
├── staticfiles/         # Collected static files
├── manage.py           # Django CLI
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## 🎨 Screenshots

<!-- ### Home Page
![Home Page](https://via.placeholder.com/600x400?text=Home+Page)

### Create Note Modal
![Create Modal](https://via.placeholder.com/600x400?text=Create+Note)

### Edit Note Modal
![Edit Modal](https://via.placeholder.com/600x400?text=Edit+Note) -->

comming soon
## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🙏 Acknowledgments

- Bootstrap for the UI framework
- Django community for excellent documentation
- PythonAnywhere for free hosting

---

⭐ **Star this repo if you find it helpful!**