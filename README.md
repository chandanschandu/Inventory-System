# Inventory-System

## Django Web Application with MySQL Database

This project is a simple web application built using Django for the backend and MySQL for the database. The goal is to create a form where users can enter item details (like name, type, purchase date, and stock availability) and display the submitted entries in a tabular format. The application includes form validation, data storage, and retrieval using JOIN operations between tables.

## Preface

Welcome to **Inventory-System**! This project aims to provide a basic inventory management system using Django and MySQL. It allows users to track various item details such as name, type, purchase date, and stock availability. The system stores this data and presents it in a structured, easily accessible tabular format, allowing for updates and deletions. The use of JOIN operations ensures that related data from multiple tables is fetched efficiently.

## Key Features

### Frontend:
- A form to input item details, including:
  - **Item Name** (Text input, required)
  - **Item Type** (Dropdown, required)
  - **Purchase Date** (Date input, required)
  - **Stock Available** (Checkbox, to indicate availability)
- Submit button to store data in the backend.

### Backend:
- Form validation for required fields.
- Data storage in a MySQL database.
- JOIN operations to fetch related data from multiple tables.

### Database Structure:
- **Two tables**: `item_types` (for item categories) and `items` (for item details).
- A JOIN operation is used to fetch related item types when displaying data.

### Table Display:
- Displays submitted data in a table, allowing updates or deletion of entries.

### Basic CSS Styling:
- Enhances the form and table readability.

## Prerequisites
Before running the project, make sure you have the following installed:
- **Python**: Version 3.6 or higher.
- **Django**: Version 3.0 or higher.
- **MySQL**: A MySQL server running for the database.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/inventory-system.git
   cd inventory-system

   Set up the virtual environment:
bash
Copy code
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Configure your MySQL Database:

## Create a MySQL database named items_db.
Update the settings.py with your MySQL database configurations:
python
Copy code
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'purcahse_db',
        'USER': 'your-username',
        'PASSWORD': 'your-password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
Running the Application
Apply migrations:

bash
Copy code
python manage.py migrate
Create a superuser for admin access:

bash
Copy code
python manage.py createsuperuser
Run the development server:

bash
Copy code
python manage.py runserver
Open your browser and go to http://127.0.0.1:8000/ to access the application.

## Usage
Add Item:
Navigate to the form page.
Enter item details including Name, Type, Purchase Date, and Stock Availability.
Click Submit to save the data to the database.
View, Edit, and Delete:
The home page displays a table showing all submitted items.
You can update or delete any item from the table.
Database Structure
Tables:
item_types table:

id (Primary Key)
type_name (Item category)
items table:

id (Primary Key)
name (Item Name)
purchase_date (Purchase Date)
stock_available (Boolean field for Stock Availability)
item_type_id (Foreign Key referencing item_types.id)
Join Operation:
When fetching data to display, a JOIN operation is used to retrieve item types along with item details.
