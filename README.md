# Django Multi-User Auth App

A Django application to handle signup and login for two types of users: Doctor and Patient.

## Features

- Signup with custom fields and profile picture
- Role-based login
- Redirect to user-specific dashboards
- Profile image upload
- Logout functionality visible on all pages

### 📚 Blog System
- Doctors can:
  - Create blog posts (with title, image, category, summary, content)
  - Mark blog posts as drafts
  - View posts they’ve uploaded
- Patients can:
  - Browse **non-draft** blog posts **category-wise**
  - See blog cards with:
    - Title
    - Image
    - Summary (truncated to 15 words)

### 📂 Categories
- Mental Health
- Heart Disease
- Covid19
- Immunization

---

## 🗃️ Database Configuration

This project uses **MySQL** instead of the default SQLite.
