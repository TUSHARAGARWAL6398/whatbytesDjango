# Project Name

This is a Django project for [brief description of the project]. Follow the instructions below to set up the project on your local machine.

## Prerequisites

- Python 3.x
- pip (Python package installer)
- Virtualenv (for creating isolated Python environments)

## Installation and Setup

1. **Clone the Repository**

    ```bash
    git clone https://github.com/TUSHARAGARWAL6398/whatbytesDjango.git
    cd whatbytesDjango
    ```

2. **Create and Activate a Virtual Environment**

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

3.**move to myproject folder**
    ```bash
    cd myproject
    ```

4. **Install Required Packages**

    ```bash
    pip install -r requirements.txt
    ```



5. **Apply Migrations**

    ```bash
    python manage.py migrate
    ```

6. **Create a Superuser (Optional)**

    To access the Django admin interface:

    ```bash
    python manage.py createsuperuser
    ```

7. **Run the Development Server**

    ```bash
    python manage.py runserver
    ```

    You can now access your project at `http://127.0.0.1:8000/`.

## Notes

- **Environment Variables**: Make sure the `.env` file is included in your `.gitignore` to prevent sensitive information from being committed to version control.
- **Static Files**: Ensure that your static files are correctly set up and available. If you make changes to your static files, run:

    ```bash
    python manage.py collectstatic
    ```

## Troubleshooting

- **If you encounter issues with environment variables**, verify that the `.env` file is correctly named and placed in the root directory. Ensure that `python-dotenv` is installed and properly loaded in your `settings.py`.

- **For 404 or CSS issues**, make sure that the static files directory is correctly configured in your `settings.py` and that you have included `{% load static %}` in your templates.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
