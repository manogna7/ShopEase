# ShopEase

ShopEase is an e-commerce product management system built using Django, Django REST Framework, and PostgreSQL. The system allows administrators to manage products and categories, while users can view and search for products by name or category. The application provides a RESTful API, supports CRUD operations, and includes user authentication and pagination features.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Database Schema](#database-schema)


## Features

- **Product and Category Management:** Administrators can add, update, and delete products and categories.
- **User Interface:** Users can view a list of products and search by name or category.
- **RESTful API:** Provides endpoints for managing products and categories.
- **Pagination:** Supports pagination for product listings.
- **User Authentication:** Secures administrative functions and restricts access.
- **PostgreSQL Database:** Uses PostgreSQL for storing product, category, and review data.

## Installation

Follow these steps to set up the project on your local machine:

### Prerequisites

- Python 3.8+
- PostgreSQL

### Setup Instructions

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/manogna7/ShopEase.git
   cd ecommerce
   ```


3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure PostgreSQL:**

   - Create a PostgreSQL database named `ecommerce_db`.
   - Update the `DATABASES` settings in `ecommerce/settings.py` with your database credentials.

5. **Run Migrations:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a Superuser:**

   ```bash
   python manage.py createsuperuser
   ```

7. **Run the Development Server:**

   ```bash
   python manage.py runserver
   ```

8. **Access the Application:**

   - Visit `http://127.0.0.1:8000/` in web browser to view the application.
   - Access the admin panel at `http://127.0.0.1:8000/admin/`.

## Usage

### User Interface

- **View Products:** Navigate to the home page to view a list of available products.
- **Search Products:** Use the search bar to filter products by name or category.

### Admin Panel

- **Manage Products and Categories:** Log in to the admin panel to add, update, or delete products and categories.

### API Endpoints

The application provides the following API endpoints:

- **Products:**
  - `GET /api/products/`: Retrieve a list of products.
  - `POST /api/products/`: Create a new product.
  - `PUT /api/products/<id>/`: Update an existing product.
  - `DELETE /api/products/<id>/`: Delete a product.

- **Categories:**
  - `GET /api/categories/`: Retrieve a list of categories.
  - `POST /api/categories/`: Create a new category.
  - `PUT /api/categories/<id>/`: Update an existing category.
  - `DELETE /api/categories/<id>/`: Delete a category.

## Database Schema

The project uses a PostgreSQL database with the following schema:

- **Products Table:**
  - `id`: Primary key
  - `name`: Product name
  - `description`: Product description
  - `price`: Product price
  - `category_id`: Foreign key referencing the Categories table

- **Categories Table:**
  - `id`: Primary key
  - `name`: Category name

- **Reviews Table:**
  - `id`: Primary key
  - `product_id`: Foreign key referencing the Products table
  - `user_id`: Foreign key referencing the Users table
  - `rating`: Review rating
  - `comment`: Review comment


