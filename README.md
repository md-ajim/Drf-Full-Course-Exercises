# 📘 Django REST Framework – Full Course Exercises

This repository contains a collection of **Django REST Framework (DRF) exercises and practice projects** completed while following a full DRF learning path. The goal of this repo is to **practice REST API development step by step**, covering everything from the basics to advanced features.

---

## 🚀 Features Covered

* ✅ Setting up Django REST Framework
* ✅ CRUD Operations (Create, Read, Update, Delete)
* ✅ Model Serializers & Custom Serializers
* ✅ Authentication (JWT, Session, Token, Social Login)
* ✅ Permissions & Role-Based Access Control
* ✅ Pagination & Filtering
* ✅ Advanced Querysets & Relationships (One-to-Many, Many-to-Many)
* ✅ API Testing with Django & Postman
* ✅ Deployment Best Practices

---

## 🛠️ Technologies Used

* **Python 3.11+**
* **Django 5+**
* **Django REST Framework (DRF)**
* **MySQL / PostgreSQL (Database)**
* **Postman / Thunder Client (API Testing)**
* **JWT Authentication**

---

## 📂 Project Structure

```
drf-full-course-exercises/
│── 01_basic_setup/
│── 02_crud_operations/
│── 03_serializers/
│── 04_authentication/
│── 05_permissions/
│── 06_pagination_filtering/
│── 07_advanced_features/
│── README.md
```

Each folder contains a separate exercise with step-by-step practice code.

---

## ⚙️ Installation & Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/md-ajim/drf-full-course-exercises.git
   cd drf-full-course-exercises
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Mac/Linux
   venv\Scripts\activate      # On Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:

   ```bash
   python manage.py migrate
   ```

5. Start the development server:

   ```bash
   python manage.py runserver
   ```

---

## 🎯 Learning Goals

* Build a **solid understanding** of Django REST Framework.
* Gain hands-on experience with **API development**.
* Prepare for **real-world projects and interviews**.

---

## 🤝 Contributing

This repository is primarily for **learning & practice**. However, suggestions and improvements are welcome.

---

## 📜 License

This project is licensed under the **MIT License** – feel free to use the code for your own learning and projects.

---

# 📂 Subfolder README Template

You can also add a **mini README.md** inside each exercise folder for better documentation:

### Example: `01_basic_setup/README.md`

````markdown
# 01 - Basic Setup

## 📌 Overview
This exercise covers the initial setup of a Django project with Django REST Framework.

## 🔑 Key Topics
- Installing Django & DRF
- Creating a new Django project
- Setting up REST Framework in `settings.py`
- Running the development server

## 🚀 Commands Used
```bash
django-admin startproject drf_setup
cd drf_setup
python manage.py runserver
````

## 🎯 Learning Goal

Understand how to start a Django project and configure it with DRF for future exercises.

```
```
