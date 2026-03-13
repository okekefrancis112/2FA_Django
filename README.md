# 2FA Django

A Django web application implementing Two-Factor Authentication (2FA) for enhanced security.

## Overview

This project demonstrates how to integrate two-factor authentication into a Django application, adding an extra layer of security beyond username and password.

## Features

- User registration and login
- Two-Factor Authentication setup and verification
- Report management system (CRUD)
- Admin panel integration
- SQLite database

## Tech Stack

- **Python** 3.10
- **Django** — Web framework
- **SQLite** — Database
- **django-otp** — 2FA implementation

## Getting Started

### Prerequisites

- Python 3.10+
- pip

### Installation

```bash
git clone https://github.com/okekefrancis112/2FA_Django.git
cd 2FA_Django
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Usage

1. Navigate to `http://localhost:8000`
2. Register a new account
3. Set up 2FA in your profile
4. Login with your credentials + 2FA code

## Project Structure

```
├── app/
│   ├── models.py        # Report model
│   ├── views.py         # View logic
│   ├── forms.py         # Django forms
│   ├── urls.py          # URL routing
│   └── migrations/      # Database migrations
├── manage.py            # Django CLI
└── db.sqlite3           # SQLite database
```

## License

MIT
