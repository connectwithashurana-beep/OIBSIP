PIZZA DELIVERY FULL-STACK APPLICATION
OIBSIP - Web Development & Design - Level 3


PROJECT OVERVIEW
----------------

Pizza Delivery is a full-stack online food ordering application developed
as part of the OIBSIP Web Development & Design Level 3 internship task.

The application allows users to browse pizzas, customize pizzas, manage
their cart, create an account, place orders, make payments, and track
their order status.

The project also includes an administrative dashboard for managing pizzas,
orders, inventory, users, and application data.


KEY FEATURES
------------

User Features:
- User registration and login
- Email verification
- JWT-based authentication
- Forgot password and password reset
- User profile and dashboard
- Browse pizza menu
- Category-based pizza browsing
- Pizza customization / Pizza Builder
- Add and remove items from cart
- Update cart quantities
- Checkout and delivery address
- Contact information management
- Razorpay payment integration
- Payment success confirmation
- Order history
- Order details and tracking
- Order status updates
- Order rating after delivery


Admin Features:
- Secure admin authentication
- Admin dashboard
- Pizza/product management
- Add, update and manage pizzas
- Order management
- Update order status
- Inventory management
- Stock monitoring
- User management
- Application analytics
- Admin settings


TECHNOLOGY STACK
----------------

Frontend:
- React.js
- JavaScript
- HTML5
- CSS3
- React Router
- Context API

Backend:
- Python
- Django
- Django REST Framework
- Django Channels
- JWT Authentication

Database:
- SQLite

Payment:
- Razorpay Test Mode

Deployment:
- PythonAnywhere


PROJECT STRUCTURE
-----------------

OIBSIP/
|
|-- backend/
|   |-- accounts/
|   |-- core/
|   |-- dashboard/
|   |-- inventory/
|   |-- notifications/
|   |-- orders/
|   |-- payments/
|   |-- manage.py
|   |-- requirements.txt
|
|-- frontend/
|   |-- src/
|   |-- public/
|   |-- package.json
|
|-- pythonanywhere_wsgi.py
|-- requirements.txt
|-- README.txt


APPLICATION WORKFLOW
--------------------

1. User visits the Pizza Delivery website.
2. User browses available pizzas and categories.
3. User selects a pizza and can customize it where applicable.
4. Selected products are added to the shopping cart.
5. User proceeds to checkout.
6. User provides delivery and contact details.
7. User selects the payment option.
8. Razorpay test payment flow is initiated.
9. After successful payment, the order is confirmed.
10. User can view order details and track the order status.
11. Admin can manage orders and update their status.
12. Inventory is updated according to order processing.


SECURITY
--------

- JWT-based authentication
- Protected user routes
- Protected admin routes
- Environment variables for sensitive configuration
- API credentials are not included in the repository
- Database files and virtual environments are excluded from Git


PAYMENT
-------

The application integrates Razorpay in test mode for demonstrating
the online payment workflow.

No real financial transactions are intended for this project.


DEPLOYMENT
----------

The application is deployed using PythonAnywhere.

The source code contains the backend and frontend required for running
and deploying the application.


PROJECT PURPOSE
---------------

This project demonstrates full-stack web development skills including:

- Frontend development
- Backend API development
- Authentication and authorization
- Database management
- E-commerce workflow
- Payment gateway integration
- Cart and order management
- Inventory management
- Admin dashboard development
- Deployment


INTERNSHIP
----------

Organization: OASIS INFOBYTE
Program: SIP Internship
Domain: Web Development & Design
Level: Level 3
Task: Pizza Delivery Full-Stack Application


AUTHOR
------

Developed as an OASIS INFOBYTE internship project.
