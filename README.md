# Ecommerce
![1](https://github.com/Sreenathkk00/Ecommerce_project/assets/133633684/83f66972-81ae-4bb4-847e-5a2143c4ff23)
![2](https://github.com/Sreenathkk00/Ecommerce_project/assets/133633684/7c746e7e-4b2f-47c4-8ca4-23350c6ea859)

## Project Overview
"Ecommerce" is an online platform for selling organic food products. The project is built using Python and Django for the backend, and Bootstrap, CSS, and JavaScript for the frontend. PostgreSQL is used as the database. The project includes features such as product listing, single product view, shopping cart functionality with quantity adjustments, user authentication, and an admin panel for managing products and orders.

## Tools and Technologies Used
- **Python**: The main programming language used.
- **Django**: A high-level Python web framework for rapid development.
- **Bootstrap**: A front-end framework for responsive web design.
- **CSS**: For styling the web pages.
- **JavaScript**: For dynamic interactions on the web pages.
- **Git**: For version control.
- **PostgreSQL**: A powerful, open-source relational database system.
- **Virtual Environment**: `virtual_env` is used to manage dependencies.

## Features

### Frontend
- **Index Page**: Displays the latest products. The page is updated automatically when a new product is added.
- **Products Page**: Lists all available products.
- **Single Product Page**: Provides detailed information about a specific product.
- **Cart Page**: Allows users to adjust the quantity of products. The total price is updated based on the selected quantities.
- **Login and Register Pages**: User authentication for accessing the cart and making purchases.

### Backend (Admin Panel)
- **Product Management**: Admins can update product details and manage the status of orders.
- **Order Management**: Admins can view and update the status of new orders.

## Installation and Setup

### Prerequisites
- Python 3.8+
- Git
- PostgreSQL

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/Sreenathkk00/Ecommerce_project.git
   cd Ecommerce
2. **Create and activate a virtual environment**
   ```bash
   python -m venv virtual_env
   source virtual_env/bin/activate   # On Windows, use `virtual_env\Scripts\activate`
3. **Install the required packages**
   ```bash
   pip install -r requirements.txt
4. **Set up the PostgreSQL database**
   - Create a database named ecommerce in PostgreSQL.
   - Update the database settings in ecommerce/settings.py to match your PostgreSQL configuration.
5. **Apply migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
6. **Create a superuser for the admin panel**
   ```bash
   python manage.py createsuperuser
7. **Run the developer server**
   ```bash
   python manage.py runserver
8. **Access the appilcation**
   - Open your browser and go to http://127.0.0.1:8000/ to view the frontend.
   - Go to http://127.0.0.1:8000/admin/ to access the admin panel.
## Usage

### Frontend
- Browse products on the index and products pages.
- View detailed information on the single product page.
- Add products to the cart and adjust quantities.
- Register and log in to make purchases.

### Backend
- Log in to the admin panel to manage products and orders.

## Contributing
- If you would like to contribute to this project, please fork the repository and submit a pull request.

## License
- This project is licensed under the MIT License.

## Acknowledgements
- Special thanks to the Django and Bootstrap communities for their excellent documentation and support.
- You can customize the repository URL and any other specific details according to your project setup. This README provides a clear overview and instructions for setting up and running your Django e-commerce project.

