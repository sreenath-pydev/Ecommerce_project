# Ecommerce
![1](https://github.com/Sreenathkk00/Ecommerce_project/assets/133633684/83f66972-81ae-4bb4-847e-5a2143c4ff23)


## Project Overview
"Ecommerce" is an online platform for selling organic food products. The project is built using Python and Django for the backend, and Bootstrap, CSS, and JavaScript for the frontend. SQLite is used as the database. The project includes features such as  single product view user authentication, and an admin panel for managing products and orders.

## Tools and Technologies Used
- **Python**: The main programming language used.
- **Django**: A high-level Python web framework for rapid development.
- **Bootstrap**: A front-end framework for responsive web design.
- **CSS**: For styling the web pages.
- **JavaScript**: For dynamic interactions on the web pages.
- **Git**: For version control.


## Features

### Frontend
- **Index Page**: Displays the latest products. The page is updated automatically when a new product is added.
- **Single Product Page**: Provides detailed information about a specific product.
- **Login and Register Pages**: User authentication for accessing the cart and making purchases.

### Backend (Admin Panel)
- **Product Management**: Admins can update product details and manage the status of orders.

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/sreenath-pydev/Ecommerce_project.git
   cd Ecommerce
2. **Create and activate a virtual environment**
   ```bash
   python -m venv env
   source env/bin/activate   # On Windows, use `virtual_env\Scripts\activate`
3. **Install the required packages**
   ```bash
   pip install -r requirements.txt
4. **Apply migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
5. **Create a superuser for the admin panel**
   ```bash
   python manage.py createsuperuser
6. **Run the developer server**
   ```bash
   python manage.py runserver
7. **Access the appilcation**
   - Open your browser and go to http://127.0.0.1:8000/ to view the frontend.
   - Go to http://127.0.0.1:8000/admin/ to access the admin panel.
## Usage

### Frontend
- Browse products on the index and products pages.
- View detailed information on the single product page.
- Register and log in to make purchases.

### Backend
- Log in to the admin panel to manage products.

## Contributing
- If you would like to contribute to this project, please fork the repository and submit a pull request.

## License
- This project is licensed under the MIT [LICENSE](LICENSE).

## Acknowledgements
- Special thanks to the Django and Bootstrap communities for their excellent documentation and support.
- You can customize the repository URL and any other specific details according to your project setup. This README provides a clear overview and instructions for setting up and running your Django e-commerce project.

