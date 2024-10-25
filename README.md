# Freelance Website Project

Welcome to the Freelance Website Project! This web application provides a platform for freelancers and clients to connect, manage projects, and handle job listings. The project is built using **HTML**, **CSS**, and **JavaScript** for the frontend, with **Django** as the backend framework, and a **MySQL** database for production with **SQLite** for local development.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation and Setup](#installation-and-setup)
- [Database Configuration](#database-configuration)
- [Usage](#usage)
- [Folder Structure](#folder-structure)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The Freelance Website Project is designed to streamline the process of job posting, hiring, and project management. Clients can post jobs, browse freelancer profiles, and hire talent. Freelancers can set up profiles, bid on jobs, and communicate with clients through the platform.

### Goals:
- To provide an intuitive and user-friendly interface for clients and freelancers.
- To manage user authentication, job postings, bids, and profiles within the platform.
- To handle large amounts of data efficiently with Django and MySQL in production, while enabling lightweight testing and development with SQLite.

## Features

- **User Authentication**: Users can sign up as freelancers or clients and log in to their dashboard.
- **Profile Management**: Freelancers can create profiles highlighting skills, experience, and portfolio.
- **Job Posting and Bidding**: Clients can post jobs, and freelancers can bid on available jobs.
- **Notifications**: Email notifications for new jobs, bids, and project updates.
- **Admin Dashboard**: A secure backend for managing users, job posts, and site content.

## Technologies Used

### Frontend
- **HTML**: Structuring the web pages.
- **CSS**: Styling the application.
- **JavaScript**: Client-side scripting and interactions.

### Backend
- **Django**: For handling backend logic, routing, and user authentication.
- **MySQL**: Used as the main database for production.
- **SQLite**: Used as the database for local development and testing.

## Installation and Setup

To get started with the project, follow these steps:

### Prerequisites
- **Python 3.8+**
- **Django 3.2+**
- **MySQL Server**
- **pip (Python package manager)**

### Clone the Repository
```bash
git clone https://github.com/yourusername/freelance-website.git
cd freelance-website
```

### Create a Virtual Environment and Install Dependencies
```bash
python3 -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
pip install -r requirements.txt
```

### Set Up the Database
1. **MySQL**:
   - Create a MySQL database and user.
   - Update the database settings in `settings.py` with your MySQL database credentials.

2. **SQLite** (for local development):
   - Simply use the default SQLite configuration in `settings.py` for a quick setup.

### Run Migrations
```bash
python manage.py migrate
```

### Start the Server
```bash
python manage.py runserver
```

The website will be accessible at `http://127.0.0.1:8000`.

## Database Configuration

1. **MySQL**: To use MySQL in production, configure the `DATABASES` setting in `settings.py`:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'your_database_name',
           'USER': 'your_database_user',
           'PASSWORD': 'your_database_password',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   ```

2. **SQLite**: For local development, simply set up as follows:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.sqlite3',
           'NAME': BASE_DIR / "db.sqlite3",
       }
   }
   ```

## Usage

1. **Create an Account**: Sign up as a freelancer or client.
2. **Post or Apply for Jobs**: Clients can post jobs, and freelancers can bid.
3. **Manage Dashboard**: Both freelancers and clients have access to a dashboard for managing activities.

## Folder Structure

```plaintext
freelance-website/
├── static/                 # Static assets (CSS, JavaScript, images)
├── templates/              # HTML templates
├── project_name/           # Django project settings and configuration
├── app_name/               # Core application folder (views, models, etc.)
├── db.sqlite3              # SQLite database file (for development)
├── manage.py               # Django management script
└── requirements.txt        # Python dependencies
```

## Contributing

1. Fork the project.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a Pull Request.


Thank you for checking out the Freelance Website Project! We look forward to your contributions and feedback. Happy coding!
