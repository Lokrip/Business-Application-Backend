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
    ```

1. **Build Docker containers**:
    ```bash
    docker-compose up --build
    ```

4. **Set up environment variables**:
    You may need to configure environment variables for your Django settings, Redis, and other services.  Create a .env file in the root directory of your project and define the following variables
    
    docker-compose.yml
    ```bash
    DB_HOST=database-1
    DB_NAME=dbname
    DB_USER=dbuser
    DB_PASS=pass
    ```

5. **Apply migrations**:
    ```bash
    docker-compose run --rm web-app sh -c "python manage.py migrate"
    ```

6. **Create a superuser** (for accessing the Django admin):
    ```bash
    docker-compose run --rm web-app sh -c "python manage.py createsuperuser"
    ```

3. **Access the application**:
   Navigate to `http://127.0.0.1:8000/` for the web application.