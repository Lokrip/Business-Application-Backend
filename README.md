# Business Application Backend

## Overview
This is a backend business application designed to manage clients, subscription plans, and services. It allows businesses to subscribe to different service plans and manage their subscriptions efficiently.

### Features
- **Client Management**: Clients are associated with their users and can store their company details.
- **Service Management**: Services can be created and updated with pricing details.
- **Subscription Plans**: Plans are categorized (e.g., full, student, discount) and associated with clients.
- **Dynamic Price Adjustment**: Subscription prices and comments are recalculated and updated upon changes to service prices or plan discounts.
- **Efficient Query Execution**: The application is designed to execute only necessary queries, with indexes applied to critical fields for faster lookups.
- **Cache Management**: Automatic cache invalidation when subscriptions are deleted.

## Technologies Used
- **Django**: The web framework for developing the backend.
- **Django REST Framework**: For building RESTful APIs.
- **Celery**: For handling asynchronous tasks like updating prices and comments.
- **Docker**: For containerizing the application and ensuring it runs consistently across environments.
- **Redis**: Used as a broker for Celery tasks.
- **Django Cachalot**: For improving database query performance with caching.

## Installation

### Prerequisites
- Python 3.x
- Docker and Docker Compose (optional but recommended for containerization)

### Steps to Run the Project

1. **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd <project-folder>
    ```

2. **Create and activate a virtual environment** (optional but recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:
    You may need to configure environment variables for Django settings, Redis, etc. Create a `.env` file and define the necessary variables.

5. **Apply migrations**:
    ```bash
    python manage.py migrate
    ```

6. **Create a superuser** (for accessing the Django admin):
    ```bash
    python manage.py createsuperuser
    ```

7. **Start the development server**:
    ```bash
    python manage.py runserver
    ```

### Docker Setup (Optional)
1. **Build Docker containers**:
    ```bash
    docker-compose build
    ```

2. **Start the containers**:
    ```bash
    docker-compose up
    ```

3. **Access the application**:
   Navigate to `http://localhost:8000` for the web application.