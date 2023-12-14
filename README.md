# Django eCommerce Website

Welcome to our Django eCommerce website! This project is designed to provide a foundation for building a fully functional eCommerce platform using Django, a high-level Python web framework.

## Getting Started

### Prerequisites

Make sure you have the following installed on your machine:

- Python (version 3.6 or higher)
- Pipenv (optional but recommended)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/kepo402/Django_ecommerce_project.git

**2. Change into the project directory:**

cd ecommerce

**3. Install dependencies:**

pipenv install

**4. Activate the virtual environment:**

venv/Scripts/activate

**5. Apply database migrations:**
 
python manage.py migrate

**6. Create a superuser (admin) account:**

python manage.py createsuperuser

**7. Start the development server:**

python manage.py runserver

Now you should be able to access the Django admin interface at http://127.0.0.1:8000/admin/ and the eCommerce site at http://127.0.0.1:8000/.

**Features**

User authentication and authorization
Product catalog and details
Shopping cart functionality
Secure checkout process
Order management
Admin interface for managing products and orders

**Contributing**

If you'd like to contribute to this project, please follow these steps:

**Fork the repository.**

Create a new branch for your feature or bugfix: git checkout -b feature-name.
Commit your changes: git commit -m 'Add new feature'.
Push to the branch: git push origin feature-name.
Create a pull request.


**Acknowledgments**

This project was inspired by manascode.com, A simple yet powerful Django-based eCommerce solution.
Special thanks to the Django community for their continuous support and contributions.
