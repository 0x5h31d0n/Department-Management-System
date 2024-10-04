# Department Management System

The **Department Management System** is a web application built using the Django framework to manage departments within an organization. This project provides a platform for department heads, employees, and administrators to manage department-related tasks such as employee management, task assignment, and progress tracking.

## Features
- **User Authentication**: Secure login and registration system for admins, department heads, and employees.
- **Department Management**: Create, update, and delete department details.
- **Employee Management**: Add, edit, and remove employee details. Each employee is associated with a department.
- **Dashboard**: Interactive dashboards for admins and department heads to view department and employee statistics.

## Technology Stack
- **Backend**: Django (Python)
- **Frontend**: HTML5, CSS3
- **Database**: SQLite (Default Django database, can be replaced with PostgreSQL or MySQL)
- **Authentication**: Django’s built-in authentication system

## Installation

To get started with the project locally, follow these steps:

### Prerequisites

Make sure you have the following installed on your machine:
- Python 3.8+
- Django 4.x
- SQLite (default database)

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/department-management-system.git
   cd department-management-system

2. Create a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt

4. Apply migrations:
    ```bash
    python manage.py migrate

5. Run the development server:
    ```bash
    python manage.py runserver

### Credits

This project was developed by [Sheldon Angelo Menezes](https://github.com/yourusername) and [Stalin Prevan Crasta](https://github.com/StalinPrevanCrasta).