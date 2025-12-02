# Django TODO App

A modern, feature-rich TODO application built with Django and Python. This project was developed as part of the [AI Dev Tools Zoomcamp](https://github.com/DataTalksClub/ai-dev-tools-zoomcamp) by [DataTalksClub](https://datatalks.club/).

## Features

- **Task Management**: Create, read, update, and delete (CRUD) tasks.
- **Due Dates**: Assign due dates to tasks and track deadlines.
- **Status Tracking**: Mark tasks as resolved or active.
- **Modern UI**: Clean and responsive interface using custom CSS and Phosphor Icons.
- **Compact Mode**: Optimized layout for better information density.

## Installation

This project uses `uv` for dependency management.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/melvinru/django-todo-app.git
    cd django-todo-app
    ```

2.  **Install dependencies:**
    ```bash
    uv sync
    ```

3.  **Set up the environment:**
    Create a `.env` file in the root directory (you can copy `.env.example` if available, or set `DEBUG=True` and a `SECRET_KEY`).

4.  **Run migrations:**
    ```bash
    uv run python manage.py migrate
    ```

5.  **Start the development server:**
    ```bash
    uv run python manage.py runserver
    ```

    Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

## Acknowledgements

Special thanks to **DataTalksClub** for the [AI Dev Tools Zoomcamp](https://github.com/DataTalksClub/ai-dev-tools-zoomcamp), which provided the inspiration and guidance for this project.

[Русская версия (Russian Version)](README_ru.md)
