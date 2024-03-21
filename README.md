# Movie API Project

## Overview

This project is a Django-based API for managing movie data. It provides endpoints for performing CRUD (Create, Read, Update, Delete) operations on movie records. The API is built using Django and Django REST Framework (DRF).

## Features

- **CRUD Operations**: Users can create, read, update, and delete movie records using API endpoints.
- **Validation and Serialization**: Data validation and serialization using Django REST Framework serializers.

## Technologies Used

- **Django**: Python-based web framework for building the API backend.
- **Django REST Framework (DRF)**: Toolkit for building Web APIs in Django.
- **Python**: Programming language used for backend development.
- **Postgres**: Relational database management system used for storing movie data.

## Installation

To run the project locally, follow these steps:

1. Clone the repository: `git clone <repository-url>`
2. Navigate to the project directory: `cd movie_api_project`
3. Install dependencies: `pip install -r requirements.txt`
4. Run the Django development server: `python manage.py runserver`

The API will be accessible at `https://movie-api-sooty.vercel.app/api/movie/`.

## API Endpoints

- `GET /api/movie/`: Retrieve a list of all movies.
- `POST /api/movie/`: Create a new movie.
- `GET /api/movie/<int:pk>/`: Retrieve details of a specific movie.
- `PUT /api/movie/<int:pk>/`: Update details of a specific movie.
- `DELETE /api/movie/<int:pk>/`: Delete a specific movie.

## Usage

Once the API is running, users can interact with it using API clients such as `curl`, Postman, or browser extensions like `REST Client`. Users can perform CRUD operations on movie records by sending requests to the appropriate endpoints.

## Contributing

Contributions are welcome! If you would like to contribute to the project, please fork the repository, create a new branch for your feature or bug fix, make changes, and submit a pull request.

## License

This project is licensed under the MIT License.
