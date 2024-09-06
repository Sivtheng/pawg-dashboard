# Pawg Dashboard with Django, ver. 1.0.0-alpha

## Prerequisites

- Python 3.x
- Django
- Node.js & npm (for Tailwind CSS)
- Tailwind CSS

## Install Dependencies

- pip install -r requirements.txt

## Frontend with Bootstrap and Font Awesome

```
<!-- Bootstrap CSS -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">

<!-- Bootstrap Bundle with Popper -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>

<!-- Font Awesome Icons -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">

```

## Configure Settings

- Configure API base URL if the API server is hosted.
- Default: API_BASE_URL = 'http://localhost:8080'

## Run the development server

- python3 manage.py runserver
- Access http://127.0.0.1:8000/