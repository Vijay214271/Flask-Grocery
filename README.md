Description:

This Flask-based Grocery Store App is a comprehensive web application designed to simplify the management and shopping experience of a grocery store. The application provides a seamless and intuitive interface for both customers and store managers, streamlining various functionalities such as browsing products, adding items to the cart, processing orders, and managing inventory.

Key Features:

User Authentication: Secure user registration and login system with role-based access control for customers and store managers.
Product Management: Store managers can add, update, and delete products, including details such as name, price, category, and stock quantity.
Shopping Cart: Customers can browse available products, add items to their cart, and view cart contents before proceeding to checkout.
Order Processing: Facilitates smooth order processing with features like order summary, payment integration, and order history tracking.
Inventory Management: Allows store managers to monitor and update stock levels to ensure product availability.
Search and Filter: Users can search for products and apply filters based on categories, price range, and popularity.
Responsive Design: Optimized for both desktop and mobile devices to provide a consistent user experience across all platforms.

Technology Stack:

Backend: Flask, a lightweight WSGI web application framework written in Python.
Frontend: HTML, CSS, JavaScript, and Bootstrap for responsive design.
Database: MySQL for robust and scalable database management.
Authentication: Flask-Login for managing user sessions and secure access.
APIs: Integration of RESTful APIs for dynamic data handling and interactions.

Setup and Installation

Clone the Repository:
git clone https://github.com/Vijay214271/Flask-Grocery.git
cd Flask-Grocery

Create a Virtual Environment:
python3 -m venv venv
source venv/bin/activate 

Install Dependencies:
pip install -r requirements.txt

Configure MySQL Database:

Install MySQL server and create a database for the application.
Update the config.py file with your MySQL database credentials:
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@localhost/yourdatabase'

Set Up the Database:
flask db init
flask db migrate -m "Initial migration."
flask db upgrade

Run the Application:
flask run

Access the Application:
Open your web browser and go to http://127.0.0.1:5000.
